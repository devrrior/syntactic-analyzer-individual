parser_table = {
    "S": {"function": ["F", "N", "PM"]},
    "F": {"function": ["function"]},
    "PM": {"(": ["PA", "PL", "PC"]},
    "PA": {"(": ["("]},
    "PC": {")": [")"]},
    "PL": {"var": ["V", "X", "LT"]},
    "V": {"var": ["var"]},
    "X": {
        "a": ["N", ":", "T"],
        "b": ["N", ":", "T"],
        "c": ["N", ":", "T"],
        "d": ["N", ":", "T"],
        "e": ["N", ":", "T"],
        "f": ["N", ":", "T"],
        "g": ["N", ":", "T"],
        "h": ["N", ":", "T"],
        "i": ["N", ":", "T"],
        "j": ["N", ":", "T"],
        "k": ["N", ":", "T"],
        "l": ["N", ":", "T"],
        "m": ["N", ":", "T"],
        "n": ["N", ":", "T"],
        "o": ["N", ":", "T"],
        "p": ["N", ":", "T"],
        "q": ["N", ":", "T"],
        "r": ["N", ":", "T"],
        "s": ["N", ":", "T"],
        "t": ["N", ":", "T"],
        "u": ["N", ":", "T"],
        "v": ["N", ":", "T"],
        "w": ["N", ":", "T"],
        "x": ["N", ":", "T"],
        "y": ["N", ":", "T"],
        "z": ["N", ":", "T"],
    },
    "N": {
        "a": ["L", "RN"],
        "b": ["L", "RN"],
        "c": ["L", "RN"],
        "d": ["L", "RN"],
        "e": ["L", "RN"],
        "f": ["L", "RN"],
        "g": ["L", "RN"],
        "h": ["L", "RN"],
        "i": ["L", "RN"],
        "j": ["L", "RN"],
        "k": ["L", "RN"],
        "l": ["L", "RN"],
        "m": ["L", "RN"],
        "n": ["L", "RN"],
        "o": ["L", "RN"],
        "p": ["L", "RN"],
        "q": ["L", "RN"],
        "r": ["L", "RN"],
        "s": ["L", "RN"],
        "t": ["L", "RN"],
        "u": ["L", "RN"],
        "v": ["L", "RN"],
        "w": ["L", "RN"],
        "x": ["L", "RN"],
        "y": ["L", "RN"],
        "z": ["L", "RN"],
    },
    "RN": {
        "a": ["L", "RN"],
        "b": ["L", "RN"],
        "c": ["L", "RN"],
        "d": ["L", "RN"],
        "e": ["L", "RN"],
        "f": ["L", "RN"],
        "g": ["L", "RN"],
        "h": ["L", "RN"],
        "i": ["L", "RN"],
        "j": ["L", "RN"],
        "k": ["L", "RN"],
        "l": ["L", "RN"],
        "m": ["L", "RN"],
        "n": ["L", "RN"],
        "o": ["L", "RN"],
        "p": ["L", "RN"],
        "q": ["L", "RN"],
        "r": ["L", "RN"],
        "s": ["L", "RN"],
        "t": ["L", "RN"],
        "u": ["L", "RN"],
        "v": ["L", "RN"],
        "w": ["L", "RN"],
        "x": ["L", "RN"],
        "y": ["L", "RN"],
        "z": ["L", "RN"],
        ":": [],
        "(": [],
    },
    "L": {
        "a": ["a"],
        "b": ["b"],
        "c": ["c"],
        "d": ["d"],
        "e": ["e"],
        "f": ["f"],
        "g": ["g"],
        "h": ["h"],
        "i": ["i"],
        "j": ["j"],
        "k": ["k"],
        "l": ["l"],
        "m": ["m"],
        "n": ["n"],
        "o": ["o"],
        "p": ["p"],
        "q": ["q"],
        "r": ["r"],
        "s": ["s"],
        "t": ["t"],
        "u": ["u"],
        "v": ["v"],
        "w": ["w"],
        "x": ["x"],
        "y": ["y"],
        "z": ["z"],
    },
    "T": {"boolean": ["boolean"], "string": ["string"]},
    "LT": {")": [], ";": ["P", "X", "LT"]},
    "P": {";": [";"]},
}


terminal_tokens = {
    "function",
    "(",
    ")",
    "var",
    "boolean",
    "string",
    ";",
    ":",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "$",
}


def isTerminal(token: str):
    return token in terminal_tokens


def analyze_syntaxis(input_list: list):
    history = ""
    input_list.append("$")
    stack = ["$", "S"]

    while len(stack) > 0:
        a_str = input_list[0]
        X_str = stack[-1]
        history += f"Pila: {stack} | Entrada: {a_str}\n"
        if isTerminal(X_str):
            if X_str == a_str:
                stack.pop()
                input_list.pop(0)
            else:
                return {
                    "success": False,
                    "message": f"Error en el caracter {a_str} en la posicion {len(input_list) - 1}. Se esperaba {X_str}",
                    "history": history,
                }
        else:
            try:
                if parser_table[X_str][a_str] or parser_table[X_str][a_str] == []:
                    stack.pop()
                    stack.extend(parser_table[X_str][a_str][::-1])
                else:
                    return {
                        "success": False,
                        "message": f"Error en el caracter {a_str} en la posicion {len(input_list) - 1}. Se esperaba {parser_table[X_str]}",
                        "history": history,
                    }
            except KeyError:
                return {
                    "success": False,
                    "message": f"Error en el caracter {a_str} en la posicion {len(input_list) - 1}. Se esperaba {parser_table[X_str]}",
                    "history": history,
                }

    return {"success": True, "message": "Gramatica correcta", "history": history}
