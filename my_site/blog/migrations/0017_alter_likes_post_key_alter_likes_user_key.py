# Generated by Django 4.2.6 on 2023-10-27 20:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0016_alter_likes_options_alter_likes_post_key_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='post_key',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='blog.post', verbose_name='Пост'),
        ),
        migrations.AlterField(
            model_name='likes',
            name='user_key',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]