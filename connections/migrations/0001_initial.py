# Generated by Django 3.2 on 2022-08-04 17:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('updated_image', models.ImageField(null=True, upload_to='images/')),
                ('file_name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'UploadedImages',
            },
        ),
    ]
