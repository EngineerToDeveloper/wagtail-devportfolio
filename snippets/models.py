from django.db import models

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.snippets.models import register_snippet

@register_snippet
class Testimonial(models.Model):
    testimony = models.TextField()
    reviewer = models.CharField(max_length=100)

    panels = [
        FieldPanel("testimony"),
        FieldPanel("reviewer"),
    ]

    def __str__(self):
        return f"by {self.reviewer}: {self.testimony[:30]}"