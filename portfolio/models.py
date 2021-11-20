from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from streamfieldblocks.models import TimelineBlock, ResponsiveImageBlock, SimpleRichTextBlock, CarouselBlock, FlushListBlock
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField

class PortfolioPage(Page):
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

    experience = StreamField([
        ("Timeline_Block", TimelineBlock()),
    ], null=True, blank=True)
    
    content_panels = Page.content_panels + [
        ImageChooserPanel("background_image"), 
        FieldPanel("headline_text"),
        StreamFieldPanel('experience'),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context['project_pages'] = self.get_children().live().order_by('-first_published_at')
        return context

class ProjectPage(Page):
    project_title = models.CharField(
        max_length=150
    )

    date = models.DateField("Project Date")

    intro = models.TextField()
    
    image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        related_name='+',
        help_text='Project Image',
        on_delete=models.SET_NULL,
    )

    content = StreamField([
        ('richtext', SimpleRichTextBlock()),
        ('carousel', CarouselBlock()),
        ('flush_list', FlushListBlock()),
        ('responsive_image', ResponsiveImageBlock()),
    ], null=True, blank=True)

    testimonials = models.ForeignKey(
        'snippets.Testimonial', 
        on_delete=models.SET_NULL, 
        related_name='+',
        help_text="Project Testimonials",
        blank=True,
        null=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("project_title"),
        FieldPanel("date"),
        ImageChooserPanel("image"),
        FieldPanel("intro"), 
        StreamFieldPanel("content"),
        SnippetChooserPanel('testimonials'),
    ]
