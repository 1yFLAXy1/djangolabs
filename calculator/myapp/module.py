
def calculate(num1, num2, operation):
    num1 = float(num1)
    num2 = float(num2)
    if operation == 'add':
        result = '{:.3f}'.format(num1 + num2)
    elif operation == 'subtract':
        result = '{:.3f}'.format(num1 - num2)
    elif operation == 'multiply':
        result = '{:.3f}'.format(num1 * num2)
    elif operation == 'divide':
        if num2 == 0:
            return {'error': 'Division by zero is impossible'}
        result = '{:.3f}'.format(num1 / num2)
    elif operation == 'convert':
        if -273 <= num1 <= 273:
            result = '{:.3f}'.format((num1 * 9 / 5) + 32)
        else:
            result = {'error': 'out of range'}
            return result
    else:
        result={'error': 'Unknown operation'}
        return result

    return result
