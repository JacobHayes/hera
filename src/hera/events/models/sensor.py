# generated by datamodel-codegen:
#   filename:  https://raw.githubusercontent.com/argoproj/argo-workflows/v3.4.4/api/openapi-spec/swagger.json
#   timestamp: 2023-02-08T02:49:24+00:00

from __future__ import annotations

from typing import Optional

from pydantic import Field

from hera.events._base_model import BaseModel

from .io.argoproj.events import v1alpha1
from .io.k8s.apimachinery.pkg.apis.meta import v1


class DeleteSensorResponse(BaseModel):
    pass


class LogEntry(BaseModel):
    dependency_name: Optional[str] = Field(None, alias='dependencyName', title='optional - trigger dependency name')
    event_context: Optional[str] = Field(None, alias='eventContext', title='optional - Cloud Event context')
    level: Optional[str] = None
    msg: Optional[str] = None
    namespace: Optional[str] = None
    sensor_name: Optional[str] = Field(None, alias='sensorName')
    time: Optional[v1.Time] = None
    trigger_name: Optional[str] = Field(None, alias='triggerName', title='optional - any trigger name')


class CreateSensorRequest(BaseModel):
    create_options: Optional[v1.CreateOptions] = Field(None, alias='createOptions')
    namespace: Optional[str] = None
    sensor: Optional[v1alpha1.Sensor] = None


class SensorWatchEvent(BaseModel):
    object: Optional[v1alpha1.Sensor] = None
    type: Optional[str] = None


class UpdateSensorRequest(BaseModel):
    name: Optional[str] = None
    namespace: Optional[str] = None
    sensor: Optional[v1alpha1.Sensor] = None