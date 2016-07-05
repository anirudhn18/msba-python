
class Fraction:
    """Represents a fraction"""
    def __init__(self,num,denom):
        self.num = num
        self.denom = denom
    
    def reduce_fraction(self):        
        gcd = 1        
        for i in range(1,min(self.num,self.denom)+1):
            if self.num%i==0 and  self.denom%i==0:
                gcd = i
    
        print '{}/{} reduced is {}/{}'.\
        format(self.num,self.denom,(self.num/gcd),(self.denom/gcd))



#Main program
numerator = int(raw_input('Numerator: '))
denominator = int(raw_input('Denominator: '))

while denominator == 0 :
    print 'Denominator cannot be zero!'
    denominator = int(raw_input('Denominator: '))


fraction = Fraction(numerator,denominator)
fraction.reduce_fraction()