def response(hey_bob):
    formatado = hey_bob.strip()
    questao = formatado.endswith("?")
    grito = formatado.isupper()
    if grito and questao:
        return "Calm down, I know what I'm doing!"
    if questao:
        return "Sure."
    if grito:
        return "Whoa, chill out!"
    if len(formatado) < 1:
        return "Fine. Be that way!"
    else:
        return "Whatever."
