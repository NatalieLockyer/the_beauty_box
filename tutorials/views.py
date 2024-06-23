from django.shortcuts import render, get_object_or_404

from .models import Tutorial


def all_tutorials(request):
    """ A view to show all tutorial videos """
    
    tutorials = Tutorial.objects.all()

    context = {
        'tutorials': tutorials,
    }

    return render(request, 'tutorials/tutorial.html', context)


def tutorial_detail(request, tutorial_id):
    """ A view to show the individual details of the tutorial videos """
    
    tutorial = get_object_or_404(Tutorial, pk=tutorial_id)

    context = {
        'tutorial': tutorial,
    }

    return render(request, 'tutorials/tutorial_detail.html', context)