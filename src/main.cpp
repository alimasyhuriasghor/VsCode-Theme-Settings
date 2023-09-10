#include <iostream>

class Employee {
    public:
    std::string name;
    int age;
    int salary;

    Employee(std::string name, int age, int salary) {
        Employee::name = name;
        Employee::age = age;
        Employee::salary = salary;

        std::cout << Employee::name << std::endl;
        std::cout << Employee::age << std::endl;
        std::cout << Employee::salary << std::endl;
    }
};

int main(int argc, char const *argv[])
{
    Employee employee1 = Employee("Pace",20,7000);
    Employee employee2 = Employee("Gerry",17,5000);

    std::cin.get();
    return 0;
}
