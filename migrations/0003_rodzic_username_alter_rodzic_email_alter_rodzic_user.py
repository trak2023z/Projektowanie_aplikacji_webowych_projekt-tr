# Generated by Django 4.1.7 on 2023-04-19 19:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dziennik', '0002_rodzic_user_alter_nauczyciel_nr_telefonu_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='rodzic',
            name='username',
            field=models.CharField(default='test', max_length=150),
        ),
        migrations.AlterField(
            model_name='rodzic',
            name='email',
            field=models.EmailField(default='test', max_length=50),
        ),
        migrations.AlterField(
            model_name='rodzic',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
