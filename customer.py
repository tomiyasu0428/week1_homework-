class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return f'"{self.first_name} {self.family_name}"'

    def full_name_2(self):
        return f"{self.first_name} {self.family_name}"

    def entry_fee(self):
        if self.age <= 3:
            return 0
        elif 3 < self.age < 20:
            return 1000
        elif 20 <= self.age < 65:
            return 1500
        elif 65 <= self.age < 75:
            return 1200
        else:
            return 500

    def info_csv(self):
        return f"{self.full_name_2()},{self.age},{self.entry_fee()}"

    def info_csv_tabu(self):
        return f"{self.full_name_2():<18}{self.age:<8}{self.entry_fee():<8}"

    def info_csv_paipu(self):
        return f"{self.full_name_2()}|{self.age}|{self.entry_fee()}"


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
tom = Customer(first_name="Tom", family_name="Ford", age=57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=75)
michelle = Customer(first_name="Michelle", family_name="Tanner", age=3)

print(ken.full_name())
print(tom.full_name())
print(ieyasu.full_name())

print(ken.age)
print(tom.age)
print(ieyasu.age)

print(ken.entry_fee())
print(tom.entry_fee())
print(ieyasu.entry_fee())
print(michelle.entry_fee())

print(ken.info_csv())
print(tom.info_csv())
print(ieyasu.info_csv())
print(michelle.info_csv())

print(ken.info_csv_tabu())
print(tom.info_csv_tabu())
print(ieyasu.info_csv_tabu())
print(michelle.info_csv_tabu())

print(ken.info_csv_paipu())
print(tom.info_csv_paipu())
print(ieyasu.info_csv_paipu())
print(michelle.info_csv_paipu())
