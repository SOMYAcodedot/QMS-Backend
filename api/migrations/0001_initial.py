# Generated by Django 5.1.1 on 2024-10-04 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=50)),
                ('received_date', models.DateTimeField(auto_now_add=True)),
                ('quality_status', models.CharField(max_length=50)),
                ('rejected_reason', models.TextField(blank=True, null=True)),
            ],
        ),
    ]