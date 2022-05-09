# Generated by Django 4.0.4 on 2022-05-04 03:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appfront', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='receta',
            name='tiempo_registro',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField(help_text='comentario')),
                ('receta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appfront.receta')),
            ],
        ),
        migrations.AlterField(
            model_name='receta',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='appfront.autor'),
        ),
    ]