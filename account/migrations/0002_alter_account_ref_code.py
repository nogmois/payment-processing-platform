# Generated by Django 4.2.3 on 2023-08-02 14:32

from django.db import migrations
import shortuuid.django_fields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='ref_code',
            field=shortuuid.django_fields.ShortUUIDField(alphabet='abcdefgh1234567890', length=10, max_length=20, prefix='', unique=True),
        ),
    ]
