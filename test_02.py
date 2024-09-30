def binary_to_hexadecimal(s: str) -> str:
    if len(s) % 4 != 0:
        multiplier = (len(s) // 4) + 1
        new_length = multiplier * 4
        adjusted_string = s.zfill(new_length)
    else:
        adjusted_string = s

    local_dict = {
        "0000": "0",
        "0001": "1",
        "0010": "2",
        "0011": "3",
        "0100": "4",
        "0101": "5",
        "0110": "6",
        "0111": "7",
        "1000": "8",
        "1001": "9",
        "1010": "A",
        "1011": "B",
        "1100": "C",
        "1101": "D",
        "1110": "E",
        "1111": "F",
    }

    # look at slice of four
    # compare it to dictionary to get assocaiated value
    # concatenate those values to get final result
    res = ""
    while len(adjusted_string) > 0:
        val = adjusted_string[:4]
        hex_value = local_dict[val]
        res += hex_value
        adjusted_string = adjusted_string[4:]

    return res


def main() -> None:
    print(binary_to_hexadecimal("110010"))


if __name__ == '__main__':
    main()

# binaryToHexadecimal('110010') => '32'
