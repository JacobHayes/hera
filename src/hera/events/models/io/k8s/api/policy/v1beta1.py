# generated by datamodel-codegen:
#   filename:  argo-workflows-3.4.4.json

from __future__ import annotations

from typing import Optional

from pydantic import Field

from hera.shared._pydantic import BaseModel

from ...apimachinery.pkg.apis.meta import v1
from ...apimachinery.pkg.util import intstr


class PodDisruptionBudgetSpec(BaseModel):
    max_unavailable: Optional[intstr.IntOrString] = Field(
        default=None,
        alias="maxUnavailable",
        description=(
            'An eviction is allowed if at most "maxUnavailable" pods selected by "selector" are unavailable after the'
            " eviction, i.e. even in absence of the evicted pod. For example, one can prevent all voluntary evictions"
            ' by specifying 0. This is a mutually exclusive setting with "minAvailable".'
        ),
    )
    min_available: Optional[intstr.IntOrString] = Field(
        default=None,
        alias="minAvailable",
        description=(
            'An eviction is allowed if at least "minAvailable" pods selected by "selector" will still be available'
            " after the eviction, i.e. even in the absence of the evicted pod.  So for example you can prevent all"
            ' voluntary evictions by specifying "100%".'
        ),
    )
    selector: Optional[v1.LabelSelector] = Field(
        default=None,
        description=(
            "Label query over pods whose evictions are managed by the disruption budget. A null selector selects no"
            " pods. An empty selector ({}) also selects no pods, which differs from standard behavior of selecting all"
            " pods. In policy/v1, an empty selector will select all pods in the namespace."
        ),
    )
