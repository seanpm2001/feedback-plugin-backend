# Generated by Django 4.1.2 on 2022-11-22 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback_plugin', '0005_add_index_to_rawdata'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='computedserverfact',
            index=models.Index(fields=['key', 'value'], name='feedback_pl_key_7da8a1_idx'),
        ),
        migrations.AddIndex(
            model_name='computeduploadfact',
            index=models.Index(fields=['key', 'value'], name='feedback_pl_key_de007c_idx'),
        ),
    ]
