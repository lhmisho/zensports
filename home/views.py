from django.shortcuts import render
from django.http import HttpRequest
from home.models import Video, Works, Team
# Create your views here.

def index(request):
    intro_vid = Video.objects.all()
    services = Works.objects.order_by('id')
    team_members = Team.objects.order_by('id')
    context = {'request': request, 'services':services, 'intro_vid':intro_vid, 'team_members':team_members}
    return render(request, 'index.html', context)