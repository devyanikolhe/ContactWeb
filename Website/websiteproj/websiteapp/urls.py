from django.urls import path
from .import views as v

urlpatterns = [
   path('',v.home),
   path('addcontact',v.addcontact),
   path('contactlist',v.conlist),
   path("delete/<int:id>",v.delete_contact),
   path("Edit/<int:id>",v.edit),
]
