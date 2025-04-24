def is_valid_parentheses(s):
    def recurse(s, stack):
        if not s:
            return (len(stack) == 0, stack)
        char = s[0]
        if char in "([{":
            return recurse(s[1:], stack + [char])
        elif char in ")]}":
            if not stack:
                return (False, stack)
            top = stack[-1]
            if (top, char) in [('(', ')'), ('[', ']'), ('{', '}')]:
                return recurse(s[1:], stack[:-1])
            else:
                return (False, stack)
        else:
            return recurse(s[1:], stack)

    return recurse(s, [])

# Test
print(is_valid_parentheses("{[()]}") == (True, []))
print(is_valid_parentheses("{[(])}") == (False, ['{']))
