from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse

from .models import *
from .forms import NewUserForm

def feed_page(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('description')
        postFile = request.FILES.get('postFile')
        print(title)
        print(postFile)
        if title and desc and postFile:
            userPost.objects.create(title=title, desc=desc, uploaded_file=postFile, user_profile=request.user)
            return HttpResponseRedirect(request.path_info)

    posts = userPost.objects.all().order_by('-published_date')
    return render(request, 'feed/feed_page.html', {'posts': posts})

def delete_post(request, id):
    print("deleting")
    post = userPost.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('feed'))


def registration_page(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("/")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request, template_name="operations/register.html", context={"register_form": form})

def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, "operations/login.html", {"login_form": form})

def logout_page(request):
    logout(request)
    return redirect('/')

class UserDetailView(DetailView):
    model = CustomUser

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        context['posts'] = userPost.objects.filter(user_profile=self.kwargs['pk'])
        return context