import csv
import io

from django.forms import model_to_dict
from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework.renderers import TemplateHTMLRenderer
import pusher
from rest_framework.viewsets import ModelViewSet

from codes.models import Codes, ICD
from codes.Serializers import SaveCodesSerializer, GetCodesSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
from .paginations import CustomPagination

pusher_client = pusher.Pusher(
    app_id='1151410',
    key='f0870f9290a23dc9e32c',
    secret='6104f860e79b2589cd4a',
    cluster='mt1',
    ssl=True
)


def saveToDataBase(codes=None, icd_id=None) -> object:
    sending = {
        'category_code': codes[0],
        'diagnosis_code': codes[1],
        'full_code': codes[2],
        'ab_description': codes[3],
        'full_description': codes[4],
        'category_title': codes[5],
        'ICD': icd_id
    }
    serializer = SaveCodesSerializer(data=sending)
    if serializer.is_valid():
        serializer.save()


def createGetICD():
    icd_code = ICD.objects.all().values().first()
    if not icd_code:
        icd_code = ICD(name='ICD-10')
        icd_code.save()
        return model_to_dict(icd_code)['id']
    return icd_code['id']


class FileUpload(APIView):
    # queryset = User.objects.all()
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        return Response({}, template_name='upload.html')

    def post(self, request):
        icd_id = createGetICD()
        try:
            for chunk in pd.read_csv(request.FILES['csv_file'].file, chunksize=100000, header=None):
                chunk_list = chunk.values.tolist()
                for i, item in enumerate(chunk_list):
                    saveToDataBase(item, icd_id)
            return Response({'status': 'success'}, template_name='upload.html')
        except Exception as e:
            print(e)
            return Response({'status': 'failed', 'message': e}, template_name='upload.html',
                            status=status.HTTP_400_BAD_REQUEST)


class CodeListViewSet(ModelViewSet):
    serializer_class = GetCodesSerializer
    pagination_class = CustomPagination

    def get_object(self):
        return get_object_or_404(Codes, id=self.request.query_params.get("id"))

    def get_queryset(self):
        return Codes.objects.all()

    def perform_destroy(self, instance):
        instance.delete()
        instance.save()

    def list(self, request, *args, **kwargs):
        icd_name = ''
        if 'ICD' in request.GET:
            icd_name = request.GET['ICD']

        queryset = self.filter_queryset(Codes.objects.filter(ICD__name=icd_name))

        try:
            page = self.paginate_queryset(queryset)
        except Exception as e:
            page = []
            data = page
            return Response({
                "status": status.HTTP_404_NOT_FOUND,
                "message": 'No more record.',
                "data": data
            })

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            data = serializer.data
            return self.get_paginated_response(data)

        return Response({
            "status": status.HTTP_200_OK,
            "message": 'Code records.',
            "data": page
        })



