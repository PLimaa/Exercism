def find_anagrams(word, candidates):
    anagrams = []
    word_normalizada = word.lower()
    word_ordenada = "".join(sorted(word_normalizada))
    for teste in candidates:
        teste_normalizado = teste.lower()
        if word_normalizada == teste_normalizado:
            continue
        teste_ordenado = "".join(sorted(teste_normalizado))
        if word_ordenada == teste_ordenado:
            anagrams.append(teste)
    return anagrams


