# Generated by Django 3.1.4 on 2020-12-24 03:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20201221_0910'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='eemail',
            new_name='emp_email',
        ),
    ]