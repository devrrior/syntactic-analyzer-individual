def separate_elements(input_string):
    elements = ["function", "(", ")", "var", "boolean", "string", ";", ":"]
    output_list = []
    current_word = ""

    for char in input_string:
        if char == " ":
            if current_word:
                if current_word in elements:
                    output_list.append(current_word)
                else:
                    output_list.extend(list(current_word))
                current_word = ""
        elif char in elements:
            if current_word:
                if current_word in elements:
                    output_list.append(current_word)
                else:
                    output_list.extend(list(current_word))
                current_word = ""
            output_list.append(char)
        else:
            current_word += char

    if current_word:
        if current_word in elements:
            output_list.append(current_word)
        else:
            output_list.extend(list(current_word))

    return output_list

# Test cases
input_strings = [
    "function main ( var asd : string ; val : boolean )",
    "function main (var asd : string ; val : boolean)",
    "function main (var asd : string)",
    "function main ( var val : string )"
]

for input_str in input_strings:
    print("\n")
    print("Input string:", input_str)
    print("Output list:", separate_elements(input_str))
