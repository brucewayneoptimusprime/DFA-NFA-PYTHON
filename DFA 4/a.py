# DFA for language L(M) = a + aa*b
def dfa_a_aab(string):
    current_state = 0
    for ch in string:
        if ch == 'a' and current_state == 0:
            current_state = 1
        elif ch == 'a' and (current_state == 1 or current_state == 2):
            current_state = 2
        elif ch == 'b' and current_state == 1:
            current_state = 2
        else:
            return False
    return current_state == 2

# Test the DFA for language L(M) = a + aa*b
test_strings = ['a', 'aa', 'aab', 'ab', 'aaa', 'aaaab', 'abaaab']
for test_string in test_strings:
    print(f'String: {test_string}, Accept: {dfa_a_aab(test_string)}')
