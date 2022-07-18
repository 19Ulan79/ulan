
class Car:
    def __init__(self,title,model,color):
        self.title = title
        self.model = model
        self.color = color

    def start_engine(self):
        return f"{self.title} start"
    def stop_engine(self):
        return f"{self.title} stop"

    def car_info(self):
        return f"{self.title} {self.model} {self.color}"

