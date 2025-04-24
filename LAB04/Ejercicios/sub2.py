def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0

def apply_op(a, b, op):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return a / b

def evaluate_infix(expression):
    def helper(expr, i):
        values = []
        ops = []
        while i < len(expr):
            if expr[i] == ' ':
                i += 1
                continue
            elif expr[i] == '(':
                val, i = helper(expr, i + 1)
                values.append(val)
            elif expr[i].isdigit():
                val = 0
                while i < len(expr) and expr[i].isdigit():
                    val = val * 10 + int(expr[i])
                    i += 1
                values.append(val)
                i -= 1
            elif expr[i] == ')':
                break
            elif expr[i] in '+-*/':
                while ops and precedence(ops[-1]) >= precedence(expr[i]):
                    right = values.pop()
                    left = values.pop()
                    op = ops.pop()
                    values.append(apply_op(left, right, op))
                ops.append(expr[i])
            i += 1
        while ops:
            right = values.pop()
            left = values.pop()
            op = ops.pop()
            values.append(apply_op(left, right, op))
        return values[0], i

    result, _ = helper(expression, 0)
    return result

expr = "(3 + 4) * 2"
print(evaluate_infix(expr))
print(evaluate_infix("3 + 4 * 2"))           # Output: 11
print(evaluate_infix("(3 + 4) * 2"))         # Output: 14
print(evaluate_infix("10 + (6 / 2) * 3"))    # Output: 19

