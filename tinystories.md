# Write Fun Mini Stories

## What this is
This app helps you make short, playful stories.
Type the beginning of a story, and it continues your story with the same vibe.
**It only knows English**

## How to get the best results
- Start simple: one character and one situation.

## Things to expect
- Sometimes the story may drift or get random.
- It may repeat itself now and then.
- It can mix up details.
- It is for creative play, _not_ facts.

## Quick story ideas
- "A shy ghost opens a bakery in Copenhagen."
- "Two kids find a tiny door in an old tree."
- "A pirate cat loses her map before sunset."

Have fun! 

## What the sliders change
- Max new tokens:
  Controls how long the next part of the story can be.
  Lower values give short replies, higher values give longer ones.
- Temperature:
  Controls creativity.
  Lower values feel safer and more predictable.
  Higher values feel more surprising, wild, and sometimes messy.
- Top-p:
  Controls how "wide" the model explores word choices.
  Lower values keep it focused.
  Higher values allow more unusual turns.

---

**TinyStories-1M** is a ~1M-parameter GPT-style causal language model trained on the TinyStories dataset for short, coherent story continuation (Model: https://huggingface.co/roneneldan/TinyStories-1M, Paper: https://arxiv.org/abs/2305.07759, PDF: https://arxiv.org/pdf/2305.07759.pdf).

**Note:** This app runs _entirely_ in Python on the server (no browser-side model inference) !
Stack: Streamlit UI + Hugging Face Transformers + PyTorch (+ Accelerate for device handling).
The model is loaded from Hugging Face Hub and generation runs in your Python runtime.
