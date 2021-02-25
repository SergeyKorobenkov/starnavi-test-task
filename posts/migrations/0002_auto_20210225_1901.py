# Generated by Django 3.1.3 on 2021-02-25 16:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='likes',
            name='liked_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked_post_id', to='posts.post'),
        ),
        migrations.AddField(
            model_name='likes',
            name='who_like_it',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liker', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='likes',
            unique_together={('who_like_it', 'liked_post')},
        ),
    ]