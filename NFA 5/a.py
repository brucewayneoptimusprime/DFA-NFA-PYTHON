# NFA for strings ending with '01'
def nfa_ends_01(string):
    current_state = 0
    for ch in string:
        if ch == '0' and current_state == 0:
            current_state = 1
        elif ch == '1' and current_state == 0:
            current_state = 0
        elif ch == '0' and current_state == 1:
            current_state = 1
        elif ch == '1' and current_state == 1:
            current_state = 2
        else:
            return False
    return current_state == 2

# Test the NFA for strings ending with '01'
test_strings = ['1101', '10101', '000001', '1010101', '1111']
for test_string in test_strings:
    print(f'String: {test_string}, Accept: {nfa_ends_01(test_string)}')
