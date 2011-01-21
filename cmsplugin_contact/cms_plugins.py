from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.template.loader import render_to_string
from models import Contact
from forms import AkismetContactForm, RecaptchaContactForm, HoneyPotContactForm
from django.core.mail import EmailMessage
from admin import ContactAdminForm

class ContactPlugin(CMSPluginBase):
    model = Contact
    name = _("Contact Form")
    render_template = "cmsplugin_contact/contact.html"
    form = ContactAdminForm
    
    fieldsets = (
        (None, {
            'fields': ('site_email', 'email_label', 'subject_label', 'content_label', 'thanks', 'submit'),
        }),
        (_('Spam Protection'), {
            'fields': ('spam_protection_method', 'akismet_api_key', 'recaptcha_public_key', 'recaptcha_private_key', 'recaptcha_theme')
        })
    )
    
    change_form_template = "cmsplugin_contact/admin/plugin_change_form.html"

    def create_form(self, instance, request):
        if instance.get_spam_protection_method_display() == 'Akismet':
            AkismetContactForm.aksimet_api_key = instance.akismet_api_key
            FormClass = AkismetContactForm
        elif instance.get_spam_protection_method_display() == 'ReCAPTCHA':
            RecaptchaContactForm.recaptcha_public_key = getattr(settings, "RECAPTCHA_PUBLIC_KEY", \
                                                        instance.recaptcha_public_key)
            RecaptchaContactForm.recaptcha_private_key = getattr(settings, "RECAPTCHA_PRIVATE_KEY", \
                                                         instance.recaptcha_private_key)
            RecaptchaContactForm.recaptcha_theme = instance.recaptcha_theme
            FormClass = RecaptchaContactForm
        else:
            FormClass = HoneyPotContactForm
            
        if request.method == "POST":
            return FormClass(request, data=request.POST)
        else:
            return FormClass(request)


    def send(self, form, site_email):
        subject = form.cleaned_data['subject']
        if not subject:
            subject = _('No subject')
        email_message = EmailMessage(
            subject,
            render_to_string("cmsplugin_contact/email.txt", {
                'data': form.cleaned_data,
            }),
            form.cleaned_data['email'],
            [site_email],
            headers = {
                'Reply-To': form.cleaned_data['email']
            },)
        email_message.send(fail_silently=True)
    
    def render(self, context, instance, placeholder):
    	request = context['request']

        form = self.create_form(instance, request)
    
    	if request.method == "POST" and form.is_valid():
			self.send(form, instance.site_email)
			context.update( {
				'contact': instance,
			})
    	else:
            context.update({
                'contact': instance,
                'form': form,
            })
            
        return context

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
			'spam_protection_method': obj.spam_protection_method if obj else 0,
            'recaptcha_settings': hasattr(settings, "RECAPTCHA_PUBLIC_KEY"),
            'akismet_settings': hasattr(settings, "AKISMET_API_KEY"),
        })
        
        return super(ContactPlugin, self).render_change_form(request, context, add, change, form_url, obj)
    	
    
plugin_pool.register_plugin(ContactPlugin)
