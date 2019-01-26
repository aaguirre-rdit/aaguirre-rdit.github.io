from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from .models import Post, Category
from django.utils import timezone
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from .forms import ContactForm

# Create your views here.
def post_list(request):
    postlist = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date').reverse()
    categories = Category.objects.filter()
    paginator = Paginator(postlist, 5)  # Show 5 contacts per page
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/post_list.html', {'posts':posts, 'categories':categories})
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
def home(request):
    return render(request, 'blog/home.html',{})
def contact(request):
    return render(request, 'blog/contact.html', {})
def projects(request):
    return render(request, 'blog/projects.html',{})
def about(request):
    return render(request, 'blog/about.html',{})
