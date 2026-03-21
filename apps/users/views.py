from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from ..bot.services.user_services import get_or_create_user
from ..bot.bot import hendle_update

class TelegramWebhookView(APIView):
    
    def post(self, request: Request):
        data = request.data
        hendle_update(data)
        return Response('ok')
    