from django.shortcuts import render
from .forms import CollaborationRequestForm

def contact(request):
    return render(request, 'contact/contact.html')


def collaboration_request(request):
    if request.method == 'POST':
        form = CollaborationRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message request has been submitted successfully! \
                We aim to get back to you within 24 hours')
            return redirect('collaboration_request')
        else:
            messages.error(request, 'Failed to send, Please check the form is valid and try again.')
    else:
        form = CollaborationRequestForm()
    
    return render(request, 'collaboration_request.html', {'form': form})