# Generated by Django 2.1.2 on 2018-10-18 20:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=100)),
                ('authors_info', models.TextField()),
                ('isbn', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date_publish', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]
