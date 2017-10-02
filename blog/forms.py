# coding=utf-8

from django import forms



class Contato(forms.Form):
    name = forms.CharField(label='nome')
    email = forms.EmailField(label='email')
