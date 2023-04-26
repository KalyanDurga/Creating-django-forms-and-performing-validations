from django import forms
from django.http import HttpResponse

def check_for_name(name):
    if name[0].lower()=='a':
        raise forms.ValidationError('name should not start with number')
def check_for_len(name):
    if len(name)<5:
        raise forms.ValidationError('name should not be less than 5 char')

class Studentform(forms.Form):
    name=forms.CharField(max_length=50,validators=[check_for_name,check_for_len])
    age=forms.IntegerField()
    email=forms.EmailField()
    Re_Enter_Email=forms.EmailField()
    botcatcher=forms.CharField(max_length=50,widget=forms.HiddenInput,required=False)
    password=forms.CharField(max_length=50,widget=forms.PasswordInput)
    Re_Enter_Password=forms.CharField(max_length=50,widget=forms.PasswordInput)

    def clean(self):
        e=self.cleaned_data['email']
        r=self.cleaned_data['Re_Enter_Email']
        p=self.cleaned_data.get('password')
        pr=self.cleaned_data.get('Re_Enter_Password')
        if e!=r or p!=pr:
            raise forms.ValidationError('email and re_enter_email not matched')
        






