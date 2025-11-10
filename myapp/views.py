from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Getdata

def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message_text = request.POST.get("message")

        if not name or not email or not message_text:
            messages.error(request, "All fields are required.")
            return redirect("index")
            
        Getdata.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message_text
        )

        messages.success(request, "Thank you! Your message has been sent.")
        return redirect("index")

    return render(request, "index.html")
