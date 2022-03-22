from re import template
from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

class PostList(ListView):
    model = Post
    template_name='blog/index.html'

    # 가장 최근에 적은 포스트부터 나열되게함.
# def index(request):
#     posts = Post.objects.all().order_by('-pk')

#     return render(
#         request,
#         'blog/index.html',
#         {
#             'posts' : posts,
#         }
#     )

def single_post_page(request, pk):
    posts = Post.objects.get(pk=pk)

    return render(
        request,
        'blog/single_post_page.html',
        {
            'posts' : posts,
        }
    )
