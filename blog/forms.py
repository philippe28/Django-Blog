# coding=utf-8

from django import forms



class Contato(forms.Form):
    name = forms.CharField(label='Nome')
    email = forms.EmailField(label='E-mail')
   