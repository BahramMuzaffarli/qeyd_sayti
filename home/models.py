from django.db import models
from django.conf import settings

class Note(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Media(models.Model):
    file = models.FileField(upload_to='media/')
    title = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or self.file.name
    
class Note(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    note = models.TextField()  # əsas qeyd sahəsi

    # Yeni sahələr
    tani_bilgisi = models.TextField(blank=True, null=True)
    sikayet = models.TextField(blank=True, null=True)
    hikaye = models.TextField(blank=True, null=True)
    ozgecmis = models.TextField(blank=True, null=True)
    fizik_muayene = models.TextField(blank=True, null=True)
    bulgular = models.TextField(blank=True, null=True)
    tedavi = models.TextField(blank=True, null=True)
    oneriler = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('doctor', 'Həkim'),
        ('patient', 'Pasiyent'),
        ('staff', 'Digər personal'),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='patient'
    )

    def __str__(self):
        return f"{self.user.username} ({self.get_role_display()})"
    


    