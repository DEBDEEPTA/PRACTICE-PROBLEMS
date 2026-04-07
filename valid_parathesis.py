"""
{{[]()}}
-> valid

{{[}]
-> invalid
"""

def valid_parenthesis_checker(str_value):
    valid_pair_dict = {
        '(': ')',
        '{': '}',
        '[': ']'
    }

    char_stack = []

    for char in str_value:
        if char in valid_pair_dict:
            char_stack.append(char)
        else:
            if not char_stack:
                return False

            stack_top = char_stack.pop()

            if valid_pair_dict[stack_top] != char:
                return False

    return len(char_stack) == 0

if __name__ == "__main__":
    str_value = input("Enter Parenthesis sequence:\n")
    if valid_parenthesis_checker(str_value):
        print("Valid Sequence")
    else:
        print("Invalid Sequence")


