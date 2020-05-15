import math
import operator

from pip._vendor.distlib.compat import raw_input

ops = {'+':operator.add,
       '-':operator.sub,
       '*':operator.mul,
       '/':operator.truediv,
       '^':operator.pow,
       'sin':math.sin,
       'tan':math.tan,
       'cos':math.cos,
       'pi':math.pi}

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

def calculate(equation):
    stack = []
    result = 0
    for i in equation:
        if is_number(i):
            stack.insert(0,i)
        else:
            if len(stack) < 2:
                print('Error: insufficient values in expression')
                break
            else:
                print('stack: %s' % stack)
                if len(i) == 1:
                    n1 = float(stack.pop(1))
                    n2 = float(stack.pop(0))
                    result = ops[i](n1,n2)
                    stack.insert(0,str(result))
                else:
                    n1 = float(stack.pop(0))
                    result = ops[i](math.radians(n1))
                    stack.insert(0,str(result))
    return result

def main():
    running = True
    while running:
        equation = raw_input('enter the equation: ').split(' ')
        answer = calculate(equation)
        print('RESULT: %f' % answer)
        again = raw_input('\nEnter another? ')[0].upper()
        if again != 'Y':
            running = False

if __name__ == '__main__':
    main()

# enter the equation: 5 8 2 15 * sin * + 2 45 tan + /
# stack: ['15', '2', '8', '5']
# stack: ['30.0', '8', '5']
# stack: ['0.5', '8', '5']
# stack: ['4.0', '5',]
# stack: ['45', '2', '9.0']
# stack: ['1.0', '2', '9.0']
# stack: ['3.0', '9.0']
