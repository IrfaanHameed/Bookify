from django.db import models

class Flight(models.Model):
    flight_name = models.CharField(max_length=100,default="N/A")
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.flight_name}"

class Booking(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    num_tickets = models.PositiveIntegerField()

    def total_amount(self):
        return self.num_tickets * self.flight.price
