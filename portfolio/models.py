from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel

class PortfolioPage(Page):
    def get_context(self, request):
        context = super().get_context(request)
        context['project_pages'] = self.get_children().live().order_by('-first_published_at')
        return context

class ProjectPage(Page):
    project_title = models.CharField(
        max_length=150
    )
    date = models.DateField("Project Date")
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
        SnippetChooserPanel('testimonials'),
    ]
