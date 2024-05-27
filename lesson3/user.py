class User:
    
    def __init__(self, first_name, last_name):
        self.firstname = first_name
        self.lastname = last_name
      
    def sayName(self):
        print("Меня зовут: ", self.firstname)  
        
    def sayLastName(self):
        print("Моя фамилия: ", self.lastname)

    def sayFullName(self):
        print("Мое имя и фамилия: ", self.firstname, self.lastname)     
      