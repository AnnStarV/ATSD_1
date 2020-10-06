import eel
import datetime
import copy
import random


# eel.init("web")
# eel.start("index.html", size=(700, 700))

class Blog(object):
    def __init__(self, numb=1, title=None, text=None, tag=None, dat=datetime.date(2012, 12, 14), amount=0):
        # numb = input('Numb: ')
        self.numb = numb
        # title = input('Title: ')
        self.title = title
        # text = input('Text: ')
        self.text = text
        # tag = input('Tag: ')
        self.tag = tag
        # dat = input('Date: ')
        self.dat = dat
        # amount = input('Amount: ')
        self.amount = amount

    def __str__(self):
        print('Number: ', self.numb, '\nTitle: ', self.title, '\nText: ', self.text, '\nTag: ', self.tag, '\nDate: ',
              self.dat, '\nAmount: ', self.amount)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def push_start(self, new_el):
        new_list = Node(new_el)
        new_list.next = self.head  # след. эл.  = NULL, если уже что-то лежит, то пред.элемент = новому, а новый
        if self.head is not None:
            self.head.prev = new_list
        self.head = new_list

    def push_in(self, prev_el, new_el):
        new_list = Node(new_el)

        while self.head.prev is not None:
            self.head = self.head.prev
        while self.head is not None:
            if self.head.data is prev_el:
                new_list.prev = self.head
                new_list.next = self.head.next
                self.head.next = new_list
                self.head = new_list
                if self.head.next is not None:
                    self.head = self.head.next
                    self.head.prev = new_list
                return
            self.head = self.head.next
        print("Data isn`t exist! ")

    def delete(self, del_el):
        del_el_list = Node(del_el)

        while self.head.prev is not None:
            self.head = self.head.prev
        while self.head is not None:
            if self.head.data is del_el:
                if self.head.prev is not None and self.head.next is not None:
                    del_el_list.next = self.head.next
                    del_el_list.prev = self.head.prev

                    self.head = self.head.prev
                    self.head.next = del_el_list.next
                    self.head = del_el_list
                    self.head = self.head.next
                    self.head.prev = del_el_list.prev
                    return
                elif self.head.prev is None:
                    del_el_list.next = self.head.next

                    self.head = self.head.next
                    self.head.prev = None

                    return
                elif self.head.next is None:
                    del_el_list.prev = self.head.prev

                    self.head = self.head.prev
                    self.head.next = None

                    return
            self.head = self.head.next
        print("Data isn`t exist! ")

    def find(self, find_el):

        while self.head.prev is not None:
            self.head = self.head.prev

        while self.head.next is not None:
            if self.head.data == find_el:
                print('Element exist!')
                return
            self.head = self.head.next

        print('Element doesn`t exist!')

    def print_asc(self, double_list):
        if double_list:
            while double_list.prev is not None:
                double_list = double_list.prev
            while double_list is not None:
                print(double_list.data)
                double_list = double_list.next

    def print_desk(self, double_list):
        if double_list:
            while double_list.next is not None:
                double_list = double_list.next
            while double_list is not None:
                print(double_list.data)
                double_list = double_list.prev

    def clear(self):
        self.__init__()


class BinHeap:
    def __init__(self):
        self.heaplist = []
        self.heapsize = 0

    def left(self, i):
        return i * 2 + 1

    def right(self, i):
        return i * 2 + 2

    def heapify(self, i):   #упорядочение кучи
        l = self.left(i)
        r = self.right(i)
        # Знаки
        if l <= self.heapsize and self.heaplist[l] > self.heaplist[i]:
            largest = l
        else:
            largest = i
        # Знаки и последний индекс
        if r <= self.heapsize and self.heaplist[r] > self.heaplist[largest]:
            largest = r
        if largest != i:
            # Обмен значениями явный
            tmp = self.heaplist[i]
            self.heaplist[i] = self.heaplist[largest]
            self.heaplist[largest] = tmp
            self.heapify(largest)

    def buildHeap(self, list):          #построение кучи
        self.heaplist = list
        self.heapsize = len(list) - 1
        for i in range(len(list) // 2, -1, -1):
            self.heapify(i)

    def insert(self, k):
        self.heaplist.append(k)
        self.heapsize = self.heapsize + 1
        self.percUp(self.heapsize)

    def percUp(self, i):
        while i // 2 > 0:
            if self.heaplist[i] < self.heaplist[i // 2]:
                tmp = self.heaplist[i // 2]
                self.heaplist[i // 2] = self.heaplist[i]
                self.heaplist[i] = tmp
            i = i // 2

    def delel(self, elem):
        lenght = self.heapsize
        for i in range(lenght):
            if(self.heaplist[i]==elem):
                del self.heaplist[i]

    def bubble_sort(nums):
        # Устанавливаем swapped в True, чтобы цикл запустился хотя бы один раз
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    # Меняем элементы
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    # Устанавливаем swapped в True для следующей итерации
                    swapped = True

    # Проверяем, что оно работает
    random_list_of_nums = [5, 2, 1, 8, 4]
    bubble_sort(random_list_of_nums)
    print(random_list_of_nums)

    def __str__(self):
        print(self.heaplist)


heap = BinHeap()
heap.buildHeap([3, 9, 2])
heap.__str__()
heap.insert(7)
heap.buildHeap(heap.heaplist)
heap.__str__()
heap.delel(7)
heap.buildHeap(heap.heaplist)
heap.__str__()

# el = Blog()
# L = LinkedList()
# L.insert(1)
#
# print(L.__str__())

# el = Blog(2, '222', '222', '222', '222', '222')


# L = LinkedList()
# L.push_start(1)
# L.push_start(2)
# L.push_start(3)
#
# L.__str__(L.head)
#
# print('\n\n')
# L.clear()
# L.push_start(0)
# L.push_start(1)
# L.push_start(2)
#
# L.print_desk(L.head)
