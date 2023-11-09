from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework import status

import pandas as pd
import openai

from example.models import Reviews

class UploadFileView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request):
        file = request.FILES.get('file')
        
        if file:
            try:
                data = pd.read_excel(file)
                for index, row in data.iterrows():
                    reviews = Reviews.objects.create(
                        text=row['Review'],
                        punctuation=row['Punctuation'],
                    )
                return Response({'message': 'Archivo Excel procesado correctamente.', 'data': data.to_dict(orient='records')})
            except Exception as e:
                return Response({'message': 'Error al procesar el archivo Excel.', 'error': str(e)})
        else:
            return Response({'message': 'No se ha proporcionado archivo o business_id.'})
        
        


class ChatView(APIView):
    def post(self, request):
        try:
            openai.api_key = "TU_API_KEY"
            message = request.data.get('message')
            chat_completion = openai.Completion.create(
                prompt=message,
                model="text-davinci-003", 
                max_tokens= 200,
                n=3 
            )

            return Response({"response": chat_completion.choices[0].text}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

