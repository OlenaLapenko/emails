import datetime
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

from django.views import generic

from django.shortcuts import render, redirect

from .forms import InputForm

from .tasks import mails


def sending_mail(request):
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            text = form.cleaned_data.get("text")
            sending_time = form.cleaned_data.get("sending_time")
            mails.apply_async((text, email), countdown=10)
            return HttpResponseRedirect(reverse(thanks))
    else:
        form = InputForm(initial={'sending_time': datetime.datetime.now()})
        return render(request, template_name='form.html', context={"form": form})


def thanks(request):
    return render(
        request=request,
        template_name='thanks.html',
        )
