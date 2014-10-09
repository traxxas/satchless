from django.conf.urls import patterns, url, include
import warnings

from . import app

warnings.warn('satchless.product.urls is deprecated, use'
              ' satchless.product.app.product_app.urls instead')

urlpatterns = patterns('',
    url(r'', include(app.product_app.urls)),
)
