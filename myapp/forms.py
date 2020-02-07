from django import  forms

class regform(forms.Form):
    usermob1=forms.IntegerField()
    Fname1=forms.CharField()
    Lname1=forms.CharField()
    pwd1=forms.CharField()
class loginform(forms.Form):
    usermob=forms.CharField()
    pwd=forms.CharField()
