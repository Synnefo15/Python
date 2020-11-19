class employee:

    num_of_emp = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first+'_'+self.last+'@gmail.com'

        employee.num_of_emp += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay*raise_amount)
    
    


emp_1 = employee('rafi', 'cahya', 200)
emp_2 = employee('gilang', 'panji', 210)

print('jml pegawai:', employee.num_of_emp)
print('emp_1:', emp_1.__dict__)
print('emp_2:', emp_2.email)
