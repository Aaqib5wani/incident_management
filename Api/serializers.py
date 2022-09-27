from rest_framework import serializers
from .models import Create_incident

class Create_incidentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Create_incident
		fields = ['incident_number','name','description','priority','incident_status']





