# Write Fun Mini Stories

## What this is
This app helps you make short, playful stories.
Type an idea, and it continues your story with the same vibe.

## How to get the best results
- Start simple: one character and one situation.
- Ask for one short step at a time.
- If the result is weird, click again or change your prompt.
- Be specific: mood, place, and style help a lot.
- Try fun twists like "make it silly" or "add a dragon."

## Things to expect
- Sometimes the story may drift or get random.
- It may repeat itself now and then.
- It can mix up details in longer stories.
- It is best for creative play, not facts.

## Quick story ideas
- "A shy ghost opens a bakery in Copenhagen."
- "Two kids find a tiny door in an old tree."
- "A pirate cat loses her map before sunset."

Have fun and keep experimenting. Small prompt changes can create very different stories.

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

## Technical notes
- Max new tokens:
  Sets the generation length cap for each response (`max_new_tokens`).
- Temperature:
  Scales token probabilities before sampling.
  `temperature < 1.0` sharpens the distribution (more deterministic).
  `temperature > 1.0` flattens it (more random).
- Top-p (nucleus sampling):
  Samples from the smallest token set whose cumulative probability reaches `p`.
  Lower `top_p` narrows candidate tokens; higher `top_p` broadens them.
- Interactions:
  High temperature + high top-p increases diversity but can reduce coherence.
  Lower settings generally improve consistency.
