# Generated by Django 3.2.9 on 2021-11-20 04:31

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20211120_0421'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfoliopage',
            name='experience',
            field=wagtail.core.fields.StreamField([('Timeline_Block', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=100)), ('text', wagtail.core.blocks.TextBlock()), ('date', wagtail.core.blocks.DateBlock())]))], blank=True, null=True),
        ),
    ]