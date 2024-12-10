from django.shortcuts import render

# Create your views here.


def about(request):
    print('about')
    template = 'pages/about.html'
    return render(request, template)


def rules(request):
    print('rules')
    template = 'pages/rules.html'
    return render(request, template)
