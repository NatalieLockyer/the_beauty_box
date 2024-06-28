from django.shortcuts import render, get_object_or_404

from .models import Blog, Comment 

def all_blogs(request):
    """ A view to show all blogs """
    
    blog = Blog.objects.all()

    context = {
        'blog': blog,
    }

    return render(request, 'blog/blog.html', context)


def blog_detail(request, blog_id):
    """ A view to show the individual details of the blogs """

    blog = get_object_or_404(Blog, pk=blog_id)

    context = {
        'blog': blog,
    }

    return render(request, 'blog/blog_detail.html', context)
