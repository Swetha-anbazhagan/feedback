from django.shortcuts import render, redirect
from .forms import FeedbackForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Feedback submission
@login_required
def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()
            return redirect('feedback_success')
    else:
        form = FeedbackForm()
    return render(request, 'feedback_form.html', {'form': form})

# Feedback success
def feedback_success(request):
    return render(request, 'feedback_success.html')

# Signup view (moved out of feedback_success!)
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('submit_feedback')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
