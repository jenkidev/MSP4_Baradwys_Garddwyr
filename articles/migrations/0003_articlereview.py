# Generated by Django 4.2.7 on 2023-12-19 07:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0002_article_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=3)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_reviews', to='articles.article')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
