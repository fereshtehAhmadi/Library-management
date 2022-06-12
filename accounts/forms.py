from django import forms
from django.urls import reverse_lazy
from phonenumber_field.formfields import PhoneNumberField

from accounts.models import CustomUserModel

from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.models import User



class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('home')
    
    

class UserRegisterationForm(forms.ModelForm):
    password = forms.CharField( label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label='User name', widget=forms.TextInput(attrs={'class': 'form-control'}))    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        
        widgets = {
        'first_name' : forms.TextInput(attrs={'class': 'form-control'}),
        'last_name' : forms.TextInput(attrs={'class': 'form-control' ,}),
        'email' : forms.TextInput(attrs={'class': 'form-control'}),
       }
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
    

class CustomUserForm(forms.ModelForm):
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    national_code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    gender = forms.CharField(widget=forms.Select(attrs={'class': 'form-control'}))
    birthday = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label='Confirm password', widget=forms.Textarea())
    
    class Meta:
        model = CustomUserModel
        fields = ('phone', 'address', 'national_code', 'gender', 'birthday')
        
    def clean_phone(self):
        phone = self.cleaned_data.get('phone', None)
        try:
            int(phone)
            l = list(phone)
            if l[0] != '0' and l[1] != '9':
                raise forms.ValidationError('Please enter a valid phone number!')
        except (ValueError):
            raise forms.ValidationError('Please enter a valid phone number!')
        return phone
    
    def clean_national_code(self):
        national_code = self.cleaned_data.get('national_code', None)
        try:
            int(national_code)
        except (ValueError):
            raise forms.ValidationError('Please enter a valid national_code!')
        return national_code
    
    
