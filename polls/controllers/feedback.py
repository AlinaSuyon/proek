from django.shortcuts import redirect
from polls.models import Feedback

def create(request):

    feedback = Feedback()
    feedback.email = request.POST.get("email")
    feedback.message = request.POST.get("comment")
    feedback.save()

    return redirect('/')
