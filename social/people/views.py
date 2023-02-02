from django.shortcuts import render

def people_search(request):
    return render(request, 'people/people_search.html')
