import re  # регулярные выражения


# Приоритет операций-символов
def op_prior(o):
    if o == '*':
        return 4
    elif o == '/':
        return 3
    elif o == '%':
        return 2
    elif o == '+':
        return 1
    elif o == '-':
        return 1


def opn(expr: str):  # входной параметр -- инфиксная строка арифметического выражения с пробелами!!!
    co = []  # выходная строка
    stack = []  # стек операторов
    tokens = re.split('[ ]+', expr)  # разбиваем в список по пробелам
    for i in tokens:
        if i.isdigit():
            co.append(int(i))  # в стек
        elif i in ['*', '/', '%', '+', '-']:
            token_tmp = ''  # смотрим на вверх стека
            if len(stack) > 0:
                token_tmp = stack[-1]  # смотрим на вверх стека
                while len(stack) > 0 and token_tmp != '(':   # пока стек не пуст и не скобка
                    if op_prior(i) <= op_prior(token_tmp):   # сравнение приоритета
                        co.append(stack.pop())  # если в стеке операция выше,то выталкиваем его в выходную строку
                    else:
                        break
            stack.append(i)  # тогда выйдя из цикла,добавим операцию в стек
        elif i == '(':
            stack.append(i)
        elif i == ')':
            token_tmp = stack[-1]  # смотрим на вверх стека
            while token_tmp != '(':  # пока не всретим открывающию скобку
                co.append(stack.pop())
                token_tmp = stack[-1]  # смотрим на вверх стека внутри цикла
                if len(stack) == 0:
                    raise RuntimeError('V virajenii propushena (')
                if token_tmp == '(':
                    stack.pop()
    while len(stack) > 0:
        token_tmp = stack[len(stack) - 1]
        co.append(stack.pop())
        if token_tmp == '(':
            raise RuntimeError('V virajenii propushena )')
    return co  # вернем постфиксную запись


def count(post_expr: list):
    stack = []
    for i in post_expr:
        if i not in ['*', '/', '%', '+', '-']:
            stack.append(i)
        elif i in ['*', '/', '%', '+', '-']:
            x = stack.pop()
            y = stack.pop()
            stack.append(int(eval(str(y) + str(i) + str(x))))  # тут явно беды с делением и дробными будут наверн
    return stack[-1]


print(count(opn('( 4 * ( 1 + 3 ) ) / 2')))
###########################################
# это конечно, все очень интересно, но команда eval('expr') посчитает это говно в одну строчку
# но для перебора всевозможных выражений постфиксная нотация удобна, спорить не буду
