from django.shortcuts import render,redirect
from logics import chatbot_response
from django.urls import reverse
# Create your views here.


def Index(request):
    if request.method == 'POST':
        input_news = request.POST.get('newsInput')
        result = chatbot_response(input_news)

        if result is not None:
            return redirect(Result)
    return render(request, "index.html")

def Result(request, result):
    context = {
        'result' : result
    }
    return render(request, 'result.html', context)