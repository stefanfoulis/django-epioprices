#-*- coding: utf-8 -*-
from django.shortcuts import redirect
from django.utils.encoding import iri_to_uri

from urlparse import urljoin


class HTTPSMiddleware(object):
    def process_request(self, request):
        if not request.is_secure():
            location = request.get_full_path()
            current_uri = 'https://%s%s' % (request.get_host(), request.path)
            location = urljoin(current_uri, location)
            url = iri_to_uri(location)
            return redirect(url, permanent=True)
