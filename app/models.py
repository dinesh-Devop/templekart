from django.db import models
from django.db.models.expressions import F
from django.db.models.fields import EmailField
from django_mysql.models import ListCharField
from django.contrib.auth.models import User
from django import forms



class txt(models.Model):
    file_name=models.FileField(verbose_name= '')
    activated =models.BooleanField(default=False)

class csv(models.Model):
    file_name=models.FileField(upload_to='csv',verbose_name= '')
    activated =models.BooleanField(default=False)
    

class Profiles(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE,related_name='Profiles')
    id          = models.AutoField(blank=True, max_length=100,primary_key=True)
    oid         = models.CharField(blank=True, max_length=100,default="",null=True)
    number      = models.CharField(blank=True, max_length=100,default="",null=True)
    name        = models.CharField(blank=True, max_length=100,default="",null=True)
    address        =  models.CharField(blank=True, max_length=500,default="",null=True)
    renewal_date   =  models.CharField(blank=True,max_length=100,default="",null=True)
    profilestatus  =  models.CharField(blank=True,max_length=100,default="PREMIUM",null=True)
    

class Admins(models.Model):
    adminmail   = models.EmailField(blank=True, max_length=100,default="")
    adminpass   = models.CharField(blank=True, max_length=100,default="")

class Tournament(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE,related_name='Tournament',null=True)
    name        = models.CharField(blank=True, max_length=100,default="")
    place       = models.CharField(blank=True, max_length=100,default="")
    teams       = models.CharField(blank=True, max_length=100,default="")
    year        = models.CharField(blank=True, max_length=100,default="")

    def __str__(self):
        return self.name
class Pointstable(models.Model):
    teams        = models.CharField(blank=True, max_length=100,default='')
    win       = models.CharField(blank=True, max_length=100,default='')
    lose    = models.CharField(blank=True, max_length=100,default="")
    draw    = models.CharField(blank=True, max_length=100,default="")
    tournament  = models.ForeignKey(Tournament, on_delete=models.CASCADE,default='',null=True)


class Match(models.Model):
    uniqueid    = models.PositiveIntegerField(blank=True, null=True,default=0)
    venue       = models.CharField(blank=True, max_length=100,default="")
    time        = models.CharField(blank=True, max_length=100,default="")
    type        = models.CharField(blank=True, max_length=100,default="")
    tournament  = models.ForeignKey(Tournament,on_delete=models.CASCADE)
    status      = models.CharField(blank=True, max_length=100,default="Upcoming")
    report      = models.CharField(blank=True, max_length=500)
    date        = models.CharField(blank=True, max_length=100)
    # [name,total,overs,wickets,innings]
    winner      = ListCharField(base_field=models.CharField(max_length=50),
                  size=8,max_length=5000,default=[])
    loser       = ListCharField(base_field=models.CharField(max_length=50),
                  size=8,max_length=5000,default=[])
    team1      = models.CharField(blank=True, max_length=500)
    team2        = models.CharField(blank=True, max_length=100)
    user        = models.ForeignKey(User, on_delete=models.CASCADE,related_name='Match',null=True)

    def __str__(self):
        return self.tournament.name+"_match"+str(self.id)

    class Meta:
        verbose_name_plural = 'matches'

class Team(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE,related_name='Team',default='',null=True)
    name        = models.CharField(blank=True, max_length=100,default='')
    type        = models.CharField(blank=True, max_length=100,default='')
    players     = models.CharField(blank=True, max_length=100,default="")
    win     = models.PositiveIntegerField(blank=True, max_length=100,default=0)
    lose    = models.PositiveIntegerField(blank=True, max_length=100,default=0)
    draws   = models.PositiveIntegerField(blank=True, max_length=100,default=0)
    tournament=models.ForeignKey(Tournament, on_delete=models.CASCADE,related_name='Tournament',null=True)


    def __str__(self):
        return self.name

class Player(models.Model):
    name        = models.CharField(blank=True, max_length=100,default='',null=True)
    runs        = models.PositiveIntegerField(blank=True, null=True,default=0)
    strike_rate = models.FloatField(default=0)
    team        = models.CharField(blank=True, max_length=100,default='',null=True)

    def __str__(self):
        return self.name

class Batsman(models.Model):
    match       = models.ForeignKey(Match,on_delete=models.CASCADE)
    team        = models.ForeignKey(Team,on_delete=models.CASCADE)
    player      = models.ForeignKey(Player,on_delete=models.CASCADE)
    inning      = models.PositiveIntegerField(blank=True,null=True,default=0)
    runs        = models.PositiveIntegerField(blank=True, null=True,default=0)
    balls       = models.PositiveIntegerField(blank=True, null=True,default=0)
    fours       = models.PositiveIntegerField(blank=True, null=True,default=0)
    sixes       = models.PositiveIntegerField(blank=True, null=True,default=0)
    strike_rate = models.FloatField(default=0)
    status      = models.CharField(blank=True, max_length=100,default='')
    last_info   = ListCharField(base_field=models.CharField(max_length=15),size=2,max_length=50,default=[])
    pos         = models.CharField(blank=True,null=True,max_length=100,default='')

    def __str__(self):
        return self.player.name

    class Meta:
        verbose_name_plural = 'Batsmen'


class Bowler(models.Model):
    match      = models.ForeignKey(Match,on_delete=models.CASCADE)
    team        = models.ForeignKey(Team,on_delete=models.CASCADE)
    player      = models.ForeignKey(Player,on_delete=models.CASCADE)
    inning     = models.PositiveIntegerField(blank=True,null=True,default=0)
    overs      = models.FloatField(default=0)
    runs       = models.PositiveIntegerField(blank=True, null=True,default=0)
    maidens    = models.PositiveSmallIntegerField(blank=True, null=True,default=0)
    no_balls   = models.PositiveIntegerField(blank=True, null=True,default=0)
    wides      = models.PositiveIntegerField(blank=True, null=True,default=0)
    wickets    = models.PositiveIntegerField(blank=True, null=True,default=0)
    economy    = models.CharField(blank=True, max_length=100,default='')

    def __str__(self):
        return self.player.name

class Comment(models.Model):
    match     = models.ForeignKey(Match,on_delete=models.CASCADE)
    inning    = models.PositiveIntegerField(blank=True,null=True)
    over      = models.PositiveIntegerField(blank=True, null=True)
    run       = models.PositiveIntegerField(blank=True, null=True)
    ball      = models.PositiveIntegerField(blank=True, null=True)
    remark    = models.CharField(blank=True, max_length=100)
    others    = models.CharField(blank=True,null=True, max_length=100)
    batsman   = models.CharField(blank=True, max_length=100)
    bowler  = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.match.tournament.name+"_match"+str(int(self.match.id))+"_comment"+str(self.id)

class Commentator(models.Model):
    name        = models.CharField(blank=True, max_length=100)
    email       = models.EmailField(blank=False,null=False)
    user        = models.ForeignKey(User, on_delete=models.CASCADE,related_name='Commentator',null=True)

class Tweet(models.Model):
    label       = models.PositiveIntegerField(blank=True, null=True)
    username    = models.CharField(blank=True, max_length=100)
    body      = models.CharField(blank=True,null=True, max_length=500)
    date   = models.CharField(blank=True, max_length=100)
    link    = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return str(self.id)