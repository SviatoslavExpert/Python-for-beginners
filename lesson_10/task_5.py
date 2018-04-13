def world_count(text):
    words = text.split(" ")
    return len(words)

text = "Hello world"
print(world_count(text))