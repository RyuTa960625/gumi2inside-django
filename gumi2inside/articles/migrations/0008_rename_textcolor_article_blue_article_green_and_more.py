# Generated by Django 4.2.5 on 2023-09-25 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_article_textcolor_article_textsize'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='textcolor',
            new_name='blue',
        ),
        migrations.AddField(
            model_name='article',
            name='green',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='red',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
