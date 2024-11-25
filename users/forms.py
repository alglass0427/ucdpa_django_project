from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile , Skill , Message
from django.core.exceptions import ValidationError
from django import forms

ALLOWED_IMAGE_TYPES = ['image/jpeg', 'image/png', 'image/gif']
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        ###django documenttion -   password1 then password2 is password confirm
        fields = ['first_name','username','email','password1','password2']
        labels = {
            'first_name':'Name'
        }

    def __init__(self,*args,**kwargs):
        super(CustomUserCreationForm,self).__init__(*args,**kwargs)

        # adds css Classes to the ClassForm

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


class ProfileForm(ModelForm,forms.Form):
    # file = forms.FileField()
    class Meta:
        model  = Profile
        # fields = '__all__'
        fields = ['name','email','username','location','bio','short_intro','profile_image',
                  'social_github','social_x','social_linkdin','social_youtube','social_website'
                  ]
   # adds css Classes to the ClassForm

    def __init__(self,*args,**kwargs):
        super(ProfileForm,self).__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


########################ADDED FOR FILE UPLOADS
    # def clean_file(self):
    #     uploaded_file = self.cleaned_data['file']

    #     if uploaded_file.content_type not in ALLOWED_IMAGE_TYPES:
    #         raise ValidationError('Invalid file type. Only image files are allowed.')

    #     if uploaded_file.size > MAX_FILE_SIZE:
    #         raise ValidationError(f'File size exceeds {MAX_FILE_SIZE // (1024 * 1024)} MB.')

    #     return uploaded_file



            
class SkillForm(ModelForm):
    class Meta:
        model  = Skill
        fields = '__all__'
        exclude = ['owner']
    
    def __init__(self,*args,**kwargs):
        super(SkillForm,self).__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email' , 'subject', 'body']

    def __init__(self,*args,**kwargs):
        super(MessageForm,self).__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})