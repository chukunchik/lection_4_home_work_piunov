STROKA = 'Hillel school'    #1.1 срез первых и крайних букв в строке
a = STROKA[:2]
b = STROKA[-2:]
c = a + b
print(c)

STROKA1 = input('Enter text: ')    #1.2 метод % и длинна строки с условием
if len(STROKA1) < 2:
    print('Ваша строка слишком короткая - %s' % STROKA1)
else:
    STROKA2 = STROKA1[:2] + STROKA1[-2:]
    print(STROKA2)

NAME = input('enter the name: ')    #4 изменение регистра букв
NAME1 = NAME.upper()
NAME2 = NAME.lower()
print(NAME1 + ' {}'.format(NAME2))

KORTEG = (1, 2, 3)    #6 удаление из кортежа
KORTEG = list(KORTEG)
KORTEG.remove(KORTEG[len(KORTEG)-1])
KORTEG = tuple(KORTEG)
print(KORTEG)

SPISOK_KORTRGEI = [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]    #7
for i in range(len(SPISOK_KORTRGEI)):
    SPISOK_KORTRGEI[i] = list(SPISOK_KORTRGEI[i])
print(SPISOK_KORTRGEI)




