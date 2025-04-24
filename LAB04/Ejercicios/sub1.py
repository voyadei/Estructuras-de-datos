def reverse_string(s):
    def fill_stack(i):
        if i < 0:
            return []
        st = fill_stack(i - 1)
        st.append(s[i])
        return st

    def build_reversed(st):
        if not st:
            return ''
        return st.pop() + build_reversed(st)

    stack = fill_stack(len(s) - 1)
    return build_reversed(stack)































text = "transhumanismo"
print(reverse_string(text))
print(reverse_string("transhuman"))      # Output: namansuhsnart
print(reverse_string("immortality"))     # Output: ytilatrommi
print(reverse_string("12345"))           # Output: 54321
