from django.db import models

# Create your models here.
class Create_incident(models.Model):
    PRIORITY = (
        ('High','High'),
        ('Medium','Medium'),
        ('Low', 'Low'),
    )
    INCIDENT_STATUS = (
        ('Open', 'Open'),
        ('In progress', 'In progress'),
        ('Closed', 'Closed'),
    )
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True,unique=False)
    description = models.TextField(max_length=10000)
    priority = models.CharField( null=False,unique=False,choices=PRIORITY,max_length=10,)
    incident_number = models.CharField( max_length=20,unique=True)
    incident_status = models.CharField(choices=INCIDENT_STATUS,max_length=100,unique=False)

    def __str__(self) -> str:
        return self.incident_number
