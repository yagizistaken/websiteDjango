from django.contrib import admin
from django.urls import path
from website.views import index, about, blog, blog01, contact, work, work01, work_detail, blog_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('about.html', about, name='about'),
    path('blog.html', blog, name='blog'),
    path('blog01.html', blog01, name='blog01'),
    path('contact.html', contact, name='contact'),  # Doğru view fonksiyonunu çağırın
    path("index.html", index, name="index"),
    path("work.html", work, name="work"),
    path("work01.html", work01, name="work01"),
    path("work_detail/", work_detail, name="work_detail"),  # Yeni URL tanımı
    path('blog_detail/<int:pk>/', blog01, name='blog_detail'),
]
