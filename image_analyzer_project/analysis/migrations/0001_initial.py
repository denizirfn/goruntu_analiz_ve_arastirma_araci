# 2025-04-22 07:54
#yeliz irfan
import analysis.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnalysisResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_type', models.CharField(choices=[('F', 'Dosya'), ('U', 'URL')], max_length=1)),
                ('source_input', models.TextField()),
                ('image_file', models.ImageField(blank=True, null=True, upload_to=analysis.models.get_image_upload_path)),
                ('object_name', models.CharField(max_length=200)),
                ('keywords', models.JSONField()),
                ('summary', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
