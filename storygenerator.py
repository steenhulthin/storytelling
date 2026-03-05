from streamlit import secrets

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


token = secrets["HF_TOKEN"]

model_name = "roneneldan/TinyStories-1M"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    token=token,
    device_map="auto",          # automatically places layers on GPU/CPU
    torch_dtype="auto",          # uses fp16/fp32 as appropriate
)


def generate_tinystory(prompt: str,
                       max_new_tokens: int = 100,
                       temperature: float = 0.8,
                       top_p: float = 0.95) -> str:
    """
    Generate a short story continuation using TinyStoriesGPT.
    
    Parameters
    ----------
    prompt : str
        Starting text (e.g., a title or opening line).
    max_new_tokens : int, default 100
        How many tokens to generate.
    temperature : float, default 0.8
        Controls randomness; lower = more deterministic.
    top_p : float, default 0.95
        Nucleus sampling threshold.
    """
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    with torch.no_grad():
        output_ids = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            temperature=temperature,
            top_p=top_p,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id
        )
    # Remove the prompt part to return only the generated continuation
    generated_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return generated_text[len(prompt):].strip()