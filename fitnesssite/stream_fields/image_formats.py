from wagtail.images.formats import Format, register_image_format
from wagtail.images.models import Filter

webp_image_format_specs: Filter = Filter('width-800|format-webp')


register_image_format(
    Format(
        'webp',
        'Compressed .WEBP image',
        'richtext-image webp',
         webp_image_format_specs
    )
)