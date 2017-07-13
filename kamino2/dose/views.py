# -*- coding: utf-8 -*-
from __future__ import unicode_literals


## django views
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils import timezone
from django.urls import reverse

from .models import Post
from .forms import PostForm

landing_html = 'dose/landing.html'
done_html = 'dose/done.html'

# Create your views here.
def done(request):
    return render(request, done_html)

def request_num(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            # change the var name and string to retrieve input 
            goal = clean_data.get('goal')
            print goal
            form.save()
            return HttpResponseRedirect(reverse('dose:done'))
    else:
        form = PostForm()

    return render(request, landing_html, {'form': form})
