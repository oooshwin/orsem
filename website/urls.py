from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", index, name="index"),
    path("check_student", check_student, name="check_student"),
    path("edit_attendance", edit_attendance, name="edit_attendance")
    
]

htmx_urlpatterns = [
    
]

urlpatterns += htmx_urlpatterns

# This might be needed, depending on your Django version
app_name = "website"

