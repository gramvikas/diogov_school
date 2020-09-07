# Generated by Django 3.1 on 2020-09-03 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='LatestNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top_Image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.AlterField(
            model_name='gallery',
            name='Img_title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
