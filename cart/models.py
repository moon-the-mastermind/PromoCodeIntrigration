from django.db import models

class PromoCode(models.Model):
    code = models.CharField(max_length=20, unique=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2)  # 0.10 for 10%
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.code
