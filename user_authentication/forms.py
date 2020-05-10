from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Extended_User, Selected_cities

class Modified_UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class DatePicker(forms.DateInput):
    # this class is for producing the datepicker widget
    input_type = 'date'

class Extended_UserCreationForm(forms.ModelForm):
    class Meta:
        model = Extended_User
        fields = ['bdate','address']
        widgets = {'bdate': DatePicker()}

class Select_cities(forms.ModelForm):
    class Meta:
        model = Selected_cities
        fields = ['cities', 'hometown']


