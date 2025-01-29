from transformers import Text2TextGenerationPipeline, GenerationConfig, AutoModelForCausalLM, AutoTokenizer
import torch

model_id = "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"
model = AutoModelForCausalLM.from_pretrained(model_id)
generation_config = GenerationConfig(
    max_new_tokens=200,
    do_sample=True,
    temperature=.6,
    top_p=.92,
    top_k=0
)
tokenizer = AutoTokenizer.from_pretrained(model_id)

inputs = tokenizer("Tell me the temperature a clermont-ferrand aujourd'hui", return_tensors="pt")
outputs = model.generate(**inputs, generation_config=generation_config)

print(tokenizer.batch_decode(outputs, skip_special_tokens=True))

# inp = input("> ")
# while inp != '\n':
#     gen = model.generate
#     print("Bot: " + gen[0]['generated_text'])
#     inp = input("> ")
