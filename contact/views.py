from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CollaborationForm

def contact(request):
    if request.method == 'POST':
        collaboration_form = CollaborationForm(data=request.POST)
        if collaboration_form.is_valid():
            collaboration_form.save()
            messages.success(request, 'Your message request has been submitted successfully! \
                We aim to get back to you within 24 hours')
            return redirect('contact')
        else:
            messages.error(request, 'Failed to send, Please check the form is valid and try again.')
    else:
        collaboration_form = CollaborationForm()
    
    return render(request, 
    "contact/contact.html",
    {
        "contact": contact,
        "collaboration_form": collaboration_form},
    )


   