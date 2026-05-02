def resistor_label(colors):
    COLORS = ["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
    TOLARENCE = {
        "grey": "±0.05%",
        "violet": "±0.1%",
        "blue": "±0.25%",
        "green": "±0.5%",
        "brown": "±1%",
        "red": "±2%",
        "gold": "±5%",
        "silver": "±10%"
    }
    if len(colors) == 4:
        ohms = (10*COLORS.index(colors[0]) + COLORS.index(colors[1])) * (10**COLORS.index(colors[2]))
        if ohms > 1_000_000_000:
            prefix = "giga"
            ohms /= 1_000_000_000
        elif ohms > 1_000_000:
            prefix = "mega"
            ohms /= 1_000_000
        elif ohms >= 1_000:
            prefix = "kilo"
            ohms /= 1_000
        else:
            prefix = ""
        ohms = int(ohms) if ohms == int(ohms) else ohms
        return f"{ohms} {prefix}ohms {TOLARENCE[colors[3]]}"
    elif len(colors) == 5:
        ohms = (100*COLORS.index(colors[0]) + (10*COLORS.index(colors[1])) + COLORS.index(colors[2])) * (10**COLORS.index(colors[3]))
        if ohms > 1_000_000_000:
            prefix = "giga"
            ohms /= 1_000_000_000
        elif ohms > 1_000_000:
            prefix = "mega"
            ohms /= 1_000_000
        elif ohms >= 1_000:
            prefix = "kilo"
            ohms /= 1_000
        else:
            prefix = ""
        ohms = int(ohms) if ohms == int(ohms) else ohms
        return f"{ohms} {prefix}ohms {TOLARENCE[colors[4]]}"
    else: return "0 ohms"

    
    
