from django.db import models

class Work(models.Model):
    title = models.CharField
    created_at = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='photos/%Y/%m/%d')
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Работа"
        verbose_name_plural = "Работы"