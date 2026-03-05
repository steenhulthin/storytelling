import storygenerator

prompt = "The brave rabbit ventured into the forest because"
story_continuation = storygenerator.generate_tinystory(prompt, max_new_tokens=80)
print(prompt + " " + story_continuation)