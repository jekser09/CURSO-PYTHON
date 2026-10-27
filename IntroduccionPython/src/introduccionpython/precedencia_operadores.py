'''
Determina la jerarquia de los operadores
1. Operador de parentesis ()
2. Exponente **
3. Unarios +x, -x, ~x, not x
4. Multiplicacion, division, div entera, div modulo *, /, //, %
5. Suma y Resta +,-
6. Comparacion ==, !=, <, <=, >, >=
7. Operadores logicos not, and y or
8. Operadores de asignacion =, +=, -=, /=, %=, //=, **=
'''
resultado = 5 + 3 * 2 ** 2 #17
resultado = (5 + 3) * 2 ** 2 #32