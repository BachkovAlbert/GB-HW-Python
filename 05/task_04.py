# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def rle_algorithm(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

def recovery_data(txt):
    num = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            num += txt[i]
        else:
            res = res + txt[i] * int(num)
            num = ''
    return res

def write_file(n, f):
    with open(n, 'w') as file:
        file.write(f)

def read_file(n):
    with open(n, 'r') as file:
        text = file.read()
    return text

write_file(('rle_text(05_task_04).txt'), rle_algorithm(read_file('text(05_task_04).txt')))

print(read_file('text(05_task_04).txt'))
print(rle_algorithm(read_file('text(05_task_04).txt')))
print(recovery_data(read_file('rle_text(05_task_04).txt')))
