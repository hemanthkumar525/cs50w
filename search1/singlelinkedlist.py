class node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def display_list(self):
        if self.head is None:
          print('empty list')
        else:
            print('element in the list are:')
            p=self.head
            while p is not None:
                print(p.data,'-->',end="")
                p=p.ref
            print()
    def count_node(self):
        p=self.head
        n=0
        while p is not None:
            n+=1
            p=p.ref
            print("NUmber of node in list is=",n)
    def insert_at_beginning(self,data):
        temp=node(data)
        temp.ref=self.head
        self.head=temp
    def insert_at_end(self,data):
        temp=node(data)
        if self.head is None:
            self.head=temp
            return
        p=self.head
        while p.ref is not None:
            p=p.ref
        p.ref=temp
    def insert_at_position(self,data,k):
        if k==1:
            temp=node(data)
            temp.ref=self.head
            self.head=temp
            return
        p=self.head
        i=1
        while i<k-1 and p is not None:
            p=p.ref
            i+=1
        if p is None:
            print("you cannot insert background position",i)
        else:
            temp=node(data)
            temp.ref=p.ref
            p.ref=temp
    def search(self,x):
        p=self.head
        position=1
        while p is not None:
            if p.data==x:
                print('found element=',x,'at position',position)
                return True
            else:
                p=p.ref
                position+=1
        print("Could not find element=",x)
        return False
    def crete_list(self):
        data=int(input('enter the element tobe inserted:'))
        temp=node(data)
        if self.head is None:
            self.head=temp
            return
        p=self.head
        while p.ref is not None:
            p=p.ref
        p.ref=temp
    def delete_node(self,del_element):
        if self.head is None:
            print('empty list')
            return
        p=self.head
        while p.ref is not None:
            if p.ref is not None:
                if p.ref.data == del_element:
                    break
                p=p.ref
                print("Element",del_element,"is not in the list")
            else:
                p.ref=p.ref.ref
list=singlelinkedlist()
while True:
    print('1. crete a list')
    print('2.insert at beginning of given list')
    print('3. insert an element at one of the list')
    print('4. insert a node of specified position')
    print('5. delete any node')
    print('6. display')
    print('7. count the number of the nodes')
    print('8. serach the elements in the list')
    print('9. quit')
    option=int(input('enter your choice'))
    if option==6:
        list.display_list()
    elif option==7:
        list.count_node()
    elif option==1:
        list.crete_list()
    elif option==8:
        data=int(input("enter the element to be inserted:"))
        list.search(data)
    elif option==3:
        data=int(input('enter the element to be inserted:'))
        list.insert_at_end(data)
    elif option==4:
        data=int(input("enter the element to be inserted:"))
        k=int(input('enter the index number'))
        list.insert_at_position(data,k)
    elif option==5:
        data=int(input("enter the element to be deleted:"))
        list.delete_node(data)
    elif option==2:
        data=int(input("enter the element to be inserted:"))
        list.insert_at_beginning(data)
    elif option==9:
        break
    else:
        print('choose the right option')
        print()