from django import forms
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    phone = forms.CharField(label='User Key', max_length=255)
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput(attrs={'class': 'input'}))

    def clean(self):
        phone = self.cleaned_data.get('phone')
        password = self.cleaned_data.get('password')
        user = authenticate(phone=phone, password=password)
        if user is None:
            raise forms.ValidationError(
                "아이디 혹은 비밀번호가 일치하지 않습니다."
            )
        return self.cleaned_data
