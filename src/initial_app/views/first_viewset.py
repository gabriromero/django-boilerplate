from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

class FirstViewSet(ViewSet):
    """
    A simple first ViewSet
    """

    def list(self, request):
        data = {
            "message": "Hello World!"
        }

        return Response(data, status=status.HTTP_200_OK)
