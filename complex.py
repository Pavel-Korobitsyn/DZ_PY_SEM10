def operation_complex(oper, one_number, two_number):
    one_complex = False
    two_complex = False
    result = ''
    try:
        one_number = complex(one_number)
        one_complex = True
    except ValueError:
        result = '\nОшибка: число 1 не комплексное'
    try:
        two_number = complex(two_number)
        two_complex = True
    except ValueError:
        result = (f'{result}\nОшибка: число 2 не комплексное')

    if oper in '+-/*' and one_complex and two_complex:
        if oper == '+':
                result = one_number + two_number
        if oper == '-':
                result = one_number - two_number
        if oper == '*':
            result = one_number * two_number
        if oper == '/':
            try:
                result = one_number / two_number
            except:
                result = 'Деление на ноль запрещено'
        
    return result
