class Employee:
    def __init__(self,name: str, age: int, salary: int) -> None:
        self.name = name
        self.age = age
        self.salary = salary

    @staticmethod
    def check_age(age: int) -> None:
        if age < 18:
            print(f"Age must be above 18 years old to get a job not {age} years old!!")

    def display_employee(self):
        return f"Name: {self.name} Age: {self.age} Years Old And Has Salary For About {self.salary}$"

if __name__ == '__main__':
    employee1 = Employee("Gerry",19,5000)
    employee2 = Employee("Mogi",16,10000)

    print(employee1.display_employee())
    employee1.check_age(employee1.age)

    print(employee2.display_employee())
    employee2.check_age(employee2.age)

    

