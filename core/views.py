from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseBadRequest
from django.urls import reverse
from core.forms import ContactForm
#from core.forms import ContactForm  Lo descomentare cuando cree el form de comentario

# Create your views here.
def index(request):
    return render(request, "core/index.html")

def nosotros(request):
    return render(request, 'core/Nosotros.html')

def contacto(request):  #Los formularios basados en clases manejan el envío de datos del formulario y la creación de instancias de formularios en la vista. Puedes acceder a los datos del formulario a través de request.POST o request.GET, dependiendo del método de envío del formulario.
    if request.method == "GET":
        formulario_contacto = ContactForm()
        # respuesta=""
    elif request.method == "POST":
        formulario_contacto = ContactForm(request.POST)
        if formulario_contacto.is_valid():
            # respuesta=f"Mensaje recibido. Agradecemos su consulta."
            return redirect(reverse('respForm'))
    else:
        return HttpResponseBadRequest ("Método no correcto")
    contexto={
        # 'respuesta': respuesta,
        'formulario': formulario_contacto,
    }
    return render(request, "core/contacto.html", contexto)

def respForm(request):
    return render(request, 'core/respForm.html')
