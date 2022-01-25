from django.db import models


class Choices(models.Model):
    Name_of_sport = models.CharField(max_length=25)
    Dress_code = models.CharField(max_length=25)
    Cost_for_equipment = models.IntegerField(default=100)
    Played_this_sport = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.Name_of_sport} -- {self.Dress_code}"

class PlayerEligibility(models.Model):
    Name_of_player_id = models.CharField(max_length=25)
    player_belong_to = models.ForeignKey(Choices, on_delete=models.CASCADE)
    Level_of_player = models.CharField(max_length=25)





