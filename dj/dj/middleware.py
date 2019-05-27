
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings


class MultipleDomainMiddleware(MiddlewareMixin):

    def process_request(self, request):
        host = request.get_host()
        url_config = getattr(settings, 'MULTIPLE_UFL_CONFIG', None)

        if url_config:
            for key in url_config.keys():
                if key in host:
                    request.urlconf = url_config[key]
