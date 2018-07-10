# Generated by Django 2.0.6 on 2018-06-22 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0009_auto_20180613_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concept',
            name='area',
            field=models.CharField(choices=[('Apps', 'Apps'), ('Cache', 'Cache'), ('Django', 'Django'), ('Docker', 'Docker'), ('General', 'General'), ('Git', 'Git'), ('HTML & CSS', 'HTML & CSS'), ('JavaScript', 'JavaScript'), ('jQuery', 'jQuery'), ('Python', 'Python')], default='APP', max_length=255, verbose_name='Area'),
        ),
    ]
