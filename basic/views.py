import json

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response


class wxService(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        """
        @attentions: 获取指定事件状态
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return Response({}, status=status.HTTP_200_OK)
