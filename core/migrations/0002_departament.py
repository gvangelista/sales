# Generated by Django 4.1.1 on 2022-09-21 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departament',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='tx_name', max_length=104, unique=True)),
                ('active', models.BooleanField(db_column='cs_active', default=True)),
            ],
            options={
                'db_table': 'department',
                'managed': True,
            },
        ),
    ]
