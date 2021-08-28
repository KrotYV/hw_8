from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return str(self.first_name)

    def get_absolute_url(self):
        return f'/person/{self.id}'
