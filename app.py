#!/usr/bin/env python3
import os

import aws_cdk as cdk

from pipelines_webinar.pipelines_webinar_stack import PipelinesWebinarStack
from pipelines_webinar.pipeline_stack import PipelineStack

app = cdk.App()
PipelinesWebinarStack(app, "PipelinesWebinarStack")

PipelineStack(app, 'PipelineStack', env={
              'account': "721918345279", 'region': 'us-east-1'})

app.synth()
