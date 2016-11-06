from django.conf import settings
def recaptcha(request):
    """context processor to add alerts to the site"""

    return {
        'GOOGLE_RECAPTCHA_SITE_KEY': settings.GOOGLE_RECAPTCHA_SITE_KEY,
    }