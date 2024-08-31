from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from .models import Produto
from .forms import ProdutoForm
from .serializers import ProdutoSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

def produto_list(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/produto_list.html', {'produtos': produtos})

def produto_create(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produto_list')
    else:
        form = ProdutoForm()
    return render(request, 'produtos/produto_form.html', {'form': form})

def produto_edit(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('produto_list')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produtos/produto_form.html', {'form': form})

def produto_delete(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        produto.delete()
        return redirect('produto_list')
    return render(request, 'produtos/produto_confirm_delete.html', {'produto': produto})

