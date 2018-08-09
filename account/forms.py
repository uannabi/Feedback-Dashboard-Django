from django import forms
from django.contrib.auth.forms import UsernameField, AuthenticationForm
from django.contrib.auth.models import User
from werkzeug.routing import ValidationError


class RegisterUserForm(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'woocommerce-Input woocommerce-Input--text input-text','placeholder':' '}))
    Re_Password = forms.CharField(label="Repeat password", widget=forms.PasswordInput(attrs={'class': 'woocommerce-Input woocommerce-Input--text input-text','placeholder':''}))


    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'woocommerce-Input woocommerce-Input--text input-text', 'placeholder':'Username','autofocus': True}),
            'email': forms.EmailInput(attrs={'class': 'woocommerce-Input woocommerce-Input--text input-text','placeholder':'Email' ,'required': True})
    }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password2'] != cd['password']:
            raise ValidationError("Password don't match")

        return cd['password2']
class LoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={'class': 'woocommerce-Input woocommerce-Input--text input-text', 'autofocus': True, 'placeholder': ' '})
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'woocommerce-Input woocommerce-Input--text input-text', 'placeholder': ' '}))
