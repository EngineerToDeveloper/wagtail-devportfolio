from django.db import models

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class ResponsiveImageBlock(ImageChooserBlock):
    class Meta:
        icon = "image"
        template = "streamfieldblocks/responsive_image_block.html"


class CardBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=False)
    title = blocks.CharBlock()
    body = blocks.TextBlock()
    page_link = blocks.PageChooserBlock()

    class Meta:
        icon = "placeholder"
        template = "streamfieldblocks/card_block.html"


class SimpleRichTextBlock(blocks.StructBlock):
    richtext = blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'link', 'ol', 'ul'])
    
    class Meta:
        icon = "pilcrow"
        template = "streamfieldblocks/simple_richtext_block.html"

class CarouselBlock(blocks.StreamBlock):
    image = ImageChooserBlock()

    class Meta:
        icon = "cog"
        template = "streamfieldblocks/carousel_block.html"