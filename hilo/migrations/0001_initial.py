# Generated by Django 2.2.4 on 2021-02-21 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('userId', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('Address_Line_1', models.CharField(max_length=40)),
                ('Address_Line_2', models.CharField(max_length=30)),
                ('City', models.CharField(max_length=30)),
                ('State', models.CharField(max_length=20)),
                ('Zip', models.IntegerField(max_length=40)),
                ('Country', models.CharField(max_length=30)),
                ('Email', models.CharField(max_length=45, null=True)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=45, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='statusReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('water', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('electricity', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('electricity_provider', models.CharField(max_length=30)),
                ('internet', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('internet_provider', models.CharField(max_length=30)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='status', to='hilo.User')),
            ],
        ),
    ]
