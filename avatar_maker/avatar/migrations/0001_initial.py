# Generated by Django 5.1.4 on 2024-12-16 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avatar_pic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='avatars/')),
                ('cartoon_img', models.ImageField(blank=True, null=True, upload_to='cartoons/')),
            ],
        ),
    ]