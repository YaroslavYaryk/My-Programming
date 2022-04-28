from django.db import models
from django.core.validators import MinValueValidator


class Room(models.Model):

    lenght = models.IntegerField()
    height = models.IntegerField()
    width = models.IntegerField()

    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"

    def get_absolute_url(self):
        return reverse("Room_detail", kwargs={"pk": self.pk})


class MyRoom(Room):

    my_storage = models.BooleanField()

    class Meta:
        verbose_name = "MyRoom"
        verbose_name_plural = "MyRooms"

    def get_absolute_url(self):
        return reverse("MyRoom_detail", kwargs={"pk": self.pk})


class Customer(models.Model):

    name = models.CharField(("customer_name"), max_length=50)
    balance = models.FloatField(
        ("customer_balance"),
        validators=[MinValueValidator(0.0)],
    )

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Customer_detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        if self.balance < 0:
            raise ValueError("balance cannot be negative")
        super(Customer, self).save(*args, **kwargs)
