# NFA for the regular expression a + aa*b + a*b
def nfa_regular_expr(string):
    current_state = 0
    for ch in string:
        if ch == 'a' and (current_state == 0 or current_state == 1):
            current_state = 1
        elif ch == 'a' and current_state == 1:
            current_state = 2
        elif ch == 'b' and current_state in (1, 2):
            current_state = 2
        else:
            return False
    return current_state == 2

# Test the NFA for the regular expression a + aa*b + a*b
test_strings = ['a', 'aa', 'aab', 'ab', 'aaa', 'aaaab', 'abaaab']
for test_string in test_strings:
    print(f'String: {test_string}, Accept: {nfa_regular_expr(test_string)}')
