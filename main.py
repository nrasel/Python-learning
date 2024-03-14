class Employee:
    companyName="Apple"
    noOfEmployees=0
    def __init__(self,name) -> None:
        self.name=name
        self.raise_amount=0.02
    def show(self):
        print(f"The name of the Employee is {self.name} and the raise amount in {self.noOfEmployees} sized {self.companyName} is {self.raise_amount}")

emp1=Employee("Harry")

emp1.raise_amount=30
emp1.companyName="Apple India"
emp1.show()

Employee.companyName="Google"
print(Employee.companyName)

emp2=Employee("Rohan")
emp2.companyName="Nestle"
emp2.show()