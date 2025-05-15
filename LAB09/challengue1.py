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

print(infix_to_postfix(['2', '+', '3']) == ['2', '3', '+'])  # Simple
print(infix_to_postfix(['2', '+', '3', '*', '4']) == ['2', '3', '4', '*', '+'])  # Precedencia
print(infix_to_postfix(['(', '2', '+', '3', ')', '*', '4']) == ['2', '3', '+', '4', '*'])  # Paréntesis
print(infix_to_postfix(['(', '1', '+', '2', ')', '*', '(', '3', '-', '4', ')']) == ['1', '2', '+', '3', '4', '-', '*'])  # Complejo
print(infix_to_postfix(['a', '+', 'b', '*', 'c', '/', 'd']) == ['a', 'b', 'c', '*', 'd', '/', '+'])  # Variables