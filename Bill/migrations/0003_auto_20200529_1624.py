# Generated by Django 3.0.3 on 2020-05-29 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Bill', '0002_client_tel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(blank=True, max_length=50, null=True)),
                ('prenom', models.CharField(blank=True, max_length=50, null=True)),
                ('adresse', models.TextField(blank=True, null=True)),
                ('tel', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='produit',
            name='fournisseur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Bill.Fournisseur'),
        ),
    ]
