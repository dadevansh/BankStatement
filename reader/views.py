# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from reader import processing
from reader.forms import UserForm


@login_required
def index(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        processing.read_table(myfile, request.user)
        upload_confirm = True

        return render(request, 'reader/index.html', {
            'upload_confirm': upload_confirm
        })
    return render(request, 'reader/index.html')


@login_required
def api_req(request):
    re = processing.query_db(request.user)
    '''In the assignment it was written call the api with name in the statement,
    I guess it makes more sense to call with the username he is using to login. So, I am gonna do it with this.'''
    return JsonResponse(re, safe=False)


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request, 'registration/registration.html',
                  {'user_form': user_form,
                   'registered': registered})
