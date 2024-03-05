from typing import Any
from django import forms
from .models import User, UserProfile
from .validators import allow_only_images_validator


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model= User
        fields =['first_name','last_name','username','email','password']


    def clean(self):
        cleaned_data = super(UserForm,self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get('confirm_password') 

        if password!= confirm_password:
            raise forms.ValidationError(
                "Password does not match"
            )
    
class UserProfileForm(forms.ModelForm):
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Start typing...','required':'required'}))
    profile_picture = forms.FileField(widget=forms.FileInput(attrs ={'class': 'btn btn-info'}),validators =[allow_only_images_validator])
    cover_photo = forms.FileField(widget=forms.FileInput(attrs ={'class': 'btn btn-info'}),validators =[allow_only_images_validator])
     
    # Making latitude and longitude fiels read only. 
    # Method-1 -> By making only readonly attribute to the fields latitude and longitude 

    #latitude = forms.CharField(widget = forms.TextInput(attrs={'readonly': 'readonly'}))
    #longitude = forms.CharField(widget = forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'cover_photo','address','country','state','city','pin_code','latitude','longitude']
            
    # Method-2 -> By overriding the __ini__ method.
        # In industry this method is preffered as their are number of fields that need to handled and different actions are needed.

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field =='latitude' or field=='longitude':
                self. fields[field].widget.attrs['readonly'] = 'readonly'
        

