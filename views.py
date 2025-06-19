from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Selamat datang di Aplikasi Django!</h1><p><a href='/address'>Lihat alamat</a> | <a href='/phone'>Lihat telepon</a></p>")

def address_views(request):
    return HttpResponse("Alamat: Jl. pd. Halimun, RT.01/RW.07, Kel. Perbawati, Kec. Sukabumi, Kab. Sukabumi, Jawa Barat")

def phone_view(request):
    return HttpResponse("Telepon: 0857-2456-2959")

