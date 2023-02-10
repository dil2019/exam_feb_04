def is_pangram(text):
    letters = "abcdefghijklmnopqrstuvwxyz"
    text = text.lower()
    for char in letters:
        if char not in text:
            return "Sentence is not a pangram"
    return "Sentence is a pangram"


sentence1 = "The quick brown fox jumps over the lazydog"
sentence2 = "The brown fox jumps over the lazydog"
print(is_pangram(sentence1))
print(is_pangram(sentence2))