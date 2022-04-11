from constructs import Construct
from aws_cdk import (
    Duration,
    Stage,
)
from .pipelines_webinar_stack import PipelinesWebinarStack


class WebServiceStage(Stage):

    def __init__(self, scope: Construct, construct_id: str, env, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        service = PipelinesWebinarStack(self, 'Webservice')

        self.url_output = service.url_output
