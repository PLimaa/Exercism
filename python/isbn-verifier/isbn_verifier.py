def is_valid(isbn):
    soma = 0
    isbn = isbn.replace('-', '')
    
    if len(isbn) != 10:
        return False
    
    for i in range(len(isbn)):
        if isbn[i] == 'X' and i == 9:
            soma += 10
        elif isbn[i].isdigit():
            soma += int(isbn[i]) * (10 - i)
        else:
            return False
    
    return soma % 11 == 0