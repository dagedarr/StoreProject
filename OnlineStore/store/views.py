from django.shortcuts import render

def store(request):
    context = {}
    return render(request, 'store/main_page.html', context)
