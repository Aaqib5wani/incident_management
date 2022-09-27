"""incident_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Api import views as api
from django.contrib.auth import logout

urlpatterns = [
    path("", api.login_request, name="login"),
    path("register/", api.register_request, name="login_register"),
    path('admin/', admin.site.urls),
    path("create/", api.Create_newincident, name="create_incident"),
    path ("update/<str:incident_number>/", api.Update_incident, name="Update_incident"),
    path("all/", api.Incident_list, name="Incident_list"),
    path("all_incident/", api.All_incident, name="All_incident"),
    path ("incident/<str:incident_number>/", api.Incident_list_search, name="Incident_list_search"),
    path("logout/",logout,name="logout"),
]
