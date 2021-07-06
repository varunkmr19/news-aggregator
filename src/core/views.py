from django.shortcuts import render
from . utils import ZeeNewsScraper, NdtvScraper

# Create your views here.


def index(request):
    ndtv = NdtvScraper()
    zee = ZeeNewsScraper()
    left_stories = ndtv.scrapeWebsite()
    right_stories = zee.scrapeWebsite()

    context = {
        "left_stories": left_stories,
        "right_stories": right_stories
    }

    return render(request, 'core/index.html', context)
