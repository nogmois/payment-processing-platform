# Generated by Django 4.2.3 on 2023-08-02 14:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shortuuid.django_fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('account_balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('account_number', shortuuid.django_fields.ShortUUIDField(alphabet='1234567890', length=10, max_length=25, prefix='217', unique=True)),
                ('account_id', shortuuid.django_fields.ShortUUIDField(alphabet='1234567890', length=7, max_length=25, prefix='DEX', unique=True)),
                ('pin_number', shortuuid.django_fields.ShortUUIDField(alphabet='1234567890', length=4, max_length=7, prefix='', unique=True)),
                ('ref_code', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefgh1234567890', length=10, max_length=7, prefix='', unique=True)),
                ('account_status', models.CharField(choices=[('active', 'Active'), ('in-active', 'In-active')], default='in-active', max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('kyc_submitted', models.BooleanField(default=False)),
                ('kyc_confirmed', models.BooleanField(default=False)),
                ('recommended_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='recommended_by', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
