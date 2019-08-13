def swap_case(s):
    char_list = list(s)
    converted_char_list = []
    for char in char_list:
        if char.isalpha():
            if char.islower():
                converted_char_list.append(char.capitalize())
            else:
                converted_char_list.append(char.lower())
        else:
            converted_char_list.append(char)
    result = "".join(converted_char_list)
    return(result)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
