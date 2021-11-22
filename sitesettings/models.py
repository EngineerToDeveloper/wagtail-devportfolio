from django.db import models
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.images.edit_handlers import ImageChooserPanel 
from wagtail.admin.edit_handlers import FieldPanel

@register_setting
class SocialMediaSettings(BaseSetting):
    class Meta:
        verbose_name = 'social media accounts'

    facebook = models.URLField(
        help_text='Your Facebook page URL'
    )
    linkedin = models.URLField(
        help_text='Your Linkedin page URL'
    )
    youtube = models.URLField(
        help_text='Your YouTube channel or user account URL'
    )

    panels = [
        FieldPanel("facebook"),
        FieldPanel("linkedin"),
        FieldPanel("youtube"),
    ]

@register_setting
class SiteSettings(BaseSetting):
    class Meta:
        verbose_name = 'general site settings'

    site_name = models.CharField(
        max_length=255,
        help_text="Name of your website."
    )
    site_logo = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        related_name='+',
        help_text='',
        on_delete=models.SET_NULL,
    )

    panels = [
        FieldPanel("site_name"),
        ImageChooserPanel("site_logo"),
    ]
    