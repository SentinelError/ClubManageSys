from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

class BaseModel(models.Model):
    objects=models.Manager()
    class Meta:
        abstract = True

class Club(models.Model):
    name = models.CharField('Club Name', max_length=50)

    def __str__(self):
        return self.name


class Field(models.Model):
    name = models.CharField('Field', max_length=50)

    def __str__(self):
        return self.name


class Year(models.Model):
    name = models.CharField('Year', max_length=50)

    def __str__(self):
        return self.name

class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=120)
    address = models.CharField('Address', max_length=320)
    phone = models.CharField('Contact Number', max_length=120)

    def __str__(self):
        return self.name


class Event(BaseModel):

    name = models.CharField('Event Name', max_length=120)
    overseer = models.ForeignKey(User, default='', blank=True, null=False, on_delete=models.CASCADE, related_name='Overseer')
    event_club = models.ForeignKey(Club, default='', blank=True, null=False, on_delete=models.CASCADE)
    event_date = models.DateTimeField('Event Date')
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(User, blank=True, related_name='Attendees')
    approved = models.BooleanField(default=False)


    def __str__(self):
        return self.name



class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, blank=True, null=True, on_delete=models.CASCADE)
    field = models.ForeignKey(Field, blank=True, null=True, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, blank=True, null=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username

class Report(models.Model):

    title = models.CharField('Event Report', max_length=100)
    event = models.OneToOneField(Event, blank=False, on_delete=models.CASCADE)
    report_date = models.DateField('Report Date')
    report_author = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    body = RichTextField(blank=False)

    def __str__(self):
        return self.title


