from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import*

class CostomerRegistrationForm(UserCreationForm):
    # password1= forms.CharField(Label='Password', widget=forms.
    # PasswordInput(attrs={'class':'form-control'}))
    # password2=forms.CharField(Label='Confirm Password',widget=forms.
    # PasswordInput(attrs={'class':'form-control'}))
    # email=forms.CharField(required=True,widget=forms.
    # EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))

    email = forms.CharField( required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))


    class Meta:
        model = User
        fields=['username','email','password1','password2']
        labels = {'email':'Email'}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'})}



class costomerform(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={"class": "form-control"}))
    email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={"class": "form-control"}))
    class Meta:
        model=Costomer
        fields=['name','locality','city','state','zipcode']
        widgets = {'name':forms.TextInput(attrs={'class':'form-control'}),

                            'locality':forms.TextInput(attrs={'class':'form-control'}),
                            'city':forms.TextInput(attrs={'class':'form-control'}),

                            'state':forms.TextInput(attrs={'class':'form-control'}),
                            'zipcode':forms.NumberInput(attrs={'class':'form-control'}),
        }
