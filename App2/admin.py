from django.contrib import admin
from .models import Venue
from .models import Event
from .models import Student
from .models import Report
from .models import Club
from .models import Field
from .models import Year
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User



# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class StudentInline(admin.StackedInline):
    model = Student
    can_delete = False
    verbose_name_plural = 'students'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (StudentInline,)


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Venue)
admin.site.register(Event)
admin.site.register(Report)
admin.site.register(Club)
admin.site.register(Field)
admin.site.register(Year)