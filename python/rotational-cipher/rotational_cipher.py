import string


def rotate(text, key):
    new_text = ""
    for char in text:
        if char.isupper():
            indice = string.ascii_uppercase.index(char)
            new_text += string.ascii_uppercase[(indice + key) % 26]
        elif char.islower():
            indice = string.ascii_lowercase.index(char)
            new_text += string.ascii_lowercase[(indice + key) % 26]
        else:
            new_text += char
    return new_text
        

            

    
