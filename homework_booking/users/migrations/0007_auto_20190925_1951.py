# Generated by Django 2.2.5 on 2019-09-25 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20190925_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='cleaner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='booked_appointment', to='users.Cleaner'),
        ),
    ]