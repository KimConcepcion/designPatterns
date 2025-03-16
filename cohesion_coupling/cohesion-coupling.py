import string
import random

class VehicleRegistry:
    def generate_vehicle_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))
    
    def generate_vehicle_license(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"

class Application:

    def register_vehicle(self, brand:str):
        # Create a registry instance
        registry = VehicleRegistry()

        # Generate vehicle id of length 12
        vehicle_id = registry.generate_vehicle_id(12)

        # Generate vehicle license
        license_plate = registry.generate_vehicle_license(vehicle_id)

        # Determinte catalogue price
        catalogue_price = 0
        if brand == 'Tesla Model s':
            catalogue_price = 90000
        elif brand == 'BMW M3':
            catalogue_price = 75000
        elif brand == 'Nissan GTR':
            catalogue_price = 80000
        
        # Determine tax percentage (default 5% of catalogue price, except for electric cars where it is 2%)
        tax_percentage = 0.05
        if brand == 'Tesla Model s':
            tax_percentage = 0.02
        
        # Calculate tax
        payable_tax = tax_percentage * catalogue_price

        # Print vehicle registration information
        print('Registration complete. Vehicle information:')
        print(f'Brand: {brand}')
        print(f'Id: {vehicle_id}')
        print(f'License: {license_plate}')
        print(f'Payable Tax: {payable_tax}')

app = Application()
app.register_vehicle('Nissan GTR')



