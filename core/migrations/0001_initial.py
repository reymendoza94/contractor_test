# Generated by Django 4.2.3 on 2023-07-28 02:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label_name', models.CharField(max_length=200)),
                ('label_type', models.CharField(choices=[('simple', 'simple'), ('attribute_based', 'attribute based'), ('multi_level', 'multi level')], max_length=20)),
                ('assignament', models.BooleanField(default=False)),
                ('exclusibity', models.BooleanField(default=False)),
                ('level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.label')),
            ],
            options={
                'verbose_name': 'Label',
                'verbose_name_plural': 'Labels',
            },
        ),
    ]
