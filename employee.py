class Employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.'+last+'@compay.com'

    def ctc(self,sal):
        if sal > self.pay:
            print("sorry over budget")
        else:
            print("our HR Team will get back to you")
        
        
emp = Employee("nisha","singh",5000)

print("{} {} earns {} and her email address is {} for further information".format(emp.first.capitalize(),emp.last.capitalize(),emp.pay,emp.email))
print(emp.ctc(10000))



