from django import forms
from .models import Panchayath,Employees

class PanchayathForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Panchayath
        fields = ('email', 'password','name','country','state','district','pincode')
    def clean(self):
        cleaned_data = super(PanchayathForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )
class EmployeesForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    confirm_password  = forms.CharField(widget = forms.PasswordInput())
    class Meta:
        model =Employees
        fields = ('email','name','jobtitle','address','phonenumber','password')
    def clean(self):
        cleaned_data = super(EmployeesForm,self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password doesnot match"
            )