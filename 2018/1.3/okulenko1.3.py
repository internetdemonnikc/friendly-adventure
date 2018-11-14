class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

infixexpr = input()
prec = {}
prec["^"] = 4
prec["*"] = 3
prec["/"] = 3
prec["+"] = 2
prec["-"] = 2
prec["("] = 1
opstack = Stack()
postfixlist = []
tokenlist = infixexpr.split()

for token in tokenlist:
    if token in "0123456789":
        postfixlist.append(token)
    elif token == '(':
        opstack.push(token)
    elif token == ')':
        toptoken = opstack.pop()
        while toptoken != '(':
            postfixlist.append(toptoken)
            toptoken = opstack.pop()

    else:
        while (not opstack.isEmpty()) and (prec[opstack.peek()] >= prec[token]):

            postfixlist.append(opstack.pop())
        opstack.push(token)

while not opstack.isEmpty():

    postfixlist.append(opstack.pop())
k = " ".join(postfixlist)


print(k)



ops = { '+': (lambda a,b: a + b),
        '-': (lambda a,b: a - b),
        '*': (lambda a,b: a * b),
        '/': (lambda a,b: a / b),
        '^': (lambda a,b: a ** b)
}

stack = []
for token in k:
    if set(token).issubset(set("0123456789.")):
        stack.append(float(token))
    elif token in ops:
        if len(stack) < 2:
            raise ValueError('Must have at least two parameters to perform op')
        arg1 = stack.pop()
        arg2 = stack.pop()
        op = ops[token]
        stack.append(op(arg2,arg1))

print(stack)

