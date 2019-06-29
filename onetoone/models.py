from django.db import models


# Create your models here.


class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return "%s the place" % self.name


class Restaurant(models.Model):
    place = models.OneToOneField(Place, on_delete=models.CASCADE, primary_key=True)

    serves_hot_dogs = models.BooleanField(default=False)
    servers_pizza = models.BooleanField(default=False)

    def __str__(self):
        return "%s the restratunt" % self.place.name


class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    name = models.CharField(max_length=50)

    def __str__(self):
        return "%s the waiter at %s"(self.name, self.restaurant)
