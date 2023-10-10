from django.shortcuts import render

def dashboard(request):

    return render(request, 'pages/dashboard.html')

def main_dashboard(request):
    return render(request, 'dashboard/main_dashboard.html', {'url': "/dashboard/test" })
