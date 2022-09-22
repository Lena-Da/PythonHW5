# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 'абвгдейка - это передача' = >" - это передача"



str_text='абвгдейка - это передача'
search_text="абв"
new_text=[]

arr_text=str_text.split()

for elem in arr_text:
    if search_text not in elem:
        new_text.append(elem)

new_str=" ".join(new_text)
print(new_str)