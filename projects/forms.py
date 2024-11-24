from django.forms import ModelForm
from .models import Project,Review
from django import forms

# creats a Form based off the model Class ORM
class ProjectForm(ModelForm):
    class Meta:
        ####  AT MINIMUM Meta rquires model and fields
        # This creats a form based on the Model it refresents
        # __all__ gives all fields OR els give Arra of fields you want to use
        model = Project
        # fields = '__all__'
        fields = ['title','featured_image','description','demo_link','source_link']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
    
    def __init__(self,*args,**kwargs):
        super(ProjectForm,self).__init__(*args,**kwargs)

        # self.fields['title'].widget.attrs.update({'class':'input'})
        # self.fields['description'].widget.attrs.update({'class':'input'})

        for name,field in self.fields.items():
            if field != 'tags':
                field.widget.attrs.update({'class':'input'})


class ReviewForm(ModelForm):

    class Meta:
        model =  Review
        fields = ['value','body']

    labels = {
        'value' : 'Place your Vote',
        'body' : 'Add a comment with your vote'
    }

    def __init__(self,*args,**kwargs):
        super(ReviewForm,self).__init__(*args,**kwargs)

        # self.fields['title'].widget.attrs.update({'class':'input'})
        # self.fields['description'].widget.attrs.update({'class':'input'})

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})