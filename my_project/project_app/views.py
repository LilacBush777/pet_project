from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]


class ViewsHome(ListView):
    paginate_by = 4
    model = Person
    template_name = 'project_app/index.html'
    context_object_name = 'posts'



def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})


def addpage(request):
    return HttpResponse("Добавление статьи")

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

class Show_post(DetailView):
    model = Person
    template_name = 'project_app/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'posts'

def test(request):
    return render(request, 'project_app/base.html')

class PersonCategory(ListView):
    model = Category
    template_name = 'project_app/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Person.objects.filter(category__slug=self.kwargs['category_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['posts'][0].category)
        context['menu'] = menu
        context['cat_selected'] = context['posts'][0].category_id
        return context