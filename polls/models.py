from django.db import models
import datetime
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    myfield = models.IntegerField(default=0)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    choice_text = models.CharField(max_length=200)

    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text



class Musician(models.Model):

    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)

    instrument=models.CharField(max_length=100)



class Album(models.Model):

    artist=models.ForeignKey(Musician,on_delete=models.CASCADE)

    name=models.CharField(max_length=100)
    release_date=models.DateField()
    num_stars=models.IntegerField()



class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)




