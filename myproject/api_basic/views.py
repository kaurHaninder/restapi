from django.shortcuts import render
from .models import Article
from .serializers import ArticleSerializer
from rest_framework import generics
# Create your views here.

class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article
    serializer_class = ArticleSerializer




# def article_list(request):
#     if request.method == "GET":
#         article = Article.objects.all()
#         serializer = ArticleSerializer(article , many=True)
#         return JsonResponse(serializer ,safe=False)
#     elif request.method == "POST":
#         data = JSONParser.parse(request)
#         serializer = ArticleSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)