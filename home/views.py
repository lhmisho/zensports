from django.shortcuts import render
from django.http import HttpRequest
from home.models import Intro, Works, Team
# Create your views here.

def index(request):
    intro_vid = Intro.objects.order_by('id')
    services = Works.objects.order_by('id')
    team_members = Team.objects.order_by('id')
    context = {'request': request, 'services':services, 'intro_vid':intro_vid, 'team_members':team_members}
    return render(request, 'index.html', context)