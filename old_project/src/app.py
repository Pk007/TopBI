"""
"""

from wheezy.http import WSGIApplication
from wheezy.http.middleware import http_cache_middleware_factory
from wheezy.web.middleware import bootstrap_defaults
from wheezy.web.middleware import http_error_middleware_factory
from wheezy.web.middleware import path_routing_middleware_factory

## project
from config import options ## config
from urls import all_urls ## urls
from database import init_db ## init databases

init_db()

main = WSGIApplication(
    middleware=[
        bootstrap_defaults(url_mapping=all_urls),
        http_cache_middleware_factory,
        http_error_middleware_factory,
        path_routing_middleware_factory
    ],
    options=options)


if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    try:
        print('Visit http://localhost:8080/')
        make_server('', 8080, main).serve_forever()
    except KeyboardInterrupt:
        pass
    print('\nThanks!')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: