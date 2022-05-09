from django.shortcuts import render

from . models import Categoria,Producto

# Create your views here.
def index(request):
    # request.session['titulo'] = "MODA DJANGO"
    listaproductos = Producto.objects.all()
    listaCategoria = Categoria.objects.all()
    context = {
        'productos':listaproductos,
        'categorias': listaCategoria
    }

    return render(request,'index.html',context)

def producto(request,producto_id):
    objproducto = Producto.objects.get(pk=producto_id)
    context = {
        'producto': objproducto
    }
    return render(request,'producto.html',context)

def productosPorCategoria(request,categoria_id):
    objCategoria = Categoria.objects.get(pk=categoria_id)
    listaProductos = objCategoria.producto_set.all()
    listaCategorias = Categoria.objects.all()
    context = {
        'productos':listaProductos,
        'categorias':listaCategorias
    }
    return render(request,'index.html',context)

from app.carrito import Cart

def carrito(request):
    return render(request,'carrito.html')

def agregarCarrito(request,producto_id):
    objProducto = Producto.objects.get(id=producto_id)
    carritoProducto = Cart(request)
    carritoProducto.add(objProducto,1)
    print(request.session.get("cart"))
    
    return render(request,'carrito.html')

def eliminarProductoCarrito(request,producto_id):
    objProducto = Producto.objects.get(id=producto_id)
    carritoProducto = Cart(request)
    carritoProducto.delete(objProducto)
    
    return render(request,'carrito.html')

def limpiarCarrito(request):
    carritoProducto = Cart(request)
    carritoProducto.clear()
    return render(request,'carrito.html')

    

    