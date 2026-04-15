def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    soma = 0
    if number<=0:
        raise ValueError("Classification is only possible for positive integers.")
    else:
        for divisor in range(1,(number//2) + 1):
            if number % divisor == 0:
                soma += divisor
        if soma == number:
            return "perfect"
        if soma > number:
            return "abundant"
        else:
            return "deficient"


