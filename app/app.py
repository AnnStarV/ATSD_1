import eel
import datetime
import json
import copy
import random


# eel.init("web")
# eel.start("index.html", size=(700, 300))

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


# ---------------------------------------------------------------------------------------------------#

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.data)


# ---------------------------------------------------------------------------------------------------#

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

    def heapify(self, i):  # упорядочение кучи
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

    def buildHeap(self, list):  # построение кучи
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
            if (self.heaplist[i] == elem):
                del self.heaplist[i]

    def heap_sort(self, list):
        self.heaplist = list
        self.heapsize = len(list) - 1

        for i in range(len(list) // 2, -1, -1):
            self.heapify(i)

        for i in range(len(list) // 2, -1, -1):
            self.heaplist[i], self.heaplist[0] = self.heaplist[0], self.heaplist[i]
            self.heapify(i)

    def __str__(self):
        print(self.heaplist)

class Sort_struct:
    def __init__(self):
        self.struct = []
        self.structsize = 0

    def heapify(self, nums, heap_size, root_index):
        # Индекс наибольшего элемента считаем корневым индексом
        largest = root_index
        left_child = (2 * root_index) + 1
        right_child = (2 * root_index) + 2

        # Если левый потомок корня — допустимый индекс, а элемент больше,
        # чем текущий наибольший, обновляем наибольший элемент
        if left_child < heap_size and nums["views"][left_child] > nums["views"][largest]:
            largest = left_child

        # То же самое для правого потомка корня
        if right_child < heap_size and nums["views"][right_child] > nums["views"][largest]:
            largest = right_child

        # Если наибольший элемент больше не корневой, они меняются местами
        if largest != root_index:
            nums["views"][root_index], nums["views"][largest] = nums["views"][largest], nums["views"][root_index]
            # Heapify the new root element to ensure it's the largest
            self.heapify(nums, heap_size, largest)

    def heap_sort(self, nums):
        n = len(nums)
        print(nums)
        # Создаём Max Heap из списка
        # Второй аргумент означает остановку алгоритма перед элементом -1, т.е.
        # перед первым элементом списка
        # 3-й аргумент означает повторный проход по списку в обратном направлении,
        # уменьшая счётчик i на 1
        for i in range(n, -1, -1):
            self.heapify(nums, n, i)

        # Перемещаем корень Max Heap в конец списка
        for i in range(n - 1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.heapify(nums, i, 0)

#
# heap = BinHeap()
# heap.buildHeap([3, 9, 2])
# heap.__str__()
# heap.insert(7)
# heap.buildHeap(heap.heaplist)
# heap.__str__()
# heap.delel(7)
# heap.buildHeap(heap.heaplist)
# heap.__str__()
#
#
# heap_2 = BinHeap()
# random_list_of_nums = [35, 12, 43, 8, 2]
# heap_2.heap_sort(random_list_of_nums)
# heap_2.__str__()
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
# el = HeapSort()
# random_list_of_nums = [35, 12, 43, 8, 51]
# el.heap_sort(random_list_of_nums)
# print(random_list_of_nums)


with open("data.json", "r") as read_file:
        data = json.load(read_file)

list_data = data["articles"]
# print(list_data[1]["tag"])

el = Sort_struct()
el.heap_sort(list_data)
print(list_data)