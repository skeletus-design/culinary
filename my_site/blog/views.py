from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)



# from blog.forms import ImageForm
from .models import Post
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
8# from .forms import PostCreateForm
from django.views.decorators.csrf import csrf_exempt



def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post
    fields = ['title', 'content', 'image']
        

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'image']
    # @method_decorator(csrf_exempt)
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    
# def form_valid(self, form):
    
    
# def SaveImage(request):
#     if request.method == 'POST':
#         p_form = ImageForm(request.POST,
#                                    request.FILES,
#                                    instance=request.user.profile)
#         if p_form.is_valid():
#             p_form.save()
#             return redirect('post-update')    
        
#     context = {
#         'p_form': p_form
#     }
#     return render(request, 'post-update', context)
        


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content' ]
    # @method_decorator(csrf_exempt)
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    # @method_decorator(csrf_exempt)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    # @method_decorator(csrf_exempt)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'О книге рецептов'})