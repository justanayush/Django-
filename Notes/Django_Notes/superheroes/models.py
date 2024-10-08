from django.db import models
from django.utils import timezone

# Create your models here.

class DC_Sups(models.Model):
    POWER_TYPE = [
        ('EL','EYELASER'),
        ('SS','SUPERSPEED'),
        ('RT','ROBOT'),
        ('SH','SUPERHUMAN_STRENGTH'),
        ('WM','WATER_MANIPULATION'),
    ]
    # ENUMS for restriction of choices common db practice
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='sups/')
    date_added = models.DateTimeField(default=timezone.now)
    power_type = models.CharField(max_length=2,choices=POWER_TYPE)
    description = models.TextField(default='')
    def __str__(self) -> str:
        return self.name