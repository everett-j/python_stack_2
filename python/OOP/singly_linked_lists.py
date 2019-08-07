class SLNode:
    def __init__ (self, value)
        self.val = value 
        self.next = None

class SList:
    def __init__ (self):
        self.head = None
    def addToFront (self, val)
        new_node = SLNode(val)
        new_node.next = self.head
        self.head = new_node
    def print_values(self):
    runner = self.head
        while (runner != None):
            print(runner.value)
        runner = runner.next 	
        return self	     
    def add_to_back(self, val):
            if self.head == None:	
                self.add_to_front(val)
        	return self	
            new_node = SLNode(val)
            runner = self.head
            while (runner.next != None):
                runner = runner.next
            runner.next = new_node	
            return self  
    

my_list = SList()

my_list.addToFront("jim").addToFront("Dwight").addToFront("andy").add_to_back("Pam")


            