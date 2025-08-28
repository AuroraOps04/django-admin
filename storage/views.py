import hashlib

from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from storage.models import UploadFile
from storage.serializers import UploadFileSerializer


# Create your views here.


class UploadFileViewSet(ModelViewSet):
    queryset = UploadFile.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UploadFileSerializer

    def create(self, request, *args, **kwargs):
        file = request.data.get("file")
        if file is None:
            raise ValidationError("请选择文件")
        md5 = hashlib.md5(file.read()).hexdigest()
        f = UploadFile.objects.filter(md5=md5).first()
        if not f:
            f = UploadFile(file=file)
            f.original_name = file.name
            f.md5 = md5
            f.size = file.size
            f.mimetype = file.content_type
            f.save()
        serializer = UploadFileSerializer(f)
        return Response(serializer.data)
