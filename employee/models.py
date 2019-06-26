from django.db import models


class Employee(models.Model):
    email = models.EmailField(max_length=120, unique=True, db_index=True, primary_key=True)
    name = models.CharField(max_length=140)
    department = models.CharField(max_length=100)

    def __str__(self):
        return 'Employee: {name}'.format(name=self.name)
