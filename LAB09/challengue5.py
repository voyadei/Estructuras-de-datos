class ExpressionNode:
    """Nodo del árbol de expresiones"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def is_operator(self):
        return self.value in ['+', '-', '*', '/']


class ExpressionTree:
    """Árbol de expresiones con método para simplificar"""
    def __init__(self, root=None):
        self.root = root

    def simplify(self):
        """Simplifica el árbol de expresiones"""
        self.root = self._simplify_helper(self.root)

    def _simplify_helper(self, node):
        if node is None:
            return None

        if not node.is_operator():
            return node

        # Simplifica recursivamente los hijos
        node.left = self._simplify_helper(node.left)
        node.right = self._simplify_helper(node.right)

        # Si ambos hijos son constantes
        if (node.left and not node.left.is_operator() and
                node.right and not node.right.is_operator()):
            try:
                left_val = float(node.left.value)
                right_val = float(node.right.value)

                # Evaluar operación
                if node.value == '+':
                    result = left_val + right_val
                elif node.value == '-':
                    result = left_val - right_val
                elif node.value == '*':
                    result = left_val * right_val
                elif node.value == '/':
                    if right_val == 0:
                        return node  # evitar división por cero
                    result = left_val / right_val

                result_str = str(int(result)) if result == int(result) else str(result)
                return ExpressionNode(result_str)
            except ValueError:
                return node  # si no son numéricos (variables)

        return node


# 🚀 TEST CASES

# Test 1: All constants (2 + 3) => 5
const_tree = ExpressionTree(ExpressionNode('+'))
const_tree.root.left = ExpressionNode('2')
const_tree.root.right = ExpressionNode('3')
const_tree.simplify()
print("Test 1:", const_tree.root.value == '5' and const_tree.root.left is None and const_tree.root.right is None)

# Test 2: Partial simplification ((2 + 3) * x) => (5 * x)
partial_tree = ExpressionTree(ExpressionNode('*'))
add = ExpressionNode('+')
add.left = ExpressionNode('2')
add.right = ExpressionNode('3')
partial_tree.root.left = add
partial_tree.root.right = ExpressionNode('x')
partial_tree.simplify()
print("Test 2:", partial_tree.root.value == '*' and
      partial_tree.root.left.value == '5' and
      partial_tree.root.right.value == 'x')

# Test 3: No simplification (x + y)
no_simp_tree = ExpressionTree(ExpressionNode('+'))
no_simp_tree.root.left = ExpressionNode('x')
no_simp_tree.root.right = ExpressionNode('y')
no_simp_tree.simplify()
print("Test 3:", no_simp_tree.root.value == '+' and
      no_simp_tree.root.left.value == 'x' and
      no_simp_tree.root.right.value == 'y')

# Test 4: Fully simplify ((2 * 3) + (8 / 4)) => 6 + 2 => 8
complex_tree = ExpressionTree(ExpressionNode('+'))
mult = ExpressionNode('*')
div = ExpressionNode('/')
mult.left = ExpressionNode('2')
mult.right = ExpressionNode('3')
div.left = ExpressionNode('8')
div.right = ExpressionNode('4')
complex_tree.root.left = mult
complex_tree.root.right = div
complex_tree.simplify()
print("Test 4:", complex_tree.root.value == '8' and
      complex_tree.root.left is None and complex_tree.root.right is None)

# Test 5: Mixed variables and constants (x * (6 / 2)) => x * 3
mixed_tree = ExpressionTree(ExpressionNode('*'))
div = ExpressionNode('/')
div.left = ExpressionNode('6')
div.right = ExpressionNode('2')
mixed_tree.root.left = ExpressionNode('x')
mixed_tree.root.right = div
mixed_tree.simplify()
print("Test 5:", mixed_tree.root.value == '*' and
      mixed_tree.root.left.value == 'x' and
      mixed_tree.root.right.value == '3')
