from django.db import models

# Create your models here.
class Bracket(models.Model):
    id = models.AutoField(primary_key = True)
    event = models.CharField()
    sport = models.CharField()
    Date = models.DateField()

class Teams(models.Model):
    id = models.AutoField(primary_key=True)

class Game(models.Model):
    id = models.AutoField(primary_key=True)
    round = models.CharField()
    section = models.CharField()


class BracketStructure(models.Model):
    id = models.AutoField(primary_key = True)
    bracket = models.ForeignKey(Bracket,on_delete=models.CASCADE)
    game = models.ForeignKey(Game)
    parentGame = models.ForeignKey(Game)
    childGame = models.ForeignKey(Game)

class Seeding(models.Model):
    id = models.AutoField(primary_key=True)
