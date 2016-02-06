oprs = ["+","-","*","/"]
Matrix = None

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def matrix():
    f = open("./spreadsheet.txt","r")
    lineOne = f.readline()
    columnLen = int(lineOne.split(" ")[0])   
    rowLen = int(lineOne.split(" ")[1])
    global Matrix
    Matrix = [[0 for x in range(columnLen)] for x in range(rowLen)] 

    for idx, line in enumerate(f):
        row, column =  divmod (idx, columnLen)
        Matrix[row][column] = line.strip()
        print((row), (column), Matrix[row][column])

def calculator(expression):
    tokens = expression.split(" ");
    if(len(tokens)==1):
        if(isfloat(expression)):
            return float(expression)
        else:
            row = ord(expression[0]) - ord('A')
            column = int(expression[1:])-1
            newExpression = Matrix[row][column]
            return calculator(newExpression)


    stack = list()
    result = 0
    for idx, token in enumerate(tokens):
        if token in oprs:
            right = stack.pop()
            left = stack.pop()
            if(token=="+"):
                result = calculator(left) + calculator(right)
            if(token=="-"):
                result = calculator(left) - calculator(right)
            if(token=='*'):
                result = calculator(left) * calculator(right)
            if(token=="/"):
                result = calculator(left) / calculator(right)
            if(idx<(len(tokens)-1)):
                stack.append(str(result))
        else:
            stack.append(token)
    if(len(stack)==0):
        return result
    else:
        return stack


matrix()
print(calculator ('3 2'))
print(calculator ('A2'))
print(calculator ('4 5 *'))
print(calculator ('A1'))
print(calculator ('A1 B2 / 2 +'))
print(calculator ('3'))
print(calculator ('39 B1 B2 * /'))
