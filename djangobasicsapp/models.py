from django.db import models

# Create your models here.

class Authors(models.Model):
    def __init__(self, author_name, country, book_name):
        self.author_name = author_name
        self.country = country
        self.book_name = book_name
    