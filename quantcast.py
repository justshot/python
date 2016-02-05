
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

    lineNumber = 0
    for line in f:
        row, column =  divmod (lineNumber, columnLen)
        Matrix[row][column] = line.strip()
        lineNumber+=1
        print((row), (column), Matrix[row][column])

def getValue(operand):
    if(isfloat(operand)):
        return float(operand)
    else:
        row = ord(operand[0]) - ord('A')
        column = int(operand[1:])-1
        expression = Matrix[row][column]
        #print("expression",expression)
        return calculator(expression)
        

def calculator(expression):
    tokens = expression.split(" ");
    if(len(tokens)==1):
        return getValue(tokens[0])

    stack = list()
    result = 0
    for i in tokens:
        if i in oprs:
            right = stack.pop()
            left = stack.pop()
            if(i=="+"):
                result = getValue(left) + getValue(right)
            if(i=="-"):
                result = getValue(left) - getValue(right)
            if(i=='*'):
                result = getValue(left) * getValue(right)
            if(i=="/"):
                result = getValue(left) / getValue(right)
            stack.append(str(result))
        else:
            stack.append(i)

    if(len(stack)==0):
       return result
    else:
      return expression
            

def RPN (expression):
    tokens = expression.split(" ")
    stack = list()
    result = 0
    for i in tokens:
        if i in oprs:
            right = stack.pop()
            left = stack.pop()
            if(i=="+"):
                result = left + right
            if(i=="-"):
                result = left - right
            if(i=='*'):
                result = left * right
            if(i=="/"):
                result = left / right
            stack.append(result)
        else:
            stack.append(float(i))
    return result


matrix()
print(calculator ('3 2'))
print(calculator ('A2'))

