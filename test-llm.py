import transformers
import torch

model_id = "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"

pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device_map="auto"
)

pipeline("Hey, how are you doing today?")
