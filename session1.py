class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display(self):
        print(f'brand = {self.brand}, model = {self.model}, year = {self.year}')

cars = [
    Car('Toyota', 'Corolla', 2019),
    Car('Honda', 'Civic', 2018),
    Car('Ford', 'Fiesta', 2017),
    ]

for all in cars:
    all.display()

# cars = []

# while True:
#     brand = str(input("Masukkan merek mobil: "))
#     model = str(input("Masukkan model mobil: "))
#     year = int(input("Masukkan tahun mobil: "))

#     cars.append(Car(brand, model, year))

#     more = input("Apakah Anda ingin menambahkan mobil lain? (y/n): ")
#     if more.lower() != 'y':
#         break