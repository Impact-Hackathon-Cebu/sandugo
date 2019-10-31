from rest_framework import serializers


class AppointmentQuerySerializer(serializers.Serializer):
    medical_institution_id = serializers.IntegerField(required=False)
    donor_id = serializers.IntegerField(required=False)


class EventQuerySerializer(serializers.Serializer):
    medical_institution_id = serializers.IntegerField(required=False)


class IncentiveQuerySerializer(serializers.Serializer):
    medical_institution_id = serializers.IntegerField(required=False)


class DonationQuerySerializer(serializers.Serializer):
    donor_id = serializers.IntegerField(required=False)
