
from django.db import models
from django.core.validators import MinLengthValidator


class Post(models.Model):
    user_id = models.CharField(max_length=255)

    text = models.CharField(
        max_length=250,
        validators=[MinLengthValidator(1)],
        error_messages={
            "blank": "Post can not be empty.",
            "max_length": "Post can not contain more than 250 characters."
        }
    )

    status = models.CharField(
        max_length=20,
        default="Published",
    )

    created_date = models.DateTimeField(auto_now_add=True)
    last_edited_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.text
