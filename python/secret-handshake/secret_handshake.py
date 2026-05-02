def commands(binary_str):
    sequence = []
    action = {
        0 : "wink",
        1 : "double blink",
        2 : "close your eyes",
        3 : "jump"
    }
    ajustada = binary_str[::-1]
    for i in range(len(ajustada)-1):
        if int(ajustada[i]) == 1:
            sequence.append(action[i])
    if int(binary_str[0]) == 1:
        return sequence[::-1]
    else: return sequence
        
        
