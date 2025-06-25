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