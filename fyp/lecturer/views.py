from django.shortcuts import render

def table_view(request):
    return render(request, 'table.html')

def dashboard_view(request):
    return render(request, 'dashboard.html')
