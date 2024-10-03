# File: mini_fb/admin.py
# Author: Samhitha Somavarapu (samhitha@bu.edu), 10/03/2024
# Description: The admin file for the mini_fb application.
# Lets the Django admin know we want to administer the
# Profile model.
from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(Profile)