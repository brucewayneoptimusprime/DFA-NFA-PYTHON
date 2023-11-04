# DFA for strings containing '00'
def dfa_00(string):
    current_state = 0
    for ch in string:
        if ch == '0':
            if current_state == 0:
                current_state = 1
            elif current_state == 1:
                current_state = 2
        elif ch == '1':
            current_state = 0
    return current_state == 2

# Test the DFA for strings containing '00'
test_strings = ['001010', '100200', '0000', '10101', '100']
for test_string in test_strings:
    print(f'String: {test_string}, Accept: {dfa_00(test_string)}')
