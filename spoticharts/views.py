from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'spoticharts/index.html')

def about(request):
    return render(request, 'spoticharts/about.html')

def charts(request):
    return render(request, 'spoticharts/charts.html')