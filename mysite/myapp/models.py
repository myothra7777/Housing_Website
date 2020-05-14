from django.db import models
from django.contrib.auth.models import User

property_types = (
    ('A', 'Apartment'),
    ('H', 'House'),
    )

class Property_Model(models.Model):
    type = models.CharField(max_length=1, choices=property_types)
    address = models.CharField(max_length=100)
    num_rooms = models.IntegerField()
    num_bathrooms = models.IntegerField()
    sq_footage = models.IntegerField()
    price = models.IntegerField()
    upload = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.address + " Property ID:" + str(self.id)

class Application_Model(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    cur_address = models.CharField(max_length=100)
    salary = models.CharField(max_length=10)
    ssn = models.CharField(max_length=11)
    phone = models.CharField(max_length=20)
    property = models.ForeignKey(Property_Model, on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.applicant.first_name + " " + self.applicant.last_name + " Application For " + self.property.address
