from wagtail.images.formats import Format, register_image_format
from wagtail.images.models import Filter




webp_image_format_specs: Filter = Filter('width-800|format-webp')

class LazyLoadedFormat(Format):
    '''
    overriding the default Format Object,
    and addding loading='lazy' to extra_attributes 
    from the base class
    '''
    def image_to_html(self, image, alt_text, extra_attributes=None):
        lazy_extra_attributes = {
            'loading' : 'lazy'
        }
        return super(LazyLoadedFormat,self).image_to_html(image, alt_text, extra_attributes=lazy_extra_attributes)


register_image_format(
    LazyLoadedFormat(
        'webp',
        'Lazy Loaded .webp image',
        'richtext-image webp',
        webp_image_format_specs
    )
)