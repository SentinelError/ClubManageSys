from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = "main"


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("register", views.register_request, name="register"),
    path("edituser", views.edit_request, name="edit"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
    path("clubhomepage", views.clubhomepage, name="clubhomepage"),
    path("events", views.events, name="events" ),
    path("addevent", views.addevents, name="addevent" ),
    path("updateevents/<eventid>", views.updevents, name="updateevents" ),
    path("deleteevent/<eventid>", views.delevents, name="delevent" ),
    path("searchevent", views.searchevent, name="searchevent" ),
    path("venues", views.venues, name="venues"),
    path("updatevenues/<venueid>", views.updvenues, name="updatevenues" ),
    path("deletevenue/<venueid>", views.delvenues, name="delvenue" ),
    path("addvenue", views.addvenues, name="addvenue" ),
    path("searchvenue", views.searchvenue, name="searchvenue" ),
    path("reports", views.reports, name="reports" ),
    path("addreport", views.addreport, name="addreport" ),
    path("updatereport/<reportid>", views.updreport, name="updatereport" ),
    path("deletereport/<reportid>", views.delreport, name="delreport" ),
    path("printreport/<reportid>", views.printreport, name="printreport"),
    path("searchreport", views.searchreport, name="searchreport" ),
    path("printcsv", views.printcsv, name="printcsv"),
    path("password/", views.changepassword, name="changepassword" ),
    path("eventapproval", views.eventapproval, name="eventapproval"),
    path("users", views.users, name="users" ),
    path("updateuser/<userid>", views.upduser, name="updateuser" ),
    path("searchuser", views.searchuser, name="searchuser" ),
]