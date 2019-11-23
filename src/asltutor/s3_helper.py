import boto3
import botocore
from datetime import datetime

from asltutor.main import app

s3 = boto3.client(
    's3',
    aws_access_key_id=app.config['S3_KEY'],
    aws_secret_access_key=app.config['S3_SECRET_ACCESS_KEY']
)

S3_LOCATION = 'https://{}.s3.amazonaws.com/'.format(app.config['S3_BUCKET'])


def upload_file_to_s3(file):
    """
    Docs: http://boto3.readthedocs.io/en/latest/guide/s3.html
    """

    try:
        s3.upload_fileobj(
            file,
            app.config['S3_BUCKET'],
            file.filename,
            ExtraArgs={
                'ACL': 'public-read',
                'ContentType': file.content_type
            }
        )
    except Exception as e:
        print(str(datetime.now()) + ' ', e)
        return e

    return "{}{}".format(S3_LOCATION, file.filename)


def delete_file_from_s3(word):
    """
    Docs: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.delete_object
    """

    try:
        s3.delete_object(
            Bucket=app.config['S3_BUCKET'],
            Key=word
        )
    except Exception as e:
        print(str(datetime.now()) + ' ', e)
        return e
