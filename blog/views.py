import logging
from django.shortcuts import render
from django.conf import settings

# Create your views here.
logger = logging.getLogger('blog.views')


def globel_setting(request):
    return {'SITE_NAME': settings.SITE_NAME, 'SITE_DESC': settings.SITE_DESC}


def index(req):
    try:
        pass
    except Exception as e:
        logging.error(e)
    return render(req, "index.html" ,locals())
