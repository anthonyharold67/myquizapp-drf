# Generated by Django 4.2.1 on 2023-06-03 18:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quizapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.PositiveSmallIntegerField()),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizapp.quiz')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='grade',
            constraint=models.UniqueConstraint(fields=('student', 'quiz'), name='unique_student_quiz'),
        ),
    ]
