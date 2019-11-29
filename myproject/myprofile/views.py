from django.shortcuts import render, get_object_or_404
from .models import Profile


# Create your views here.
def list(request):
    profiles = Profile.objects
    return render(request, 'myprofile/list.html',{'profiles':profiles})

def detail(request, profile_id):
    profile = get_object_or_404(Profile, pk = profile_id)
    return render(request, 'myprofile/detail.html', {'profile':profile})