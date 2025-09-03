from django.shortcuts import render

def show_main(request):
    context = {
        "npm": "2406495382",
        "name": "Valerian Hizkia Emmanuel",
        "class": "PBP E"
    }

    return render(request, "main.html", context)