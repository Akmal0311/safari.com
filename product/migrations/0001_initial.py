# Generated by Django 3.1.5 on 2022-09-12 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=111)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=111)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=111)),
                ('image', models.ImageField(default='mountain.jpg', upload_to='')),
                ('size', models.CharField(max_length=11)),
                ('color', models.CharField(max_length=11)),
                ('price', models.IntegerField()),
                ('like', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.type')),
            ],
        ),
    ]
