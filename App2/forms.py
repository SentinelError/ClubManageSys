from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.forms import ModelForm
from .models import Venue, Event, Student, Report


# Create your forms here.

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100, )
    last_name = forms.CharField(max_length=100, )

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class NewEditForm(UserChangeForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    first_name = forms.CharField(max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    username = forms.CharField(max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UserName'}))

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password",)


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ("club", "field", "year")
        labels = {
            'club': "Select Club",
            'field': "Select Field",
            'year': "Select year",
        }
        widgets = {
            'club': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Club'}),
            'field': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Field'}),
            'year': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Year'}),
        }


# Admin EventForm
class EventFormA(ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'overseer', 'event_club', 'event_date', 'venue', 'attendees', 'description')
        labels = {
            'name': 'Enter Event',
            'overseer': 'Enter the Event Overseer',
            'event_club': 'Select the club for the event.',
            'event_date': 'Enter Date and Time in Format [YYYY-MM-DD HH:MM:SS]',
            'venue': 'Select Event Venue',
            'attendees': 'Select Members attending',
            'description': 'Enter Event Description',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Name'}),
            'overseer': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Event Overseer'}),
            'event_club': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Event Club'}),
            'event_date': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Event Date'}),
            'venue': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Venue'}),
            'attendees': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Attendees'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }


# Student Rep EventForm
class EventFormS(ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'overseer', 'event_club', 'event_date', 'venue', 'attendees', 'description')
        labels = {
            'name': 'Enter Event',
            'overseer': 'Enter the Event Overseer',
            'event_club': 'Select the club for the event.',
            'event_date': 'Enter Date and Time in Format [YYYY-MM-DD HH:MM:SS]',
            'venue': 'Select Event Venue',
            'attendees': 'Select Members attending',
            'description': 'Enter Event Description',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Event Name', 'readonly': 'readonly'}),
            'overseer': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Event Overseer'}),
            'event_club': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Event Club'}),
            'event_date': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Event Date'}),
            'venue': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Venue'}),
            'attendees': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Attendees'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }


class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ('name', 'address', 'phone',)
        labels = {
            'name': 'Enter Venue',
            'address': 'Enter Venue Address',
            'phone': 'Enter Venue contact number',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Venue Name'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Venue Address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Venue Address'}),
        }


class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = ('title', 'event', 'report_date', 'report_author', 'body',)
        labels = {
            'title': 'Enter the Report Title',
            'event': 'Select the Event for the Report',
            'report_date': 'Enter the Report date on format [YYYY-MM-DD]',
            'report_author': 'Enter the representative for the Report',
            'body': 'Enter Report',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Report Title'}),
            'event': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Report on Event'}),
            'report_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Report Date'}),
            'report_author': forms.Select(
                attrs={'class': 'form-select', 'placeholder': 'Representative writing Report'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Report'})
        }
