from aws_cdk import (
    Duration,
    Stack,
    aws_s3 as s3,
)

from constructs import Construct


class S3Bucket(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        s3.Bucket(self, "Create-cutcket",
                  bucket_name="cloud-ninja-cdk-pipeline")
