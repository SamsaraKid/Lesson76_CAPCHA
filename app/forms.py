from django import forms
from captcha.fields import CaptchaField
import captcha.conf.settings
# captcha.conf.settings.CAPTCHA_CHALLENGE_FUNCT = "captcha.helpers.math_challenge"
captcha.conf.settings.CAPTCHA_LENGTH = 16


class MyForm(forms.Form):
    name = forms.CharField()
    captcha = CaptchaField()
