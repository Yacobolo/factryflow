# schemas.py

from typing import List, Optional

from ninja import ModelSchema
from pydantic.fields import Field
from api.utils.generate_custom_schema import generate_custom_field_schema

from api.models import (
    CustomField,
    Dependency,
    DependencyStatus,
    DependencyTypes,
    Job,
    JobStatus,
    JobType,
    Resource,
    ResourceGroup,
    Task,
    TaskStatus,
    TaskType,
    WeeklyShiftTemplate,
    WorkCenter,
)

# ====================================
# ============ DEPENDENCY ============
# ====================================


class DependencyTypeOut(ModelSchema):
    class Config:
        model = DependencyTypes
        model_fields = ["id", "name"]


class DependencyStatusOut(ModelSchema):
    class Config:
        model = DependencyStatus
        model_fields = ["id", "name"]


class DependencyBaseOut(ModelSchema):
    dependency_status: DependencyStatusOut
    dependency_type: DependencyTypeOut

    job_ids: List[int] = Field([], alias="job_id_list")
    task_ids: List[int] = Field([], alias="task_id_list")

    class Config:
        model = Dependency
        model_fields = "__all__"


# ====================================
# =============== JOB ================
# ====================================


class JobStatusOut(ModelSchema):
    class Config:
        model = JobStatus
        model_fields = ["id", "name"]


class JobTypeOut(ModelSchema):
    class Config:
        model = JobType
        model_fields = ["id", "name"]


class JobBaseOut(ModelSchema):
    job_status: JobStatusOut
    job_type: JobTypeOut
    task_ids: List[int] = Field([], alias="task_id_list")
    dependency_ids: List[int] = Field([], alias="dependency_id_list")
    custom_fields: Optional[generate_custom_field_schema(model_name= 'Job', class_suffix= 'Job')]

    class Config:
        model = Job
        model_exclude = ["dependencies"]


# ====================================
# =============== TASK ===============
# ====================================


class TaskWorkCenterOut(ModelSchema):
    class Config:
        model = WorkCenter
        model_fields = ["id", "name"]


class TaskTypeOut(ModelSchema):
    class Config:
        model = TaskType
        model_fields = ["id", "name"]


class TaskStatusOut(ModelSchema):
    class Config:
        model = TaskStatus
        model_fields = ["id", "name"]


class TaskJobOut(ModelSchema):
    class Config:
        model = Job
        model_fields = ["id", "name", "priority"]


class TaskBaseOut(ModelSchema):
    task_status: TaskStatusOut
    task_type: TaskTypeOut
    work_center: TaskWorkCenterOut
    job: TaskJobOut = None
    predecessor_ids: List[int] = Field([], alias="predecessor_id_list")
    successor_ids: List[int] = Field([], alias="successor_id_list")
    dependency_ids: List[int] = Field([], alias="dependency_id_list")
    custom_fields: Optional[generate_custom_field_schema(model_name= 'Task', class_suffix= 'Task')]

    class Config:
        model = Task
        model_exclude = ["dependencies", "predecessors", "job", "work_center"]


# ====================================
# =============== Resource ===============
# ====================================


class ResourceWeeklyShiftTemplateOut(ModelSchema):
    class Config:
        model = WeeklyShiftTemplate
        model_fields = ["id", "name", "details"]


class ResourceBaseOut(ModelSchema):
    resource_group_ids: List[int] = Field([], alias="resource_group_id_list")
    weekly_shift_template: ResourceWeeklyShiftTemplateOut = None

    class Config:
        model = Resource
        model_exclude = ["resource_groups"]


# ====================================
# =============== ResourceGroup ===============
# ====================================


class ResourceGroupBaseOut(ModelSchema):
    resource_ids: List[int] = Field([], alias="resource_id_list")

    class Config:
        model = ResourceGroup
        model_fields = "__all__"


# ====================================
# =============== WeeklyShiftTemplate ===============
# ====================================


class WeeklyShiftTemplateBaseOut(ModelSchema):
    resource_ids: List[int] = Field([], alias="resource_id_list")

    class Config:
        model = WeeklyShiftTemplate
        model_fields = "__all__"


# ====================================
# =============== CustomField ===============
# ====================================


class CustomFieldBaseOut(ModelSchema):
    class Config:
        model = CustomField
        model_fields = "__all__"
