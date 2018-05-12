from django.shortcuts import render
from django.http import HttpResponse
from .models import Account
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm

class UserFormView(View):
	form_class = UserForm
	template_name = 'login/registration_form.html'