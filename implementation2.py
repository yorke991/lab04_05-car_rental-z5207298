from abc import ABC, abstractmethod
class Customer(ABC):
    def __init__(self, name, email, licenseNo, age):
        self._name = name
        self._email = email
        self._licenseNo = licenseNo
        self._age = age

    def get_name(self):
        return self._name;
    def set_name(name):
        self._name = name;

    def get_email(self):
        return self._email;
    def set_email(email):
        self._email = email;

    def get_licenseNo(self):
        return self._licenseNo;
    def set_licenseNo(licenseNo):
        self._licenseNo = licenseNo;

    def get_age(self):
        return self._age;
    def set_age(age):
        self._age = age;

    @abstractmethod
    def cost(self):
        pass

class vehicle(ABC):

    def __init__(self, make, year, registration, model, vehicle_ID, rate):
        self._make = make
        self._year = year
        self._registration = registration
        self._model = model
        self._vehicle_ID = vehicle_ID
        self._rate = rate

    def get_make(self):
        return self._make;
    def set_make(make):
        self._make = make;

    def get_year(self):
        return self._year;
    def set_year(year):
        self._year = year;

    def get_registration(self):
        return self._registration;
    def set_registration(registration):
        self._registration = registration;

    def get_model(self):
        return self._model;
    def set_model(model):
        self._model = model;

    def get_vehicle_ID(self):
        return self._vehicle_ID;
    def set_vehicle_ID(vehicle_ID):
        self._vehicle_ID: vehicle_ID;

    def get_rate(self):
        return self._rate
    def set_rate(rate):
        self._rate = rate;

    def __str__(self):
        return self._rate + "is the rate, and the cost is: "


# class small(vehicle):
#     def __init__(self, make, year, registration, model, vehicle_ID, rate):
#         super().__init__(make, year, registration, model, vehicle_ID, rate)
#
#     def get_cost(self, start_date, end_date):
#         return abs(start_date - end_date) * (1)  * self._rate
#
#     def __str__(self):
#         return super().__str__() + "{0}".format(self.get_cost)
# class medium(vehicle):
#     def __init__(self, make, year, registration, model, period, vehicle_ID, rate):
#         super().__init__(make, year, registration, model, period, vehicle_ID, rate)
#
#     def get_cost(self, start_date, end_date):
#         return abs(start_date - end_date) * (1.5) * self._rate
#
#     def __str__(self):
#         return super().__str__() + "{0}".format(self.get_cost)
# class large(vehicle):
#     def __init__(self, start_date, end_date, rate):
#         super().__init__(make, year, registration, model, period, vehicle_ID, rate)
#
#     def get_cost(self, start_date, end_date):
#         return abs(start_date - end_date) * (2) * self._rate
#
#     def __str__(self):
#         return super().__str__() + "{0}".format(self.get_cost)
# class premium(vehicle):
#     def __init__(self, make, year, registration, model, period, vehicle_ID, rate):
#         super().__init__(make, year, registration, model, period, vehicle_ID, rate)
#
#     def get_cost(self, start_date, end_date):
#         return abs(start_date - end_date) * (5) * self._rate
#
#     def __str__(self):
#         return super().__str__() + "{0}".format(self.get_cost)

class Order(Customer, vehicle):
    def __init__(self, name, email, licenseNo, age, totalDuration, pickup, dropoff, vehicleType, rate):
        super().__init__(name, email, licenseNo, age)
        self._totalDuration = totalDuration
        self._pickup = pickup
        self._dropoff = dropoff
        self._vehicleType = vehicleType
        self._rate = rate

    def get_totalDuration(self):
        return self._totalDuration;
    def set_totalDuration(totalDuration):
        self._totalDuration = totalDuration;

    def get_pickup(self):
        return self._pickup;
    def set_pickup(pickup):
        self._pickup = pickup;

    def get_dropoff(self):
        return self._dropoff;
    def set_dropoff(pickup):
        self._dropoff = dropoff;

    def get_vehicleType(self):
        return self._vehicleType;
    def set_vehicleType(vehicleType):
        self._vehicleType = vehicleType;

    def get_rate(self):
        return self._rate;
    def set_rate(rate):
        self._rate = rate;


    # implementation after merging with car
    def cost(self):
        totalCost = int(self.get_rate()) * int(self.get_totalDuration())
        if self.get_vehicleType() == "large" and int(self.get_totalDuration()) > 7:
            totalCost *= 0.95
        if self.get_vehicleType() == "premium" and int(self.get_totalDuration()) > 7:
            totalCost *= 0.95
        if self.get_vehicleType() == "premium":
            totalCost += int(self.get_rate()) * 0.15 * int(self.get_totalDuration())
        return totalCost

    def __str__(self):
        return Customer.get_name(self) + " will pick up from {0}".format(self.get_dropoff()) + \
        " and drop off at {0}.".format(self.get_dropoff()) + " Total payable: {0}".format(self.cost())


# main function
print("-----Book a car form-----")
print("Please enter customer details:")
customer1 = Order(input("Name: "), input("Email: "), input("License Number: "), input("Age: "),
input("Total booking length (days): "), input("Pickup location: "), input("Dropoff location: "),
input("Vehicle type: "), input("Vehicle rate ($): "))
print(customer1)
