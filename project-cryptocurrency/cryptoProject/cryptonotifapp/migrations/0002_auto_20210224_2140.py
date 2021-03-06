# Generated by Django 3.1.7 on 2021-02-24 20:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cryptonotifapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='password_text',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='email_text',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='name_text',
            new_name='surname',
        ),
        migrations.RemoveField(
            model_name='user',
            name='surname_text',
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='session',
            name='startDate',
            field=models.DateTimeField(),
        ),
    ]
