from django.shortcuts import render, redirect
from .models import getdata
# Create your views here.

def index(request):
    if request.method=="POSt":
        name = request>POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        if not name or email or message:
            message.error(request, "All fields are reqired")
            return redirect("index")

            getdata.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            message.success(request, "Thank you! Your message your sent.")
            return redirect("index")
    return render(request, 'index.html')