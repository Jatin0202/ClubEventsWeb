# Generated by Django 2.2.7 on 2020-03-11 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_name', models.CharField(choices=[('Coding Club', 'Coding Club IITG'), ('Electronics', 'Electroncis Club IITG'), ('Robotics', 'Robotics Club IITG'), ('LitSoc', 'Literary Society IITG'), ('Xpressions', 'Drama Club IITG'), ('Aeromodelling', 'Aeromodelling Club IITG'), ('Cadence', 'Dance Club IITG'), ('IITG.AI', 'Artificial intelligence Club IITG')], max_length=50)),
                ('club_secy', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_on', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('clubname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Club.club')),
            ],
            options={
                'ordering': ['-updated_on'],
            },
        ),
    ]
