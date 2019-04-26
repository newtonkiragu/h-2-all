from django.http import JsonResponse
from rest_framework.views import APIView
from .handlers import default_handler


class CallbackHandler(APIView):
    message_handler = default_handler()

    def post(self, request):
        response = self.message_handler.receive_message(request)
        return JsonResponse(response)
