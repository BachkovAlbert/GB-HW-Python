# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = 'Мы неабв очень любим Питон иабв Джавабв'

text_find = 'абв'

list1 = text.split(' ')

list2 = [item for item in list1 if text_find not in item]

print(list2)