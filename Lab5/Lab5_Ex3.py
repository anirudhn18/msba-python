
class WageCalculator():
    """Tool to calculate total pay"""
    def cal_gross_pay(self):
        return self.hours*self.wage



a_calculator = WageCalculator()
a_calculator.hours = int(raw_input('Please enter hours : '))
a_calculator.wage = float(raw_input('Please enter wage : '))

print "Total wage is {}.".format(a_calculator.cal_gross_pay())
