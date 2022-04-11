import code
# from distutils import core
from re import S
from aws_cdk import (
    Duration,
    Stack,
    aws_lambda as lmb,
    aws_apigateway as apigw,
    CfnOutput
)
from os import path
from constructs import Construct


class PipelinesWebinarStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        this_dir = path.dirname(__file__)
        handler = lmb.Function(self, 'function',
                               runtime=lmb.Runtime.PYTHON_3_7,
                               handler='handler.hanlder',
                               code=lmb.Code.from_asset(path.join(this_dir, 'lambda')))

        gw = apigw.LambdaRestApi(self, 'Gateway',
                                 description='Endpoint for a simple Lambda-powered web service',
                                 handler=handler.current_version)

        self.url_output = CfnOutput(self, 'Url',
                                    value=gw.url)
