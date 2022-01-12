
from django.conf import settings
from django.contrib import admin
from django.urls import path
from app import views
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls.static import static

urlpatterns = [
#WebPages
    path('admin/',admin.site.urls),
    path('', views.landingPage),
    path('start', views.startPage,name="start"),
    path('scorecard/<id>',csrf_exempt(views.scorecardPage),name="scorecard"),
    path("tournaments",csrf_exempt(views.tournamentsPage),name="tournaments"),
    path('edittour', views.editTournament,name="edittour"),
    path('editteam', views.editTeam,name="editteam"),
    #  path('edi', views.edi,name="edi"),
   
    path("comments",csrf_exempt(views.commentaryPage),name="events"),
    path("<id>/matches",csrf_exempt(views.matchesPage),name="matches"),
    path("td/<id>",views.tda,name="teamdata"),
    path("<tournament>/teams",csrf_exempt(views.tteamsPage),name="tteams"),
    path("teams",csrf_exempt(views.teamsPage),name="teams"),

    path("teamss",views.teamspages,name="teamss"),
    path("players",views.playerstable,name="playerstable"),
    path("matches",views.matchestable,name="matchestable"),
    path("matchessave",csrf_exempt(views.matchtablesave),name="matchessave"),
    path("matchedelete",csrf_exempt(views.deletematchtable),name="matchedelete"),
    #loginPages
    path('login', views.oragnizerLogin,name="login"),
    path('codelogin', views.commentatorLogin,name="codelogin"),
    path('logout', views.logout,name="logout"),#lP
    #adminInterfacePages
    path('adminlog', views.adminLogin,name="adminlog"),
    path('adminadd', views.addOrganizer,name="adminadd"),
    path('admindel', views.del_organizerList,name="admindel"),
    path('olist', views.edit_organizerList,name="olist"),
    path('add', views.add,name="add"),
    path('csv', views.csvs,name="csv"),
    path('txt', views.txts,name="txt"),
    path('edit', views.edit_radio,name="edit"),
    path("checkbox",csrf_exempt(views.delOrganizer),name="checkbox"),
    path('team', views.team,name="edit"),
    path('ct', views.ct,name="ct"),
    path('<id>/pointstable', views.PointsTable,name="pointstable"),
    
    
    path("onclick",csrf_exempt(views.editOrganizer),name="onclick"),#aIP
    #forgotpasswordpages
    path('email', views.email,name="email"),
    path('mail', views.mail,name="mail"),
    path('forgotpassword', views.forgotpassword,name="forgotpassword"),

    path('livescores', views.pagenotcreated,name="livescores"),
    path('stat/<id>/<user>', views.stat),
    path('tstat', views.tstats,name="tstat"),
    path('cp', views.createPlayers,name="cp"),
    path("create/commentator",csrf_exempt(views.createcommentator),name="createcommentator"),
    path("edit/commentator",csrf_exempt(views.editcommentator),name="editcommentator"),
    path("delcommentator",csrf_exempt(views.delcommentator),name='delcommentator'),
#APIs
    path("tournament/create",csrf_exempt(views.createTournament),name="createtour"),
  
    path("tournament/delete",csrf_exempt(views.deleteTournament),name="deletetour"),
    path("match/create",csrf_exempt(views.createMatch),name="creatematch"),
    path("match/delete",csrf_exempt(views.deleteMatch),name="deletematch"),
    path("team/create",csrf_exempt(views.createTeam),name="createteam"),
    path("team/delete",csrf_exempt(views.deleteTeam),name="deleteteam"),
    path("match/event",csrf_exempt(views.setComment),name="event"),
    path("match/toss",csrf_exempt(views.setToss),name="toss"),
    path("match/finish",csrf_exempt(views.finishMatch),name="finish"),
    path("scorecard/live/<id>",csrf_exempt(views.setMatchlive)),
    path('fetch/<inn>',csrf_exempt(views.fetchPlayers),name='fetch'),
    path('stats/<id>',csrf_exempt(views.stats),name='stats'),
    path("match/editevent",csrf_exempt(views.editComment),name="editcomment"),
    path('settings', views.settings,name="settings"),
    path('editsettings', views.editsettings,name="editsettings"),
    path("editsettingss",csrf_exempt(views.editsettingss),name="editsettingss"),
    path("managecomm",csrf_exempt(views.managecommentator),name="managecomm"),
    path("morganiser",csrf_exempt(views.morganiser),name="morganiser"),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings)