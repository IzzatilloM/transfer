from django.db import models

from django.core.validators import MinValueValidator

class Season(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
         return self.name
class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Club(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='clubs')
    president = models.CharField(max_length=100, blank=True, null=True)
    coach = models.CharField(max_length=100, blank=True, null=True)
    found_date = models.DateField(blank=True,null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Player(models.Model):
     name = models.CharField(max_length=100)
     age = models.PositiveSmallIntegerField()
     position = models.CharField(max_length=100)
     price = models.FloatField(validators = [MinValueValidator(0.0)])
     country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
     club = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True)

     def __str__(self):
         return self.name

class Transfer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    club_old = models.ForeignKey(Club, on_delete=models.CASCADE, related_name = 'expenditure_transfers')
    club_new = models.ForeignKey(Club, on_delete=models.CASCADE, related_name = 'income_transfers')
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    price_tft = models.FloatField(validators=[MinValueValidator(0.0)])
    season = models.ForeignKey(Season, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.player.name}: {self.club_old.name} -> {self.club_new.name}"