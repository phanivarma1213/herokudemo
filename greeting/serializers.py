# serializers.py
from rest_framework import serializers

class SFDocSyncSerializer(serializers.Serializer):
    doc_ID = serializers.CharField()
    doc_endpoint = serializers.CharField()
    inserted_by_user = serializers.CharField()
    SF_doc_parent_ID = serializers.CharField()
    SF_doc_parent_object_ID = serializers.CharField()