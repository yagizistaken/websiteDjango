from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render


def contact(request):
    if request.method == 'POST':
        name = request.POST['firstname']
        email = request.POST['mail']
        message = request.POST['message']

        # E-posta gönderme işlemini gerçekleştir
        send_mail(
            "Message from: " + name,
            message + "\n" + email,
            email,
            ["yagizcimx@gmail.com"],
        )

        return render(request, 'contact.html', {"message_name": name})
    else:
        return render(request, "contact.html", {})

def blog01(request):
    return render(request, 'blog01.html')
def blog_detail(request, pk):
    return render(request, 'blog_detail.html')

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def blog01(request):
    return render(request, 'blog01.html')

def work(request):
    return render(request, 'work.html')

def work01(request):
    return render(request, 'work01.html')

def work_detail(request):
    # İş detaylarının gösterildiği bir görünüm fonksiyonu
    return render(request, 'work_detail.html')



