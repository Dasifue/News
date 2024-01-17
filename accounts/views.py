from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import User
from .forms import UserRegistrationForm, ChangePasswordForm

from news.models import Article


def register_view(request): 
    form = UserRegistrationForm() # Определяется пустая форма для регистрации пользователя
 
    if request.method == "POST": # Если пользователь ввёл данные в html форму и отправил их на сервер
        form = UserRegistrationForm(data=request.POST) # передаём данные в форму
        if form.is_valid(): # форма проверяет данные
            user = User.objects.create( # создаём пользователя
                username = form.cleaned_data['username'], # передаём пользователю username
                email = form.cleaned_data['email'], # передаём пользователю email
            )
            user.set_password(raw_password=form.cleaned_data['password']) # хешируем пароль пользователя
            user.save() # сохранение пользователя
            return redirect("accounts:login") # перенаправление пользователя на страницу авторизации
    

    context = { # определение контекса
        "form": form
    }
    # отправка контекстных данных на html шаблон
    return render(request=request, template_name="register.html", context=context)


def login_view(request):
    if request.method == "POST": # получаем POST запрос с его данными
        username = request.POST.get("username") # достаём из запроса username
        password = request.POST.get("password") # достаём из запроса password
        user = authenticate(request, username=username, password=password) # проверяем username и password на существование
        if user is not None: # Если пользователь с таким username и password найден
            login(request, user) # авторизуем пользователя
            return redirect("news:index") # перенаправляем его на главную страницу
        
        context = {
            "error": "Ошибка! Проверьте username и password!"
        }
        return render(request=request, template_name="login.html", context=context)
    return render(request=request, template_name="login.html")


def logout_view(request):
    logout(request=request) # Вынести пользователя из системы (выйти из аккаунта)
    return redirect("accounts:login")


@login_required # декоратор, перенаправляющий пользователя на страицу авторизации, если он не авторизован
def change_password_view(request):
    # if not request.user.is_authenticated: # если пользователь не авторизован
    #     return redirect("accounts:login") # перенапрваление к авторизации

    form = ChangePasswordForm() # Определяем пустую форму
    user: User = request.user # находим авторизованного пользователя

    context = { # определяем контекстные данные, которые будут отправлены на фронт
        "form": form
    }

    if request.method == "POST": # Если пользоваатель отправил POST запрос с данными для изменения пароля
        form = ChangePasswordForm(data=request.POST) # отправляем полученные данные из фронта в форму
        real_password = request.POST['real_password'] # достаём вручную действительный пароль пользователя из POST запроса

        if not user.check_password(real_password): # check_password - проверка на действительность введённого пароля
            context.update({"error": "Неправильный пароль!"}) # добавление ошибки, если пароль не действительный

        elif form.is_valid():  # is_valid - проверка новых паролей
            user.set_password(raw_password=form.cleaned_data['new_password']) # Меняем пароль у пользователя и хешируем его
            user.save() # сохранение изменений в бд
            logout(request) # выход из системы
            return redirect("accounts:login") # перенаправление на страницу авторизации
    
    context.update({"form": form}) # обновление контекста
    return render(request=request, template_name="change_password.html", context=context) # отправка context данных на html страницу


@login_required
def add_to_favorites_view(request, article_pk: int):
    article = get_object_or_404(Article, id=article_pk)
    user: User = request.user
    user.favorites.add(article)
    return redirect(request.META.get("HTTP_REFERER", "/"))


@login_required
def remove_from_favorites_view(request, article_pk: int):
    article = get_object_or_404(Article, id=article_pk)
    user: User = request.user
    user.favorites.remove(article)
    return redirect(request.META.get("HTTP_REFERER", "/"))


@login_required
def favorites_view(request):
    user: User = request.user
    articles = user.favorites.all()

    context = {
        "articles": articles 
    }
    return render(request=request, template_name="favorites.html", context=context)