from app.models import *
from django.db.models.signals import post_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

@receiver(post_save, sender=Comment)
def announce_new_comment(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "Commentary", {"type"    : "cricket.commentary",
                           "event"   : "New Commentary",
                           "id"      : instance.match.id,
                           "inning"  : instance.inning,
                           "overs"   : instance.over,
                           "runs"    : instance.run,
                           "balls"   : instance.ball,
                           "batsman" : instance.batsman,
                           "bowler"  : instance.bowler,
                           "others"  : instance.others,
                           "remarks" : instance.remark})

@receiver(post_save, sender=Match)
def announce_match(sender, instance, created, **kwargs):
    if not created:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "Commentary", {"type"    : "cricket.commentary",
                           "event"   : "Match",
                           "id"      : instance.id,
                           "tournmt" : instance.tournament.name,
                           "status"  : instance.status,
                           "venue"   : instance.venue,
                           "winner"  : instance.winner,
                           "loser"   : instance.loser})

@receiver(post_save, sender=Batsman)
def announce_batsman(sender, instance, created, **kwargs):
    if True:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "Commentary", {"type"    : "cricket.commentary",
                           "event"   : "Batsman",
                           'thisid'  : instance.id,
                           "id"      : instance.match.id,
                           "runs"    : instance.runs,
                           "inning"  : instance.inning,
                           "balls"   : instance.balls,
                           "fours"   : instance.fours,
                           "sixes"   : instance.sixes,
                           "sr"      : instance.strike_rate,
                           "last_in" : instance.last_info,
                           "name"    : instance.player.name,
                           "status"  : instance.status})

@receiver(post_save, sender=Bowler)
def announce_bowler(sender, instance, created, **kwargs):
    if True:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "Commentary", {"type"    : "cricket.commentary",
                           "event"   : "Bowler",
                           'thisid'  : instance.id,
                           "id"      : instance.match.id,
                           "runs"    : instance.runs,
                           "inning"  : instance.inning,
                           "extras"  : int(instance.wides)+int(instance.no_balls),
                           "wickets" : instance.wickets,
                           "eco"     : instance.economy,
                           "maidens" : instance.maidens,
                           "name"    : instance.player.name,
                           "overs"   : instance.overs})

@receiver(post_save, sender=Match)
def announce_new_match(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "Commentary", {"type"    : "cricket.commentary",
                           "event"   : "UniqueID",
                           "tname"   : instance.tournament.name,
                           "name"    : instance.type+": "+ instance.winner[0]+" v "+instance.loser[0],
                           "uid" : instance.uniqueid})