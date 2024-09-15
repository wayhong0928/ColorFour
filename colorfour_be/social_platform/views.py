from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Comment
from .serializers import CommentSerializer

class CommentCreateView(APIView):
    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # 保存當前使用者
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # 打印出錯誤信息，幫助調試
            print("序列化驗證錯誤:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        