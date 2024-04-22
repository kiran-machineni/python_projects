def print_formatted(number):
    """Prints decimal, octal, hexadecimal, and binary representations of numbers up to the given number.
    Aligns the columns for a neat output.
    """

    width = len(bin(number)[2:])  # Calculate width based on the binary representation

    for i in range(1, number + 1):
        print(
            str(i).rjust(width),
            oct(i)[2:].rjust(width),
            hex(i)[2:].upper().rjust(width),
            bin(i)[2:].rjust(width),
        )


print_formatted(17)
