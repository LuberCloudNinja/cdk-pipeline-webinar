
from argparse import Action
import code

from aws_cdk import (
    Duration,
    Stack,
    aws_codepipeline as codepipeline,
    pipelines as pipelines,
    aws_codepipeline_actions as cpactions,
    aws_secretsmanager as secretmanager,
    SecretValue
)
from os import path
from constructs import Construct
# from executing import Source


class PipelineStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, env, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        source_artifact = codepipeline.Artifact()
        cloud_assembly_artifact = codepipeline.Artifact()

        pipeline = pipelines.CodePipeline(
            self,
            "Pipeline",
            pipeline_name='WebinarPipeline',
            # cloud_assembly_artifact=cloud_assembly_artifact,

            synth=pipelines.ShellStep(
                "Synth",
                # source_artifact=source_artifact,
                # cloud_assembly_artifact=cloud_assembly_artifact,
                input=pipelines.CodePipelineSource.git_hub('LuberCloudNinja/cdk-pipeline-webinar', 'main',
                                                           authentication=SecretValue.secrets_manager(
                                                               'GitHub-token')
                                                           ),
                commands=[
                    "npm install -g aws-cdk",  # Installs the cdk cli on Codebuild
                    # Instructs Codebuild to install required packages
                    "pip install -r requirements.txt",
                    "npx cdk synth"
                ]
            ),

        )
