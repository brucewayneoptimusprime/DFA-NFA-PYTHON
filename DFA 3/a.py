# DFA for only the input 'aaab'
def dfa_aaab(string):
    current_state = 0
    for ch in string:
        if ch == 'a' and current_state == 0:
            current_state = 1
        elif ch == 'a' and current_state == 1:
            current_state = 2
        elif ch == 'b' and current_state == 2:
            current_state = 3
        else:
            return False
    return current_state == 3

# Test the DFA for only the input 'aaab'
test_strings = ['aaab', 'aaa', 'aab', 'aabaa', 'ab']
for test_string in test_strings:
    print(f'String: {test_string}, Accept: {dfa_aaab(test_string)}')
