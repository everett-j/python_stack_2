from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		# "leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		"baseball": League.objects.filter(sport='Baseball'),
		"women": League.objects.filter(name__contains='women'),
		"hockey": League.objects.filter(sport__contains='hockey'),
		"not_football": League.objects.filter(sport='Football'),
		"atlantic_region": League.objects.filter(name__contains='atlantic'),
		"dallas": Team.objects.filter(location__contains='dallas'),
		"raptor": Team.objects.filter(team_name__contains='raptors'),
		"city": Team.objects.filter(location__contains='city'),
		"team_t": Team.objects.filter(team_name__startswith='T'),
		"alpha" : Team.objects.order_by('team_name'),
		"rev_alpha" : Team.objects.order_by('-team_name'),
		"cooper": Player.objects.filter(last_name__contains='cooper'),
		"joshua": Player.objects.filter(first_name__contains='joshua'),
		"combo": Player.objects.filter(first_name__contains='alexander') | Player.objects.filter(first_name__contains='wyatt'),

	


	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")