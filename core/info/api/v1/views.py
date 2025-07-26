from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

class CreateNewLinkAPIView(APIView):
    def post(self, request):
        serializer = LinkSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            print(validated_data)
            return Response({"message": "اطلاعات با موفقیت دریافت شد."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)












