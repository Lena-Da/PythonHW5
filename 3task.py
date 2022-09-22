# Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже, 
# то кортеж остается, его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. 
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
# Cложите получившиеся числа и верните из функции в качестве ответа вместе с преобразованным списком

list_name=["Java", "C", "Python", "Go", "JavaScript"]
list_num=[1,2,3,4,5]


def common_list(list_name,list_num):
    list_name=[elem.upper() for elem in list_name]
    comlist=list(zip(list_name,list_num))
    print("Список кортежей, состоящих из номера и языка: ", comlist)

list_tuple=common_list(list_name,list_num)

def summa_points():
    list_res=[]
    list_res2=[]
    sum_of_points=0
    for i in range(len(list_num)):
        sum_of_points=sum(ord(i) for i in list_name[i])%list_num[i]
        if sum_of_points==0:
            sum_point2=sum(ord(i) for i in list_name[i].upper())
            list_res.append(sum_point2)
            list_res2.append(list_name[i])
            common_list2=list(zip(list_res,list_res2))
            summa_list_res=sum(list_res)
    print("Сумма очков слова имеет в делителях номер, с которым она в паре в кортеже: ", common_list2)
    print("Сумма всех очков: ", summa_list_res)

summa_points()