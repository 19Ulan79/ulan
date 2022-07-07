#Создать классы машин допустим (Bmw, Mercedes)
#определить такие атрибуты как (title, model, weight, hp, nm, max_speed, color)
#создать метод start_engine() -> output title + model engine started!
#создать метод stop_engine() -> output title + model engine stoped!
#создать метод info() -> All Info


class Car:
    def __init__(self, title, model, weight, hp, nm, max_speed, color):
        self.title = title
        self.model = model
        self.weight = weight
        self.hp = hp
        self.nm = nm
        self.max_speed = max_speed
        self.color = color
    def start_engine(self):
         print(f'engine on{self.title} {self.model} started')

    def stop_engine(self):
        print(f'engine off {self.title} {self.model} stopped')

    def info(self):
        print(f'All_Info {Nissan.title} {Nissan.model} {Nissan.weight} {Nissan.hp} {Nissan.nm} {Nissan.max_speed} {Nissan.color} \n')
Nissan = Car('Nissan', 'Patrol',2800,220, 5000, 240, 'white' )
Nissan.start_engine()
Nissan.stop_engine()
Nissan.info()