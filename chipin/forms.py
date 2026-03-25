from django import forms
from .models import Group, Comment, Event
import datetime

import datetime

class EventCreationForm(forms.ModelForm): #create the new form to validate the input for event creation
    class Meta:
        model = Event
        fields = ['name', 'date', 'total_spend']

    def clean_total_spend(self):
        value = self.cleaned_data.get('total_spend')
        if value is None or value <= 0:
            raise forms.ValidationError("Total spend must be a positive number.")
        return value

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if date and date < datetime.date.today():
            raise forms.ValidationError("Event date cannot be in the past.")
        return date

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter your comment...'})
        }
    # Clean the content to sanitise input
    def clean_content(self):
        content = self.cleaned_data.get('content')
        for i, char in enumerate(content):
            if char == '<' and '>' in content[i:]:
                raise forms.ValidationError("Invalid content.")
        return content

class GroupCreationForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        group = super().save(commit=False)
        group.admin = self.user
        if commit:
            group.save()
            group.members.add(self.user)
        return group