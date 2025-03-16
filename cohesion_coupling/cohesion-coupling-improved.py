import string
import random

class VehicleInfo:
    brand: str
    electric: bool
    catalogue_price: int

    def __init__(self, brand, electric, catalogue_price):
        self.brand           = brand
        self.electric        = electric
        self.catalogue_price = catalogue_price

    def compute_tax(self):
        # Determine tax percentage (default 5% of catalogue price, except for electric cars where it is 2%)
        tax_percentage = 0.05
        if self.electric:
            tax_percentage = 0.02
        return tax_percentage * self.catalogue_price
    
    def print(self):
        print(f"Brand: {self.brand}")
        print(f"Payable Tax: {self.compute_tax()}")

class Vehicle:
    id: str
    license_plate:str
    info: VehicleInfo

    def __init__(self, id, license_plate, info):
        self.id            = id
        self.license_plate = license_plate
        self.info          = info

    def print(self):
        print('=============================')
        print(f"Id: {self.id}")
        print(f"License plate: {self.license_plate}")
        self.info.print()

class VehicleRegistry:
    vehicle_info = {}

    def add_vehicle_information(self, brand, electric, catalogue_price):
        self.vehicle_info[brand] = VehicleInfo(brand, electric, catalogue_price)

    def __init__(self):
        self.add_vehicle_information('Tesla Model s', True, 90000)
        self.add_vehicle_information('BMW M3', False, 75000)
        self.add_vehicle_information('Nissan GTR', False, 80000)
        self.add_vehicle_information('BMW I4', True, 85000)
        self.add_vehicle_information('Ionic 5', True, 40000)

    def generate_vehicle_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))
    
    def generate_vehicle_license(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"
    
    def create_vehicle(self, brand):
        # Generate vehicle id of length 12
        vehicle_id = self.generate_vehicle_id(12)

        # Generate vehicle license
        license_plate = self.generate_vehicle_license(vehicle_id)

        return Vehicle(vehicle_id, license_plate, self.vehicle_info[brand])

class Application:

    def register_vehicle(self, brand:str):
        # Create a registry instance
        registry = VehicleRegistry()

        # Create vehicle
        return registry.create_vehicle(brand)


app = Application()

nissan_gtr = app.register_vehicle('Nissan GTR')
nissan_gtr.print()

bmw_m3 = app.register_vehicle('BMW M3')
bmw_m3.print()

bmw_i4 = app.register_vehicle('BMW I4')
bmw_i4.print()
