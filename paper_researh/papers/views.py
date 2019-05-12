from django.shortcuts import render

# Create your views here.
def paperparse(request):
    return render(request, 'papers/titles.html')
