def is_armstrong_number(number):
    soma = 0 
    for digito in str(number):
        soma += (int(digito))**len(str(number))
    if soma == number:
        return True
    else:
        return False
