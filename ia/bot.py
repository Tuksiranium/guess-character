import os
from transformers import AutoModelForCausalLM, AutoTokenizer, GenerationConfig

class Bot:

    def __init__(self,
                 role_name: str,
                 prompt: list,
                 model_id: str = "meta-llama/Llama-3.1-8B-Instruct",
                 generation_config: dict = {
                    "do_sample": True,
                    "device_map": "auto",
                    "max_new_tokens": 512,
                 }):

        self.model_id = model_id
        self.generation_config = generation_config
        self.role_name = role_name
        self.prompt = prompt

        self._token = os.getenv("HF_TOKEN")

        self.model = AutoModelForCausalLM.from_pretrained(self.model_id, token=self._token)
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_id, token=self._token)


    def send_message_and_get_response(self, text: str, role: str = "user") -> str:
        self.prompt.append({
            "role": role,
            "content": text
        })
        formatted_chat = self.tokenizer.apply_chat_template(self.prompt, tokenize=False, add_generation_prompt=True)
        inputs = self.tokenizer(formatted_chat, return_tensors="pt", add_special_tokens=False)
        outputs = self.model.generate(**inputs, generation_config=GenerationConfig(**self.generation_config), pad_token_id=self.tokenizer.eos_token_id)
        decoded_output = self.tokenizer.decode(outputs[0][inputs['input_ids'].size(1):], skip_special_tokens=True)
        self.prompt.append({"role": self.role_name, "content": decoded_output})
        return decoded_output

    