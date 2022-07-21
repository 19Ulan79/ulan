
import  re
class ValidCarNumber:
    def __init__(self,number):
        self.number = number
    def is_valid (self):
        iss = re.search("0 [0-9]{1}KG([0-9]){3}([A-Z] {2-3})", self.number)
        try:
            if iss.end() ==len(self.number):
                return  "Номер не валидный!"
        except:
            return  "Номер валидный!"
car_number = input('Введите номер машины:' )
num = ValidCarNumber(car_number)
print(num.is_valid())