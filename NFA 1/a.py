# NFA for strings containing two 0's separated by a substring of length multiple of 3
def nfa_2_zeros_3_mult(string):
    current_state = 0
    for ch in string:
        if ch == '0' and current_state == 0:
            current_state = 1
        elif ch == '0' and current_state == 1:
            current_state = 2
        elif ch == '0' and current_state == 2:
            current_state = 2
        elif ch == '1' and current_state in (0, 1, 2):
            current_state = 0
        else:
            return False
    return current_state == 2

# Test the NFA for strings containing two 0's separated by a substring of length multiple of 3
test_strings = ['0101010', '000101010', '0000', '01010', '101010']
for test_string in test_strings:
    print(f'String: {test_string}, Accept: {nfa_2_zeros_3_mult(test_string)}')
