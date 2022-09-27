from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import NewUserForm,Create_incidentForm
from .models import Create_incident
from django.http import  JsonResponse
from .serializers import Create_incidentSerializer
import datetime



def new_incident_number():
    obj = int(Create_incident.objects.latest ('created').incident_number[3:8])
    new_number = obj + 1
    today = datetime.date.today ()
    year = today.strftime ("%Y")
    print(type(year))
    new_incident = "RMG" + str (new_number).zfill(5) + year
    return new_incident

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("login_request")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


def login_request(request):
    if request.user.is_authenticated:
        return render(request, "index.html", {'username': request.user})
    else:
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.info(request, f"You are now logged in as {username}.")
                    return render(request, "index.html", {'username': request.user})
                else:
                    messages.error(request, "Invalid username or password.")
            else:
                messages.error(request, "Invalid username or password.")
        form = AuthenticationForm()
        return render(request=request, template_name="login.html", context={"login_form": form})



def Create_newincident(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = Create_incidentForm(request.POST)
            if form.is_valid ():
                description = form.cleaned_data.get ('description')
                priority = form.cleaned_data.get ('priority')
                incident_status = form.cleaned_data.get ('incident_status')
                name = request.user.username
                incident_number=new_incident_number()
                b2 = Create_incident(description=description,priority=priority,incident_status=incident_status,name=name,incident_number=incident_number)
                b2.save()
            return redirect ("All_incident")
        else:
            form = Create_incidentForm()
        return render(request, "Create_incident.html", {'username': request.user,"Create_incident": form})

def Incident_list(request):
    if request.method == 'GET':
        List = Create_incident.objects.filter(name=request.user.username)
        serializer = Create_incidentSerializer(List, many=True)
        return JsonResponse (serializer.data, safe=False)


def Incident_list_search(request,incident_number):
    if request.method == 'GET':
        List = Create_incident.objects.filter (name=request.user.username,incident_number=incident_number)
        serializer = Create_incidentSerializer(List, many=True)
        return JsonResponse (serializer.data, safe=False)

def Update_incident(request,incident_number):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = Create_incidentForm(request.POST)
            if form.is_valid ():
                description = form.cleaned_data.get ('description')
                priority = form.cleaned_data.get ('priority')
                incident_status = form.cleaned_data.get ('incident_status')
                b2=Create_incident.objects.get(name=request.user.username, incident_number=incident_number)
                b2.description=description
                b2.priority=priority
                b2.incident_status=incident_status
                b2.save()
                b2.incident_number
            return redirect ("All_incident")

        else:
            List = Create_incident.objects.get(name=request.user.username, incident_number=incident_number)
            form = Create_incidentForm(instance=List)
            List.incident_number
            if List.incident_status == 'Closed':
                form.fields ['description'].disabled = True
                form.fields ['priority'].disabled = True
                form.fields ['incident_status'].disabled = True
        return render(request, "Update_incident.html", {'username': request.user,"Update_incident": form,'incident_number':List.incident_number})

def All_incident(request):
    if request.user.is_authenticated:
        List = Create_incident.objects.filter (name=request.user.username).order_by('-created')
        serializer = Create_incidentSerializer (List, many=True)
        return render(request, "incident_details.html", {'username': request.user,"list": serializer.data})