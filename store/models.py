from django.db import models


class HeadLines(models.Model):
    headline = models.TextField(max_length=250, blank=True, null=True)
    image = models.ImageField(upload_to="Image", blank=True, null=True)
    is_real = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Headline"
        verbose_name_plural = "Headlines"
            