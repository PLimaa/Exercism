def is_pangram(sentence):
    sentence = sentence.lower()
    pangram = set(character for character in sentence if character.isalpha())
    if len(pangram) >= 26:
        return True
    else: return False

