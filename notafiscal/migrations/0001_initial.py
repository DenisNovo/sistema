# Generated by Django 4.0.4 on 2022-06-08 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='notafiscal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto', models.CharField(max_length=100)),
                ('marca', models.CharField(max_length=100)),
                ('cpf', models.IntegerField(max_length=100)),
                ('cores', models.CharField(max_length=100)),
                ('preco', models.IntegerField(max_length=100)),
            ],
        ),
    ]
