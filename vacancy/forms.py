# -*- coding: utf-8 -*-
from django import forms as form

class ApplyForm(form.Form):
    name = form.CharField(label="Nombre", help_text = "Escribe tu nombre completo")
    email = form.EmailField(help_text = "Escribe tu email nombre@gmail.com")
    phone = form.CharField(help_text = u"Escribe tu teléfono", label="Mobile")
    cv_file = form.FileField(help_text = u"Anexa un archivo")
