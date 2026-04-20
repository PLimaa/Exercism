def value(colors):
    valor=""
    cores = {
        "black": "0",
        "brown": "1",
        "red": "2",
        "orange": "3",
        "yellow": "4",
        "green": "5",
        "blue": "6",
        "violet": "7",
        "grey": "8",
        "white": "9",
    }
    for cor in colors:
        if colors.index(cor) > 1:
            continue
        valor += cores[cor]
    return int(valor)
