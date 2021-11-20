from django.db import models

from wagtail.core.models import Page
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel 
from streamfieldblocks.models import (
    ResponsiveImageBlock, 
    CardBlock, 
    SimpleRichTextBlock, 
    CarouselBlock,
    FlushListBlock,
)

class BlogListingPage(Page):
    background_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        related_name='+',
        help_text='Header background image',
        on_delete=models.SET_NULL,
    )

    headline_text = models.CharField(
        max_length=70,
        blank=True, 
        help_text='Blog listing page header text.'
    )
        
    content_panels = Page.content_panels + [
        ImageChooserPanel("background_image"), 
        FieldPanel("headline_text"),
    ]

    subpage_types = ["blog.BlogPage", ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        context['blogpages'] = self.get_children().live().order_by('-first_published_at')
        return context


class BlogPage(Page):
    date = models.DateField("Article Date")
    intro = models.TextField("Introduction")
    featured = models.BooleanField(default=False)
    main_content = StreamField([
        ('responsive_image', ResponsiveImageBlock()),
        ('card', CardBlock()),
        ('carousel', CarouselBlock()),
        ('flush_list', FlushListBlock()),
        ('richtext', SimpleRichTextBlock()),
    ], blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('featured'),
        FieldPanel('intro'),
        StreamFieldPanel('main_content'),
    ]

    subpage_types = []
