from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    bio = models.TextField()
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    favorite_genres = models.ManyToManyField('books.Genre')
    books_read = models.ManyToManyField('books.Book', through='ReadingStatus', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
    
class ReadingStatus(models.Model):
    STATUS_CHOICE = [
        ('completed', 'Completed'),
        ('reading', 'Reading'),
        ('dropped', 'Dropped'),
    ]
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='reading_statuses')
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE, related_name='reading_statuses')
    status = models.CharField(max_length=20, choices=STATUS_CHOICE)

    started_at = models.DateField(null=True, blank=True)
    completed_at = models.DateField(null=True, blank=True)

    class Meta:
        unique_together = ['user', 'book']

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"