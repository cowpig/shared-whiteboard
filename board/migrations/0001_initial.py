# Generated by Django 2.2 on 2019-06-06 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stroke',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=225)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('prev_x', models.IntegerField(null=True)),
                ('prev_y', models.IntegerField(null=True)),
                ('coordenate_x', models.IntegerField()),
                ('coordenate_y', models.IntegerField()),
                ('is_point', models.IntegerField(default=0)),
                ('color', models.CharField(default='black', max_length=225)),
            ],
        ),
    ]