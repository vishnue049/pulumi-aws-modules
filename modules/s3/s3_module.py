import pulumi
from pulumi_aws import s3

def create_s3_bucket(name: str) -> s3.Bucket:
    """
    Creates an S3 bucket with the specified name.

    Args:
        name (str): The name of the S3 bucket.

    Returns:
        s3.Bucket: The created S3 bucket resource.
    """
    bucket = s3.Bucket(name)
    return bucket
