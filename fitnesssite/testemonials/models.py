from django.db import models


# Create your models here.
class Testemonial(models.Model):
    body = models.TextField(blank=False, max_length=500)
    attribution = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self) -> str:
        return f"A Testemonial from {self.attribution}"
