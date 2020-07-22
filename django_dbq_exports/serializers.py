from rest_framework import serializers
from django_dbq_exports.models import Export


class ExportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Export
        fields = [
            "id",
            "created",
            "modified",
            "started",
            "completed",
            "runtime",
            "export_type",
            "priority",
            "status",
            "status_detail",
            "result_reference",
            "export_params",
        ]
        read_only_fields = [
            "id",
            "created",
            "modified",
            "started",
            "completed",
            "runtime",
            "status",
            "status_detail",
            "result_reference",
        ]
