from django.shortcuts import render
from .email import send_welcome_email

# Create your views here.

def profile(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']

            recipient = NewsLetterRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)

            HttpResponseRedirect('news_today')
            #.................
    return render(request, 'all-news/today-news.html', {"date": date,"news":news,"letterForm":form})