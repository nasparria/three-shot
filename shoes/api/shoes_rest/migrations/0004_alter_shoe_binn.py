# Generated by Django 4.0.3 on 2022-07-28 00:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shoes_rest', '0003_rename_bin_shoe_binn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoe',
            name='binn',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='shoes', to='shoes_rest.binvo'),
        ),
    ]