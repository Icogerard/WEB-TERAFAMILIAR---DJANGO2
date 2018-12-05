from django.shortcuts import render, get_object_or_404
from .models import Post, Category
# Create your views here.
def testimonials(request):
    posts = Post.objects.all()
    return  render(request, "testimonials/testimonials.html", {'posts':posts})

"""Creamos la vista "category", y le pasamos request y un campo mas, 
que sera el identificador de lacategoria. Es el numero interno que se crea 
automaticamente. Diferencia las filas de las tablas que son el registro de la base de datos"""
def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    return render(request, "testimonials/category.html", {'category':category})