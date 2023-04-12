from django.http import httpRespose, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import ( Son, Botao, PlayList )
from .serializers import ( UserSerializer, SonSerializer )


@csrf_exempt
def listar_son(request):
    if request.method == 'GET':
        son = Son.objects.all()
        serializer = SonSerializer(son, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.mothod == 'POST':
        dados = JSONParser().parse(request)
        serializer = SonSerializer(data=dados)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
