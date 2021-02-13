import codecs
import csv
from typing import List
from django.core.files.storage import default_storage

from django.db.transaction import atomic
from django.forms import model_to_dict
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response

from ..Serializers import SaveCodesSerializer
from ..models import ICD, Codes


def saveToDataBase(codes=None, icd_id=None) -> object:
    try:
        sending = {
            'category_code': codes[0],
            'diagnosis_code': codes[1],
            'full_code': codes[2],
            'ab_description': codes[3],
            'full_description': codes[4],
            'category_title': codes[5],
            'ICD': icd_id,
        }
        serializer = SaveCodesSerializer(data=sending)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return True
    except Exception as e:
        print(e)
        return False


@atomic
def import_process(file_name):
    icd_id = createGetICD()
    try:
        file = default_storage.open(file_name)
        decoded_file = csv.reader(codecs.iterdecode(file, 'utf-8'))
        for row in decoded_file:
            if not saveToDataBase(row, icd_id):
                return False

        return True
    except Exception as e:
        print(e)
        return False


def createGetICD():
    icd_code = ICD.objects.all().values().first()
    if not icd_code:
        icd_code = ICD(name='ICD-10')
        icd_code.save()
        return model_to_dict(icd_code)['id']
    return icd_code['id']
