def label(colors):
    valor = ""
    traducao = {
        "black": "0",
        "brown": "1",
        "red": "2",
        "orange": "3",
        "yellow": "4",
        "green": "5",
        "blue": "6",
        "violet": "7",
        "grey": "8",
        "white": "9"
    }
    prefixos = {
        0:" ohms",
        3: " kiloohms",
        6:" megaohms",
        9:" gigaohms"

    }
    for cor in colors[:2]:
        valor += traducao[cor]
    valor_final = int(valor) * (10**int(traducao[colors[2]]))
    for prefixo in reversed(prefixos):
        if valor_final == 0:
            return "0 ohms"
        if valor_final % (10**prefixo) == 0:
            return str(valor_final//(10**prefixo)) + prefixos[prefixo]
    return str(valor_final) + " ohms"
    
        

    
    


    
