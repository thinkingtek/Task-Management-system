from PIL import Image
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator


class User(AbstractUser):
    email = models.EmailField(verbose_name='Email Address', max_length=60, unique=True,
                              help_text='This email address will be valiated', error_messages={'unique': 'Sorry this email cannot be used'})

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['-date_joined']

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        default='profile_pix/profile_img.png', upload_to='profile_pix', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 310 or img.width > 310:
            output_size = (310, 310)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return self.user.full_name
