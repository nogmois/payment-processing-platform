# Generated by Django 4.2.3 on 2023-08-02 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_kyc'),
    ]

    operations = [
        migrations.AddField(
            model_name='kyc',
            name='identity_image',
            field=models.ImageField(blank=True, null=True, upload_to='kyc'),
        ),
    ]
