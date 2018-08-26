from abc import ABC, abstractmethod

class vehicle(ABC):

    def __init__(self, make, year, registration, model, period, vehicle_ID, rate):
        self._make = make
        self._year = year
        self._registration = registration
        self._model = model
        self._period = period
        self._vehicle_ID = vehicle_ID
        self._rate = rate
    
    def get_make(self):
        return self._make
    
    def get_year(self):
        return self._year
    
    def get_registration(self):
        return self._registration
    
    def get_model(self):
        return self._model
    
    def get_period(self):
        return self._period
    
    def get_vehicle_ID(self):
        return self._vehicle_ID
        
    def get_rate(self):
        return self._rate
        
    @abstractmethod
    def get_cost(self, start_date, end_date):
        pass
    def __str__(self):
        return self._rate + "is the rate, and the cost is: "

 
        
class small(vehicle):
    def __init__(self, make, year, registration, model, period, vehicle_ID, rate):
        super().__init__(make, year, registration, model, period, vehicle_ID, rate)
    
    def get_cost(self, start_date, end_date):
        return abs(start_date - end_date) * (1)  * self._rate
       
    def __str__(self):
        return super().__str__() + "{0}".format(self.get_cost)
class medium(vehicle):
    def __init__(self, make, year, registration, model, period, vehicle_ID, rate):
        super().__init__(make, year, registration, model, period, vehicle_ID, rate)
    
    def get_cost(self, start_date, end_date):
        return abs(start_date - end_date) * (1.5) * self._rate
       
    def __str__(self):
        return super().__str__() + "{0}".format(self.get_cost)
class large(vehicle):
    def __init__(self, start_date, end_date, rate):
        super().__init__(make, year, registration, model, period, vehicle_ID, rate)
    
    def get_cost(self, start_date, end_date):
        return abs(start_date - end_date) * (2) * self._rate
       
    def __str__(self):
        return super().__str__() + "{0}".format(self.get_cost)
class premium(vehicle):
    def __init__(self, make, year, registration, model, period, vehicle_ID, rate):
        super().__init__(make, year, registration, model, period, vehicle_ID, rate)
    
    def get_cost(self, start_date, end_date):
        return abs(start_date - end_date) * (5) * self._rate
       
    def __str__(self):
        return super().__str__() + "{0}".format(self.get_cost)


car1 = premium(1,1,1,1,1,1,1)
print(car1)

