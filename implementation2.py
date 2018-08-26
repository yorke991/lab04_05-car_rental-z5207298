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

class Order(Customer):
    def __init__(self, name, email, licenseNo, age, start, end, totalDuration):
        super().__init__(name, email, licenseNo, age)
        self._start = start
        self._end = end
        self._totalDuration = totalDuration

    def get_start(self):
        return self._start;
    def set_start(start):
        self._start = start;

    def get_end(self):
        return self._end;
    def set_end(end):
        self._end = end;

    def get_totalDuration(self):
        return self._totalDuration;
    def set_totalDuration(totalDuration):
        self._totalDuration = totalDuration;

    # implementation after merging with car
    def cost(self):
        pass

    def __str__(self):
        return Customer.get_name(self) + " (License number: {0})".format(Customer.get_licenseNo(self)) \
        + " has made a booking from {0}".format(self.get_start()) + " to {0}".format(self.get_end())


# main function
print("-----Book a car form-----")
print("Please enter customer details:")
customer1 = Order(input("Name: "), input("Email: "), input("License Number: "), input("Age: "),
input("Booking start date (DDMMYYYY): "), input("Booking end date (DDMMYYYY): "), input("Total booking length (days): "))
print(customer1)

