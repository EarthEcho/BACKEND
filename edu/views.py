from rest_framework.permissions import IsAuthenticated
from .models import ClimateEducation, ClimateFact
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import (
    ClimateEducationSerializer,
    ClimateFactSerializer,
)


class ClimateEducationListView(APIView):
    serializer_class = ClimateEducationSerializer
    # permission_classes = [IsAuthenticated]
    """
    Climate Education View
    """

    def get(self, request):
        climateEducation_list = ClimateEducation.objects.all()
        serializer = ClimateEducationSerializer(
            climateEducation_list, many=True)
        if serializer.data:
            return Response(serializer.data)
        return Response(
            {'Message': 'No Climate Education Found'},
            status=status.HTTP_404_NOT_FOUND
        )


class ClimateEducationDetailUpdateDeleteView(APIView):
    serializer_class = ClimateEducationSerializer
    """
    Climate Education Detail, Update, and Delete View.
    """

    def get_object(self, pk):
        try:
            return ClimateEducation.objects.get(pk=pk)
        except ClimateEducation.DoesNotExist:
            return None

    def get(self, request, pk):
        climateEducation_detail = self.get_object(pk)
        if climateEducation_detail:
            serializer = ClimateEducationSerializer(climateEducation_detail)
            return Response(serializer.data)
        return Response(
            {'Message': 'No Climate Education Found'},
            status=status.HTTP_404_NOT_FOUND
        )

    def put(self, request, pk):
        climateEducation_detail = self.get_object(pk)

        if climateEducation_detail:
            serializer = ClimateEducationSerializer(
                climateEducation_detail, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(
            {'Message': 'No Climate Education Found'},
            status=status.HTTP_404_NOT_FOUND
        )

    def delete(self, request, pk):
        climateEducation_detail = self.get_object(pk)
        if climateEducation_detail:
            climateEducation_detail.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(
            {'Message': 'No Climate Education Found'},
            status=status.HTTP_404_NOT_FOUND
        )


class ClimateFactListView(APIView):
    serializer_class = ClimateFactSerializer
    """
    Climate Fact View
    """

    def get(self, request):
        climateFact_list = ClimateFact.objects.all()
        serializer = ClimateFactSerializer(
            climateFact_list, many=True)
        if serializer.data:
            return Response(serializer.data)
        return Response(
            {'Message': 'No Climate Fact Found'},
            status=status.HTTP_404_NOT_FOUND
        )


class ClimateFactDetailUpdateDeleteView(APIView):
    serializer_class = ClimateFactSerializer
    """
    Climate Fact Detail, Update, and Delete View.
    """

    def get_object(self, pk):
        try:
            return ClimateFact.objects.get(pk=pk)
        except ClimateFact.DoesNotExist:
            return None

    def get(self, request, pk):
        climateFact_detail = self.get_object(pk)
        if climateFact_detail:
            serializer = ClimateFactSerializer(climateFact_detail)
            return Response(serializer.data)
        return Response(
            {'Message': 'No Climate Fact Found'},
            status=status.HTTP_404_NOT_FOUND
        )

    def put(self, request, pk):
        climateFact_detail = self.get_object(pk)

        if climateFact_detail:
            serializer = ClimateFactSerializer(
                climateFact_detail, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(
            {'Message': 'No Climate Fact Found'},
            status=status.HTTP_404_NOT_FOUND
        )

    def delete(self, request, pk):
        climateFact_detail = self.get_object(pk)
        if climateFact_detail:
            climateFact_detail.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(
            {'Message': 'No Climate Fact Found'},
            status=status.HTTP_404_NOT_FOUND
        )


climateFact_list = ClimateFactListView.as_view()
climateEducation_list = ClimateEducationListView.as_view()
climateEducation_detail_update_delete = ClimateEducationDetailUpdateDeleteView.as_view()
climateFact_detail_update_delete = ClimateFactDetailUpdateDeleteView.as_view()
