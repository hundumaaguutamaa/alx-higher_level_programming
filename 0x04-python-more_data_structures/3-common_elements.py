   #!/usr/bin/python3

def common_elements(set_1, set_2):
    el_result = []

    for letter in set_1:
        if letter in set_2:
           el_result.append(letter)
    return el_result

