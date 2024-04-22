def get_segment_display_dict():
    segment_dict = {
        0: [' ___ ', '|   |', '|   |', '|   |', '|   |', '|   |', '|___|'],
        1: ['     ', '    |', '    |', '    |', '    |', '    |', '    |'],
        2: [' ___ ', '    |', '    |', ' ___|', '|    ', '|    ', '|___ '],
        3: [' ___ ', '    |', '    |', ' ___|', '    |', '    |', ' ___|'],
        4: ['     ', '|   |', '|   |', '|___|', '    |', '    |', '    |'],
        5: [' ___ ', '|    ', '|    ', ' ___|', '    |', '    |', ' ___|'],
        6: [' ___ ', '|    ', '|    ', '|___ ', '|   |', '|   |', '|___|'],
        7: [' ___ ', '    |', '    |', '    |', '    |', '    |', '    |'],
        8: [' ___ ', '|   |', '|   |', '|___|', '|   |', '|   |', '|___|'],
        9: [' ___ ', '|   |', '|   |', '|___|', '    |', '    |', '    |']
    }
    return segment_dict


def print_number_as_8_segment_display(number):
    segment_dict = get_segment_display_dict()

    digits = [int(digit) for digit in str(number)]
    for line in range(7):  # 7 lines in the display
        for digit in digits:
            # for i in range(1):
                print(segment_dict[digit][line], end='  ')
        print()


if __name__ == "__main__":

    #N = int(input())  # Number of lines for each segment
    number_to_display = int(input())
    print_number_as_8_segment_display(number_to_display)
