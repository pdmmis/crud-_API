from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuapi/',views.StudentAPI.as_view()),
    path('stuapi/<int:pk>',views.StudentAPI.as_view())


]
