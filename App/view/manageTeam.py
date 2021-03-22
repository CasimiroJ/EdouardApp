from App.form import ManageTeamForm
from django.shortcuts import render, redirect
from App.view.ScoreBoard import score_board
from App.models import Team


def manage_team(request, team_id=None):
    form = ManageTeamForm(request.POST or None)
    if team_id is None:
        redirect('/scoreBoard')

    team = Team.objects.get(TeamId=team_id)

    if form.is_valid():
        team = Team.objects.get(TeamId=team_id)
        team.Realized += 1
        team.save()

    name = team.Name
    size = team.Size
    goal = team.Goal
    realized = team.Realized

    return render(request, 'manageTeam.html', locals())
