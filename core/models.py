from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Employee(models.Model):
    M = '0'
    F = '1'

    SEX_CHOICES = (
        (M, _('Masculine')),
        (F, _('Feminine'))
    )

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
    salary = models.DecimalField(
        db_column='nb_salary',
        null=False,
        blank=False,
        max_digits=10,
        decimal_places=2
    )
    sex = models.CharField(
        db_column='cs_sex',
        null=False,
        max_length=1,
        choices=SEX_CHOICES,
        verbose_name=_('sex')
    )
    department = models.ForeignKey(
        to='Departament',
        on_delete=models.DO_NOTHING,
        db_column='id_department',
        null=True,
        blank=True
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
