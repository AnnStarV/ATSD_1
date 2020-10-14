from heapq import heapify

import eel
import datetime
import json
import copy
import random


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
        del_el_list = Node(int(del_el))

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
                    return L.print_asc(L.head)
                elif self.head.prev is None:
                    del_el_list.next = self.head.next

                    self.head = self.head.next
                    self.head.prev = None

                    return L.print_asc(L.head)
                elif self.head.next is None:
                    del_el_list.prev = self.head.prev

                    self.head = self.head.prev
                    self.head.next = None

                    return L.print_asc(L.head)
            self.head = self.head.next
        k = "Data isn`t exist! "
        return k

    def find(self, find_el):
        k = 0;
        while self.head.prev is not None:
            self.head = self.head.prev

        while self.head is not None:
            if self.head.data == int(find_el):
                print_find = ('Element exist in pos: ' + str(k + 1))
                return print_find
            self.head = self.head.next
            k += 1
        print_find = 'Element doesn`t exist!'
        return print_find

    def print_asc(self, double_list):
        list = []
        if double_list:
            while double_list.prev is not None:
                double_list = double_list.prev
            while double_list is not None:
                list.append(double_list.data)
                double_list = double_list.next
            return list

    def print_desk(self, double_list):
        list = []
        if double_list:
            while double_list.next is not None:
                double_list = double_list.next
            while double_list is not None:
                list.append(double_list.data)
                double_list = double_list.prev
            return list

    def clear(self):
        self.__init__()


class BinHeap(object):
    def __init__(self):
        self.heaplist = []
        self.heapsize =0
    def heapify(self, arr, n, i):
        largest = i  # Initialize largest as root
        l = 2 * i + 1  # left = 2*i + 1
        r = 2 * i + 2  # right = 2*i + 2

        # Проверяем существует ли левый дочерний элемент больший, чем корень

        if l < n and arr[i] < arr[l]:
            largest = l

        # Проверяем существует ли правый дочерний элемент больший, чем корень

        if r < n and arr[largest] < arr[r]:
            largest = r

        # Заменяем корень, если нужно
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # свап

            # Применяем heapify к корню.
            self.heapify(arr, n, largest)

    def heapSort(self, arr):
        self.heapsize  = len(arr)
        self.heaplist = arr
        # Построение max-heap.
        for i in range(self.heapsize, -1, -1):
            self.heapify(self.heaplist, self.heapsize, i)

        # Один за другим извлекаем элементы
        for i in range(self.heapsize - 1, 0, -1):
            self.heaplist[i], self.heaplist[0] = self.heaplist[0], self.heaplist[i]  # свап
            self.heapify(self.heaplist, i, 0)

    def insert(self, k):
        self.heaplist.append(k)
        self.heapsize = self.heapsize + 1
        self.heapSort(self.heaplist)

    def delel(self, elem):
        lenght = self.heapsize
        for i in range(lenght):
            if (self.heaplist[i] == elem):
                del self.heaplist[i]
                return
        return

    def __str__(self):
        return (self.heaplist)



class Sort_struct:
    def __init__(self):
        self.print = False

    def heapify(self, arr, n, i):
        largest = i  # Initialize largest as root
        l = 2 * i + 1  # left = 2*i + 1
        r = 2 * i + 2  # right = 2*i + 2

        # Проверяем существует ли левый дочерний элемент больший, чем корень

        if l < n and arr[i]["views"] < arr[l]["views"]:
            largest = l
        elif l < n and arr[i]["views"] == arr[l]["views"] and arr[i]["date"] < arr[l]["date"]:
            largest = l

        # Проверяем существует ли правый дочерний элемент больший, чем корень

        if r < n and arr[largest]["views"] < arr[r]["views"]:
            largest = r
        elif r < n and arr[largest]["views"] == arr[r]["views"] and arr[largest]["date"] < arr[r]["date"]:
            largest = r

        # Заменяем корень, если нужно
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # свап

            # Применяем heapify к корню.
            self.heapify(arr, n, largest)

    # Основная функция для сортировки массива заданного размера
    def heapSort(self, arr):
        n = len(arr)
        # Построение max-heap.
        for i in range(n, -1, -1):
            self.heapify(arr, n, i)

        # Один за другим извлекаем элементы
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # свап
            self.heapify(arr, i, 0)

    def sort_print(self, arr):
        list = []
        for element in arr:
            list.append(str('\n\n'+element['text'])+'\n'+str(element['views'])+'\n'+str(element['date'])+'\n'+str(element['name']))
        return list[::-1]



eel.init("web")

with open("data.json", "r") as read_file:
    data = json.load(read_file)

list_data = data["articles"]

el = Sort_struct()
el.heapSort(list_data)

# list_data.append({'views': 70})
#
# el.heapSort(list_data)
# el.sort_print(list_data)



L = LinkedList()
L.push_start(1)
L.push_start(2)
L.push_start(3)

heap = BinHeap()
random_list_of_nums = [35, 12, 43, 8, 2]
heap.heapSort(random_list_of_nums)

@eel.expose
def list_print():
    return L.print_asc(L.head)

@eel.expose
def add_el_start_list(el_start):
    L.push_start(int(el_start))
    return list_print()

@eel.expose
def add_el_after_list(addelem_after, el_after):
    L.push_in(int(addelem_after), int(el_after))
    return list_print()
@eel.expose
def el_find_list(elem_find):
    return L.find(elem_find)
@eel.expose
def el_del_list(elem_del):
    return L.delete(int(elem_del))
@eel.expose
def el_print_start():
    return list_print()
@eel.expose
def el_print_end():
    return L.print_desk(L.head)
@eel.expose
def heap_print():
    return heap.__str__()
@eel.expose
def input_array_heap(a, b, c, d):
    arr = [int(a), int(b), int(c), int(d)]
    random_list_of_nums[:] = arr
    return random_list_of_nums
@eel.expose
def sort_array_heap(a, b, c, d):
    arr = input_array_heap(a, b, c, d)
    heap.heapSort(arr)
    return heap.__str__()
@eel.expose
def el_del_heap(el_del):
    heap.delel(int(el_del))
    return heap.__str__()
@eel.expose
def el_add_heap(el_add):
    heap.insert(int(el_add))
    heap.heapSort(random_list_of_nums)
    return heap.__str__()
@eel.expose
def struct_print():
    el.heapSort(list_data)
    return  el.sort_print(list_data)
@eel.expose
def add_el_struct(add_el_number, add_el_name, add_el_text, add_el_tag, add_el_date, add_el_views):
    arr = list_data
    arr.append({'number': int(add_el_number), 'name': add_el_name, 'text': add_el_text, 'tag': add_el_tag,'date':add_el_date, 'views': int(add_el_views)})
    list_data[:] = arr
    el.heapSort(list_data)
    return  el.sort_print(list_data)

eel.start("index.html", size=(1000, 900))
