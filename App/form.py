from django import forms


class CreateTeamsForm(forms.Form):
    TeamName = forms.CharField(max_length=100, empty_value='None', required=False)
    TeamSize = forms.IntegerField(required=False, initial=0)
    TeamGoal = forms.IntegerField(required=False, initial=0)

    TeamName2 = forms.CharField(max_length=100, empty_value='None', required=False)
    TeamSize2 = forms.IntegerField(required=False, initial=0)
    TeamGoal2 = forms.IntegerField(required=False, initial=0)

    TeamName3 = forms.CharField(max_length=100, empty_value='None', required=False)
    TeamSize3 = forms.IntegerField(required=False, initial=0)
    TeamGoal3 = forms.IntegerField(required=False, initial=0)

    TeamName4 = forms.CharField(max_length=100, empty_value='None', required=False)
    TeamSize4 = forms.IntegerField(required=False, initial=0)
    TeamGoal4 = forms.IntegerField(required=False, initial=0)

    TeamName5 = forms.CharField(max_length=100, empty_value='None', required=False)
    TeamSize5 = forms.IntegerField(required=False, initial=0)
    TeamGoal5 = forms.IntegerField(required=False, initial=0)

    TeamName6 = forms.CharField(max_length=100, empty_value='None', required=False)
    TeamSize6 = forms.IntegerField(required=False, initial=0)
    TeamGoal6 = forms.IntegerField(required=False, initial=0)

    TeamName7 = forms.CharField(max_length=100, empty_value='None', required=False)
    TeamSize7 = forms.IntegerField(required=False, initial=0)
    TeamGoal7 = forms.IntegerField(required=False, initial=0)

    TeamName8 = forms.CharField(max_length=100, empty_value='None', required=False)
    TeamSize8 = forms.IntegerField(required=False, initial=0)
    TeamGoal8 = forms.IntegerField(required=False, initial=0)


class ManageTeamForm(forms.Form):
    nothing = forms.CharField(required=False)
