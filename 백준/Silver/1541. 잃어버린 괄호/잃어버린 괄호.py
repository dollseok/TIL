
math_eq = input()
start = math_eq[0]
item_list = math_eq.split('-')
result = 0

if start == '-':
    print(item_list)
    for item in item_list[1:]:
        result -= sum(map(int, item.split('+')))

else:
    result += sum(map(int, item_list[0].split('+')))
    for item in item_list[1:]:
        result -= sum(map(int, item.split('+')))

print(result)