# Generated by Django 3.2.6 on 2021-08-07 14:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('body', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(upload_to='uplodes')),
                ('category', models.CharField(choices=[('Travel', 'Travel'), ('Movie', 'Movie'), ('Technology', 'Technology'), ('Climate Change', 'Climate Change')], max_length=200)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]