import calendar
import csv
from calendar import HTMLCalendar
from datetime import datetime
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .forms import NewUserForm, EventFormA, EventFormS, VenueForm, StudentForm, ReportForm, NewEditForm
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .models import Event, Venue, Report, Student
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.core.paginator import Paginator


# Registration View

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        Sform = StudentForm(request.POST)

        if form.is_valid() and Sform.is_valid():
            user = form.save()

            student = Sform.save(commit=False)
            student.user = user

            student.save()

            # login(request, user)
            messages.success(request, "Registration successful.")
            return HttpResponseRedirect("/login")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    Sform = StudentForm()
    return render(request=request, template_name="App2/register.html",
                  context={"register_form": form, "Student": Sform})


# Edit Profile View

def edit_request(request):
    if request.method == "POST":
        form = NewEditForm(request.POST, instance=request.user)
        Sform = StudentForm(request.POST, instance=request.user.student)
        if form.is_valid() and Sform.is_valid():
            user = form.save()

            student = Sform.save(commit=False)
            student.user = user

            student.save()

            messages.success(request, ("Profile updated."))
            return HttpResponseRedirect("/clubhomepage")
        messages.error(request, "Unsuccessful update. Invalid information.")
    else:
        form = NewEditForm(instance=request.user)
        Sform = StudentForm(instance=request.user.student)
    return render(request=request, template_name="App2/edituser.html", context={"edit_form": form, "Student": Sform})


# Change Password View

def changepassword(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, ("Password Change successful."))
            return HttpResponseRedirect("/")
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request=request, template_name="App2/passwordchange.html", context={"passwordchange_form": form, })


# Login View

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/clubhomepage')
            else:
                messages.error(request, ("Invalid username or password."))
        else:
            messages.error(request, ("Invalid username or password."))
    form = AuthenticationForm()
    return render(request=request, template_name="App2/login.html", context={"login_form": form})


# Logout View

def logout_request(request):
    logout(request)
    messages.success(request, ("Logout successful."))
    return HttpResponseRedirect('/')
    # return render(request=request, template_name='App2/homepage.html')


# Homepage View

def homepage(request):
    return render(request=request, template_name='App2/homepage.html')


# ClubHomepage View

def clubhomepage(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    if request.user.is_authenticated:
        month = month.capitalize()
        monthnum = list(calendar.month_name).index(month)
        monthnum = int(monthnum)

        cal = HTMLCalendar().formatmonth(year, monthnum)

        now = datetime.now()
        cyear = now.year

        Identity = request.user.id
        org = request.user.student.club

        events = Event.objects.filter(attendees=Identity,
                                      event_club=org,
                                      event_date__year=year,
                                      event_date__month=monthnum).order_by('event_date')

        return render(request, 'App2/clubhomepage.html',
                      {"events": events,
                       "year": year,
                       "month": month,
                       "monthnum": monthnum,
                       "cal": cal,
                       "cyear": cyear, })


    else:
        messages.error(request, ("You are not logged in."))
        return HttpResponseRedirect('/homepage')


# Events View

def events(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            p = Paginator(Event.objects.all().order_by('event_date'), 3)
            page = request.GET.get('page')
            event1 = p.get_page(page)
            pg = 'n' * event1.paginator.num_pages

            return render(request, 'App2/events.html', {'event1': event1, 'pg': pg})
        else:
            org = request.user.student.club
            p = Paginator(Event.objects.filter(event_club=org).order_by('event_date'), 3)
            page = request.GET.get('page')
            event1 = p.get_page(page)
            pg = 'n' * event1.paginator.num_pages

            return render(request, 'App2/events.html', {'event1': event1, 'pg': pg})
    else:
        messages.error(request, ("Please login to view events."))
        return HttpResponseRedirect('/homepage')


# Update Events View

def updevents(request, eventid):
    if request.user.is_authenticated:
        event = Event.objects.get(pk=eventid)
        if request.user == event.overseer or request.user.is_superuser:
            if request.user.is_superuser:
                form = EventFormA(request.POST or None, instance=event)
            else:
                form = EventFormS(request.POST or None, instance=event)

            if form.is_valid():
                form.save()
                messages.success(request, ("Event Updated."))
                return HttpResponseRedirect('/events')

        else:
            messages.error(request, ("Only the Admin or Event Creator can update the event."))
            return HttpResponseRedirect('/events')

    else:
        messages.error(request, ("Please login to update events."))
        return HttpResponseRedirect('/')

    return render(request, 'App2/updateevents.html',
                  {'event': event,
                   'form': form})


# Add Events View

def addevents(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            initial_data = {
                'name': 'Training'
            }
            if request.method == 'POST':
                if request.user.is_superuser:
                    form = EventFormA(request.POST)
                else:
                    form = EventFormS(request.POST)

                if form.is_valid():
                    form.save()
                    messages.success(request, ("Event Added."))
                    return HttpResponseRedirect('/events')
            if request.user.is_superuser:
                form = EventFormA()
            else:
                form = EventFormS(initial=initial_data)
        else:
            messages.error(request, ("Only Admins and Student Representatives can add Events."))
            return HttpResponseRedirect('/')
    else:
        messages.error(request, ("Please login to add events."))
        return HttpResponseRedirect('/')
    return render(request=request, template_name='App2/addevent.html', context={'form': form, })


# Event Deletion View

def delevents(request, eventid):
    if request.user.is_authenticated:
        event = Event.objects.get(pk=eventid)
        if request.user == event.overseer or request.user.is_superuser:
            event.delete()
            messages.success(request, ("Event Deleted."))
            return HttpResponseRedirect('/events')
        else:
            messages.error(request, ("Event deletion failed. Only Event Overseer or Admin can delete events."))
            return HttpResponseRedirect('/events')
    else:
        messages.error(request, ("Please login to delete events."))
        return HttpResponseRedirect('/')


# Venues View

def venues(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            p = Paginator(Venue.objects.all().order_by('name'), 5)
            page = request.GET.get('page')
            venue1 = p.get_page(page)
            pg = 'n' * venue1.paginator.num_pages

            return render(request, 'App2/venues.html', {'venue1': venue1, 'pg': pg})
        else:
            messages.error(request, "Only Admin can view venues")
            return HttpResponseRedirect('/')

    else:
        messages.error(request, "Please login to view venues.")
        return HttpResponseRedirect('/')


# Update Venues View

def updvenues(request, venueid):
    if request.user.is_authenticated:

        if request.user.is_superuser:
            venue = Venue.objects.get(pk=venueid)
            form = VenueForm(request.POST or None, instance=venue)

            if form.is_valid():
                form.save()
                messages.success(request, ("Venue Updated."))
                return HttpResponseRedirect('/venues')

            return render(request, 'App2/updatevenues.html',
                          {'venue': venue,
                           'form': form})
        else:
            messages.error(request, ("Only Admin can view venues"))
            return HttpResponseRedirect('/')

    else:
        messages.error(request, ("Please login to delete events."))
        return HttpResponseRedirect('/')


# Delete Venues View

def delvenues(request, venueid):
    if request.user.is_authenticated:
        venue = Venue.objects.get(pk=venueid)
        if request.user.is_superuser:
            venue.delete()
            messages.success(request, ("Venue Deleted."))
            return HttpResponseRedirect('/venues')
        else:
            messages.error(request, ("Venue deletion failed. Only Admin can delete venues."))
            return HttpResponseRedirect('/venues')
    else:
        messages.error(request, ("Please login to delete venues."))
        return HttpResponseRedirect('/')


# Add Venues View

def addvenues(request):
    if request.user.is_authenticated:

        if request.user.is_superuser:

            if request.method == 'POST':
                form = VenueForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, ("Event Venue Added."))
                    return HttpResponseRedirect('/venues')
            form = VenueForm()
            return render(request=request, template_name='App2/addvenue.html', context={'form': form, })

        else:
            messages.error(request, "Only Admin can view venues")
            return HttpResponseRedirect('/')

    else:
        messages.error(request, "Please login to delete events.")
        return HttpResponseRedirect('/')


# Report View

def reports(request):
    if request.user.is_authenticated:
        if request.user.is_staff or request.user.is_superuser:
            p = Paginator(Report.objects.all().order_by('report_date'), 3)
            page = request.GET.get('page')
            report1 = p.get_page(page)
            pg = 'n' * report1.paginator.num_pages

            return render(request, 'App2/reports.html', {'report1': report1, 'pg': pg, })
        else:
            messages.error(request, "Only Student Representatives and Admins can view Reports.")
            return HttpResponseRedirect('/')
    else:
        messages.error(request, "Please login to view Reports.")
        return HttpResponseRedirect('/')


# Add Report View

def addreport(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            if request.method == 'POST':
                form = ReportForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, ("Report Added."))
                    return HttpResponseRedirect('/reports')
            form = ReportForm()
            return render(request=request, template_name='App2/addreport.html', context={'form': form, })
        else:
            messages.error(request, "Only Student Representatives and Admins can view Reports.")
            return HttpResponseRedirect('/')
    else:
        messages.error(request, "Please login to view Reports.")
        return HttpResponseRedirect('/')

# Update Report View

def updreport(request, reportid):
    report = Report.objects.get(pk=reportid)
    if request.user == report.report_author or request.user.is_superuser:
        form = ReportForm(request.POST or None, instance=report)

        if form.is_valid():
            form.save()
            messages.success(request, ("Report updated."))
            return HttpResponseRedirect('/reports')

    else:
        messages.error(request, ("Only the Admin or the Report Author can update the report."))
        return HttpResponseRedirect('/reports')

    return render(request, 'App2/updatereport.html',
                  {'report': report,
                   'form': form})


# Delete Report View

def delreport(request, reportid):
    report = Report.objects.get(pk=reportid)
    if request.user == report.report_author or request.user.is_superuser:
        report.delete()
        messages.success(request, ("Report Deleted."))
        return HttpResponseRedirect('/reports')
    else:
        messages.error(request, ("Only the Admin or the Report Author can delete the report."))
        return HttpResponseRedirect('/reports')


# Event Approval View

def eventapproval(request):
    event2 = Event.objects.all()

    events_all = Event.objects.all()
    events_all_ids = []

    for i in range(0, len(events_all), 1):
        events_all_ids.append(str(events_all[i].id))

    if request.user.is_superuser:
        if request.method == "POST":
            id_list = request.POST.getlist('boxes')

            # update database

            for x in id_list:
                Event.objects.filter(pk=int(x)).update(approved=True)

            id_set_false = set(events_all_ids) - set(id_list)
            id_list_false = list(id_set_false)

            for y in id_list_false:
                Event.objects.filter(pk=int(y)).update(approved=False)

            messages.success(request, ("Event Approval Updated."))
            return HttpResponseRedirect('/eventapproval')
        else:
            return render(request=request, template_name='App2/eventapproval.html', context={"event2": event2})


    else:
        messages.error(request, ("You need to be an Admin to acces this page"))
        return HttpResponseRedirect('/events')


# All Users View

def users(request):
    if request.user.is_authenticated:

        if request.user.is_superuser:

            p = Paginator(User.objects.all().order_by('username'), 5)
            page = request.GET.get('page')
            user1 = p.get_page(page)
            pg = 'n' * user1.paginator.num_pages

            return render(request, 'App2/users.html', {'user1': user1, 'pg': pg,})

        else:
            messages.error(request, "Only Admin can view users")
            return HttpResponseRedirect('/')

    else:
        messages.error(request, "Please login to view users.")
        return HttpResponseRedirect('/')


# Print PDF View

def printreport(request, reportid):
    reports = get_object_or_404(Report, pk=reportid)

    if request.user == reports.report_author or request.user.is_superuser:

        template_path = 'App2/reportpdf.html'
        context = {'report': reports}

        # Create a Django response object, and specify content_type as pdf
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Report.pdf"'

        # find the template and render it.
        template = get_template(template_path)
        html = template.render(context)

        # create a pdf
        pisa_status = pisa.CreatePDF(html, dest=response, )

        # if error then show some funny view
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response

    else:
        messages.error(request, ("Only the Admin or the Report Author can print the report."))
        return HttpResponseRedirect('/reports')


# Generate CSV File

def printcsv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students.csv"'

    writer = csv.writer(response)

    # Calling Models

    users = User.objects.all()
    students = Student.objects.all()

    # Column Details

    writer.writerow(['Username', 'First Name', 'Last Name', 'Email', 'Club', 'Field', 'Year'])

    for user, student in zip(users, students):
        writer.writerow(
            [user.username, user.first_name, user.last_name, user.email, student.club, student.field, student.year])

    return response
