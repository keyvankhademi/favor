from django import forms

from favor_exchange.models import ExchangeUser, Token

TYPE_CHOICES = (
    ('Cigarette Sharing', 'Cigarette Sharing',),
    ('Car Pulling', 'Car Pulling',),
    ('Meal Sharing', 'Meal Sharing',),
)


class FavorRequestForm(forms.Form):
    type = forms.ChoiceField(choices=TYPE_CHOICES)

    def __init__(self, *args, **kwargs):
        super(FavorRequestForm, self).__init__(*args, **kwargs)
        self.fields['user'] = forms.ChoiceField(
            choices=((user.user.username, user.user.username) for user in ExchangeUser.objects.all()))


class AddCreditForm(forms.Form):
    token = forms.CharField()

    def clean(self):
        super(AddCreditForm, self).clean()
        if not Token.objects.filter(token=self.cleaned_data['token'], used=False).exists():
            raise forms.ValidationError("Token is Invalid or Used before!")
