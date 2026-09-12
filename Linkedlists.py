class Node():
    def __init__(self,data):
        self.data=data
        self .next=None





append=Node
first=append(1)
second=append(2)
third=append(3)
second.next=third

second.next=first
first.next=third