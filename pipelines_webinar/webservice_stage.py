from constructs import Construct
from aws_cdk import (
    Duration,
    Stage,
)
from .pipelines_webinar_stack import PipelinesWebinarStack
from .s3_bucket import S3Bucket


class WebServiceStage(Stage):

    def __init__(self, scope: Construct, construct_id: str, env, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        service = PipelinesWebinarStack(self, 'Webservice')
        # s3_bucket = S3Bucket(self, 'S3-Bucket-1')

        self.url_output = service.url_output
