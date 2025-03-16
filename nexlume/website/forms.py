from django import forms
from .models import Contact
from .models import EmailSubmission

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'organization', 'email', 'contact', 'services', 'investment', 'source', 'message']
        widgets = {
            'services': forms.CheckboxSelectMultiple(),  # For checkbox fields
        }

class EmailSubmissionForm(forms.ModelForm):
    class Meta:
        model = EmailSubmission
        fields = ['email']