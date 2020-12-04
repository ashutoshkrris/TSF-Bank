# Generated by Django 3.1.4 on 2020-12-02 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20201202_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='credited_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='core.customer'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='debited_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='core.customer'),
        ),
    ]