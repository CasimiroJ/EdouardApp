from django.shortcuts import render
from App.models import Team


def score_board(request):
    all_teams = Team.objects.all()
    teams = []
    for team in all_teams:
        teams.append([team.Name, team.Size, team.Goal, team.Realized, team.TeamId])
    return render(request, 'scoreBoard.html', locals())
