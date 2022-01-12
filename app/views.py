from json.encoder import JSONEncoder
import math
from typing import Counter

from django.db.models.fields import PositiveIntegerField
from app.forms import CsvModelForm,txtform
import logging
import unicodedata,twint,os,pandas as pd
from django.http.response import HttpResponseRedirect
from six import b
import requests,json,random,datetime
from background_task import background
from bs4 import BeautifulSoup
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from app.models import *
from django.contrib import messages
from app.models import Match
from django import http
from django.contrib.auth import authenticate, get_user_model
from datetime import date
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from .models import Profiles
from django.conf import settings
from django.core.mail import send_mail
from django.core.validators import validate_email
from django import forms


#Webpage functions
def createcommentator(request):
    userr=request.session.get('user')
    user=User.objects.get(username=userr)
    user=user.id
    if not request.POST:
        my_json = request.body.decode('utf8').replace("'", '"')
        data = json.loads(my_json)
    else:
        data=request.POST
    comm=Commentator.objects.values('email')
    a=True
    for i in range(len(comm)):
        if data['Email']==comm[i]['email']:
            a=False
            return HttpResponse('email already registerd')
        else:
            a=True
    if a==True:
        useer=User.objects.get(id=data['User'])
        p = Commentator(name=data['Name'], email=data['Email'],user=useer)
        p.save()
        
    return redirect('managecomm')

def editcommentator(request):
    data=request.POST
    comm=Commentator.objects.values('email')
    comme=Commentator.objects.get(id=data['id'])
    print(comme.email)
    if data['email']==comme.email:
        commm=Commentator.objects.get(id=data['id'])
        commm.name,commm.email=data['name'],data['email']
        commm.save()
    else:
        a=True
        for i in range(len(comm)):
            if data['Email']==comm[i]['email']:
                a=False
                return HttpResponse('email already registerd')
            else:
                a=True
        if a==True:
            commm=Commentator.objects.get(id=data['id'])
            commm.name,commm.email=data['name'],data['email']
            commm.save()

    return redirect('managecomm')

def delcommentator(request):
    comm=Commentator.objects.get(id=request.POST['id'])
    comm.delete()
    return redirect('managecomm')

def PointsTable(request,id):
    rightpane=getRightpane()
    To=Pointstable.objects.get(tournament=id)
    u=Tournament.objects.get(id=id)
    g=Match.objects.values('winner')
    mk=Match.objects.all()
    h=Match.objects.values('loser')
    fl=[]
    kl=[]
    draws=[]
    q=0
    d=0
    win=To.win
    lose=To.lose
    draw=To.draw
    teams=Team.objects.filter(tournament=u)
    print(teams)
    for i in range(len(teams)):
        print('round')
        for j in range(len(mk)):
            if mk[j].status=='Result':
                a=g[j]['winner'][0]
                fh=g[j]['winner'][1]
                fhl=h[j]['loser'][1]
                if str(teams[i])==a :
                    if fh!=fhl:
                        q=q+1
                    if fh==fhl:
                        d=d+1       
        draws.append(d)
        print(draw)
        print('l',q)
        fl.append(q)
        print(fl)
        q=0 
        for j in range(len(mk)):
            if mk[j].status=='Result':
                a=h[j]['loser'][0]
                fh=g[j]['winner'][1]
                fhl=h[j]['loser'][1]
                if str(teams[i])==a:
                    if fh!=fhl:
                        q=q+1
                    if fh==fhl:
                        d=d+1
        print('l',q)
        kl.append(q)
        print(kl)
        q=0
    xs=[]
    xcs=[]
    x=0
    print(fl,kl,draws)
    for i in range(len(kl)):
        x=int(fl[i])*int(win)
        y=int(draws[i])*int(draw)
        z=int(kl[i])*int(lose)
        xs.append(x+y+z)
        xcs.append(int(fl[i])+int(draws[i])+int(kl[i]))
    print(x)
   

    print(teams,kl,fl,draws,xs)
    vc=zip(teams,xcs,fl,kl,draws,xs)
    user=User.objects.get(username=request.session['user'])
    tourn=Tournament.objects.filter(user=user)
    for i in range(len(tourn)):
        b=tourn[i].teams
        c=b.split(',')
        print(c)
        teamss=c[0 ]

    userl=User.objects.get(username=request.session['user'])
    j=userl.id
    
    return render(request,'pointstable.html',{'teams':teams,"vc":vc,'u':u,'win':win,'lose':lose,'draw':draw,'j':j,'rightpane':rightpane})
def tda(request, id):
    rightpane=getRightpane()
    
    tb=Team.objects.get(id=id)
    # print(t)
    players=Player.objects.filter(team=tb.name)
    # for i in range(len(k)):
    #  print(k[i])
    # players=Player.objects.get(name=k[i])
    h=Match.objects.values('winner')
    g=Match.objects.values('loser')
    match=''
    w=''
    l=''
    matche=''
    wo=''
    lo=''
    n,v,s,t,d,los,win=[],[],[],[],[],[],[]
    for i in range(len(h)):
        if tb.name==h[i]['winner'][0]:
            print(h[i]['winner'][0])
            
            match=Match.objects.get(winner=h[i]['winner'])
            print(match)
            no=match.id
            n.append(no)
            venue=match.venue
            v.append(venue)
            status=match.status
            s.append(status)
            type=match.type
            t.append(type)
            date=match.date
            d.append(date)
            w=match.winner[0]
            win.append(w)
            l=match.loser[0]
            los.append(l)
            print(w,l)
    
        if tb.name==g[i]['loser'][0]:
            
            matche=Match.objects.get(loser=g[i]['loser'])
            print(matche)
            no=matche.id
            n.append(no)
            venue=matche.venue
            v.append(venue)
            status=matche.status
            s.append(status)
            type=matche.type
            t.append(type)
            date=matche.date
            d.append(date)
            w=matche.winner[0]
            win.append(w)
            l=matche.loser[0]
            los.append(l)
    zi=zip(n,v,s,t,d,win,los)
    print(zi)
            
    # matche=Match.objects.get(loser=t.name)
    '''for j in range(len(g)):
        if h[i]['loser'][0]==t.name:
            matche=h[i]['loser']'''

    return render(request,"teamda.html",{"players":players,'rightpane':rightpane,'zi':zi})
def ct(request):
    rightpane=getRightpane()
    teams=Team.objects.all()
    tournaments='c'
    return render(request,'tcreate.html',{'teams':teams,'tournaments':tournaments,'rightpane':rightpane})

def txts(request):

    if request.method=='POST':
        try:
            form=txtform(request.POST,request.FILES)
            userl=User.objects.get(username=request.session['user'])
            tp=request.POST.get('t')
            r=Tournament.objects.get(id=tp)
            nh=str(r.id)
            v=Team.objects.all()
            n=r.teams
            if form.is_valid():
                form.save()
                form=txtform() 
                try:
                    obj=txt.objects.get(activated=False)
                    with open(obj.file_name.path,'r') as f:
                        if not f.name.endswith('.txt'):
                            obj.delete()
                            return HttpResponse('invalid file format')
                        for row in f: 
                            row=row.split(';')
                            print(row)
                            t=Tournament.objects.get(id=tp)
                            t.teams=n+','+ row[0]
                            t.save()
                            sp=row[1:-1]
                            spp=",".join(sp)
                            for i in range(len(v)):
                                for j in range(i+1,len(v)):
                                    if row[0]==v[j].name:
                                        return HttpResponse('Team name already exists')
                            g=Team.objects.create(tournament=t,user=userl,name=row[0],type=row[-1],players=spp)
                            for ik in range(len(sp)):
                                ply=Team.objects.get(name=row[0])
                                player=Player(name=sp[ik],team=ply,)
                                
                                
                                player.save()
                            
                        obj.activated=True
                        obj.save()
                        return redirect('/'+nh+'/teams')
                except Exception as e:
                    obj=txt.objects.get(activated=False)
                    obj.delete()
                    return HttpResponse('Team name already exists')
        except Exception as e:
            obj=txt.objects.get(activated=False)
            obj.delete()
            return HttpResponse('Team name already exists')

    if request.method=='POST':
        try:
            form=txtform(request.POST,request.FILES)
            userl=User.objects.get(username=request.session.get('user'))
            tournament=request.POST.get('t')
            r=Tournament.objects.get(id=tournament)
            print(r)
            v=Team.objects.all()
            n=r.teams
            if form.is_valid():
                form.save()
                form=txtform() 
                try:
                    obj=txt.objects.get(activated=False)
                    with open(obj.file_name.path,'r') as f:
                        if not f.name.endswith('.txt'):
                            obj.delete()
                            return HttpResponse('invalid file format')
                        for row in f: 
                            row=row.split(';')
                            t=Tournament.objects.get(name=tournament)
                            t.teams=row[1]+','+n
                            t.save()
                            for i in range(len(v)):
                                for j in range(i+1,len(v)):
                                    if row[0]==v[j].name:

                                        
                                        return HttpResponse('Team name already exists')
                            g=Team.objects.create(tournament=t,user=userl,name=row[0],type=row[-1],players='')
                           
                        obj.activated=True
                        obj.save()
                        return redirect('tournaments')
                except Exception as e:
                    obj=csv.objects.get(activated=False)
                    obj.delete()
                    return HttpResponse('invalid format')
        except Exception as e:
            obj=csv.objects.get(activated=False)
            obj.delete()
            return HttpResponse('Team name already exists')


def team(request):
    brand=Team.objects.values('name')
    for i in range(len(brand)):
        b=brand[i]['name']
    print(b)
    return HttpResponse('success')

def pagenotcreated(request):
    return render(request,'livescores.html')

def mail(request):
    return render(request,'confirmmail.html')
    
def email(request):
        global fmail
        fmail=request.POST.get('email')
        print(User.objects.values('email'))
        if {'email':fmail} in User.objects.values('email'):
            subject = 'confirm user mail.click the link below to change password.'
            message = f'https://crimpulse.herokuapp.com/forgotpassword'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [fmail, ]
            send_mail( subject, message, email_from, recipient_list )
            messages.success(request,'check mail!')
            return render(request,'confirmmail.html')
        else:
            messages.success(request,'Email not found')
            return render(request,'confirmmail.html')
    
def forgotpassword(request):
    if request.method=="POST":
        uo=User.objects.get(email=fmail)
        print(uo.password)
        print(uo)
        password=request.POST.get('password')
        cpassword=request.POST.get('confirmpassword')
        if password==cpassword:
            word=make_password(password)
            uo.password=word
            print(uo.password)
            uo.save()
            print(uo.password)
            #uo.password==password
            messages.success(request,'password changed successfully!')
            return render(request,'login.html')
        else:
            messages.success(request,'password doesnt match')
            return render(request,'forgotpassword.html')
    else:
        return render(request,'forgotpassword.html')

def addOrganizer(request):
  if request.method == "POST":
        try:
            username=request.POST.get('username')
            password=request.POST.get('password')
            name= request.POST.get('name')
            number= request.POST.get('number')
            omail= request.POST.get('mail')
            try:
                validate_email(omail)
            except Exception as e:
                valid_email = False
                messages.error(request,'please enter a valid email')
                return render(request,'addadmin.html')
            valid_email = True
            u=get_user_model()
            users=u.objects.values('email')
            for i in range(len(users)):
                if omail==users[i]['email']:
                    messages.error(request,'email already exists!')
                    return render(request,'addadmin.html')
            oid= request.POST.get('oid') #organizer id
            hashid=str(hash(oid))
            hashid1=hashid[0:6]
            word=make_password(password)
            post2=User(username=username,password=word,email=omail) 
            post2.save()
            uid=post2.id #user id
            post=Profiles(user=post2,name=name,number=number,id=uid,oid=hashid1)
            post.save() 
            messages.success(request,'organizer added successfully!')
            return render(request,'addadmin.html')
        except Exception as e:
            messages.success(request,'organizer name already exists!')
            return render(request,'addadmin.html')
  else:
      return render(request, 'addadmin.html') 

def add(request):
    return render(request,'addadmin.html')

def del_organizerList(request):
    lists=User.objects.values_list('username')
    print(lists)
    return render(request, 'deladmin.html', {"lists": lists})

def delOrganizer(request):
    if request.method == "POST":
        dellist=request.POST.getlist('select')     
        for i in range(0,len(dellist)):
            user=dellist[i][2:-3]
            user = User.objects.get(username=user)
            user.delete()
            Profile=Profiles.objects.filter(user=user)
            Profile.delete()
        return HttpResponse('deleted')

def edit_organizerList(request):
    lists=User.objects.values_list('username')
    print(lists)
    return render(request, 'organiserlist.html', {"lists": lists})

def edit_radio(request):
    if request.method == "POST":
        selected_user=request.POST.getlist('select')     
        for i in range(0,len(selected_user)):
            global u
            g=selected_user[i][2:-3]
            u = User.objects.get(username=g) 
            return render(request,'editadmin.html')
    else:  
        return render(request,'editadmin.html') 

def editOrganizer(request):
    if request.method == "POST":
        try:
            uid=u.id
            x=User.objects.get(id=uid)
            name= request.POST.get('name')
            oid= request.POST.get('oid')
            number= request.POST.get('number')
            mail= request.POST.get('mail')
            try:
                validate_email(mail)
                valid_email = True
            except Exception as e:
                    valid_email = False
                    messages.error(request,'please enter a valid email')
                    return render(request,'editadmin.html')
            username=request.POST.get('username')
            password=request.POST.get('password')
            use=get_user_model()
            users=use.objects.values('email')
            for i in range(len(users)):
                print(username)
                print(users[i]['email'])
                if mail==users[i]['email']:
                    messages.error(request,'email already exists!')
                    return render(request,'editadmin.html')
            word=make_password(password)
            hashid=str(hash(oid))
            hashid1=hashid[0:6]
            x.username=username
            x.save()
            x.password=word
            x.save()
            x.email=mail
            x.save()
            post3=Profiles(user=x,name=name,number=number,id=uid,oid=hashid1)
            post3.save()
            messages.error(request,'Organizer edited successfully')
            return render(request,'editadmin.html')
        except Exception as e:
                    valid_email = False
                    messages.error(request,'Organiser name already exists')
                    return render(request,'editadmin.html')

    else:  
        return render(request,'editadmin.html') 
        
def session(request):
    if request.META['HTTP_HOST'] == ['crimpulse.herokuapp.com'] and request.session._session_key is not None:
        return True
    else:
        return False

def adminLogin(request):
    if request.method == 'POST':
        amail=request.POST.get('amail')
        apass=request.POST.get('apass')
        adminmail=Admins.objects.values('adminmail')
        adminpass=Admins.objects.values('adminpass')
        if {'adminmail': amail} in adminmail and {'adminpass': apass} in adminpass:
            return render(request,'ahome.html')
        else:
            messages.error(request,'invalid data')
            return render(request, 'admin.html')    
    else:
        return render(request, 'admin.html')

def oragnizerLogin(request):
    if request.session._session_key is None:
        if request.method == 'POST':
            global ousername
            ousername = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=ousername, password=password) 
            if user:
                if user.is_active:
                    
                    request.session.set_test_cookie()
                    request.session['user'] = ousername
                    use=User.objects.get(username=ousername)
                    usse=use.id
                    team=Team.objects.filter(user=use)
                    try:
                       tee=team[0]
                       response=redirect('/stat/'+str(tee.id)+'/'+str(usse))
                    except:
                         response=redirect('tournaments')
                    # response=render(request,'tournaments.html')
                    
                    return response
            else:
                messages.error(request,'invalid username or password')
                
                return render(request, 'login.html')
            
        else:
            return render(request, 'login.html')
    else:
        return redirect("tournaments")
def commentatorLogin(request):    
        if request.method == 'POST':
                code=int(request.POST.get('matchcode'))
                email=request.POST.get('email')
                data=Match.objects.values('uniqueid')
                cmail=Commentator.objects.values('email')
                try:
                    validate_email(email)
                    valid_email = True
                except Exception as e:
                    valid_email = False
                    messages.error(request,'invalid email!')
                    return render(request, 'login.html')
                try:
                    match=Match.objects.get(uniqueid=code)
                    user1=User.objects.get(username=match.user)
                    teams1=Team.objects.get(name=match.winner[0])
                    teams2=Team.objects.get(name=match.loser[0])
                    user=User.objects.get(username=teams1.user)
                    user2=User.objects.get(username=teams2.user)
                    comm=Commentator.objects.get(email=email)
                    if comm.user==teams1.user or comm.user==teams2.user:
                        if {'uniqueid':code} in data and valid_email:
                            request.session.flush()
                            mcode=Match.objects.get(uniqueid=code)
                            if mcode.status=='Upcoming':
                                response=redirect('start')
                                response.set_cookie('code',code,max_age=43200)
                                return response
                            elif mcode.status=='Live':
                                response=redirect('events')
                                response.set_cookie('code',code,max_age=43200)
                                return response
                            elif mcode.status=='Result':
                                response=redirect('scorecard',id=mcode.id)
                                response.set_cookie('code',code,max_age=43200)
                                return response
                            elif mcode.status=='Abandoned':
                                messages.error(request,'match not found!')
                                return render(request, 'login.html')

                        else:
                            messages.error(request,'invalid matchcode!')
                            return render(request, 'login.html')
                except Exception as e:
                        messages.error(request,'invalid commentator')
                        return render(request, 'login.html')
               
        else:
            messages.error(request,'please enter valid data')
            return render(request, 'login.html')

def logout(request):
    if request.session._session_key is not None:
            request.session.flush()
            return redirect('login')
    try:
        if request.COOKIES['code'] is not None:
            response=redirect('login')
            response.delete_cookie("code")
            return response
    except KeyError:
                return render(request,'login.html')       
    else:
        return HttpResponse(status=401)

def startPage(request):
    if request.COOKIES.get("code", None) is not None:
        rightpane=getRightpane()
        try:
            match=Match.objects.get(uniqueid=request.COOKIES["code"])
        except:
            return HttpResponse("<h1>Page not authorized for Organizers</h1>") 
       
        team1,team2=Team.objects.get(name=match.winner[0]),Team.objects.get(name=match.loser[0])
        return render(request,"matchstart.html",{'team1': team1,'team2':team2,"rightpane":rightpane})
    else:
       return HttpResponse(status=401)

def landingPage(request):
    try:
        os.remove("static/twitter/tweets.json")
    except:
        pass
    getTweets()
    rightpane=getRightpane()
    centerpane=getLeftpane()
    tweets=Tweet.objects.all()
    return render(request,"home.html",{'tweets':tweets,'centerpane':centerpane,'rightpane':rightpane})
    
def tournamentsPage(request):
    if request.session._session_key is not None: 
         #Rightpane
            rightpane=getRightpane()
            #Centerpane
            use= request.session.get('user')
            userl=User.objects.get(username=request.session.get('user'))
            j=userl.id
            vb=''
            tea=''
            tournaments=Tournament.objects.filter(user=j)
            bn=[]
            for i in range(len(tournaments)):
                b=tournaments[i].teams
                c=b.split(',')
                
                team=c[0 ]
                
                try:
                    tea=Team.objects.get(name=team)
                except:
                    tea=0
              
                bn.append(tea)
                vb=zip(tournaments,bn)
            teams=Team.objects.filter(user=j)
            return render(request,'tournaments.html',{'rightpane':rightpane,"tournaments":tournaments,'vb':vb,'teams':teams,'tea':tea,'j':j})   
    else:
        if  request.COOKIES.get('code') is not None:
            return HttpResponse("<h1>Page not authorized for Commentators</h1>")
        else:
            return HttpResponse(status=401)

def stat(request,id,user):
    if request.session._session_key is not None:
        try:

            lastmatchscore=0
            lastmatchopponent=0
            wonby=0
            lostby=0
            id=int(id)
            print(id)
            v=Team.objects.get(id=id)
            name=v.name
            g=Match.objects.values('winner')
            x=Match.objects.values('loser')
            q=0
            f=0
            li=[]
            n=str(name)
            nextmatch='0'
            nextmatchdate='0'
            nextmatchvenue='0'
            #matchwon
            for i in range(0,len(g)):
                d=g[i]['winner'][5]
                a=g[i]['winner'][0]
                sa=g[i]['winner'][7]
                n=str(v)
                if d!='nil' and a==n and d>x[i]['loser'][1] and sa=='1':
                    q=q+1
                    li.append(i)
                if d!='nil' and a==n and d==x[i]['loser'][1] and sa=='1':
                    f=f+1
                    li.append(i)
            print(li)
            try:
                lastmatchwon=li[-1]
            except:
                lastmatchwon=0

            print(lastmatchwon)
       
            matcheswon=q   
            #matchdraw
            matchdraw=f
            b=0
            bi=[]
            #matchlost
            for j in range(0,len(x)):
                c=x[j]['loser'][1]
                w=x[j]['loser'][0]
                ga=x[j]['loser'][7]
                if w==n and c<g[j]['winner'][1] and ga=='1':
                    b=b+1 
                    bi.append(j)  
                if w==n and c==g[j]['winner'][1] and ga=='1':
                    b=b+1 
                    bi.append(j)
            try:
                lastmatchlost=bi[-1]
            except Exception as e:
                lastmatchlost=0
            matcheslost=b 
            #totalmatches                                     
            matchesplayed=matcheswon+matcheslost+matchdraw          
            y=0
            h=0
            #winbattingfirst
            for s in range(0,len(g)):
                if g[s]['winner'][4]!='0' and g[s]['winner'][0]==n and g[s]['winner'][7]=='1':
                    y=y+1
                if g[s]['winner'][4]!='0' and g[s]['winner'][1]==x[s]['loser'][1] and g[s]['winner'][7]=='1':
                    h=h+1
            Firstbattingwon=y   
            #drawbattingfirst
            drawbattingfirst=h                        
            mo=0
            #winbattingsecond
            for z in range(0,len(x)):
                po=x[z]['loser'][4]
                a=x[z]['loser'][0]
                if po=='0'and a==n and x[z]['loser'][1]!=g[z]['winner'][1] and x[z]['loser'][7]=='1':
                    mo=mo+1
            Firstbattinglost=mo
            secondbattingwon=matcheswon-Firstbattingwon     
            bg=0
            #wins when toss won
            for jh in range(0,len(g)):
                cf=g[jh]['winner'][6]
                wf=g[jh]['winner'][0]
                if wf==n and cf=='1' and g[jh]['winner'][7]=='1':
                    bg=bg+1
            winswhentosswon=bg
            bgf=0
            #loss when toss won
            for jhf in range(0,len(x)):
                cfd=x[jhf]['loser'][6]
                wfd=x[jhf]['loser'][0]
                if wfd==n and cfd=='1' and x[jhf]['loser'][7]:
                    bgf=bgf+1
            losseswhentosswon=bgf
            totaltosswon=winswhentosswon+losseswhentosswon
            totaltosslost=matchesplayed-totaltosswon
            #tosswinpercentage
            try:
                tosswinperc=int((totaltosswon/matchesplayed)*100)
            except Exception as e:
                tosswinperc=0
            print('po')
            print(lastmatchlost)
            print(lastmatchwon)

            if lastmatchwon==lastmatchlost:
                
                    lastmatchplayed=''
                    lastmatchscore=0
                    lastmatchwickets=0
                    lastmatchopponent=''
                    wonby='nil'
                    nextmatchvenue=''
                    nextmatchdate=''

            #lastmatchplayed,lastmatchscore,opponent,wonby     (if lastmatch was a win)                     
            if lastmatchwon>lastmatchlost:
                print('thth')
                lastmatchplayed=g[lastmatchwon]
                lastmatchscore=g[lastmatchwon]['winner'][1]
                lastmatchwickets=g[lastmatchwon]['winner'][3]
                lastmatchopponent=x[lastmatchwon]['loser'][0]
                if g[lastmatchwon]['winner'][1]!=x[lastmatchwon]['loser'][1]:
                    wonby=int(g[lastmatchwon]['winner'][1])-int(x[lastmatchwon]['loser'][1])
                else:
                    wonby='draw'
                #nextmatch
                for sd in range(lastmatchwon+1,len(g)): 
                        if g[sd]['winner'][0]==n:                  
                            nextmatch=x[sd]['loser'][0]
                            next=Match.objects.filter(loser=g[sd]['winner'])
                            try:
                                if next[sd].loser[0]==n:
                                        nextmatchvenue=next[sd].venue
                                        nextmatchdate=next[sd].date
                            except Exception as e:
                                pass          
                        elif x[sd]['loser'][0]==n:
                            nextmatch=g[sd]['winner'][0]
                            next=Match.objects.filter(winner=x[sd]['loser'])
                            try:
                                if next[sd].winner[0]==n:
                                        nextmatchvenue=next[sd].venue
                                        nextmatchdate=next[sd].date  
                            except Exception as e:
                                pass                                
            #lastmatchplayed,lastmatchscore,opponent,lostby     (if lastmatch was a loss)  
            if lastmatchlost>lastmatchwon:
                print('t')
                lastmatchplayed=x[lastmatchlost]
                lastmatchscore=x[lastmatchlost]['loser'][1]
                lastmatchwickets=x[lastmatchlost]['loser'][3]
                lastmatchopponent=g[lastmatchlost]['winner'][0]
                if x[lastmatchlost]['loser'][1]==g[lastmatchlost]['winner'][1]:
                    wonby='draw'
                    
                else:
                    lostby=int(g[lastmatchlost]['winner'][1])-int(x[lastmatchlost]['loser'][1])
                    
                
                #nextmatch
                for sd in range(lastmatchlost+1,len(x)):
                    if x[sd]['loser'][0]==n or g[sd]['winner'][0]==n:
                        if x[sd]['loser'][0]!=n:
                            nextmatch=x[sd]['loser'][0]
                            next=Match.objects.filter(loser=x[sd]['loser'])
                            try:
                                if next[sd].winner[0]==n:
                                        nextmatchvenue=next[sd].venue
                                        nextmatchdate=next[sd].date
                            except Exception as e:
                                pass
                        if g[sd]['winner'][0]!=n:
                            nextmatch=g[sd]['winner'][0]
                            next=Match.objects.filter(winner=g[sd]['winner'])
                            try:
                                if next[sd].loser[0]==n:
                                        nextmatchvenue=next[sd].venue
                                        nextmatchdate=next[sd].date
                            except Exception as e:
                                pass              
            h=[]   
            h.append(lastmatchlost)
            h.append(lastmatchwon)
            h.sort()
            ad=h[-1]
            kl=[]   
            jl=[]    
            jh=[]
            kj=[]
            hl=[]
            wl=[]
            for sdf in range(0,ad+1):
                if g[sdf]['winner'][0]==n and g[sdf]['winner'][5]!='nil':
                    kl.append(g[sdf]['winner'][1])
                    jl.append(x[sdf]['loser'][1])
                    hl.append(g[sdf]['winner'][3])
                    wl.append(x[sdf]['loser'][3])
                    date=Match.objects.get(winner=g[sdf]['winner']).date
                    jh.append(date)  
                if  x[sdf]['loser'][0]==n and x[sdf]['loser'][5]!='nil':
                    kl.append(x[sdf]['loser'][1])
                    jl.append(g[sdf]['winner'][1])
                    hl.append(x[sdf]['loser'][3])
                    wl.append(g[sdf]['winner'][3])
                    print(g[sdf]['winner'])
                    try:
                        date=Match.objects.get(winner=g[sdf]['winner'])
                    except Exception as e:
                        date='-'
                    jh.append(date)
                    
            for sdfb in range(0,ad+1):
             if g[sdfb]['winner'][0]==n or x[sdfb]['loser'][0]==n :
                 if g[sdfb]['winner'][0]==n and g[sdfb]['winner'][5]!='nil' :
                    if g[sdfb]['winner'][1]>x[sdfb]['loser'][1]:
                        kj.append('win')
                    elif g[sdfb]['winner'][1]==x[sdfb]['loser'][1]:
                        kj.append('loss')
                    else:
                        kj.append('loss')
                 elif x[sdfb]['loser'][0]==n and x[sdfb]['loser'][5]!='nil' :
                     if x[sdfb]['loser'][1]>g[sdfb]['winner'][1]:
                        kj.append('win')
                     elif x[sdfb]['loser'][1]==g[sdfb]['winner'][1]:
                        kj.append('loss')
                     else:
                        kj.append('loss')
            print(kj)
            for i in range(5):
                a='-'
                if len(jh)<5:
                    a='nextmatch'+str(i)
                    jh.append(a)
                    print(jh)
                    jl.append("0")
                    kl.append("0")
                    kj.append("loss")
                    hl.append("0")
                    wl.append("0")
                 
                    
            last5mathchesrunsscored=kl
            last5matchesrunsconceeded=jl
            last5matchdates=jh
            last5matcheswicketstaken=wl
            last5matcheswicketslost=hl
            last5matchresults=kj[0:5]
            print(last5matchresults)
            lastmatchwickets=last5matcheswicketslost[-1]
            T=User.objects.get(id=user)
            hhhkkk=T.id
            teams=Team.objects.filter(user=user)
            
            context ={'hhhkkk':hhhkkk,'n':n,'user':user,'teams':teams,'n':n,'lastmatchwickets':lastmatchwickets,'id':id,'last5matchresults':last5matchresults,'last5matcheswicketstaken':last5matcheswicketstaken,'last5matcheswicketslost':last5matcheswicketslost,'last5matchesrunsconceeded':last5matchesrunsconceeded,'last5mathchesrunsscored':last5mathchesrunsscored,'last5matchdates':last5matchdates,'matchesplayed':matchesplayed,'matcheswon':matcheswon,'matcheslost':matcheslost,
            'matchdraw':matchdraw,'Firstbattingwon':Firstbattingwon,'secondbattingwon':secondbattingwon,'totaltosswon':totaltosswon,'totaltosslost':totaltosslost,'tosswinperc':tosswinperc,
            'lastmatchscore':lastmatchscore,'lastmatchopponent':lastmatchopponent,'wonby':wonby,'lostby':lostby ,'nextmatch':nextmatch,'nextmatchvenue':nextmatchvenue,'nextmatchdate':nextmatchdate}
            return render(request,'tdashboard.html',context)
        except Exception as e:
           return redirect('tournaments')

    else:
        return HttpResponse(status=401)
def tstats(request):
    if request.session._session_key is not None:
        try:    
            T=User.objects.get(username=request.session.get('user'))
            hhhkkk=T.id
            
            teams=Team.objects.filter(user=T)
            id=teams[0].id
            lastmatchscore=0
            lastmatchopponent=0
            wonby=0
            lostby=0
            id=int(id)
            print(id)
            v=Team.objects.get(id=id)
            name=v.name
            g=Match.objects.values('winner')
            x=Match.objects.values('loser')
            q=0
            f=0
            li=[]
            n=str(name)
            nextmatch='0'
            nextmatchdate='0'
            nextmatchvenue='0'
            #matchwon
            for i in range(0,len(g)):
                d=g[i]['winner'][5]
                a=g[i]['winner'][0]
                sa=g[i]['winner'][7]
                n=str(v)
                if d!='nil' and a==n and d>x[i]['loser'][1] and sa=='1':
                    q=q+1
                    li.append(i)
                if d!='nil' and a==n and d==x[i]['loser'][1] and sa=='1':
                    f=f+1
                    li.append(i)
            print(li)
            try:
                lastmatchwon=li[-1]
            except:
                lastmatchwon=0

            print(lastmatchwon)
       
            matcheswon=q   
            #matchdraw
            matchdraw=f
            b=0
            bi=[]
            #matchlost
            for j in range(0,len(x)):
                c=x[j]['loser'][1]
                w=x[j]['loser'][0]
                ga=x[j]['loser'][7]
                if w==n and c<g[j]['winner'][1] and ga=='1':
                    b=b+1 
                    bi.append(j)  
                if w==n and c==g[j]['winner'][1] and ga=='1':
                    b=b+1 
                    bi.append(j)
            try:
                lastmatchlost=bi[-1]
            except Exception as e:
                lastmatchlost=0
            matcheslost=b 
            #totalmatches                                     
            matchesplayed=matcheswon+matcheslost+matchdraw          
            y=0
            h=0
            #winbattingfirst
            for s in range(0,len(g)):
                if g[s]['winner'][4]!='0' and g[s]['winner'][0]==n and g[s]['winner'][7]=='1':
                    y=y+1
                if g[s]['winner'][4]!='0' and g[s]['winner'][1]==x[s]['loser'][1] and g[s]['winner'][7]=='1':
                    h=h+1
            Firstbattingwon=y   
            #drawbattingfirst
            drawbattingfirst=h                        
            mo=0
            #winbattingsecond
            for z in range(0,len(x)):
                po=x[z]['loser'][4]
                a=x[z]['loser'][0]
                if po=='0'and a==n and x[z]['loser'][1]!=g[z]['winner'][1] and x[z]['loser'][7]=='1':
                    mo=mo+1
            Firstbattinglost=mo
            secondbattingwon=matcheswon-Firstbattingwon     
            bg=0
            #wins when toss won
            for jh in range(0,len(g)):
                cf=g[jh]['winner'][6]
                wf=g[jh]['winner'][0]
                if wf==n and cf=='1' and g[jh]['winner'][7]=='1':
                    bg=bg+1
            winswhentosswon=bg
            bgf=0
            #loss when toss won
            for jhf in range(0,len(x)):
                cfd=x[jhf]['loser'][6]
                wfd=x[jhf]['loser'][0]
                if wfd==n and cfd=='1' and x[jhf]['loser'][7]:
                    bgf=bgf+1
            losseswhentosswon=bgf
            totaltosswon=winswhentosswon+losseswhentosswon
            totaltosslost=matchesplayed-totaltosswon
            #tosswinpercentage
            try:
                tosswinperc=int((totaltosswon/matchesplayed)*100)
            except Exception as e:
                tosswinperc=0
            print('po')
            print(lastmatchlost)
            print(lastmatchwon)

            if lastmatchwon==lastmatchlost:
                
                    lastmatchplayed=''
                    lastmatchscore=0
                    lastmatchwickets=0
                    lastmatchopponent=''
                    wonby='nil'
                    nextmatchvenue=''
                    nextmatchdate=''

            #lastmatchplayed,lastmatchscore,opponent,wonby     (if lastmatch was a win)                     
            if lastmatchwon>lastmatchlost:
                print('thth')
                lastmatchplayed=g[lastmatchwon]
                lastmatchscore=g[lastmatchwon]['winner'][1]
                lastmatchwickets=g[lastmatchwon]['winner'][3]
                lastmatchopponent=x[lastmatchwon]['loser'][0]
                if g[lastmatchwon]['winner'][1]!=x[lastmatchwon]['loser'][1]:
                    wonby=int(g[lastmatchwon]['winner'][1])-int(x[lastmatchwon]['loser'][1])
                else:
                    wonby='draw'
                #nextmatch
                for sd in range(lastmatchwon+1,len(g)): 
                        if g[sd]['winner'][0]==n:                  
                            nextmatch=x[sd]['loser'][0]
                            next=Match.objects.filter(loser=g[sd]['winner'])
                            try:
                                if next[sd].loser[0]==n:
                                        nextmatchvenue=next[sd].venue
                                        nextmatchdate=next[sd].date
                            except Exception as e:
                                pass          
                        elif x[sd]['loser'][0]==n:
                            nextmatch=g[sd]['winner'][0]
                            next=Match.objects.filter(winner=x[sd]['loser'])
                            try:
                                if next[sd].winner[0]==n:
                                        nextmatchvenue=next[sd].venue
                                        nextmatchdate=next[sd].date  
                            except Exception as e:
                                pass                                
            #lastmatchplayed,lastmatchscore,opponent,lostby     (if lastmatch was a loss)  
            if lastmatchlost>lastmatchwon:
                print('t')
                lastmatchplayed=x[lastmatchlost]
                lastmatchscore=x[lastmatchlost]['loser'][1]
                lastmatchwickets=x[lastmatchlost]['loser'][3]
                lastmatchopponent=g[lastmatchlost]['winner'][0]
                if x[lastmatchlost]['loser'][1]==g[lastmatchlost]['winner'][1]:
                    wonby='draw'
                    
                else:
                    lostby=int(g[lastmatchlost]['winner'][1])-int(x[lastmatchlost]['loser'][1])
                    
                
                #nextmatch
                for sd in range(lastmatchlost+1,len(x)):
                    if x[sd]['loser'][0]==n or g[sd]['winner'][0]==n:
                        if x[sd]['loser'][0]!=n:
                            nextmatch=x[sd]['loser'][0]
                            next=Match.objects.filter(loser=x[sd]['loser'])
                            try:
                                if next[sd].winner[0]==n:
                                        nextmatchvenue=next[sd].venue
                                        nextmatchdate=next[sd].date
                            except Exception as e:
                                pass
                        if g[sd]['winner'][0]!=n:
                            nextmatch=g[sd]['winner'][0]
                            next=Match.objects.filter(winner=g[sd]['winner'])
                            try:
                                if next[sd].loser[0]==n:
                                        nextmatchvenue=next[sd].venue
                                        nextmatchdate=next[sd].date
                            except Exception as e:
                                pass              
            h=[]   
            h.append(lastmatchlost)
            h.append(lastmatchwon)
            h.sort()
            ad=h[-1]
            kl=[]   
            jl=[]    
            jh=[]
            kj=[]
            hl=[]
            wl=[]
            for sdf in range(0,ad+1):
                if g[sdf]['winner'][0]==n and g[sdf]['winner'][5]!='nil':
                    kl.append(g[sdf]['winner'][1])
                    jl.append(x[sdf]['loser'][1])
                    hl.append(g[sdf]['winner'][3])
                    wl.append(x[sdf]['loser'][3])
                    date=Match.objects.get(winner=g[sdf]['winner']).date
                    jh.append(date)  
                if  x[sdf]['loser'][0]==n and x[sdf]['loser'][5]!='nil':
                    kl.append(x[sdf]['loser'][1])
                    jl.append(g[sdf]['winner'][1])
                    hl.append(x[sdf]['loser'][3])
                    wl.append(g[sdf]['winner'][3])
                    print(g[sdf]['winner'])
                    try:
                        date=Match.objects.get(winner=g[sdf]['winner'])
                    except Exception as e:
                        date='-'
                    jh.append(date)
                    
            for sdfb in range(0,ad+1):
             if g[sdfb]['winner'][0]==n or x[sdfb]['loser'][0]==n :
                 if g[sdfb]['winner'][0]==n and g[sdfb]['winner'][5]!='nil' :
                    if g[sdfb]['winner'][1]>x[sdfb]['loser'][1]:
                        kj.append('win')
                    elif g[sdfb]['winner'][1]==x[sdfb]['loser'][1]:
                        kj.append('loss')
                    else:
                        kj.append('loss')
                 elif x[sdfb]['loser'][0]==n and x[sdfb]['loser'][5]!='nil' :
                     if x[sdfb]['loser'][1]>g[sdfb]['winner'][1]:
                        kj.append('win')
                     elif x[sdfb]['loser'][1]==g[sdfb]['winner'][1]:
                        kj.append('loss')
                     else:
                        kj.append('loss')
            print(kj)
            for i in range(5):
                a='-'
                if len(jh)<5:
                    a='nextmatch'+str(i)
                    jh.append(a)
                    print(jh)
                    jl.append("0")
                    kl.append("0")
                    kj.append("loss")
                    hl.append("0")
                    wl.append("0")
                 
                    
            last5mathchesrunsscored=kl
            last5matchesrunsconceeded=jl
            last5matchdates=jh
            last5matcheswicketstaken=wl
            last5matcheswicketslost=hl
            last5matchresults=kj[0:5]
            print(last5matchresults)
            lastmatchwickets=last5matcheswicketslost[-1]
            
            if(wonby==0,lostby==0):
                wonby='nil'
            context ={'hhhkkk':hhhkkk,'n':n,'teams':teams,'n':n,'lastmatchwickets':lastmatchwickets,'id':id,'last5matchresults':last5matchresults,'last5matcheswicketstaken':last5matcheswicketstaken,'last5matcheswicketslost':last5matcheswicketslost,'last5matchesrunsconceeded':last5matchesrunsconceeded,'last5mathchesrunsscored':last5mathchesrunsscored,'last5matchdates':last5matchdates,'matchesplayed':matchesplayed,'matcheswon':matcheswon,'matcheslost':matcheslost,
            'matchdraw':matchdraw,'Firstbattingwon':Firstbattingwon,'secondbattingwon':secondbattingwon,'totaltosswon':totaltosswon,'totaltosslost':totaltosslost,'tosswinperc':tosswinperc,
            'lastmatchscore':lastmatchscore,'lastmatchopponent':lastmatchopponent,'wonby':wonby,'lostby':lostby ,'nextmatch':nextmatch,'nextmatchvenue':nextmatchvenue,'nextmatchdate':nextmatchdate}
            return render(request,'tdashboard.html',context)
        except Exception as e:
            return redirect('tournaments')
    else:
        return HttpResponse(status=401)
def matchesPage(request,id):
    if request.session._session_key is not None:
         #Rightpane
        rightpane=getRightpane()
        #Centerpane
        match=Match.objects.all()
        for i in match:
            t=datetime.datetime.now()
            tt=datetime.datetime.strptime(i.date,'%Y-%m-%d')
            if(tt.date() < t.date()):
                if(i.status == 'Upcoming'):
                    i.status="Abandoned"
                    i.save()
            if(tt.date() > t.date()):
                if(i.status == 'Abandoned'):
                    i.status="Upcoming"
                    i.save()
        tmatches=Match.objects.filter(tournament=id).order_by('id')
        tour=Tournament.objects.get(id=id)
        tid=tour.id
        t=Team.objects.filter(tournament=tour)
        use=User.objects.get(username=request.session.get('user'))
        user=use.id
        print(user)
        try:
            teams=t[0]
        except Exception as e:
            teams=''
        for i in range(len(tmatches)):
            for j in range(i+1,len(tmatches)):
                    if tmatches[i].date==tmatches[j].date:
                        if tmatches[i].time==tmatches[j].time:
                            if (tmatches[i].winner[0] in (tmatches[j].winner[0] or tmatches[j].loser[0])) or tmatches[i].loser[0] in (tmatches[j].winner[0] or tmatches[j].loser[0]) :
                                lo=tmatches[j].id
                                print(lo)
                                jo=Match.objects.get(id=lo)
                                jo.delete() 
                                print(tmatches[i].date)
                            # print(tmatches[j].date)
                                tour=Tournament.objects.get(id=id)
                    else:
                        tour=Tournament.objects.get(id=id)
        form= CsvModelForm()
        
        return render(request,'matches.html',{'rightpane':rightpane,"tmatches":tmatches,'tour':tour,'tid':tid,'form':form,'teams':teams,'user':user})
    else:    
         return HttpResponse("<h1>Page not authorized for Commentators</h1>")

def teamsPage(request):
    if request.session._session_key is not None:
        bv=[]
         #Rightpane
        rightpane=getRightpane()
        #Centerpane
        user=User.objects.get(username=request.session.get('user'))
        i=user.id
        teams=Team.objects.filter(user=i)
        players=Player.objects.all()
        To=0   
        v=Team.objects.all()
        for i in range(len(v)):
            bv.append(v[i].name)
        
        return (JsonResponse({'bv':bv}))
    else:           
         return HttpResponse("<h1>Page not authorized for Commentators</h1>")
def tteamsPage(request,tournament):
    if request.session._session_key is not None:
         #Rightpane
        rightpane=getRightpane()
        #Centerpane
        Tow=Tournament.objects.get(id=tournament)
        te=Team.objects.filter(tournament=Tow)
        To=Tow.id
        team=Tow.teams
        t=team.split(',')
        print(t)
        id=[]
        name=[]
        for i in range(len(t)):
            print('hi')
        print(id)
        
        players=Player.objects.all()
        form= txtform()
        v=Team.objects.all()


        
        
        user=User.objects.get(username=request.session.get('user'))
        use=user.id
        tourn=Tournament.objects.filter(user=user)
        for i in range(len(tourn)):
            b=tourn[i].teams
            c=b.split(',')
            #print(c)
            teamss=c[0 ]

        userl=User.objects.get(username=request.session.get('user'))
        j=userl.id
        try:
            tea=Team.objects.get(name=teamss)
        except Exception as e:
            tea=''
        return render(request,'teams.html',{'rightpane':rightpane,"te":te,'form':form,'To':To,"players":players,'j':j,'tea':tea,'tournament':tournament,'t':t,'use':use})
    else:           
         return HttpResponse("<h1>Page not authorized for Commentators</h1>")

def scorecardPage(request,id):
        print(id)
        match = Match.objects.get(id=id)
        batsmen = Batsman.objects.filter(match=match)
        bowlers = Bowler.objects.filter(match=match)
        comments = Comment.objects.filter(match=match).order_by('id')
        #Leftpane
        leftpane=getLeftpane()
        #Rightpane
        rightpane=getRightpane()
        #Match Live
        matchlive,inning,matchlive_comm,last_wicket,batlive,bowlive=dataLive(match)
        return render(request,'scorecard.html',context=
        {'match':match,'batsmen':batsmen,"bowlers":bowlers,"matchlive":matchlive,
        'commentary':comments,'last':last_wicket,"fromcreate":match.date=="January 1st, 2021","livecomment":matchlive_comm
         ,"batlive":batlive,"bowlive":bowlive,'rightpane':rightpane,'leftpane':leftpane})


def commentaryPage(request):
    if request.COOKIES.get("code", None) is not None:
        rightpane=getRightpane()
        match=Match.objects.get(uniqueid=request.COOKIES["code"])
        comments=list(Comment.objects.filter(match=match).order_by('id').values())[::-1][:6]
        # try:
        #     matchcode=code
        # except:
        #     return HttpResponse("<h1>Page not authorized for Organizers</h1>") 
        return render(request,'comment.html',{'comments':False if len(comments)==0 else comments,'show':False,"rightpane":rightpane,"message":False})
        
    else:
         if request.session._session_key is not None:
            return HttpResponse('<h1>Page not authorized for Organizers</h1>')
         else:
             return HttpResponse(status=401)
       

#API functions


def stats(request,id):
    if request.session._session_key is not None:
        lastmatchscore=0
        lastmatchopponent=0
        wonby=0
        lostby=0
        id = id
        id=id
        v=Team.objects.get(id=id)
        g=Match.objects.values('winner')
        x=Match.objects.values('loser')
        q=0
        f=0
        li=[]
        lastmatchdraw=[]
        n=str(v)
        nextmatch=0
        nextmatchdate=0
        nextmatchvenue=0

        #matchwon
        for i in range(0,len(g)):
            d=g[i]['winner'][1]
            a=g[i]['winner'][0]
            sa=g[i]['winner'][7]
            n=str(v)
            if d!='0' and a==n and d>x[i]['loser'][1] and sa=='1':
                q=q+1
                li.append(i)
            if d==x[i]['loser'][1] and sa=='1':
                f=f+1
                li.append(i)
                wonby='draw'
        try:
            lastmatchwon=li[-1]
            print(lastmatchwon)
        except Exception as e:
            lastmatchwon=0
        matcheswon=q   

        #matchdraw
        matchdraw=f
        b=0
        bi=[]
        #matchlost
        for j in range(0,len(x)):
            c=x[j]['loser'][1]
            w=x[j]['loser'][0]
            ga=x[j]['loser'][7]
            if w==n and c<g[j]['winner'][1] and ga=='1':
                b=b+1 
                bi.append(j)  
        try:
            lastmatchlost=bi[-1]
        except Exception as e:
            lastmatchlost=0
        matcheslost=b 

        #totalmatches                                     
        matchesplayed=matcheswon+matcheslost+matchdraw          
        y=0
        h=0
        #winbattingfirst
        for s in range(0,len(g)):
            if g[s]['winner'][4]!='0' and g[s]['winner'][0]==n and g[s]['winner'][7]=='1':
                y=y+1
            if g[s]['winner'][4]!='0' and g[s]['winner'][1]==x[s]['loser'][1] and g[s]['winner'][7]=='1':
                h=h+1
        Firstbattingwon=y   
        #drawbattingfirst
        drawbattingfirst=h                        
        mo=0
        #winbattingsecond
        for z in range(0,len(x)):
            po=x[z]['loser'][4]
            a=x[z]['loser'][0]
            if po=='0'and a==n and x[z]['loser'][1]!=g[z]['winner'][1] and x[z]['loser'][7]=='1':
                mo=mo+1
        Firstbattinglost=mo
        secondbattingwon=matcheswon-Firstbattingwon     
        bg=0
        #wins when toss won
        for jh in range(0,len(g)):
            cf=g[jh]['winner'][6]
            wf=g[jh]['winner'][0]
            if wf==n and cf=='1' and g[jh]['winner'][7]=='1':
                bg=bg+1
        winswhentosswon=bg

        bgf=0
        #loss when toss won
        for jhf in range(0,len(x)):
            cfd=x[jhf]['loser'][6]
            wfd=x[jhf]['loser'][0]
            if wfd==n and cfd=='1' and x[jhf]['loser'][7]:
                bgf=bgf+1
        losseswhentosswon=bgf
        totaltosswon=winswhentosswon+losseswhentosswon
        totaltosslost=matchesplayed-totaltosswon
        #tosswinpercentage
        try:
            tosswinperc=(totaltosswon/matchesplayed)*100
        except Exception as e:
             tosswinperc=0         
        #lastmatchplayed,lastmatchscore,opponent,wonby     (if lastmatch was a win)                     
        if lastmatchwon>lastmatchlost: 
            print('thth')
            lastmatchplayed=g[lastmatchwon]
            lastmatchscore=g[lastmatchwon]['winner'][1]
            lastmatchwickets=g[lastmatchwon]['winner'][3]
            lastmatchopponent=x[lastmatchwon]['loser'][0]
            wonby=int(g[lastmatchwon]['winner'][1])-int(x[lastmatchwon]['loser'][1])
            #nextmatch
            for sd in range(lastmatchwon+1,len(g)):
               
                    if g[sd]['winner'][0]!=n:
                        nextmatch=g[sd]['winner'][0]
                        next=Match.objects.filter(winner=g[sd]['winner'])
                        try:
                       
                            if next[sd].loser[0]==n:
                                nextmatchvenue=next[sd].venue
                                nextmatchdate=next[sd].date
                        except Exception as e:
                            pass
                    if x[sd]['loser'][0]!=n:
                        nextmatch=x[sd]['loser'][0]
                        next=Match.objects.filter(loser=x[sd]['loser'])
                        try:
                            if next[sd].winner[0]==n:
                                nextmatchvenue=next[sd].venue
                                nextmatchdate=next[sd].date    
                        except Exception as e:
                            pass                                 
                    
        #lastmatchplayed,lastmatchscore,opponent,lostby     (if lastmatch was a loss)  
        if lastmatchlost>lastmatchwon:
            lastmatchplayed=x[lastmatchlost]
            lastmatchscore=x[lastmatchlost]['loser'][1]
            lastmatchwickets=x[lastmatchlost]['loser'][3]
            lastmatchopponent=g[lastmatchlost]['winner'][0]
            lostby=int(g[lastmatchlost]['winner'][1])-int(x[lastmatchlost]['loser'][1])
            #nextmatch
            for sd in range(lastmatchlost+1,len(x)):
                if x[sd]['loser'][0]==n or g[sd]['winner'][0]==n:
                    if x[sd]['loser'][0]!=n:
                        nextmatch=x[sd]['loser'][0]
                        next=Match.objects.filter(loser=x[sd]['loser'])
                        for fg in range(0,len(next)):
                            if next[fg].winner[0]==n:
                                nextmatchvenue=next[fg].venue
                                nextmatchdate=next[fg].date
                    if g[sd]['winner'][0]!=n:
                        nextmatch=g[sd]['winner'][0]
                        next=Match.objects.filter(winner=g[sd]['winner'])
                        for fg in range(0,len(next)):
                            if next[fg].loser[0]==n:
                                nextmatchvenue=next[fg].venue
                                nextmatchdate=next[fg].date               
        h=[]   
        h.append(lastmatchlost)
        h.append(lastmatchwon)
        h.sort()
        ad=h[-1]
        kl=[]   
        jl=[]    
        jh=[]
        kj=[]
        hl=[]
        wl=[]
        for sdf in range(0,ad+1):
            if g[sdf]['winner'][0]==n and g[sdf]['winner'][5]!='nil':
                kl.append(g[sdf]['winner'][1])
                jl.append(x[sdf]['loser'][1])
                hl.append(g[sdf]['winner'][3])
                wl.append(x[sdf]['loser'][3])
                
                date=Match.objects.get(winner=g[sdf]['winner']).date
                jh.append(date)
            if  x[sdf]['loser'][0]==n and x[sdf]['loser'][5]!='nil':
                print('huy')
                kl.append(x[sdf]['loser'][1])
                jl.append(g[sdf]['winner'][1])
                hl.append(x[sdf]['loser'][3])
                wl.append(g[sdf]['winner'][3])
                
                date=Match.objects.get(winner=g[sdf]['winner']).date
                print(date)
                jh.append(date)

        for sdfb in range(0,ad+1):
             if g[sdfb]['winner'][0]==n or x[sdfb]['loser'][0]==n :
                 if g[sdfb]['winner'][0]==n and g[sdfb]['winner'][5]!='nil' :
                    if g[sdfb]['winner'][1]>x[sdfb]['loser'][1]:
                        kj.append('win')
                    elif g[sdfb]['winner'][1]==x[sdfb]['loser'][1]:
                        kj.append('loss')
                    else:
                        kj.append('loss')
                 elif x[sdfb]['loser'][0]==n and x[sdfb]['loser'][5]!='nil' :
                     if x[sdfb]['loser'][1]>g[sdfb]['winner'][1]:
                        kj.append('win')
                     elif x[sdfb]['loser'][1]==g[sdfb]['winner'][1]:
                        kj.append('loss')
                     else:
                        kj.append('loss')
        print(jh)
        print('mk') 
        try:
            jh=sorted(jh, key=lambda x: datetime.datetime.strptime(x, '%Y-%m-%d'))
            print(jh)
            bhdate=pd.date_range(start = jh[-1], periods = 2).to_pydatetime().tolist()
            print(bhdate)
            
            k2=bhdate[-1].strftime('%Y-%m-%d')
            print(k2)
            np=pd.date_range(start = k2, periods = 5).to_pydatetime().tolist()
        except:
            print('m')
            np=pd.date_range(end = datetime.datetime.today(), periods = 5).to_pydatetime().tolist()
        for i in range(5):
            a='-'
            if len(jh)<5:
                    k=np[i].strftime('%Y-%m-%d')
                    jh.append(k)
                    
                    print(jh)
                    jl.append("0")
                    kl.append("0")
                    kj.append("loss")
                    hl.append("0")
                    wl.append("0")
        
        
        print(jh)
        last5mathchesrunsscored=kl
        last5matchesrunsconceeded=jl
        print(jh)
        last5matchdates=jh
        last5matcheswicketstaken=wl
        last5matcheswicketslost=hl
        last5matchresults=kj
        lastmatchwickets=last5matcheswicketslost[-1]
        context ={'lastmatchwickets':lastmatchwickets,'id':id,'last5matchresults':last5matchresults,'last5matcheswicketstaken':last5matcheswicketstaken,'last5matcheswicketslost':last5matcheswicketslost,'last5matchesrunsconceeded':last5matchesrunsconceeded,'last5mathchesrunsscored':last5mathchesrunsscored,'last5matchdates':last5matchdates,'matchesplayed':matchesplayed,'matcheswon':matcheswon,'matcheslost':matcheslost,
        'matchdraw':matchdraw,'Firstbattingwon':Firstbattingwon,'secondbattingwon':secondbattingwon,'totaltosswon':totaltosswon,'totaltosslost':totaltosslost,'tosswinperc':tosswinperc,
        'lastmatchscore':lastmatchscore,'lastmatchopponent':lastmatchopponent,'wonby':wonby,'lostby':lostby ,'nextmatch':nextmatch,'nextmatchvenue':nextmatchvenue,'nextmatchdate':nextmatchdate}
        return JsonResponse(context)
    else:
        return HttpResponse(status=401)

def createTournament(request):
    data=request.POST
 
    if 'id' not in data:
        print('of  ')
        user=User.objects.get(username=request.session.get('user'))
        tournament=Tournament(name=data["tname"],place=data["place"],teams=data['allteams'],year=data['year'],user=user)
        tournament.save()
        print(data)
        point=Pointstable(tournament=tournament,teams=data['allteams'],win=data['win'],lose=data['loss'],draw=data['draw'])
        point.save()
        createteam(data,user,tournament)
        # if c[i]['date']==date:
        #     # print(c[i])
        #     obj=csv.objects.get(activated=False)
        #     obj.delete()
        #     return HttpResponse('match already there')
    else:
        print('yehh')
        tournament=Tournament.objects.get(id=data['id'])
        user4=User.objects.get(username=request.session.get('user'))
        tournament.name,tournament.place,tournament.teams,tournament.year,tournament.user==data["tname"],data["place"],data['allteams'],data['year'],user4
        tournament.save()
        return redirect('tournaments')
        
     
    
    if request.POST:return redirect('tournaments')
    return HttpResponse(str(tournament.pk))
  
def editTournament(request):
   
    name = request.POST.get('tname')
    id = request.POST.get('id')
    place=request.POST.get('place')
    year=request.POST.get('year')
    am=request.POST.get(id+'op')
    print(am)
    
    b=am.split('close')
    m=b[0:-1]
    print(m)
    tour=Tournament.objects.get(id=id)
    tour.name,tour.place,tour.year=name,place,year
     
    tour.save()
    tour=Tournament.objects.get(id=id)
    tour.teams=''
    removefromtour(id)
    if len(m)>1:
        for i in range(len(m)):

            tour.teams=tour.teams+','+m[i]
        tour.teams=tour.teams[1:]
        tour.save()
    else:
            tour.teams=m
            tour.save()
    
    user=User.objects.get(username=request.session.get('user'))
    n=Team.objects.all()
    for i in range(len(m)) :
            if m[i] not in n:
                print(n)
                x=Team.objects.get_or_create(name=m[i],user=user,tournament=tour)


    return redirect('tournaments')

def editTeam(request):
    
    name = request.POST.get('name')
    type = request.POST.get('type')
    id = request.POST.get('id')
    d = request.POST.get('t')
   
    am=request.POST.get(id+'op')
    print(am)
    
    b=am.split('close')
    m=b[0:-1]
    print(m)
    team=Team.objects.get(id=id)
    team.name,team.type=name,type
     
    team.save()
    team=Team.objects.get(id=id)
    team.players=''
    removefromteam(team)
    if len(m)>1:
        for i in range(len(m)):
        
            
            team.players=team.players+','+m[i]
        team.players=team.players[1:]
        team.save()
    else:
        team.players=m
        team.save()

    user=User.objects.get(username=request.session.get('user'))
    n=Team.objects.all()
    for i in range(len(m)) :
            if m[i] not in n:
                print(n)
                x=Player.objects.get_or_create(name=m[i],team=team)

    if d!='':
        return redirect(d+'/teams')
    else:
        return redirect('teamss')



# def edi(request):
#     if request.method=='POST':
        
        




def createteam(data,user,tournament):
    print(data)
    n=Team.objects.all()
    team=data["allteams"].split(",")
    for i in range(len(team)) :
            
            if team[i] not in n:x=Team.objects.get_or_create(name=team[i],user=user,tournament=tournament)
    n=Team.objects.all()
    # for k in range (len(n)):
    #     if n[k].name==i:
    #         g=g+1
    #         if g>2:
    #             if n[k].tournament==tournament:
    #                 n[k].delete()


def csvs(request):
    if request.method=='POST':
        form=CsvModelForm(request.POST,request.FILES)
        
        userl=User.objects.get(username=request.session.get('user'))
        ment=request.POST.get('t')
        if form.is_valid():
            form.save()
            form=CsvModelForm() 
            
            
            obj=csv.objects.get(activated=False)
            with open(obj.file_name.path,'r') as f:
                if not f.name.endswith('.csv'):
                    obj.delete()
                    obj=csv.objects.get(activated=False)
                    obj.delete()
                    
                    return HttpResponse('invalid file format')
                    
                else:
                    print(f)
                    next(f)
                    for row in f:
                        t=Tournament.objects.get(id=ment)
                        uid=int(random.random()*10*6)
                        row=''.join(row)
                        row=row.replace(","," ")
                        row=row.split()
                        # print(row)
                        venue=row[1]
                        team=Team.objects.filter(tournament=t)
                        kk=[]
                        for i in range(len(team)):
                            kk.append(team[i].name)
                        print(kk,row[2])
                        if row[2] in kk:
                            team1=row[2]
                        else:
                            return HttpResponse('Team is not in Tournament')
                        if row[3] in kk:
                            team2=row[3]
                        else:
                            return HttpResponse('Team is not in Tournament')
                        date=row[4]
                        print(date)
                        time=row[5]
                        report=row[6]
                        c=Match.objects.filter(tournament=t)
                        print(c)
                        Match.objects.create(uniqueid=uid,tournament=t,venue=venue,type='odi',status='Upcoming',report=report,winner=[team1,'0','0','0','0',"nil",'0','0'],loser=[team2,'0','0','0','0',"nil",'0','0'],date=date,time=time,user=userl)
                        print(row)
                        print(type(row))
                        obj.activated=True
                        obj.save()
                    return redirect('/'+ment+'/matches')
        
        else:
              return HttpResponse('invalid file format')
    else:
        return HttpResponse('invalid  file format')
    
            

def deleteTournament(request):
    tournament=Tournament.objects.get(id=request.POST['id'])
    tournament.delete()
    return redirect('tournaments')

def createMatch(request):
    #Request body
    if not request.POST:
        my_json = request.body.decode('utf8').replace("'", '"')
        data = json.loads(my_json)
    else:
        data=request.POST
    #Create match

    if data["fromcreate"]=="yes":
        if 'mid' in data:
            match=Match.objects.get(id=data['mid'])
            match.winner[0],match.venue,match.loser[0],match.date=data["Winner"],data["Venue"],data['Loser'],data["Date"]
            match.type,match.time=data["Type"],data["Time"]
            match.save()
            return redirect('matches',id=int(data["id"]))
        match=saveMatch(data)
        if request.POST:return redirect('matches',id=int(data["id"]))
        return HttpResponse(str(match.pk))
    #Save match

    match=saveMatch(data)
    saveComment(match,data["ballbyball"],"Result")
    saveBatsman(match,data)
    saveBowler(match,data)
    return HttpResponse(str(match.pk))
    

def deleteMatch(request):
    match=Match.objects.get(id=request.POST['id'])
    match.delete()
    return redirect('matches',id=request.POST['tid'])

def createTeam(request):
    #Request body
    if not request.POST:
        my_json = request.body.decode('utf8').replace("'", '"')
        data = json.loads(my_json)
    else:
        data=request.POST
    #Create match
    try:
        for i in data["allteams"].split(","):
            x,y=Player.objects.get_or_create(name=i,team=data["name"])
           
        if 'id' in data:
            t=Tournament.objects.get(id=data['id'])
            user=User.objects.get(username=request.session.get('user'))
            team=Team.objects.get(id=data['id'])
            team.name,team.type,team.players,team.user,team.tournament=data["name"],data["type"],data['allteams'],user,t
            team.save()
            if request.POST:
                return redirect('teams')
            return HttpResponse(str(team.pk))
        user=User.objects.get(username=request.session.get('user'))
        if data['tour']=='0':
            print('yesssssssssssssss')
            team=Team(name=data["name"],type=data["type"],players=data['allteams'],user=user)
            team.save()         
        else:
            t=Tournament.objects.get(id=data['tour'])
            print('yes')
            h=(t.teams).split(',')
            team=Team(name=data["name"],type=data["type"],players=data['allteams'],user=user,tournament=t)
            team.save()
            
            h.append(team.name)
            h=",".join(h)
            print(h)
            print('end')
            t.teams=h
            
            t.save()
               
        if request.POST:return redirect('teams')
        return HttpResponse(str(team.pk))
    except Exception as e:
        return HttpResponse("Teams creation failed")

def deleteTeam(request):
    team=Team.objects.get(id=request.POST['id'])
    team.delete()
    t=Tournament.objects.all()
    v=request.POST['t']
    for i in range(len(t)):
        if team.name in t[i].teams:
            t[i].teams.replace(team.name, "")
            
    return redirect('/'+v+'/'+'teams')

def removefromtour(tourn):
    te=Team.objects.filter(tournament=tourn)
    for i in range(len(te)):
        te[i].tournament=None
        te[i].save()

def removefromteam(team):
    te=Player.objects.filter(team=team)
    for i in range(len(te)):
        te[i].team=None
        te[i].save()

def setToss(request):
    #Request body
    if not request.POST:
        my_json = request.body.decode('utf8').replace("'", '"')
        data = json.loads(my_json)
    else:
        data=request.POST
    #Allot toss
    try:
        print(data["team1"])
        print(data["toss"])
        print(data["batteam"])
        matchcode=request.COOKIES["code"]
        match=Match.objects.get(uniqueid=matchcode)
        if(data["team1"]==match.winner[0]):
            match.winner[5]="-".join(data.getlist("players1[]"))
            match.loser[5]="-".join(data.getlist("players2[]"))
        else:
            match.winner[5]="-".join(data.getlist("players2[]"))
            match.loser[5]="-".join(data.getlist("players1[]"))
        if(data["toss"]==match.winner[0]):
            match.winner[6],match.loser[6]=(1,0)
            
        else:
            match.loser[6],match.winner[6]=(1,0)
            
        if(data["batteam"]==match.winner[0]):
            match.winner[4],match.loser[4]=(1,0)
        else:
            match.loser[4],match.winner[4]=(1,0)
        match.report=data["report"]
        match.status="Live"
        match.save()
        if request.POST:
            return redirect("events")
        return HttpResponse("Toss created successfully")
    except Exception as e:
        return HttpResponse("Toss creation failed")

def setMatchlive(request,id):
    match,fow = Match.objects.get(id=id),""
    matchlive,inning,matchlive_comm,last_wicket,batlive,bowlive=dataLive(match)
    change  = True if len(list(Comment.objects.filter(match=match,inning=2)))==1 else False
    wickets = list(Batsman.objects.filter(match=match,inning=inning).exclude(status="Not out").values())
    #Fall of wickets
    if len(wickets)!=0:
        fow="𝐅𝐚𝐥𝐥 𝐨𝐟 𝐰𝐢𝐜𝐤𝐞𝐭𝐬: "
        for i in wickets:
            fow+=str(wickets.index(i)+1)+"-"+i['last_info'][0]+" ("+i['name'].capitalize()+", "+i['last_info'][1]+" ov)"
            if wickets.index(i)!=len(wickets)-1:fow+=", "
    return JsonResponse({'last':last_wicket,"inni":inning,'fow':fow,'matchlive':matchlive,'change':change,'livecomment':matchlive_comm,'batlive':batlive,'bowlive':bowlive})

def editComment(request):
    data=request.POST
    try:
        comment=Comment.objects.get(id=data["cid"])
        #Change match
        match=Match.objects.get(id=data["mid"])
        temp=match.winner if int(data["einning"])%2==int(match.winner[4]) else match.loser
        temp=[temp[0],str(int(temp[1])+int(data['erun'])-int(comment.run)),temp[2],temp[3],temp[4],temp[5]]
        if int(data["einning"])%2==int(match.winner[4]):match.winner=temp
        else:match.loser=temp
        #change batsmen and bowlers
        player1,player2=Player.objects.get(name=request.POST["p1"].lower()),Player.objects.get(name=request.POST["p2"].lower())
        striker=Batsman.objects.get(match=match,inning=data["einning"],player=player1)
        bowler=Bowler.objects.get(match=match,inning=data["einning"],player=player2)
        four=setBoundaries(int(data["erun"]),int(comment.run),4)
        six=setBoundaries(int(data["erun"]),int(comment.run),6)
        striker.runs,striker.fours,striker.sixes=striker.runs+int(data["erun"])-int(comment.run),striker.fours+four,striker.sixes+six
        striker.strike_rate=float(str(round(striker.runs/striker.balls,2)*100)[:len(str(int(round(striker.runs/striker.balls,2)*100)))+3])
        bowler.runs=bowler.runs+int(data["erun"])-int(comment.run)
        try:bowler.economy=round(bowler.runs/(int(bowler.overs)*6 + (bowler.overs-int(bowler.overs))*10),2)
        except Exception as e:bowler.economy=0
        striker.save()
        bowler.save()
        comment.remark=data["eremark"]
        comment.run=data["erun"]
        comment.save()
        match.save()
        return redirect('events')
    except Exception as e:
        return HttpResponse(e)
        
def setMatchlive(request,id):
    match,fow = Match.objects.get(id=id),""
    matchlive,inning,matchlive_comm,last_wicket,batlive,bowlive=dataLive(match)
    change  = True if len(list(Comment.objects.filter(match=match,inning=2)))==1 else False
    wickets = list(Batsman.objects.filter(match=match,inning=inning).exclude(status="Not out").values())
    #Fall of wickets
    if len(wickets)!=0:
        fow="𝐅𝐚𝐥𝐥 𝐨𝐟 𝐰𝐢𝐜𝐤𝐞𝐭𝐬: "
        for i in wickets:
            fow+=str(wickets.index(i)+1)+"-"+i['last_info'][0]+" ("+Player.objects.get(id=int(i["player_id"])).name.capitalize()+", "+i['last_info'][1]+" ov)"
            if wickets.index(i)!=len(wickets)-1:fow+=", "
    return JsonResponse({'last':last_wicket,"inni":inning,'fow':fow,'matchlive':matchlive,'change':change,'livecomment':matchlive_comm,'batlive':batlive,'bowlive':bowlive})

def setComment(request):
    if not request.POST:
        my_json = request.body.decode('utf8').replace("'", '"')
        data = json.loads(my_json)
    else:
        data=request.POST
    #Read event
    if True:
        #Match details
        match=Match.objects.get(uniqueid=request.COOKIES["code"])
        if match.status!="Result":
            if match.status=="Upcoming":match.status="Live"
            temp=match.winner if int(data["inning"])%2==int(match.winner[4]) else match.loser
            if len(list(set(data['others'].split(",")).intersection({'caught','bowled','obstruct','handled','runouts','hit wicket','lbw','stumped','hit twice'})))>0:
                temp,last_info=[temp[0],str(int(temp[1])+int(data['run'])),data['over']+"."+data["ball"],str(int(temp[3])+1),temp[4],temp[5],temp[6],temp[7]],[str(int(temp[1])+int(data['run'])),data['over']+"."+data["ball"]]
            else:
                temp,last_info=[temp[0],str(int(temp[1])+int(data['run'])),data['over']+"."+data["ball"],temp[3],temp[4],temp[5],temp[6],temp[7]],[]
            if int(data["inning"])%2==int(match.winner[4]):match.winner=temp
            else:match.loser=temp
            match.save()
        #Striker details
            ball,pos=1,"stk"
            four=1 if data["run"]=='4' else 0
            six=1 if data["run"]=='6' else 0
            if len(list(set(data['others'].split(",")).intersection({'bye','leg bye','dead ball'})))>0:ball=0
            wides=1 if "wide" in data['others'].split(",") else 0
            noballs=1 if "no ball" in data['others'].split(",") else 0
            team1,team2=(match.winner[0],match.loser[0]) if int(data["inning"])-1==int(match.winner[4]) else (match.loser[0],match.winner[0])
            if len(list(set(data['others'].split(",")).intersection({'caught','bowled','obstruct','handled','runouts','hit wicket','lbw','stumped','hit twice'})))>0:status,wickets="("+list(set(data['others'].split(",")).intersection({'caught','bowled','obstruct','handled','runouts','hit wicket','lbw','stumped','hit twice'}))[0][0]+") "+data["bowler"].capitalize(),1
            else:status,wickets="Not out",0
            team1,team2=Team.objects.get(name=team1),Team.objects.get(name=team2)
            player1,player2,player3=Player.objects.get(name=data["striker"].lower()),Player.objects.get(name=data["nonstriker"].lower()),Player.objects.get(name=data["bowler"].lower())
            try:
                striker=Batsman.objects.get(match=match,player=player1)
                striker.runs,striker.balls,striker.fours,striker.sixes,striker.status=striker.runs+int(data["run"]),striker.balls+ball,striker.fours+four,striker.sixes+six,status
                striker.strike_rate,striker.last_info=float(str(round(striker.runs/striker.balls,2)*100)[:len(str(int(round(striker.runs/striker.balls,2)*100)))+3]),last_info            
                try:
                    prev_striker=Batsman.objects.get(match=match,inning=int(data["inning"]),pos="stk")
                    if striker.pos=="nonstk" and prev_striker.status!="Not out":
                        prev_striker.pos=""
                        prev_striker.save()
                except Exception:
                    pass
            except Exception:
                try:
                    prev_striker=Batsman.objects.get(match=match,inning=int(data["inning"]),pos="stk")
                    prev_striker.pos=""
                    prev_striker.save()
                except Exception:
                    pass
                striker=Batsman(match=match,pos=pos,last_info=last_info,inning=int(data["inning"]),runs=int(data["run"]),balls=ball,fours=four,sixes=six,strike_rate =int(data["run"])*100,team=team1,status=status,player=player1)
            striker.pos="stk"
            striker.save()
        #Nonstriker Details
            try:
                nonstriker=Batsman.objects.get(match=match,player=player2)
            except Exception:
                try:
                    prev_nonstriker=Batsman.objects.get(match=match,inning=int(data["inning"]),pos="nonstk")
                    prev_nonstriker.pos=""
                    prev_nonstriker.save()
                except Exception:
                    pass
                nonstriker=Batsman(match=match,pos="nonstk",inning=int(data["inning"]),runs=0,balls=0,fours=0,sixes=0,strike_rate=0,team=team1,status="Not out",player=player2)
            nonstriker.pos="nonstk"
            nonstriker.save()
        #Bowler Details
            maiden,prev_over=0,[]
            if data["ball"]=='1' and int(data["over"])>=1:prev_over=Comment.objects.filter(match=match,inning=int(data["inning"]),over=int(data["over"])-1)
            for i in list(prev_over):maiden=maiden+1 if i.run==0 and i.bowler==data["bowler"] else maiden
            try:
                bowler=Bowler.objects.get(match=match,player=player3)
                if maiden==6:bowler.maidens+=1
                if round(bowler.overs-int(bowler.overs),1)==0.6:
                    bowler.overs=bowler.overs+0.5
                    if wides==1 or noballs==1:bowler.overs-=0.5
                else:
                    bowler.overs=(bowler.overs*10 + 1)/10
                    if wides==1 or noballs==1:bowler.overs-=0.1
                bowler.runs,bowler.no_balls,bowler.wides,bowler.wickets,bowler.overs=bowler.runs+int(data["run"]),bowler.no_balls+noballs,bowler.wides+wides,bowler.wickets+wickets,float(str(bowler.overs)[:3])
                try:bowler.economy=round(bowler.runs/(int(bowler.overs)*6 + (bowler.overs-int(bowler.overs))*10),2)
                except Exception as e:bowler.economy=0
            except Exception:
                over=0 if wides==1 or noballs==1 else 0.1
                bowler=Bowler(match=match,inning=int(data["inning"]),overs=over,runs=int(data["run"]),no_balls=noballs,wides=wides,wickets=wickets,economy=int(data["run"]),team=team2,maidens=0,player=player3)
            bowler.save()
        #Comment Details
            saveComment(match,data,"Live")
            match=Match.objects.get(uniqueid=request.COOKIES["code"])
            comments=list(Comment.objects.filter(match=match).order_by('id').values())[::-1][:6]
            return JsonResponse({"recentcomment":comments})
        else:
            return HttpResponse("Match completed already")

def finishMatch(request):

        matchcode=request.COOKIES["code"]#from session
        match=Match.objects.get(uniqueid=matchcode)
        match.status="Result"
        match.winner[7],match.loser[7]=(1,1)
        match.save()
        if match.winner[1]<match.loser[1]:
            f=Team.objects.get(name=match.winner[0])
            
            f.win==2
            f.save()
            
            match.winner,match.loser=match.loser,match.winner
            match.save()

            
        
        if request.POST:return redirect("scorecard",id=match.id)
        return HttpResponse("Success")
 

def fetchPlayers(request,inn)    :
    match,bat,bowl=Match.objects.get(uniqueid=request.COOKIES["code"]),[],[]
    team1,team2=(match.winner[5],match.loser[5]) if int(inn)%2==int(match.winner[4]) else (match.loser[5],match.winner[5])
    for i in team1.split("-"):bat.append(i)
    for i in team2.split("-"):bowl.append(i)
    return JsonResponse({"bat":bat,"bowl":bowl})


#Helper functions
@background(schedule=0)
def getTweets():
    inst=twint.Config()
    inst.Search="cricket"
    inst.Lang = "en"
    inst.Limit=5
    inst.Verified=True
    inst.Store_json=True
    inst.Output="static/twitter/tweets.json"
    twint.run.Search(inst)
    data=pd.read_json("static/twitter/tweets.json",lines=True)
    no=random.sample(range(0, 20), 5)
    for i in range(5):
        tweet=Tweet.objects.get(label=i)
        tweet.username=str(data['username'][no[i]]),
        tweet.body=str(unicodedata.normalize("NFKD",data['tweet'][no[i]])),
        tweet.date=str(data['date'][no[i]]),
        tweet.link=str(data['link'][no[i]])
        tweet.save()

def getLeftpane():
    page = requests.get('https://medium.com/crimpulse')
    soup,leftpane = BeautifulSoup(page.content,'html.parser'),[]
    links= soup.find_all(attrs={"data-action" : "open-post"})
    authors= soup.find_all('a',class_="ds-link ds-link--styleSubtle link link--darken link--accent u-accentColor--textNormal u-accentColor--textDarken")
    titles= soup.find_all('h3',class_="graf--title")
    images=soup.find_all('img')
    j,k=2,0
    for i in range(9):
        text = titles[i].text
        leftpane.append([unicodedata.normalize("NFKD",text),links[k]['href'],authors[i].text,images[j]['src']])
        j+=2
        k+=2
    return leftpane

def getRightpane():
    upcomimg=Match.objects.filter(status="Upcoming")
    for i in upcomimg:
        datelist=i.date.split("-")
        temp = datetime.datetime(int(datelist[0]), int(datelist[1]), int(datelist[2]))
        i.date=temp.strftime("%b")+" "+str(int(temp.strftime("%d")))+", "+temp.strftime("%Y")
    return {'upcoming':upcomimg,
    'completed':Match.objects.filter(status="Result"),'live':Match.objects.filter(status="Live")}

def dataLive(match):
    #Determine Live inning
    inning=2
    matchlive=match.winner if match.winner[4]=='0' else match.loser
    if len(list(Comment.objects.filter(match=match,inning=2)))==0:
        inning=1
        matchlive=match.winner if match.winner[4]=='1' else match.loser
    else:
        inning=2
        matchlive=match.winner if match.winner[4]=='0' else match.loser
    #Live Batsmen
    try:batlive=[Batsman.objects.filter(match=match,inning=inning,pos="stk").values()[0],Batsman.objects.filter(match=match,inning=inning,pos="nonstk").values()[0]]
    except Exception:batlive=[]
    for i in batlive:i["name"]=Player.objects.get(id=int(i["player_id"])).name
    #Live Bowlers
    bowlive=list(Bowler.objects.filter(match=match,inning=inning).values())[::-1][:2][::-1]
    for i in bowlive:i["name"]=Player.objects.get(id=int(i["player_id"])).name
    #Live commentary(12) and last wicket
    matchlive_comm=list(Comment.objects.filter(match=match,inning=inning).order_by('id').values())[::-1][:12]
    try:last_wicket=list(Batsman.objects.filter(match=match,inning=inning).exclude(status="Not out").values())[-1]
    except Exception:last_wicket=False
    return (matchlive,inning,matchlive_comm,last_wicket,batlive,bowlive)

# Save to DB functions
def saveComment(match,data,type):
    if type=="Result":
        for i in range(1,3):
            for j in data["Inning"+str(i)]:
                comment=Comment(match=match,inning=i,over=j["over"],run=j["runs"],ball=j["ball"],others=j["other"],remark="Lorem ipsum tempor incididunt ut labor ex ea commodo consequat.",batsman=j["batsman"],bowler=j["bowler"])
                comment.save()
    else:
        comment=Comment(match=match,inning=data["inning"],over=data["over"],run=data["run"],ball=data["ball"],remark=data["remark"],batsman=data["striker"].capitalize(),bowler=data["bowler"].capitalize(),others=","+data["others"])
        comment.save()

def saveMatch(data):
    tournament=Tournament.objects.get(id=data["id"])
    user=User.objects.get(username='dk')
    
    uid=int(random.random()*10**6)
    while(True):
        try:
            temp=Match.objects.get(uniqueid=uid)
            uid=int(random.random()*10**6)
        except Exception:
            break
    if data["fromcreate"] == 'yes':match=Match(uniqueid=uid,date=data["Date"],status=data['status'],type=data["Type"],time=data['Time'],tournament=tournament,venue=data["Venue"],winner=[data["Winner"],'0','0','0','0',"nil",'0','0'],loser=[data["Loser"],'0','0','0','0',"nil",'0','0'],user=user)
    else:match=Match(uniqueid=uid,status=data['status'],type="International",time="00:00",report="sample match report",date="January 1st, 2021",tournament=tournament,venue=data["Venue"],winner=data["Winner"],loser=data["Loser"])
    match.save()
    return match

def saveBatsman(match,data):
    for i in range(1,3):
        for j in data["Inning"+str(i)]["Batsmen"]:
            player=Player.objects.get_or_create(name=j["name"])[0]
            team=Team.objects.get_or_create(name=j["Team_Name"])[0]
            batsman=Batsman(match=match,inning=i,player=player,runs=j['runs'],balls=j['balls'],
            fours=j['fours'],sixes=j['six'],team=team,status=j['status'],strike_rate=j['strike_rate'])
            batsman.save()

def saveBowler(match,data):
    for i in range(1,3):
        for j in data["Inning"+str(i)]["Bowlers"]:
            player=Player.objects.get_or_create(name=j["name"])[0]
            team=Team.objects.get_or_create(name=j["Team_Name"])[0]
            bowler=Bowler(match=match,inning=i,player=player,runs=j['runs'],no_balls=j['No_balls'],
            maidens=j['maiden'],overs=j['Overs'],team=team,wides=j['wides'],economy=j['Economy'],wickets=j["wickets"])
            bowler.save()

def setBoundaries(new,old,boundary):
    if old==boundary and new==boundary: return 0
    elif  old!=boundary and new==boundary:return 1
    elif old==boundary and new!=boundary:return -1
    else:return 0

def settings(request):
    user=user=User.objects.get(username=request.session.get('user'))
    try:
       users=Profiles.objects.get(user=user)
    except Exception:
        print('profile not found')
        users=0
    tourn=Tournament.objects.filter(user=user)
    for i in range(len(tourn)):
        b=tourn[i].teams
        c=b.split(',')
        print(c)
        teamss=c[0 ]

    userl=User.objects.get(username=request.session['user'])
    j=userl.id
    
    return render(request, 'settings.html',{'user':user,'users':users,'j':j})

def editsettings(request):
    user=user=User.objects.get(username=request.session.get('user'))
    users=Profiles.objects.get(user=user)
    return render(request, 'editsettings.html',{'user':user,'users':users})

def editsettingss(request):
    if not request.POST:
        my_json = request.body.decode('utf8').replace("'", '"')
        data = json.loads(my_json)
    else:
        data=request.POST
    
    profile=Profiles.objects.get(oid=data['oid'])
    user=User.objects.get(id=data['iddd'])
    profile.name=data['oname']
    profile.number=data['number']
    profile.address=data['address']
    user.username=data['hname']
    user.email=data['email']
    profile.save()
    user.save()

    if request.POST:return redirect('settings')

def managecommentator(request):
    commentator=Commentator.objects.all()
    userr=request.session.get('user')
    user=User.objects.get(username=userr)
    user=user.id
    return render(request, 'mcommentator.html',{'commentator':commentator,'user':user})

def morganiser(request):
    organizers=Profiles.objects.all()
    return render(request, 'morganiser.html',{'organizers':organizers})

def teamspages(request):
    if request.session._session_key is not None:
         #Rightpane
        rightpane=getRightpane()
        #Centerpane
        user=User.objects.get(username=request.session.get('user'))
        use=user.id
        teams=Team.objects.filter(user=use)
        players=Player.objects.all()
        players=Player.objects.all()
        tourn=Tournament.objects.filter(user=user)
        for i in range(len(tourn)):
            b=tourn[i].teams
            c=b.split(',')
            print(c)
            teamss=c[0 ]

        userl=User.objects.get(username=request.session['user'])
        j=userl.id
        

        return render(request,'teamss.html',{'rightpane':rightpane,"teams":teams,"players":players,'j':j,'use':use})
    else:           
         return HttpResponse("<h1>Page not authorized for Commentators</h1>")

def playerstable(request):
    rightpane=getRightpane()
    userl=User.objects.get(username=request.session.get('user'))
    j=userl.id
    team=Team.objects.filter(user=j)
    players=Player.objects.all()
    bat=Batsman.objects.all()
    plr=[]
    # for i in range(len(players)):
    #     print(players[i])
        
    #     n=Batsman.objects.get(player=players[i])
    #     b=Bowler.objects.get(player=players[i])
    #     plr.append(n)
    #     plr.append(b)


    #     print(players[i],n)

    #     print('p')
    
    listofplayers=[]
    for le in range(len(team)):
        
        li2=Player.objects.filter(team=team[le].name)
        listofplayers.append(li2)
    tourn=Tournament.objects.filter(user=userl)
    for i in range(len(tourn)):
        b=tourn[i].teams
        c=b.split(',')
        print(c)
        teamss=c[0 ]

    userl=User.objects.get(username=request.session['user'])
    j=userl.id
  
    print(plr)
    return render(request,"players.html",{'rightpane':rightpane,'listofplayers':listofplayers,'j':j,'team':team,'plr':plr})

def createPlayers(request):

    print('op')
                
    player = request.POST.get('name')
    team = request.POST.get('team')
    print(player)
    Player.objects.create(name=player,team=team)
    print('ok')
    t=Team.objects.get(name=team)
    p=t.players
    t.players=t.players+player
    t.save()
    return redirect('playerstable')
                



def matchestable(request):
    match=Match.objects.all()
    for i in match:
        t=datetime.datetime.now()
        tt=datetime.datetime.strptime(i.date,'%Y-%m-%d')
        if(tt.date() < t.date()):
            if(i.status == 'Upcoming'):
                i.status="Abandoned"
                i.save()
        if(tt.date() > t.date()):
            if(i.status == 'Abandoned'):
                i.status="Upcoming"
                i.save()

    userl=User.objects.get(username=request.session['user'])
    j=userl.id
    team=Team.objects.filter(user=j)
    tourn=Tournament.objects.filter(user=j)
    toourn=[]
    for i in range(len(tourn)):
        toourn.append(tourn[i].name)
    print(toourn)
    
    for jk in tourn:
        print(jk.name)
        try:
            teams=Team.objects.filter(tournament=jk.id)
        except:
            teams=[]
    for kj in teams:
        print(kj.name)
    match=Match.objects.values('winner')
    matchl=Match.objects.values('loser')
    tkn=Match.objects.all()
    mtid=[]
    print(' dfsfaew')

    for k in range(len(tkn)):
        for i in range(len(team)):
            neee=match[k]['winner']
            neeel=matchl[k]['loser']
            if(team[i].name in neee):
                mtid.append(tkn[k])
            if(team[i].name in neeel):
                mtid.append(tkn[k])  
    mtid=list(set(mtid))
    tttk=[]
    for i in mtid:
        print(str(i.user),userl)
        if i.user==userl:
            print(i.user)
            tttk.append('1')
        else:
            tttk.append('0')
    ip=zip(mtid,tttk)
    for i in range(len(tourn)):
        b=tourn[i].teams
        c=b.split(',')
        print(c)
        teamss=c[0 ]

    userl=User.objects.get(username=request.session['user'])
    j=userl.id
    


    rightpane=getRightpane()
    return render(request,"matchestable.html",{'ip':ip,'rightpane':rightpane,'team':team,'teams':teams,'tourn':tourn,'mtid':mtid,'j':j})
def matchtablesave(request):
    if not request.POST:
        my_json = request.body.decode('utf8').replace("'", '"')
        data = json.loads(my_json)
    else:
        data=request.POST
    #Create match
    
    if data["fromcreate"]=="yes":
        if 'mid' in data:
            match=Match.objects.get(id=data['mid'])
            match.winner[0],match.venue,match.loser[0],match.date=data["Winner"],data["Venue"],data['Loser'],data["Date"]
            match.type,match.time=data["Type"],data["Time"]
            use=User.objects.get(username=request.session.get('user'))
            match.user=use
            match.save()
    return redirect('matchestable')

def deletematchtable(request):
    match=Match.objects.get(id=request.POST['id'])
    match.delete()
    return redirect('matchestable')
