from django.db import models

# Create your models here.

#one to one relationship
#Car Company and CEO

class CarCompany(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class CEO(models.Model):
    name = models.CharField(max_length=100)
    car_company = models.OneToOneField(CarCompany, on_delete=models.CASCADE, related_name='ceo')

    def __str__(self):
        return self.name


class CarModel(models.Model):
    name = models.CharField(max_length=100)
    car_company = models.ForeignKey(CarCompany, on_delete=models.CASCADE, related_name='car_models')

# foreign key --> many to one relationship
    def __str__(self):
        return self.name
    

#many to many relationship

#electric --> kon kon car use kore (eta amader use case)
#car model -->kon kon fuel ke use kore 

class FuelType(models.Model):
    name = models.CharField(max_length=100)
    car_models = models.ManyToManyField(CarModel, related_name='fuel_types')

    def __str__(self):
        return self.name