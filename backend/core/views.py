from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from decouple import config
import openai

openai.api_key = config("OPENAI_API_KEY")

class SummarizeView(APIView):
    def post(self, request):
        text = request.data.get("text", "")
        if not text:
            return Response({"error": "Missing 'text' field"}, status=400)

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": text}
                ]
            )
            summary = response.choices[0].message.content.strip()
            return Response({"summary": summary})
        except Exception as e:
            return Response({"error": str(e)}, status=500)
