#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#


from enum import Enum
from typing import List
from pydantic import BaseModel

class ConnectorTypeEnum(str, Enum):
    source = "source"
    destination = "destination"

class ReleaseStageEnum(str, Enum):
    alpha = "alpha"
    beta = "beta"
    generally_available = "generally_available"

class ConnectorQAReport(BaseModel):
    connector_type: ConnectorTypeEnum
    connector_name: str
    docker_image_tag: str
    release_stage: ReleaseStageEnum
    is_on_cloud: bool
    latest_build_is_successful: bool
    documentation_is_available: bool
    number_of_connections: int 
    number_of_users: int
    sync_success_rate: float

class QAReport(BaseModel):
    connectors_qa_report: List[ConnectorQAReport]
