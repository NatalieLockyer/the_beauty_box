from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe

from .models import Blog, Comment
from .forms import BlogForm, CommentForm

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
    comments = blog.comments.all().order_by('created_on')
    comment_count = blog.comments.filter(approved=True).count()

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.blog = blog
            comment.save()
            messages.success(request, 'Your comment has been \
                submitted and waiting approval')

    comment_form = CommentForm()

    return render(request, 'blog/blog_detail.html',{
        'blog': blog,
        'comments': comments,
        'comment_form': comment_form,
        'comment_count': comment_count}, 
        )

@login_required
def add_blog(request):
    """ Add a blog to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners have permission to do that')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save()
            messages.success(request, 'Successfully uploaded blog!')
            return redirect(reverse('blog_detail', args=[blog.id]))
        else:
            messages.error(request, 'Failed to upload blog. Please check the form is valid and try again.')
    else:
        form = BlogForm()
        
    template = 'blog/add_blog.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_blog(request, blog_id):
    """ Edit a blog within the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners have permission to do that')
        return redirect(reverse('home'))

    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
        form = BlogForm(request.POST,  request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your blog has been successfully updated!')
            return redirect(reverse('blog_detail', args=[blog.id]))
        else:
            messages.error(request, 'Failed to upload blog. Please check the form is valid and try again')
    else:
        form = BlogForm(instance=blog)
    messages.info(request, f'You are editing {blog.title}')
    
    template = 'blog/edit_blog.html'
    context = {
        'form': form,
        'blog': blog,
    }

    return render(request, template, context)


@login_required
def delete_blog(request, blog_id):
    """ Delete a blog in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners have permission to do that')
        return redirect(reverse('home'))

    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    messages.success(request, 'Your blog has now been deleted')
    return redirect(reverse('blog'))