from App.form import CreateTeamsForm
from django.shortcuts import render, redirect
from App.view.ScoreBoard import score_board
from App.models import Team


def create_teams(request):
    form = CreateTeamsForm(request.POST or None)
    if form.is_valid():
        Team.objects.all().delete()
        team1 = Team(TeamId=1, Name=form.cleaned_data['TeamName'], Size=form.cleaned_data['TeamSize'], Goal=form.cleaned_data['TeamGoal'], Realized=0)
        team1.save()
        team2 = Team(TeamId=2, Name=form.cleaned_data['TeamName2'], Size=form.cleaned_data['TeamSize2'], Goal=form.cleaned_data['TeamGoal2'], Realized=0)
        team2.save()
        team3 = Team(TeamId=3, Name=form.cleaned_data['TeamName3'], Size=form.cleaned_data['TeamSize3'], Goal=form.cleaned_data['TeamGoal3'], Realized=0)
        team3.save()
        team4 = Team(TeamId=4, Name=form.cleaned_data['TeamName4'], Size=form.cleaned_data['TeamSize4'], Goal=form.cleaned_data['TeamGoal4'], Realized=0)
        team4.save()
        team5 = Team(TeamId=5, Name=form.cleaned_data['TeamName5'], Size=form.cleaned_data['TeamSize5'], Goal=form.cleaned_data['TeamGoal5'], Realized=0)
        team5.save()
        team6 = Team(TeamId=6, Name=form.cleaned_data['TeamName6'], Size=form.cleaned_data['TeamSize6'], Goal=form.cleaned_data['TeamGoal6'], Realized=0)
        team6.save()
        team7 = Team(TeamId=7, Name=form.cleaned_data['TeamName7'], Size=form.cleaned_data['TeamSize7'], Goal=form.cleaned_data['TeamGoal7'], Realized=0)
        team7.save()
        team8 = Team(TeamId=8, Name=form.cleaned_data['TeamName8'], Size=form.cleaned_data['TeamSize8'], Goal=form.cleaned_data['TeamGoal8'], Realized=0)
        team8.save()
        return redirect('/scoreBoard')
    return render(request, 'createTeams.html', locals())
