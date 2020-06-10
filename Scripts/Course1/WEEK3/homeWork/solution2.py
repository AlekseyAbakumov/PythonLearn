import csv
import os
import sys


class CarBase:
    csv_car_type = 0
    csv_brand = 1
    csv_passenger_seats_count = 2
    csv_photo_file_name = 3
    csv_body_whl = 4
    csv_carrying = 5
    csv_extra = 6

    def vff(self, filename):
        for ext in ['.png', '.jpeg', '.jpg', '.gif']:
            if filename.endswith(ext):
                return filename
        raise ValueError

    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        if brand == '':
            raise ValueError
        self.carrying = float(carrying)
        self.photo_file_name = self.vff(photo_file_name)

    def get_photo_file_ext(self):
        _, ext = os.path.splitext(self.photo_file_name)
        return ext


class Car(CarBase):
    car_type = 'car'

    def __init__(self, brand, photo_file_name, carrying,
                 passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)

    @classmethod
    def instance(cls, col):
        return cls(col[cls.csv_brand],
                   col[cls.csv_photo_file_name],
                   col[cls.csv_carrying],
                   col[cls.csv_passenger_seats_count])


class Truck(CarBase):
    car_type = 'truck'

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        try:
            length, width, height = (float(x) for x in body_whl.split('x', 2))
        except:
            length, width, height = .0, .0, .0
        self.body_length = length
        self.body_width = width
        self.body_height = height

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height

    @classmethod
    def instance(cls, col):
        return cls(col[cls.csv_brand], col[cls.csv_photo_file_name],
                   col[cls.csv_carrying], col[cls.csv_body_whl])


class SpecMachine(CarBase):
    car_type = 'spec_machine'

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra
        if extra == '':
            raise ValueError

    @classmethod
    def instance(cls, col):
        return cls(col[cls.csv_brand], col[cls.csv_photo_file_name],
                   col[cls.csv_carrying], col[cls.csv_extra])


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        dict_cars = {car_class.car_type: car_class for car_class in
                     (Car, Truck, SpecMachine)}
        for col in reader:
            try:
                car_type = col[CarBase.csv_car_type]
            except IndexError:
                continue
            try:
                car_class = dict_cars[car_type]
            except KeyError:
                continue
            try:
                car_list.append(car_class.instance(col))
            except (ValueError, IndexError):
                pass
    return car_list