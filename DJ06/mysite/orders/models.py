from django.db import models

class Order(models.Model):
    product = models.CharField(max_length=100)
    customer = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.product} — {self.customer}"
