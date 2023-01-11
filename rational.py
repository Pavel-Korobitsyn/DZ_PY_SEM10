def operation_rational(oper, one_number, two_number):
    if oper in '+-/*':
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
                result = '\nОшибка: Деление на ноль запрещено.'
    return result