# DFA for strings starting with 'ab'
def dfa_starting_ab(string):
    current_state = 0
    for ch in string:
        if ch == 'a' and current_state == 0:
            current_state = 1
        elif ch == 'b' and current_state == 1:
            current_state = 1
        else:
            return False
    return current_state == 1

# Test the DFA for strings starting with 'ab'
test_strings = ['ababab', 'abba', 'baaa', 'abb', 'ab']
for test_string in test_strings:
    print(f'String: {test_string}, Accept: {dfa_starting_ab(test_string)}')
