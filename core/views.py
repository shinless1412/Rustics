from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Producto
from core.Carrito import Carrito    
from .forms import CervezaForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseNotAllowed, JsonResponse
from .models import Review
from .forms import ReviewForm
# Create your views here.

def home(request):
    return render(request, 'index.html')


def products(request):
    productos = Producto.objects.all()
    return render(request, 'products.html', {'productos':productos})


@user_passes_test(lambda u: u.is_superuser)
def listado(request):
    productos = Producto.objects.all()
    print(listado)
    return render(request, 'cerveza/listado.html', {'productos':productos})


def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("products")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("products")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("products")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("products")
@login_required
def perfil(request):    
    return render(request, 'perfil.html')
def about(request):
    return render(request, 'about.html')
def exit(request):
    logout(request)
    return redirect('home')

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('home')
    return render(request, 'registration/register.html',data)


@user_passes_test(lambda u: u.is_superuser)
def crear(request):
    if request.method == 'POST':
        formulario = CervezaForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('listado')
    else:       
        formulario = CervezaForm()
    
    return render(request, 'cerveza/crear.html', {'formulario': formulario})

@user_passes_test(lambda u: u.is_superuser)
def editar(request, id=None):
    if id:
        producto = get_object_or_404(Producto, id=id)
    else:
        producto = None

    if request.method == 'POST':
        formulario = CervezaForm(request.POST, request.FILES, instance=producto)
        if formulario.is_valid():
            formulario.save()
            return redirect('listado')
    else:
        formulario = CervezaForm(instance=producto)

    return render(request, 'cerveza/editar.html', {'formulario': formulario})


@user_passes_test(lambda u: u.is_superuser)
def eliminar(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect("listado")

@login_required
def lista_reviews(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    reviews = Review.objects.filter(producto=producto)  # Filtrar las reviews por producto
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.producto = producto  # Asignar el producto a la review
            review.save()
            return redirect('lista_reviews', producto_id=producto_id)
    return render(request, 'lista_reviews.html', {'producto': producto, 'reviews': reviews, 'form': form})

@login_required
def eliminar_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.method == 'POST':
        review.delete()
        return redirect('lista_reviews', producto_id=review.producto_id)
    else:
        return HttpResponseNotAllowed(['POST'])