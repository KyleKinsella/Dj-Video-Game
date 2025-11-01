class Dj:
    def __init__(self, name, age, gender, location, cost, status):
        self.name = name
        self.age = age
        self.gender = gender
        self.location = location
        self.cost = cost
        self.status = status

    def show(self):
        print("Dj Data:\n")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Location:", self.location)
        print("Cost:", self.cost)
        print("Status:", self.status)