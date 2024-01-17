'''
1541번 잃어버린 괄호

양수 , + , - , 괄호로 식을 만듦 but 다 지움
괄호를 적절히 쳐서 식의 값을 최소로
'''

math_eq = str(input())

num_list = ''
num = ''
bracket = False


for i in range(len(math_eq)):
    e = math_eq[i]
    if e == '-':
        if not bracket:
            num_list += num + e + '('
            bracket = True
            num = ''

        else:
            num_list += num + ')' + e + '('
            num = ''

    elif e == '+':
        num_list += num + '+'
        num = ''
    else:
        if num == '0':
            num = e
        else:
            num += e

    if i == len(math_eq) - 1:
        num_list += num
        if bracket:
            num_list += ')'

print(eval(num_list))