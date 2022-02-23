# Список
# +
# Возможность обратиться по индексу (скорость индексного доступа О(1))
# Последовательный доступ О(n)
# Временная сложность О(n)
# Операции со списком (Добавление в конец О(1), удаление из конца О(1), Добавление и удаление в/из позицию, отличную от конца О(n))

# -
# Временная сложность поиска О(n)



# Связный список
# +
# Вставка и удаление элемента во всех случаях О(1)



# -
# Временная сложность поиска О(n)



# Временная сложность - это зависимость увеличения времени от количества элментов в списке


# a = [1, 2, 3, 4, 5]
# a.append(6)

# a = [5, 'hj', None, 4.88]

# nums1 = [7, 9, 0, -8]
# nums1 = []
# nums2 = [8, 8, 10, 48]
# [7, 9, 0, -8, 8, 8, 10, 48]
# nums3 = nums1 + nums2
# nums1 += nums2
# nums1.append(nums2) # => Данный тип вставки выполняет вставку второго массива как элемента
# print(nums1)
# print(nums1[4])
# print(nums1[4][3])
# try:
#     nums1.pop()
# except IndexError:
#     print('Empty list')

# print(nums1)

# cards = ['2H', '3C', 'AD']
# cards.clear()
# cards = []
# print(cards)

cards = ['2H', '3C', 'AD']
try:
    print(cards.index('3D'))
except ValueError:
    print('No such card')
    
''' Находит сумму чисел '''
def summ(a: int, b: int) -> int:
    pass


# summ
def shuffle(cards):
    # cards = None
    cards[0] = None
    print(cards)
    
# shuffle(cards)
# print(cards)

#  аргументы без "=" обязательные
#  аргументы по умолчанию идут обязательно в конце
# def foo(a, b, c=4, d=8):
#     print(a, b, c, d)

# foo(1, 2, 3, 4) # 1 2 3 4
# foo(1, 2, 3) # 1 2 3 8
# foo(1, 2) # 1 2 4 8
# foo(1) # err
# foo() # err

# tuple -  неизменяемый

# a = [1, 2, 3, 4]
# b = (1, 2, 3, 4) # immutable 
# b[2] = 7

# non-primitive objects для функции создаются единожды (по умолчанию)
# def add(elem, nums=[1, 2, 3, 4]):
#     nums.append(elem)
#     print(nums)
    
# def add(elem, nums=0):
#     if nums == 0:
#         nums = [1, 2, 3, 4]
#     nums.append(elem)
#     print(nums)
   
# nums = [1, 2] 
# add(5, nums)
# add(5)
# add(5)
# add(5)
# add(5)

dic = {
    'Идиот': 'Достоевский',
    'Война и мир': 'Толстой',
}

dic['Война миров'] = 'Уэльс'
# dic['Книга'] = "О'Нил"
# dic['Книга'] = 'О\'Нил'
# dic['Книга'] = "Цитата \"Мой лучший друг как-то сказал\""
# print(dic['Война и мир'])

try:
    print(dic['Война'])
except KeyError:
    print('Book not found')

book = dic.get('Война и мир')
if book is None:
    print('Wrong book')
else:
    print(book)

for key in dic:
    # value => dic[key]
    pass

for key, value in dic.items():
    print(key, value)

