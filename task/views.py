from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .forms import InputForm

from .tasks import send_mail


@csrf_exempt
def sending_mail(request):
    submit_button = request.POST.get("submit")
    if request.method == "POST":
        form = InputForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get("email")
            text = form.cleaned_data.get("text")
            sending_time = form.cleaned_data.get("sending_time")
            context = {'form': form, 'email': email,
                       'text': text, 'submit_button': submit_button,
                       'sending_time': sending_time}
            send_mail.apply_async((text, email), eta=sending_time)
            return render(request, 'form.html', context)

    else:
        form = InputForm()

    return render(request, 'form.html', context={"form": form})

