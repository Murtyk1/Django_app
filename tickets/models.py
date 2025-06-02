from django.db import models

class Ticket(models.Model):
    origin = models.CharField(max_length=3, verbose_name="Откуда (IATA код)")
    destination = models.CharField(max_length=3, verbose_name="Куда (IATA код)")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    departure_date = models.DateField(verbose_name="Дата вылета")
    airline = models.CharField(max_length=50, verbose_name="Авиакомпания")

    def __str__(self):
        return f"{self.origin}-{self.destination} ({self.departure_date}): {self.price} руб."
