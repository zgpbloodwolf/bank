# Generated by Django 2.1.7 on 2019-04-28 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userinfor',
            fields=[
                ('card_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('idnumber', models.CharField(max_length=255)),
                ('money', models.IntegerField()),
                ('password', models.IntegerField()),
                ('feed', models.IntegerField()),
                ('satime', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'userinfor',
            },
        ),
    ]
