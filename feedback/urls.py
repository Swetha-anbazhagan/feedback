from django.urls import path
from .views import signup_view, submit_feedback, feedback_success

urlpatterns = [
    path('', signup_view, name='signup'),  # home = signup
    path('submit/', submit_feedback, name='submit_feedback'),
    path('success/', feedback_success, name='feedback_success'),
]


