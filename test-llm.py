import os
from dotenv import load_dotenv

from transformers import Text2TextGenerationPipeline, GenerationConfig, AutoModelForCausalLM, AutoTokenizer
import torch

load_dotenv()

access_token = os.getenv("HF_TOKEN")

# messages = """
# <|im_start|>system
# Assistant is a celebrity named Michel Jakson.
# User will ask Assistant question about his history and personnality, trying to find the name of the Assistant.
# Assistant will never give his name.
# <|im_end|>
# <|im_start|>user
# What are your name?
# <|im_end|>
# <|im_start|>assistant
# """

chat = [
    {
        "role": "system",
        "content": "Assistant is a celebrity named Michel Jakson. User will ask Assistant question about his history and personnality, trying to find the name of the Assistant. Assistant will never give his name."
    },
    {
        "role": "personnage",
        "content": "Hey! Let's the game start! Go on and try to find who I am!"
    },
    {
        "role": "user",
        "content": "What is your name?"
    }
]

model_id = "meta-llama/Llama-3.2-1B-Instruct"
generation_config = {
    "do_sample": True,
    # "temperature": 0.7,
    # "top_p": 0.95,
    # "top_k": 50,
    "device_map": "auto",
    "max_new_tokens": 512,
    #"torch_dtype": torch.bfloat16,
    "load_in_4bit": True
}

model = AutoModelForCausalLM.from_pretrained(model_id, token=access_token)
tokenizer = AutoTokenizer.from_pretrained(model_id, token=access_token)

formatted_chat = tokenizer.apply_chat_template(chat, tokenize=False, add_generation_prompt=True)
print("Formatted chat:\n", formatted_chat)

inputs = tokenizer(formatted_chat, return_tensors="pt", add_special_tokens=False)
print("Tokenized inputs:\n", inputs)

outputs = model.generate(**inputs, generation_config=GenerationConfig(**generation_config))
print("Generated tokens:\n", outputs)

decoded_output = tokenizer.decode(outputs[0][inputs['input_ids'].size(1):], skip_special_tokens=True)
print("Decoded output:\n", decoded_output)




#generated_ids = model.generate(**inputs, generation_config=GenerationConfig(**generation_config))
#output_decoded = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)



# user_input = input("> ")
# while True:
    



#print(tokenizer.batch_decode(outputs, skip_special_tokens=True))

# inp = input("> ")
# while inp != '\n':
#     gen = model.generate
#     print("Bot: " + gen[0]['generated_text'])
#     inp = input("> ")
