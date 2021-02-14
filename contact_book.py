import time
from datetime import datetime



class Node:
    def __init__(self, value, link=None):
        self.value = value 
        self.link = link 

    def get_value(self):
        return self.value 

    def get_link(self):
        return self.link 

    def set_link(self, new_link):
        self.link = new_link


class LinkedList:
    

    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node 

    def insert_node(self, new_value):
        new_node = Node(new_value)
        new_node.set_link(self.head_node)
        self.head_node = new_node 

    def stringify_list(self):
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != None:
                print(current_node.get_value())
            current_node = current_node.get_link()

    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()
        if value_to_remove in str(current_node.get_value()):
            for i in current_node.get_value().values():
                if i == value_to_remove:
                    self.head_node = current_node.get_link()
        else:
            while current_node:
                next_node = current_node.get_link()
                for i in next_node.get_value().values():
                    if i == value_to_remove:
                        current_node.set_link(next_node.get_link())
                        current_node = None 
                    else:
                        current_node = next_node
                
    
    def tracker(self, string_lst):
        self.string_lst = string_lst 
        current_node = self.get_head_node() 
        while current_node:
            if current_node.get_value() != None:
                self.string_lst.append(current_node.get_value())
            
            current_node = current_node.get_link()
        self.string_lst = self.string_lst
        return self.string_lst
        


playing = None


def intro(name):
    print("Hello " + str(name) + ", here is your contact book")
    time.sleep(1)
    print("Please press /commands to check the commands of your contact book")

    updated_date = datetime.strftime(datetime.now(), " %c ")
    ll = LinkedList("Current date and time: " + str(updated_date))
    print()
    print(ll.stringify_list())
    print("\n")
    playing = True 

    while playing: 
        question = input()
        
        
        if question == "/commands":
            print("Type /add_contact to add a new contact")
            print("Type /remove_contact to remove a contact")
            print("Type /view to view your contact book")
            print("Type /quit to quit the program")
        
        elif question == "/add_contact":
            user_input = input("Name: ")
            telephone = input("Phone Number: ")
            Email = input("Email: ")
            Address = input('Address: ')
            Business_telephone = input("Business Phone Number: ")
            Extra_notes = input("Extra Notes: ")
            ll.insert_node({"Name": user_input, "Phone Number": telephone, "Email": Email, "Address": Address, "Business Phone Number": Business_telephone, "Extra Notes": Extra_notes})
            print("\n")
            print(ll.stringify_list())
            print("\n")
        
        elif question == "/view":
            print(ll.stringify_list())
            print("\n")

        elif question == "/remove_contact":
            user = input("Please enter the name of the contact you want to remove: ")
            for i in ll.tracker([]):
                try:
                    for j in i.values():
                        if user == j:
                            ll.remove_node(user)
                            break
                        else:
                            continue
                except AttributeError:
                    break

        elif question == "/quit":
            break
        
        elif not question == '' or not question == "/view" or not quetsion == "/add_contact" or not question == "/remove_contact":
            print("That command is not valid!")
            print('\n')
            
            
            

            
            
            
          
                





print(intro('name'))








