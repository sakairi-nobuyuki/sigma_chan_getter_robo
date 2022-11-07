# coding: utf-8

import boto3

from sigma_chan_getter_robo.post_process.io import AbstractStorage


class S3Storage(AbstractStorage):
    def __init__(
        self,
        type: str,
        project_name: str,
        bucket_name: str,
        endpoint_url: str,
        access_id: str,
        access_key: str,
        region_name: str,
    ) -> None:
        if type != "s3":
            raise NotImplementedError(f"{type} is not implemented.")
        self.s3_resource = boto3.resource(
            service_name="s3",
            endpoint_url=endpoint_url,
            aws_access_key_id=access_id,
            aws_secret_access_key=access_key,
            region_name=region_name,
        )
        self.bucket_name = bucket_name
        self.bucket = self.s3_resource.Bucket(bucket_name)

    def save_data(self, data: bytes, file_name: str) -> bool:
        s3_object = self.s3_resource.Object(self.bucket_name, file_name)
        if s3_object.put(Body=data):
            return True
        else:
            return False

    def save_json(self, src: dict) -> bool:
        return super().save_json(src)
