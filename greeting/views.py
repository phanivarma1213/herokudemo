# views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import SFDocSyncSerializer
import psycopg2
from django.conf import settings

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def sync_from_salesforce(request):
    serializer = SFDocSyncSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.validated_data

        try:
            # Heroku PostgreSQL credentials from settings.py
            conn = psycopg2.connect(
                host="c5cnr847jq0fj3.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com",
                database="dfqli4s83tjnha",
                user="udm1fo5lg3lana",
                password="p4d28ab0724c7e24a34d5eb9d84756b0192125cb9088b89577b1fa545e59a85bb",
                port="5432"
            )
            cursor = conn.cursor()
            query = """
                INSERT INTO sf_doc_sync (doc_ID, doc_endpoint, inserted_by_user, SF_doc_parent_ID, SF_doc_parent_object_ID)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (
                data['doc_ID'],
                data['doc_endpoint'],
                data['inserted_by_user'],
                data['SF_doc_parent_ID'],
                data['SF_doc_parent_object_ID']
            ))
            conn.commit()
            cursor.close()
            conn.close()

            return Response({"message": "Data posted successfully"}, status=201)

        except Exception as e:
            return Response({"error": str(e)}, status=500)

    return Response(serializer.errors, status=400)

