from django.db import models

# Create your models here.

class Employee(models.Model):
    id = models.AutoField(
        db_column='id',
        primary_key=True,
        null=False
    )
    name = models.CharField(
        db_column='tx_name',
        null=False,
        blank=False,
        max_length=104
    )
    salary = models.FloatField(
        db_column='nb_salary',
        null=False,
        blank=False,
    )

    class Meta:
        db_table = 'employee'
        managed = True


class Departament(models.Model):
    id = models.AutoField(
        db_column='id',
        primary_key=True,
        null=False
    )
    name = models.CharField(
        db_column='tx_name',
        max_length=104,
        null=False,
        blank=False,
        unique=True)
    active = models.BooleanField(
        db_column='cs_active',
        null=False,
        blank=False,
        default=True
    )

    class Meta:
        db_table = 'department'
        managed = True
