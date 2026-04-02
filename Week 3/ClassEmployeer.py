class Employeer:
    SALARY_MAX = 50_000_000 

    def __init__(self, name, salary, salary_coefficient):

        self.__NameEmployeer = name
        self.__BasicSalary = salary
        self.__SalaryCoefficient = salary_coefficient

    @property 
    def NameEmployeer (self):
        return self.__NameEmployeer

    @NameEmployeer.setter 
    def NameEmployeer(self, value):
        if not value.strip():
            print("Error: Name cannot be empty!")
        else:
            self.__NameEmployeer = value

    @property 
    def BasicSalary(self):
        return self.__BasicSalary

    @BasicSalary.setter 
    def BasicSalary(self, value):
        if value < 0:
            print("Error: Salary cannot be negative!")
        else:
            self.__BasicSalary = value

    def salary_calculation(self):
        return self.__BasicSalary * self.__SalaryCoefficient

    def salary_increase(self, amount_increased):
        expected_salary = (self.__BasicSalary + amount_increased) * self.__SalaryCoefficient
        
        if expected_salary > Employeer.SALARY_MAX:
            print(f"Warning: New salary ({expected_salary:,.0f}) exceeds the maximum allowed!")
            return False
        
        self.__BasicSalary += amount_increased
        print(f"Successfully increased salary for {self.__NameEmployeer}.")
        return True

    def print_information(self):
        Total_salary = self.salary_calculation()
        print("-" * 40)
        print(f"Employeer: {self.__NameEmployeer}")
        print(f"Basic Salary: {self.__BasicSalary:,.0f} VNĐ")
        print(f"Salary Coefficient: {self.__SalaryCoefficient}")
        print(f"Total Salary: {Total_salary:,.0f} VNĐ")
        print("-" * 40)


E1 = Employeer("Phung Khanh Linh", 100000, 3.0)
E1.print_information()

E1.salary_increase(5000)
E1.print_information()

E1.salary_increase(1000000)