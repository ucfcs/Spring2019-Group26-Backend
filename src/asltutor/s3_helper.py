import boto3
import botocore

from asltutor.main import app

s3 = boto3.client(
    "s3",
    aws_access_key_id=app.config['S3_KEY'],
    aws_secret_access_key=app.config['S3_SECRET_ACCESS_KEY']
)

S3_LOCATION = 'https://{}.s3.amazonaws.com/'.format(app.config['S3_BUCKET'])


def upload_file_to_s3(file, bucket_name=app.config['S3_BUCKET'], acl='public-read'):
    """
    Docs: http://boto3.readthedocs.io/en/latest/guide/s3.html
    """

    try:

        s3.upload_fileobj(
            file,
            bucket_name,
            file.filename,
            ExtraArgs={
                'ACL': acl,
                'ContentType': file.content_type
            }
        )

    except Exception as e:
        print('Something Happened: ', e)
        return e

    return "{}/{}".format(S3_LOCATION, file.filename)
