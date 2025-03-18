from abc import ABC, abstractmethod

# Abstract Class
class Vehicle(ABC):
    def __init__(self, registration_number, weight):
        self.registration_number = registration_number
        self.weight = weight

    @abstractmethod
    def calculate_fee(self):
        pass