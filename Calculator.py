#!/usr/bin/env python
# coding: utf-8

# In[ ]:


###### 계산식을 입력 받아 부호에 맞는 계산식을 출력 elif, else 사용
# 10 + 20 -> 10 + 20 = 30 -> 부호는 (+, -, *, /)
# 처음 숫자에 'q' 가 입력되면 프로그램 종료

while True:
    formul = input('계산식을 입력하세요 ex) 10 + 20 > ')
    if formul.upper() == 'Q':
        break
    formul = formul.split()
    if len(formul) == 3 and formul[1] in '+-*/':
        if not (formul[0].isdecimal() or formul[2].isdecimal()):
            print('계산식 및 숫자를 확인해 주세요')
            continue
        a = int(formul[0])
        b = int(formul[2])
        if formul[1] == '+':
            ans = a + b
        elif formul[1] == '-':
            ans = a - b
        elif formul[1] == '*':
            ans = a * b
        else:
            ans = a / b

        print('{} {} {} = {}'.format(formul[0], formul[1], formul[2], ans))
    else:
        print('계산식 및 부호를 확인해 주세요')
print('Program End !!!')

