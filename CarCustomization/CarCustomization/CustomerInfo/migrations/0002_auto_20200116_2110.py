# Generated by Django 3.0.1 on 2020-01-16 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerInfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DesireInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('pdf', models.FileField(upload_to='info/pdfs/')),
                ('cover', models.ImageField(blank=True, null=True, upload_to='info/covers/')),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]