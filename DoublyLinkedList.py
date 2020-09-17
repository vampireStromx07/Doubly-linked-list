class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class doublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.numOfNodes = 0

    def insert_at_end(self, data):
        self.numOfNodes += 1
        new_node = node(data)

        if self.head is None:
            self.head = self.tail = new_node

        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def insert_at_start(self, data):
        self.numOfNodes += 1
        new_node = node(data)

        if self.head is None:
            self.head = self.tail = new_node

        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def __len__(self):
        return self.numOfNodes

    def insert_at_pos(self, data, pos):
        lens = self.numOfNodes
        if pos < 1 or pos > lens:
            print("Invalid Position.\n")

        elif pos == 1:
            self.numOfNodes += 1
            self.insert_at_start(data)
            self.numOfNodes += 1

        else:
            self.numOfNodes += 1
            new_node = node(data)

            i = 1
            temp = self.head

            while i < pos-1:
                temp = temp.next
                i += 1

            new_node.prev = temp
            new_node.next = temp.next
            temp.next = new_node
            new_node.next.prev = new_node.next
            self.numOfNodes += 1

    def insert_aft_pos(self, data, pos):
        lens = self.numOfNodes
        if pos < 1 or pos >= lens:
            print("Invalid Position.\n")

        else:
            self.numOfNodes += 1
            new_node = node(data)

            i = 1
            temp = self.head

            while i < pos:
                temp = temp.next
                i += 1

            new_node.prev = temp
            new_node.next = temp.next
            temp.next = new_node
            new_node.next.prev = new_node.next
            self.numOfNodes += 1

    def remove_from_beg(self):
        if self.head is None:
            print("List is Empty.")

        elif self.head.next is None:
            self.head = self.tail = None
            self.numOfNodes -= 0

        else:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            self.numOfNodes -= 1
            del temp

    def remove_from_end(self):
        if self.tail is None:
            print("List is empty")

        elif self.tail.prev is None:
            self.head = self.tail = None
            self.numOfNodes = 0

        else:
            temp = self.tail
            self.tail.prev.next = None
            self.tail = self.tail.prev
            self.numOfNodes -= 1
            del temp

    def remove_from_pos(self, pos):
        temp = self.head
        i = 1
        count = self.numOfNodes

        if pos < 1 or pos >= count:
            print("Enter a valid position")

        elif pos == 1:
            self.remove_from_beg()
            self.numOfNodes -= 1

        else:
            while i < pos:
                temp = temp.next
                i += 1

            temp.prev.next = temp.next
            temp.next.prev = temp.prev
            temp = None
            self.numOfNodes -= 1

    def reverse_doubly_linked_list(self):
        current = None
        nextNode = None

        if self.head is None:
            return

        else:
            current = self.head
            while current is not None:
                nextNode = current.next
                current.next = current.prev
                current.prev = nextNode
                current = nextNode
            current = self.head
            self.head = self.tail
            self.tail = current
            print("\n")

    def Traverse(self):
        if self.head is None:
            print("List is Empty")
            return

        temp = self.head
        while temp is not None:
            print(f"{temp.data} -->", end='')
            temp = temp.next

        print("\n")


if __name__ == '__main__':

    DLL = doublyLinkedList()

    while True:
        print("<-- Doubly Linked List -->\n"
              "1. Insert_At_End\n"
              "2. Insert_At_Start\n"
              "3. Insert_At_Pos\n"
              "4. Insert_Aft_Pos\n"
              "5. Remove_From_Start\n"
              "6. Remove_From_End\n"
              "7. Remove_From_Pos\n"
              "8. Display_List\n"
              "9. Exit\n"
              "10.Reverse_Doubly_Linked_List")

        print("Enter a choice: ", end='')
        choice = int(input())

        if choice == 1:
            a = input("Enter a data: ")
            DLL.insert_at_end(a)
            print("\n")

        if choice == 2:
            a = input("Enter a data: ")
            DLL.insert_at_start(a)
            print('\n')

        if choice == 3:
            a = input("Enter a data: ")
            b = int(input("Enter a position"))
            DLL.insert_at_pos(a, b)

        if choice == 4:
            a = input("Enter a data: ")
            b = int(input("Enter a position"))
            DLL.insert_aft_pos(a, b)

        if choice == 5:
            DLL.remove_from_beg()

        if choice == 6:
            DLL.remove_from_end()

        if choice == 7:
            a = int(input("Enter a position: "))
            DLL.remove_from_pos(a)

        if choice == 8:
            DLL.Traverse()

        if choice == 9:
            exit()

        if choice == 10:
            DLL.reverse_doubly_linked_list()

