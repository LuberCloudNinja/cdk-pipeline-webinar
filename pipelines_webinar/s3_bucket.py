from aws_cdk import (
    Duration,
    Stack,
    aws_s3 as s3,
)

from constructs import Construct


class S3Bucket(Stack):

    def __init__(self, scope: Construct, construct_id: str, env, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        s3.Bucket(self, "Create-cutcket",
                  bucket_name="cloudNinja-cdk-pipeline")
