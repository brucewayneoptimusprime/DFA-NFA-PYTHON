# NFA for the regular expression (a + ba)*bb(a + ab)*
def nfa_expr(string):
    current_state = 0
    for ch in string:
        if ch == 'a' and (current_state == 0 or current_state == 1):
            current_state = 1
        elif ch == 'b' and current_state == 1:
            current_state = 2
        elif ch == 'b' and current_state in (2, 3):
            current_state = 3
        elif ch == 'a' and current_state == 3:
            current_state = 4
        elif ch == 'b' and current_state == 4:
            current_state = 2
        else:
            return False
    return current_state == 2 or current_state == 4

# Test the NFA for the regular expression (a + ba)*bb(a + ab)*
test_strings = ['bb', 'ababab', 'aabba', 'a', 'b', 'abaab', 'ababb']
for test_string in test_strings:
    print(f'String: {test_string}, Accept: {nfa_expr(test_string)}')
