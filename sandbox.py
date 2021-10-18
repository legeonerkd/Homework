# Задачи

# 1. list (array)
# 2. linked list
# 3. dictionary (dict)
# 4. trees (binary trees)


# complexity - сложность алгоритма
# => time complexity
# => space complexity

# O(n) - алгоритм работает пропорционально количеству элементов
# O(1) - время работы алгоритма не зависит от количества элементов

#             best_case       middle_case            worst_case
# array
#     find:      O(1)     O((1/2) * n) = O(n)           O(n)

# import time
# from datetime import datetime

# def measure_execution_time(fn):
#     def wrapper(*args):
#         start = datetime.now()
#         result = fn(*args) # => True / False
#         delta = datetime.now() - start
#         total_microseconds = delta.seconds * 1000000 + delta.microseconds
#         print('function %s: %.3f mcs' % (fn.__name__, total_microseconds))
#         return result #! После return функция прекращает выполнение
#     return wrapper

# @measure_execution_time
# def binary_search(array, elem):
#     left = 0
#     right = len(array) - 1 
#     while left <= right:
#         middle_index = (left + right) // 2
#         if elem == array[middle_index]:
#             return True 
#         elif elem > array[middle_index]:
#             left = middle_index + 1
#         else:
#             right = middle_index - 1 
#     return False

# @measure_execution_time
# def linear_search(array, required_elem):
#     for elem in array:
#         if elem == required_elem:
#             return True
            
#     return False

# # items = [i for i in range(1, 1_000_000+1)]
# # count = 100
# # start = datetime.now()
# # binary_search(items, 999999)
# # delta = datetime.now() - start
# # total_microseconds = delta.seconds * 1000000 + delta.microseconds
# # print(total_microseconds / count)


# # items = [i for i in range(1, 1_000_000+1)]
# # count = 100
# # start = datetime.now()
# # linear_search(items, 999999)
# # delta = datetime.now() - start
# # total_microseconds = delta.seconds * 1000000 + delta.microseconds
# # print(total_microseconds / count)
# #print(items)

# def generate_array():
#     array = [i for i in range(1, 100_000_000+1)]
#     return array
    
# # # def measure_execution_time(fn = binary_search, *args = [array, 723_456]):
# # # from timeit import default_timer as timer
# # # from datetime import timedelta


# # def measure_execution_time(fn, *args):
# #     # fn(*[array, 723_456] => array, 723_456)
# #     start = time.time()
# #     result = fn(*args)
# #     stop = time.time()
# #     print('{:s} function took {:.3f} ms'.format(fn.__name__, (stop-start)*1000.0))
# #     # print(description, timedelta(seconds=end-start), 's')
# #     return result



# # # Wrapper - обертка


# # # array = [3, 5, 11, 85, 100, 500]
# # array = generate_array()

# # # print(measure_execution_time('Linear search: ', linear_search, array, 723_456))
# # print(measure_execution_time(binary_search, array, 723_456))
# # print(binary_search(array, 723_456))

# # print(binary_search(array, 723_456))
# # print(linear_search(array, 723_456))

# # # print(binary_search(array, 86))
# # print(binary_search(array, 1_000_233))
# # print(linear_search(array, 1_000_233))
# # from typing import List

# # nums: List[int] = [1, 2, 3, 4]
# # count = 0

# # # [] list()
# # # occurrences = dict() / {}

# # occurrences = dict()

# # #! occurrences[num] => value
# # #! if num is not available, KeyError
# # # occurrences.get(key) => value
# # #! if num is not available, => None
# # # if value is None

# # # print(occurrences[num])
# # # occurrences[num] = 5

# # for num in nums:
# #     # if occurrences.get(num) is None
# #     if num not in occurrences:
# #         occurrences[num] = 1
# #     else:
# #         count += occurrences[num]
# #         occurrences[num] += 1
# # print(count)

# array = generate_array()

# print(binary_search(array, 723_456))
# print(linear_search(array, 723_456))


# import time

# @measure_execution_time
# def wait():
#    time.sleep(1) 
   
# wait()


#from abc import ABC, abstractmethod


# class Observer(ABC):
#     @abstractmethod
#     def update(self, state):
#         pass


# # ConcreteObserver
# class TextObserver(Observer):
#     def __init__(self, name):
#         self.name = name

#     def update(self, state):
#         print(self.name + ": " + state)


# # Subject
# class TectSubject(ABC):
#     def __init__(self):
#         self.observers = []

#     def attach(self, observer):
#         self.observers.append(observer)

#     def detach(self, observer):
#         self.observers.remove(observer)

#     def notify(self, state):
#         for observer in self.observers:
#             observer.update(state)


# # ConcreteSubject
# class TextEdit(TectSubject):
#     def __init__(self):
#         super().__init__()
#         self.text = ""

#     # SetState(State)
#     def set_text(self, text):
#         self.text = text
#         self.notify(text)

#     def get_text(self):
#         return self.text


# # Client
# observer1 = TextObserver('Friend')
# observer2 = TextObserver('Recrution station')
# observer3 = TextObserver('Mom')

# textEdit = TextEdit()
# textEdit.attach(observer1)
# textEdit.attach(observer2)
# textEdit.attach(observer3)

# textEdit.set_text('I got a diploma')
# # printed:
# # Observer #1: test text
# # Observer #2: test text

from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List, Dict
import math


# class Observer(ABC):
#     @abstractmethod
#     def update(self, topic: str, data: any) -> None:
#         pass


# class Publisher:
#     observers: Dict[str, List[Observer]] = {}
    
#     def attach(self, topic: str, observer: Observer) -> None:
#         if topic not in self.observers:
#             self.observers[topic] = []
#         self.observers[topic].append(observer) # => list of observers

#     def detach(self, topic: str, observer: Observer) -> None:
#         self.observers[topic].remove(observer)

#     def notify(self, topic: str, data: any = None) -> None:
#         for observer in self.observers[topic]:
#             observer.update(topic, data)


# finish_university = 'university.finish'  


# class University(Publisher):
#     pass


# class Friend(Observer):
#     def update(self, topic: str, _: any) -> None:
#         if topic == finish_university:   
#             print('It\'s beer time!')


# class Mom(Observer):
#     def update(self, topic: str, data: any) -> None:
#         if topic == finish_university:    
#             if data == 5:
#                 print('Well done, son!')
#             elif data == 4:
#                 print('Not bad, son!')
#             else:
#                 # print('You\'re able to do this better!')
#                 print('You would be better!')


# class Army(Observer):
#     def update(self, topic: str, _: any) -> None:
#         if topic == finish_university:
#             print('You\'re in the army now!')

 
# if __name__ == "__main__":
#     sharaga = University()
#     igor = Friend()
#     mom = Mom()
#     russian_army = Army()
    
#     sharaga.attach(finish_university, igor)
#     sharaga.attach(finish_university, mom)
#     sharaga.attach(finish_university, russian_army)

#     sharaga.notify(finish_university, 5)







# p = Publisher()
# dmit = Observer()
# igor = Observer()

# p.attach('rock', dmit)
# p.attach('classic', igor)
# p.attach('rock', igor)

# p.notify('rock', 'resurrection .....')

# def summator(arr):
#     sum = 0
#     for i in range(len(arr)):
#         sum += arr[i]
#     return sum

# arr = [5, 3, 0, 0, -5, 3]
# print(summator(arr))

# def summator(arr):
#     sum = 0
#     for i in arr:
#         sum += i
#     return sum

# arr = [5, 3, 0, 0, -5, 3]
# print(summator(arr))

# def is_prime(n):
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             return False
#     return True

# def print_primes(n):
#     for num in range(2, n):
#         if is_prime(num):
#             print(num)
            
# print_primes(12)

# jewels = 'aA'
# stones = 'aAAbbbb'
# result = 0
# for i in range(len(jewels)):
#     result += stones.count(jewels[i])
# print(result)

# nums = [1,2,3,4]
# nums_new = []
# for i in range(0, len(nums), 2):
#     data = [nums[i + 1]] * nums[i]
#     nums_new += data
# print(nums_new)

# n = int(input("Enter number:"))
# temp = n
# rev = 0
# while n > 0:
#     dig = n % 10
#     rev = rev * 10 + dig
#     n //= 10
# if temp == rev:
#     print("The number is a palindrome!")
# else:
#     print("The number isn't a palindrome!")

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, elem: Node):
        if self.head is None:
            self.head = elem
            return 
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = elem
    
    def print(self):
        cur = self.head
        while cur is not None:
            print(cur.val)
            cur = cur.next

    def get_length(self) -> int:
        length = 0
        cur = self.head
        while cur is not None:
            length += 1
            cur = cur.next
        return length

    # def remove_by_value(self, value: int):
    #     # [1, 4, 7, 4, 0, 0]
    #     # arg: 4 (value)
    #     # => [1, 7, 0, 0]
    #     if self.head is None:
    #         return
    #     cur = self.head
    #     while cur is not None and cur.next is not None:
    #         if cur != value and cur.next != value:
    #             return
    #         if cur.next.val == value:
    #             cur.next = cur.next.next
    #         else:
    #             cur = cur.next
    #     if self.head.val == value:
    #         self.head = self.head.next

    def remove_by_value(self, value: int):
        # [1, 4, 7, 4, 0, 0]
        # arg: 4 (value)
        # => [1, 7, 0, 0]
        cur = self.head
        while cur is not None:
            if self.head.val == value:
                self.head = self.head.next
                cur = cur.next
            elif cur.next is not None and cur.next.val == value:
                cur.next = cur.next.next
            else:
                cur = cur.next

    def reverse(self):
        cur = self.head
        prev = None
        while cur is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head = prev
        

        
lst = LinkedList()
lst.add(Node(1))
lst.add(Node(2))
lst.add(Node(3))
lst.add(Node(4))
lst.add(Node(5))
lst.add(Node(6))
lst.add(Node(7))
lst.print()
lst.reverse()
#print('Size: %d' % lst.get_length())

#lst.remove_by_value(3)
lst.print()



# class Node:
#     def __init__(self, val) -> None:
#         self.val = val
#         self.next = None


# class LinkedList:
#     def __init__(self) -> None:
#         self.head = None

#     def add(self, elem: Node):
#         if self.head is None:
#             self.head = elem
#             return
#         cur = self.head
#         while cur.next is not None:
#             cur = cur.next
#         cur.next = elem

#     def print(self):
#         cur = self.head
#         while cur is not None:
#             print(cur.val)
#             cur = cur.next

# lst = LinkedList()
# lst.add(Node(1))
# lst.add(Node(2))
# lst.add(Node(3))
# lst.print()
# hello
