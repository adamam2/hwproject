# Generated by Django 2.0.5 on 2018-06-12 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0007_auto_20180612_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concept',
            name='area',
            field=models.CharField(choices=[('Apps', 'Apps'), ('Django', 'Django'), ('Docker', 'Docker'), ('General', 'General'), ('Git', 'Git'), ('HTML & CSS', 'HTML & CSS'), ('JavaScript', 'JavaScript'), ('jQuery', 'jQuery'), ('Python', 'Python')], default='APP', max_length=255, verbose_name='Area'),
        ),
    ]
