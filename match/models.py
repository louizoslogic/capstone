from django.db import models
from accounts.models import CustomUser


class Participant(models.Model):
    summoner = models.CharField(null=True, max_length=100)
    team = models.CharField(null=True, max_length=100)
    win = models.BooleanField(null=True)
    is_user = models.BooleanField(default=False)

    championid = models.CharField(null=True, max_length=100)
    championname = models.CharField(null=True, max_length=100)
    championicon = models.CharField(null=True, max_length=100)
    # spell1Id = models.CharField(null=True, max_length=100)
    # spell2Id = models.CharField(null=True, max_length=100)

    lane = models.CharField(null=True, max_length=100)

    kills = models.CharField(null=True, max_length=100)
    deaths = models.CharField(null=True, max_length=100)
    assists = models.CharField(null=True, max_length=100)


def __str__(self):
    return self.summoner


class Match(models.Model):

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    matchid = models.CharField(max_length=100)
    victory = models.BooleanField(null=True)
    win = models.CharField(null=True, max_length=100)

    userparticipant = models.ForeignKey(Participant, on_delete=models.CASCADE, null=True, related_name='pu')

    participant1 = models.ForeignKey(Participant, on_delete=models.CASCADE, null=True, related_name='p1')
    participant2 = models.ForeignKey(Participant, on_delete=models.CASCADE, null=True, related_name='p2')
    participant3 = models.ForeignKey(Participant, on_delete=models.CASCADE, null=True, related_name='p3')
    participant4 = models.ForeignKey(Participant, on_delete=models.CASCADE, null=True, related_name='p4')
    participant5 = models.ForeignKey(Participant, on_delete=models.CASCADE, null=True, related_name='p5')
    participant6 = models.ForeignKey(Participant, on_delete=models.CASCADE, null=True, related_name='p6')
    participant7 = models.ForeignKey(Participant, on_delete=models.CASCADE, null=True, related_name='p7')
    participant8 = models.ForeignKey(Participant, on_delete=models.CASCADE, null=True, related_name='p8')
    participant9 = models.ForeignKey(Participant, on_delete=models.CASCADE, null=True, related_name='p9')
    participant10 = models.ForeignKey(Participant, on_delete=models.CASCADE, null=True, related_name='p10')

    def __str__(self):
        return self.matchid
