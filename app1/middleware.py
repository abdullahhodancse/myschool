from django.utils.deprecation import MiddlewareMixin

class SimpleMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print("Before View")

    def process_response(self, request, response):
        print("After View")
        return response