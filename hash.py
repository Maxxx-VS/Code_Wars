# # hash-set
# my_set = set()
# my_set.add(1)
# my_set.add('Igor')
# my_set.add(7)
#
# print(my_set)
# print(1 in my_set)
#
# set2 = {11, 32, 31, "Igor"}
#
# uniot_set = my_set.union(set2)
# print(uniot_set)
#
# dif = my_set.difference(set2)
# print(dif)
#
# # hash-tab
# my_dict = {'apple':1, "banan":2, "orange":3}
# print(my_dict['apple'])
#
# print("orange" in my_dict)
# my_dict["orange"] = 10
#
# print(my_dict)
#
# del my_dict["orange"]
# print(my_dict)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    def prepend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    def delete(self, data):
        if self.is_empty():
            return
        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
    def search(self, data):
        if self.is_empty():
            return  False

        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    def display(self):
        if self.is_empty():
            print("Пусто")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

my_list = LinkedList()
my_list.append("Bim-bim")
my_list.append("Bom-bom")
my_list.append("1")
my_list.prepend("All")


my_list.display()

print(my_list.search("All"))