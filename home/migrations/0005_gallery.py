# Generated by Django 3.1 on 2020-08-26 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_contact_date1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Img_title', models.CharField(max_length=100)),
                ('Image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
