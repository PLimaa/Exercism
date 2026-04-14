'''
Equacao da circunferencia == (x-a)**2 + (y-b)**2 = r**2
(a,b) == Centro -> Nesse caso é : (0,0)
Logo, x**2 + y**2 = r**2

'''

def score(x, y):
    equacao = x**2 + y**2
    if equacao > 10**2:
        return 0
    if 5**2 < (x**2 + y**2) <= 10**2:
        return 1
    if 1 < (x**2 + y**2) <= 5**2:
        return 5
    else:
        return 10

    
