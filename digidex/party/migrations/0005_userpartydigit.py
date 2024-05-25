# Generated by Django 5.0.2 on 2024-05-25 02:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digitization', '0011_remove_digitalobject_content_type_and_more'),
        ('party', '0004_alter_userparty_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPartyDigit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('digit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='party', to='digitization.digitalobject')),
                ('user_party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='digits', to='party.userparty')),
            ],
        ),
    ]
