from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Note

# Sadə index səhifəsi
def index(request):
    return HttpResponse("""
    <html>
    <head>
        <title>Sadə Sayt</title>
        <style>
            body {
                background-color: #a0d8f1;  /* Açıq mavi background */
                font-family: Arial, sans-serif;
                text-align: center;
                padding-top: 100px;
            }
            .giris {
                background-color: white;
                display: inline-block;
                padding: 30px 50px;
                border-radius: 15px;
                box-shadow: 0 0 20px rgba(0,0,0,0.2);
            }
            h1 { color: #004080; }
            p { color: #333; }
        </style>
    </head>
    <body>
        <div class="giris">
            <h1>Salam Bahram!</h1>
            <p>Saytına xoş gəlmisən 😊</p>
        </div>
    </body>
    </html>
    """)

# Login səhifəsi
def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        # username-i session-a yazırıq ki, welcome səhifəsində istifadə edək
        request.session['username'] = username
        return redirect('welcome')  # login sonrası welcome səhifəsinə yönləndir

    return render(request, "home/login.html")

# Welcome səhifəsi – username və notes table göstərir
def welcome(request):
    username = request.session.get('username', 'Qonaq')

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        note_text = request.POST.get('note')
        if first_name and last_name and note_text:
            Note.objects.create(first_name=first_name, last_name=last_name, note=note_text)
        return redirect('welcome')  # form submit → səhifəni yenilə
        

    notes = Note.objects.all()
    return render(request, "home/welcome.html", {'username': username, 'notes': notes})

# mövcud welcome view-in altında əlavə et
def logout_view(request):
    request.session.flush()  # sessiyanı təmizləyir
    return redirect('login')  # əsas login səhifəsinə yönləndir
