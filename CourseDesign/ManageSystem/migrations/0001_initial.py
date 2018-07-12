# Generated by Django 2.0.6 on 2018-06-28 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('username', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('caption', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=32, null=True)),
                ('cls', models.ForeignKey(db_column='cls', on_delete=django.db.models.deletion.CASCADE, to='ManageSystem.Classes')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('cls', models.ManyToManyField(to='ManageSystem.Classes')),
            ],
        ),
    ]
