from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from .models import checkin
from django.forms import ModelForm

class edit_form(forms.Form):
    id = forms.CharField(max_length=10)
    review = forms.CharField(max_length=1000)

    class Meta:
        model = checkin
        fields = ['review', ]

class delete_form(forms.Form):
    id = forms.CharField(max_length=10)

    class Meta:
        model = checkin
        fields = []

class checkin_form(ModelForm):
    address = forms.CharField(max_length=100)
    longitude = forms.CharField(max_length=50)
    latitude = forms.CharField(max_length=50)
    place_name = forms.CharField(max_length=50)
    review = forms.CharField(max_length=1000)
    class Meta:
        model = checkin
        fields = ['address', 'longitude', 'latitude', 'place_name', 'review', ]




class EditProfileForm(UserChangeForm):
    email = forms.EmailField(label="Enter Email", widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=20, label="Enter First Name", widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=20, label="Enter Last Name", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="", widget=forms.TextInput(attrs={'type': 'hidden'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', ]


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(max_length=20, label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=20, label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter Password'
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'


        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'




