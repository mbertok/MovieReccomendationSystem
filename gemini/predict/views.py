from django.conf import settings
from rest_framework.views import APIView

# Create your views here.


class PredictionView(APIView):
    def post(self, request):
        data = request.data
        sagemaker_url = settings.SAGEMAKER_API_ENDPOINT
        print(data)
        print(sagemaker_url)
