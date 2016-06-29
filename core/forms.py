from django import forms
from .models import SignUp

class ContactForm(forms.Form):
    full_name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField()

# SignIn form
class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name', 'email', 'newsletter']

        def clean_email(self):
            email = self.cleaned_data.get('email')
            email_base, provider = email.split('@')
            domain, extension = provider.split('.')
            if not extension == 'com':
                raise forms.ValidationError('Please use .com in your mail address!')
            return email

        def clean_full_name(self):
            full_name = self.cleaned_date.get('full_name')
            return full_name

        def clean_newsletter(self):
            newsletter = self.cleaned_data.get('newsletter')
            return newsletter
