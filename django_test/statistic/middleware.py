from .models import UserStat



class SaveHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request_headers = request.headers
        UserStat.objects.create(headers=request_headers)
        response = self.get_response(request)
        print(request_headers)
        return response
