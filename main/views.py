from django.shortcuts import render

def show_main(request):
    context = {
        'npm': '2406495716',
        'name': 'Sahila Khairatul Athia',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)