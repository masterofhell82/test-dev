from django.db import models

import re

# Create your models here.
# Model created to verify license plate numbers
class VehicleNumberPlate(models.Model):
    
    number_plate = models.CharField(max_length=12)
    
    def __str__(self) -> str:
        return f"{self.number_plate}"

    def validate_number_plate(self) -> bool:
        regex = re.compile(r"([A-Z0-9][A-Z0-9])-([A-Z0-9][A-Z0-9])-([A-Z0-9][A-Z0-9])\W/g")
        return regex.search(self.number_plate)



class VehicleType(models.Model):
    name = models.CharField(max_length=32)
    max_capacity = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.name


class Vehicle(models.Model):
    name = models.CharField(max_length=32)
    passengers = models.PositiveIntegerField()
    vehicle_type = models.ForeignKey(VehicleType, null=True, on_delete=models.SET_NULL)
    number_plate = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.name

    def can_start(self) -> bool:
        return self.vehicle_type.max_capacity >= self.passengers

    # Function created for distribution 
    def get_distribution(self) -> []:
        lst = []
        if self.passengers != 0:
            index = self.passengers/2
            while index > 0:
                if index == 0.5:
                    lst.append([True, False])
                else:
                    lst.append([True, True])
                index -=1
            return lst


class Journey(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.PROTECT)
    start = models.DateField()
    end = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.vehicle.name} ({self.start} - {self.end})"

    # Function created to know if it has an end date. Returns a Boolean
    def is_finished(self) -> bool:
        return self.end != None
