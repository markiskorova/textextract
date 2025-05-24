from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Submission
from decouple import config
from openai import OpenAI
import os


# Load your API key from the environment
client = OpenAI(api_key=config("OPENAI_API_KEY"))

class SummarizeView(APIView):
    def post(self, request):
        user_input = request.data.get("text")
        if not user_input:
            return Response({"error": "No input text provided."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Call OpenAI Chat Completion API
            chat_response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": f"Summarize this:\n\n{user_input}"}
                ]
            )

            summary = chat_response.choices[0].message.content

            # Save to DB
            Submission.objects.create(user_input=user_input, summary=summary)

            return Response({"summary": summary}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
