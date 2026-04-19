def is_isogram(string):
    string=string.lower()
    c= sum(1 for caracter in string if caracter.isalpha())
    isogram = set( caracter for caracter in string if caracter.isalpha())
    if len(isogram) == c:
        return True
    else: return False