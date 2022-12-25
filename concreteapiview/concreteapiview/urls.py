from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('stuapi/',views.StudentList.as_view()),
    # path('stuapi/',views.StudentCreate.as_view()),
    path('stuapi/',views.LCstudent.as_view()),
    path('stuapi/<int:pk>',views.RUDStudent.as_view()),




]
