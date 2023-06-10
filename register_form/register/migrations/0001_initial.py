# Generated by Django 4.2.1 on 2023-06-10 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('department', models.IntegerField(choices=[(1, '1부'), (2, '2부'), (3, '3부')])),
                ('phone_number', models.CharField(max_length=13)),
                ('paid', models.CharField(choices=[('O', '송금했습니다.'), ('X', '아직 송금하지 않았습니다.')], max_length=1)),
                ('etc', models.TextField()),
                ('registered_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]