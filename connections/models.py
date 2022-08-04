from django.db import models
import uuid

# Create your models here.

class UploadedImages(models.Model):
    User_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    updated_image = models.ImageField(upload_to="images/", null=True)

    class Meta:
        db_table = "UploadedImages"
