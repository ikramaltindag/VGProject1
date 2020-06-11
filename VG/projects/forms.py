from django import forms
from projects.models import Project,Client

class ProjectForm(forms.ModelForm):
    class Meta():
        model = Project
        fields = ('creator','title','type','client','definition','duration_in_days','start_date','deadline','status','approval_status')

        #
        # widget = {
        #     'project_title':forms.TextInput(attrs={'class':'textinputclass'}),
        #     'definition':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        # }

class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ('creator','name','contact_person','address','phone')

        #
        # widgets = {
        #     'client_name':forms.TextInput(attrs={'class': 'textinputclass'}),
        #     'client_contact_person':forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        # }
