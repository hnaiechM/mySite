# Generated by Django 5.0.2 on 2024-02-26 12:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0003_categorie_produit_categorie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('adresse', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(max_length=8)),
            ],
        ),
        migrations.AddField(
            model_name='produit',
            name='fournisseur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='magasin.fournisseur'),
        ),
    ]
