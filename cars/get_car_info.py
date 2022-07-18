

from cars.create_car import Car
def get_car_info(title,model,color):
    car = Car(
        title=title,
        model=model,
        color=color
)
    return car