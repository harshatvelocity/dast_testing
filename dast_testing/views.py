from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def onlyView(request):
    current_path = request.path
    return Response({'url_path': current_path})