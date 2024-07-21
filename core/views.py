from django.shortcuts import render

from .models import Produto

# Create your views here.
def index(request):
    produtos = Produto.objects.all()
    context = {
        'curso': 'Aplicações Web com Python',
        'desc': 'Django é brabo demais!',
        'produtos': produtos,
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

def produto(request, pk):
    produtoUn = Produto.objects.get(id=pk)
    print(produtoUn)
    context = {
        'produto': produtoUn,
    }
    return render(request, 'produto.html', context)
