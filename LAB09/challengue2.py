class TreeNode:
    """Nodo para los árboles de expresión"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class ExpressionTree:
    """Implementación de árbol de expresión"""
    
    def __init__(self):
        self.root = None
    
    @classmethod
    def from_infix(cls, tokens):
        """Construye un árbol de expresión a partir de notación infija"""

        postfix = infix_to_postfix(tokens)
    
        def build_tree_from_postfix(postfix):

            stack = []
    
            for token in postfix:
                node = TreeNode(token)
                if token in ['+', '-', '*', '/']:
                    node.right = stack.pop()
                    node.left = stack.pop()
                stack.append(node)
            

            return stack[0] if stack else None
        

        tree = cls()

        tree.root = build_tree_from_postfix(postfix)
        return tree

def infix_to_postfix(tokens):
    """Convierte una expresión infija a notación postfija"""
    operadores = []
    resultado = []
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2}
    
    for token in tokens:
        if token not in ['+', '-', '*', '/', '(', ')']:
            resultado.append(token)
        elif token == '(':
            operadores.append(token)
        elif token == ')':
            while operadores and operadores[-1] != '(':
                resultado.append(operadores.pop())
            if operadores and operadores[-1] == '(':
                operadores.pop()
        else:
            while (operadores and operadores[-1] != '(' and
                   (operadores[-1] in precedencia) and
                   (precedencia.get(operadores[-1], 0) >= precedencia.get(token, 0))):
                resultado.append(operadores.pop())
            operadores.append(token)
    
    while operadores:
        resultado.append(operadores.pop())
        
    return resultado

tree1 = ExpressionTree.from_infix(['2', '+', '3'])
print(tree1.root.value == '+' and tree1.root.left.value == '2' and tree1.root.right.value == '3')

tree2 = ExpressionTree.from_infix(['2', '+', '3', '*', '4'])
print(tree2.root.value == '+' and tree2.root.right.value == '*')

tree3 = ExpressionTree.from_infix(['(', '2', '+', '3', ')', '*', '4'])
print(tree3.root.value == '*' and tree3.root.left.value == '+')

tree4 = ExpressionTree.from_infix(['x', '+', 'y', '*', 'z'])
print(tree4.root.value == '+' and tree4.root.right.value == '*')

tree5 = ExpressionTree.from_infix(['(', 'a', '+', 'b', ')', '/', '(', 'c', '-', 'd', ')'])
print(tree5.root.value == '/' and tree5.root.left.value == '+' and tree5.root.right.value == '-')