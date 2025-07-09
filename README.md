# ✅Assignment 2

## 📅Date: 09/07/2025

### Build a `Feedback` model with a foreign key to `User`, text content, rating (1 to 5), and timestamp. Ensure rating is validated to be within 1–5.

## Program

models.py
```
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedbacks')
    content = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.user.username} - Rating: {self.rating}"

```
## Output

![Screenshot 2025-07-09 133459](https://github.com/user-attachments/assets/75f1ecb1-b4f6-42f1-b341-1f7f78db8fa1)

![Screenshot 2025-07-09 133518](https://github.com/user-attachments/assets/cd019957-042f-4df1-8a18-851366111744)

![Screenshot 2025-07-09 133551](https://github.com/user-attachments/assets/3cada4ae-d029-4112-85c5-812518b85d8c)

![Screenshot 2025-07-09 133605](https://github.com/user-attachments/assets/456baddc-264c-4659-8f9a-f27ce1959dbb)

![Screenshot 2025-07-09 133627](https://github.com/user-attachments/assets/2a7bfa94-7637-4a28-8d81-a79831d79f80)


