# Django imports
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
# Rest Framework  imports
from rest_framework import generics, status
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
# project imports

from api.serializers import (NewsSerializer, 
                            ListTypeSerializer,
                            SemiFullCardSerializer,
                            ReadMoreNewsSerializer
                            )
from api.models import TestBlog, News

from datetime import timedelta


class LatestNewsView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        # "news_index" is the starting index of the object to be fetched
        news_index = self.kwargs.get("rank") - 1
        fetch_threshold = news_index + 1
        # order all the objects by id in descending order
        queryset = News.objects.order_by(
            "-date_posted")[news_index:fetch_threshold]
        news_data = SemiFullCardSerializer(queryset, many=True)
        if news_data.data != []:
            return Response(news_data.data, status=status.HTTP_200_OK)
        return Response({"error": "news not found"},
                        status=status.HTTP_404_NOT_FOUND)


class TrendingNewsView(RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        # "news_index" is the starting index of the object to be fetched
        news_index = 4
        fetch_threshold = news_index + 5
        # order all the objects by id in descending order
        queryset = News.objects.order_by(
            "-date_posted")[news_index:fetch_threshold]
        news_data = SemiFullCardSerializer(queryset, many=True)
        if news_data.data != []:
            return Response(news_data.data, status=status.HTTP_200_OK)
        return Response({"error": "news not found"},
                        status=status.HTTP_404_NOT_FOUND)


# List all the Top of the week news
class TopOfTheWeekView(RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        queryset = News.objects.exclude(top_of_the_week=False).filter(
            date_posted__gte=timezone.now() -
            timedelta(days=7)).order_by("-date_posted")[0:15]
        serializer = SemiFullCardSerializer(queryset, many=True)
        if serializer.data != []:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "News Not Found"},
                        status=status.HTTP_404_NOT_FOUND)


class EditorsPickView(RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        queryset = News.objects.exclude(editors_pick=False)
        news = queryset.order_by("-date_posted")[0:10]
        serializer = SemiFullCardSerializer(news, many=True)
        if serializer.data != []:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "News Not Found"},
                        status=status.HTTP_404_NOT_FOUND)


class CategorizedNewsView(RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        queryset = News.objects.filter(category__contains=self.kwargs.get(
            "category")).order_by("-date_posted")[10:17]
        serializer = SemiFullCardSerializer(queryset, many=True)
        if serializer.data != []:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "News Not Found"},
                        status=status.HTTP_404_NOT_FOUND)
     


class AlsoReadNewsView(RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        if self.kwargs.get("index") >= 10:
            queryset = News.objects.filter(category=self.kwargs.get(
                "category")).filter(id__lt = self.kwargs.get("index")).order_by("-date_posted")[0:6]
        else:
             queryset = News.objects.filter(category=self.kwargs.get(
                "category")).filter(id__gt = self.kwargs.get("index")).order_by("-date_posted")[0:6]
        serializer = SemiFullCardSerializer(queryset, many=True)
        if serializer.data != []:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "News Not Found"},
                        status=status.HTTP_404_NOT_FOUND)



class ReadMoreView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        if self.kwargs.get("index") >= 10:
            queryset = News.objects.filter(category=self.kwargs.get(
                "category")).filter(id__lt = self.kwargs.get("index")).order_by("-date_posted")[0:6]
        else:
             queryset = News.objects.filter(category=self.kwargs.get(
                "category")).filter(id__gt = self.kwargs.get("index")).order_by("-date_posted")[0:6]
        serializer = SemiFullCardSerializer(queryset, many=True)
        if serializer.data != []:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "News Not Found"},
                        status=status.HTTP_404_NOT_FOUND)



class TabLatestNewsView(RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        queryset = News.objects.filter(category=self.kwargs.get("category")).order_by("-date_posted")[0:6]
        serializer = SemiFullCardSerializer(queryset, many=True)
        if serializer !=[]:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response ({"error":"News Not Found"}, status=status.HTTP_404_NOT_FOUND)



class TabTopNewsView(RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        queryset = News.objects.filter(category=self.kwargs.get("category")).order_by("-date_posted")[0:6]
        serializer = SemiFullCardSerializer(queryset, many=True)
        if serializer !=[]:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response ({"error":"News Not Found"}, status=status.HTTP_404_NOT_FOUND)

class TabBotNewsView(RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        queryset = News.objects.filter(category=self.kwargs.get("category")).order_by("-date_posted")[0:10]
        serializer = SemiFullCardSerializer(queryset, many=True)
        if serializer !=[]:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response ({"error":"News Not Found"}, status=status.HTTP_404_NOT_FOUND)

class OtherNewsView(RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        queryset = News.objects.filter(category=self.kwargs.get("category")).order_by("-date_posted")[0:10]
        serializer = SemiFullCardSerializer(queryset, many=True)
        if serializer !=[]:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response ({"error":"News Not Found"}, status=status.HTTP_404_NOT_FOUND)












class NewsView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        # "news_index" is the starting index of the object to be fetched
        news_index = self.kwargs.get("index") - 1
        # " fetch_threshold" is the ending index to be fetched. "fetch_threshold" is only
        #   incremented by 1 since we only want to fetch 1 object;
        fetch_threshold = news_index + 1
        # order all the objects by id in descending order
        queryset = News.objects.order_by("-id")[news_index:fetch_threshold]
        news_data = SemiFullCardSerializer(queryset, many=True)
        # return status=200 if the data exist and 404 if doesn't exist
        if news_data.data != []:
            return Response(news_data.data, status=status.HTTP_200_OK)
        return Response({"error": "news not found"},
                        status=status.HTTP_404_NOT_FOUND)



class NewsDetails(RetrieveAPIView):
    queryset = News.objects.all()

    def get(self, request, pk, *args, **kwargs):
        news = get_object_or_404(News, id=self.kwargs.get("pk"))
        serializer = NewsSerializer(news)
        return Response(serializer.data)


class ScienceLatestView(RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        queryset = News.objects.filter(category__contains="science")
        news = queryset.order_by("-date_posted")[0:6]
        serializer = SemiFullCardSerializer(news, many=True)
        return Response(serializer.data)

