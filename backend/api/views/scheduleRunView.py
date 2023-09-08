from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema
from api.utils.schemas import *


from api.services.scheduleRun import SchduleRunService

schedule_run_service = SchduleRunService()

class ScheduleRunListView(APIView):
    @swagger_auto_schema(
        responses=schedule_run_details_response,
        operation_summary="List all schedule run",
    )
    def get(self, request, format=None):
        """
        List all schedule run
        """
        result = schedule_run_service.get_all_schedule_run(request, format=None)
        return Response(result, status=result["code"])


class CreateScheduleRunView(APIView):
    @swagger_auto_schema(
        request_body=create_update_schedule_run_request_body,
        responses=response_create_update_schedule_run,
        operation_summary="Create schedule run",
    )
    def post(self, request, format=None):
        """
        Create schedule run.
        """
        result = schedule_run_service.create_schedule_run(request, format=None)
        return Response(result, status=result["code"])

class UpdateScheduleRunView(APIView):
    @swagger_auto_schema(
        request_body=create_update_schedule_run_request_body,
        responses=response_create_update_schedule_run,
        operation_summary="upadte schedule run",
    )

    def put(self, request, id, format=None):
        """
        Update schedule run
        """
        result = schedule_run_service.update_schedule_run(request, id, format=None)
        return Response(result, status=result["code"])


class GetScheduleRunByIdView(APIView):
    @swagger_auto_schema(
        responses=schedule_run_details_response,
        operation_summary="get schedule run detail by id",
    )
    
    def get(self, request, id, format=None):
        """
        get schedule run detail by id
        """
        result = schedule_run_service.get_schedule_run_details_by_id(request, id, format=None)
        return Response(result, status=result["code"])
    
    
class DeleteScheduleRunByIdView(APIView):
    @swagger_auto_schema(
        responses=response_delete_schedule_run,
        operation_summary="delete schedule run detail by id",
    )
    def delete(self, request, id, format=None):
        """
        delete schedule run detail by id
        """
        result = schedule_run_service.delete_schedule_run(request, id, format=None)
        return Response(result, status=result["code"])
    