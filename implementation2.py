pyfrom abc import ABC, abstractmethod
class Customer(ABC):
    def __init__(self, name, email, licenseNo, age):
        self._name = name
        self._email = email
        self._licenseNo = licenseNo
        self._age = age

    def get_name():
        return self._name;
    def set_name():
        self._name = name;

    def get_email():
        return self._email;
    def set_email():
        self._email = email;

    def get_licenseNo():
        return self._licenseNo;
    def set_licenseNo():
        self._licenseNo = licenseNo;

    def get_age():
        return self._age;
    def set_age():
        self._age = age;

    @abstractmethod
    def cost(self):
        pass

class Order(Customer):
    def __init__(self, start, end, totalDuration):
        self._start = start
        self._end = end
        self._totalDuration = totalDuration

    def get_start():
        return self._start;
    def set_start():
        self._start = start;

    def get_end():
        return self._end;
    def set_end():
        self._end = end;

    def get_totalDuration():
        return self._totalDuration;
    def set_totalDuration():
        self._totalDuration = totalDuration;

    # implementation after merging with car
    def cost(self):
        pass

    def __str__(self):
        pass
