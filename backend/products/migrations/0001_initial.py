# Generated by Django 4.2.4 on 2024-04-07 11:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0003_rename_name_project_projectname'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('reference', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('last_modified_date', models.DateTimeField(auto_now=True)),
                ('image_product', models.BinaryField(blank=True, null=True)),
                ('permission_level', models.CharField(max_length=20)),
                ('previous_project_id', models.IntegerField(blank=True, null=True)),
                ('change_date', models.DateTimeField(blank=True, null=True)),
                ('change_reason', models.TextField(blank=True, null=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_products', to=settings.AUTH_USER_MODEL)),
                ('modifier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modified_products', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='projects.project')),
            ],
        ),
    ]