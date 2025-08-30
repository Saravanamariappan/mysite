from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        role = request.POST.get("role")
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            # Redirect based on role
            if role == "student":
                return redirect("student_dashboard")
            elif role == "mentor":
                return redirect("mentor_dashboard")
            elif role == "guide":
                return redirect("guide_dashboard")
            elif role == "coordinator":
                return redirect("coordinator_dashboard")
            elif role == "hod":
                return redirect("hod_dashboard")
        else:
            messages.error(request, "Invalid credentials")

    return render(request, "accounts/login.html")
