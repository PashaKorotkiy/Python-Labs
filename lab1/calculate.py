def calculate(x, y, operation):
    if operation == 'add':
        try:
            return x + y
        except TypeError:
            pass
    elif operation == 'sub':
        try:
            return x - y
        except TypeError:
            pass
    elif operation == 'mul':
        try:
            return x * y
        except TypeError:
            pass
    elif operation == 'div':
        try:
            return x / y
        except (ZeroDivisionError, TypeError):
            pass
    else:
        return None
