from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe


from .models import Tutorial
from .forms import TutorialForm


def all_tutorials(request):
    """ A view to show all tutorial videos """
    
    tutorials = Tutorial.objects.all()

    context = {
        'tutorials': tutorials,
    }

    return render(request, 'tutorials/tutorial.html', context)


def tutorial_detail(request, tutorial_id):
    """ A view to show the individual details of the tutorial videos """
    
    tutorials = get_object_or_404(Tutorial, pk=tutorial_id)

    context = {
        'tutorial': tutorial,
    }

    return render(request, 'tutorials/tutorial_detail.html', context)

@login_required
def add_tutorial(request):
    """ Add a tutorial to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners have permission to do that')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = TutorialForm(request.POST, request.FILES)
        if form.is_valid():
            tutorial = form.save()
            messages.success(request, 'Successfully uploaded tutorial!')
            return redirect(reverse('tutorial_detail', args=[tutorial.id]))
        else:
            messages.error(request, 'Failed to upload tutorial. Please check the form is valid and try again.')
    else:
        form = TutorialForm()
        
    template = 'tutorials/add_tutorial.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_tutorial(request, tutorial_id):
    """ Edit a tutorial within the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners have permission to do that')
        return redirect(reverse('home'))

    tutorial = get_object_or_404(Tutorial, pk=tutorial_id)
    if request.method == 'POST':
        form = TutorialForm(request.POST,  request.FILES, instance=tutorial)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your tutorial has been successfully updated!')
            return redirect(reverse('tutorial_detail', args=[tutorial.id]))
        else:
            messages.error(request, 'Failed to upload tutorial. Please check the form is valid and try again')
    else:
        form = TutorialForm(instance=tutorial)
    messages.info(request, f'You are editing {tutorial.title}')
    
    template = 'tutorials/edit_tutorial.html'
    context = {
        'form': form,
        'tutorial': tutorial,
    }

    return render(request, template, context)


@login_required
def delete_tutorial(request, tutorial_id):
    """ Delete a tutorial in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners have permission to do that')
        return redirect(reverse('home'))

    tutorial = get_object_or_404(Tutorial, pk=tutorial_id)
    tutorial.delete()
    messages.success(request, 'Your tutorial has now been deleted')
    return redirect(reverse('tutorials'))