from datetime import datetime

class Employee:
    gender_all=['M','F']
    def __init__(
            self,
            first_name,
            last_name,
            work_email,
            join_date,
            gender,
            salary=0,
            leave_date=None,
            trial_passed=False,
            phone_number=None,
            ):
        if not isinstance(first_name, str):
            raise ValueError('Name shoul be a string')
        self.fname = first_name
        self.lname = last_name
        self.mail = work_email
        date_format='%d.%m.%Y'
        self.jdate = datetime.strptime(join_date,date_format).date()
        self._gender = None
        self.gender = gender
        self.salary = salary
        self._ldate = None
        self.tp = trial_passed
        self.phone = phone_number

    @property
    def full_name(self):
        return self.fname + ' ' + self.lname    
    
    @full_name.setter
    def full_name(self, value):
        self.fname, self.lname = value.split()
    
    def __lt__(self, other):
        return self.salary < other.salary
    
    def __eq__(self, other):
        return self.salary == other.salary
    
    def __len__(self):
        return len(self.full_name)    
    
    def __add__(self,other):
        return self.salary + other
    
    @property
    def gender(self):
        return self._gender
    
    @gender.setter
    def gender(self, value):
        if value not in Employee.gender_all:
            raise ValueError("please enter 'M' or 'F'")
        self._gender = value
    
    @property
    def ldate(self):
        return self._ldate
    
    @ldate.setter
    def ldate(self,value):
        date_format='%d.%m.%Y'
        value_1 = datetime.strptime(value,date_format).date()

        self._ldate = value_1        
    
    def __repr__(self):
        return f"this person is { self.fname} {self.lname} with salary {self.salary}"

a1 = Employee('Armen', 'Karapetyan','mail@mail.ru', '12.01.2001','M')
a2 = Employee('Anna','Vardanyan','nell@mail.ru','24.06.2020','F')
a1.fname='Armenchik'
a1.phone = 876876
a1.salary = 230000
a1.tp='True'
print(a1.tp)
a1.ldate='22.01.2021'
print(a1.ldate.year)
a_sal = a1 + 2000
print(len(a1))
print(a_sal)
print(a1)
print(a1.gender)
