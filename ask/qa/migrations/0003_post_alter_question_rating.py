# Generated by Django 4.0.5 on 2023-01-01 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0002_rename_content_question_text_alter_question_added_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('creation_date', models.DateTimeField(blank=True)),
                ('is_published', models.BooleanField()),
            ],
        ),
        migrations.AlterField(
            model_name='question',
            name='rating',
            field=models.IntegerField(default=True),
        ),
    ]