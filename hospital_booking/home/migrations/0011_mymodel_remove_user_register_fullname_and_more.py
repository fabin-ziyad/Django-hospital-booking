# Generated by Django 4.0.6 on 2022-07-26 08:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_user_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('Email', models.EmailField(default='', max_length=255)),
                ('password', models.CharField(default='', max_length=400)),
                ('password2', models.CharField(default='', max_length=400)),
                ('fullname', models.CharField(default='', max_length=400)),
            ],
        ),
        migrations.RemoveField(
            model_name='user_register',
            name='fullname',
        ),
        migrations.RemoveField(
            model_name='user_register',
            name='pass1',
        ),
        migrations.RemoveField(
            model_name='user_register',
            name='pass2',
        ),
        migrations.RemoveField(
            model_name='user_register',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='user_register',
            name='password',
            field=models.CharField(default=django.utils.timezone.now, max_length=400),
            preserve_default=False,
        ),
    ]