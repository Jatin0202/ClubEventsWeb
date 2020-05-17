from django.db import models

# Create your models here.

CLUB_CHOICES=[
    ('Coding Club','Coding Club IITG'),
    ('Electronics','Electroncis Club IITG'),
    ('Robotics','Robotics Club IITG'),
    ('LitSoc','Literary Society IITG'),
    ('Xpressions','Drama Club IITG'),
    ('Aeromodelling','Aeromodelling Club IITG'),
    ('Cadence','Dance Club IITG'),
    ('IITG.AI','Artificial intelligence Club IITG'),
]
class Club(models.Model):

    club_name = models.CharField(max_length=50, choices=CLUB_CHOICES)
    club_secy = models.CharField(max_length=50)

    def __str__(self):
        return self.club_name


class Post(models.Model):

    uid         = models.CharField(max_length=30)
    club_name   = models.ForeignKey(Club,on_delete=models.CASCADE)
    updated_on  = models.CharField(max_length=50)
    content     = models.TextField()

    class Meta:
        ordering=['updated_on']

    def content_as_list(self):
        return self.content.split('\n')

    def __str__(self):
        return self.content
