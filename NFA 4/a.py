# NFA for {}, {ε}, {(ab)n | n ∈ N} with regular expression (ab)*
def nfa_ab_star(string):
    current_state = 0
    for ch in string:
        if ch == 'a' and current_state == 0:
            current_state = 1
        elif ch == 'b' and current_state == 1:
            current_state = 0
        else:
            return False
    return current_state == 0

# Test the NFA for {}, {ε}, {(ab)n | n ∈ N} with regular expression (ab)*
test_strings = ['', 'ab', 'ababab', 'abababab']
for test_string in test_strings:
    print(f'String: {test_string}, Accept: {nfa_ab_star(test_string)}')
