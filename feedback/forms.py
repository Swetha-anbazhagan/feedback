from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['content', 'rating']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write your feedback...'}),
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }
