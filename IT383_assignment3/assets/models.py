from django.db import models

class Asset(models.Model):
    name = models.CharField(max_length=100)
    asset_type = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    assigned_user = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MaintenanceLog(models.Model):
    asset = models.ForeignKey(
        Asset,
        on_delete=models.CASCADE,
        related_name='maintenance_logs'
    )
    service_date = models.DateField()
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.asset.name} - {self.service_date}"