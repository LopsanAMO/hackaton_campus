from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.views.generic import TemplateView


class detalleView(TemplateView):
    def get(self, request):
        template_name = 'shop/product/detail.html'
        return render(request, template_name)

class ProductoView(TemplateView):
    def get(self, request):
        template_name = 'shop/product/list.html'
        return render(request, template_name)


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    template_name = 'shop/product/detail.html'
    ctx = {'product': product, 'cart_product_form': cart_product_form}
    return render(request, template_name, ctx)

class artesalanView(TemplateView):
    def get(self, request):
        template_name = 'shop/product/pricing.html'
        return render(request, template_name)
