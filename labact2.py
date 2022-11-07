from linkedliststack import Stack


def precedence(operator):
    if (operator == '*' or operator == '/'):
        return 2
    elif (operator == '+' or operator == '-'):
        return 1


def infix_to_postfix(infix):
    opStack = Stack()
    postfix = ''
    operand = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # Scan karakter per karakter dari string infix
    for token in infix:
        # Kasus 1: Jika token adalah operand (A s.d Z), konkatenasi ke akhir postfix.
        if token in operand:
            postfix += token


        # Kasus 2: Jika token sama dengan '(', push ke opStack.
        elif token == '(':
            opStack.push(token)



        # Kasus 3: Jika token sama dengan ')', selama opStack tidak kosong dan top tidak sama dengan '(',
        # pop isi opStack dan konkatenasi ke string postfix.
        # Lalu, pop '(' dari stack.
        elif token == ')':
            while not opStack.isEmpty() and opStack.peek() != '(':
                postfix += opStack.pop()
            opStack.pop()

        elif precedence(token) in (1, 2):
            while not opStack.isEmpty() and opStack.peek() != '(' and precedence(opStack.peek()) >= precedence(token):
                postfix += opStack.pop()
            opStack.push(token)

    # Pop semua yang tersisa dalam stack dan konkatenasi ke akhir string postfix.
    while not opStack.isEmpty():
        postfix += opStack.pop()

    # Kembalikan string postfix.
    return postfix