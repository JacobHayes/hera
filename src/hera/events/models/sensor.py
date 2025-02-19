# generated by datamodel-codegen:
#   filename:  argo-workflows-3.4.4.json

from __future__ import annotations

from typing import Optional

from hera.shared._base_model import BaseModel
from pydantic import Field

from .io.argoproj.events import v1alpha1
from .io.k8s.apimachinery.pkg.apis.meta import v1


class DeleteSensorResponse(BaseModel):
    pass


class LogEntry(BaseModel):
    dependency_name: Optional[str] = Field(
        default=None, alias="dependencyName", title="optional - trigger dependency name"
    )
    event_context: Optional[str] = Field(default=None, alias="eventContext", title="optional - Cloud Event context")
    level: Optional[str] = None
    msg: Optional[str] = None
    namespace: Optional[str] = None
    sensor_name: Optional[str] = Field(default=None, alias="sensorName")
    time: Optional[v1.Time] = None
    trigger_name: Optional[str] = Field(default=None, alias="triggerName", title="optional - any trigger name")


class CreateSensorRequest(BaseModel):
    create_options: Optional[v1.CreateOptions] = Field(default=None, alias="createOptions")
    namespace: Optional[str] = None
    sensor: Optional[v1alpha1.Sensor] = None


class SensorWatchEvent(BaseModel):
    object: Optional[v1alpha1.Sensor] = None
    type: Optional[str] = None


class UpdateSensorRequest(BaseModel):
    name: Optional[str] = None
    namespace: Optional[str] = None
    sensor: Optional[v1alpha1.Sensor] = None
