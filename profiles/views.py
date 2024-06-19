from django.shortcuts import render


def profile(request):
    """ Will display the User Profile """

    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
