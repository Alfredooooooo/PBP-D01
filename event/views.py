from django.shortcuts import render

# Create your views here.
def event_manager(request):
    return render(request, "show-event-manager.html")

def event_user(request):
    return render(request, "show-event-user.html")
