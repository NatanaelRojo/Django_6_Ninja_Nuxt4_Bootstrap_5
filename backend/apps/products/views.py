from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product
from .forms import ProductForm
from django.contrib.auth.mixins import LoginRequiredMixin


class ProductListView(LoginRequiredMixin, ListView):
    """Displays the product list"""
    model = Product
    template_name = 'products/home.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ProductDetailView(LoginRequiredMixin, DetailView):
    """Shows product details"""
    model = Product
    template_name = 'products/detail.html'
    context_object_name = 'product'

class ProductCreateView(LoginRequiredMixin, CreateView):
    """Display the form and create a product"""
    model = Product
    form_class = ProductForm
    template_name = 'products/create.html'
    success_url = reverse_lazy('products:home')

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """Display the form and update a product"""
    model = Product
    form_class = ProductForm
    template_name = 'products/update.html'
    
    def get_success_url(self):
        return reverse_lazy('products:detail', kwargs={'pk': self.object.pk})

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """Confirm and delete a product"""
    model = Product
    template_name = 'products/delete.html'
    success_url = reverse_lazy('products:home')
