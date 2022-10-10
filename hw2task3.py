with open('2.txt', 'r', encoding='utf-8') as file_1:
    text_1 = file_1.readlines()
    count_1 = 0
    for a in text_1:
        count_1 += 1
    print('2.txt')
    print(count_1)
    for a in text_1:
        print(a)
with open('1.txt', 'r', encoding='utf-8') as file_2:
    text_2 = file_2.readlines()
    count_2 = 0
    for b in text_2:
        count_2 += 1
    print('1.txt')
    print(count_2)
    for b in text_2:
        print(b)
with open('3.txt', 'r', encoding='utf-8') as file_3:
    text_3 = file_3.readlines()
    count_3 = 0
    for c in text_3:
        count_3 += 1
    print('3.txt')
    print(count_3)
    for c in text_3:
        print(c)



