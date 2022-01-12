from django import template
from .. import models
register=template.Library()

@register.filter(name='split')
def split(value,type):
    if type==3:
        return value.split("-")
    return value.split(",") if type==1 else value.split(",")[1:]

@register.filter(name='check')
def check(value):
    if value==None:
        return False
    if value.split(",")[-1]=="":
        return False
    return True

@register.filter(name='top')
def top(value):
    return value[0:3].upper()

@register.filter(name='format')
def format(value,extent):
    return value[2:-extent]

@register.filter(name='partner')
def partner(last,batlist):
    for i in range(2):
        if batlist[i]==last:
            return True
    return False

@register.filter(name='subtract')
def subtract(value, arg):
    return float(value) - float(arg)

@register.filter(name='fow')
def fow(value,arg):
    r=""
    l=[]
    for i in value:
        if i.status!="Not out" and i.inning==arg:
            l.append(i)
    if len(l)!=0:
        r="𝐅𝐚𝐥𝐥 𝐨𝐟 𝐰𝐢𝐜𝐤𝐞𝐭𝐬: "
        for i in l:
            r+=str(l.index(i)+1)+"-"+" ("+i.player.name.capitalize()+", "+" ov)"
            if l.index(i)!=len(l)-1:r+=", "
    return r

@register.filter
def find_replace(string, find_replace=",|_"):
    find, replace = find_replace.split("|")
    return string.replace(',', ' ')
