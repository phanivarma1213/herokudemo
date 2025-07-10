from rest_framework.views import APIView
from rest_framework.response import Response

class GreetingView(APIView):
    def post(self, request):
        name = request.data.get("name")
        dept = request.data.get("department")
        exp = request.data.get("experience")
        msg = f"Hi {name}, thanks for the services of nearly {exp} years in the {dept} department. Looking forward to you!"
        return Response({"message": msg})