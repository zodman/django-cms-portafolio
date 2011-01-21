from django import forms
#import settings
from stopspam.forms import HoneyPotForm, RecaptchaForm, AkismetForm
  
class HoneyPotContactForm(HoneyPotForm):
    email 	= forms.EmailField()
    subject	= forms.CharField(required=False)
    content	= forms.CharField(widget=forms.Textarea())


class AkismetContactForm(AkismetForm):
    akismet_fields = {
        'comment_author_email': 'email',
        'comment_content': 'content'
    }
    email     = forms.EmailField()
    subject    = forms.CharField(required=False)
    content    = forms.CharField(widget=forms.Textarea())
    
    akismet_api_key = None
    

class RecaptchaContactForm(RecaptchaForm):
    email     = forms.EmailField()
    subject    = forms.CharField(required=False)
    content    = forms.CharField(widget=forms.Textarea())

    recaptcha_public_key = None
    recaptcha_private_key = None
    recaptcha_theme = None