import uuid
import boto3


def create_bucket_name(bucket_prefix):
    return ''.join([bucket_prefix, str(uuid.uuid4())])


def create_bucket(bucket_prefix, s3_connection):
    session = boto3.session.Session()
    current_region = session.region_name
    bucket_name = create_bucket_name(bucket_prefix)
    bucket_response = s3_connection.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': current_region})

    print("Bucket created: {} in Region: {}".format(bucket_name, current_region))
    return bucket_name, bucket_response


def create_temp_file(size, file_name, file_content):
    random_file_name = ''.join([str(uuid.uuid4().hex[:6]), file_name])
    with open(random_file_name, 'w') as f:
        f.write(str(file_content) * size)
    print("File created: {}".format(random_file_name))
    return random_file_name


def copy_to_bucket(bucket_from_name, bucket_to_name, file_name):
    copy_source = {
        'Bucket': bucket_from_name,
        'Key': file_name
    }
    s3_resource.Object(bucket_to_name, file_name).copy(copy_source)
    print("Copy file {} FROM {} TO {}".format(
        file_name, bucket_from_name, bucket_to_name))


def enable_bucket_versioning(bucket_name):
    bkt_versioning = s3_resource.BucketVersioning(bucket_name)
    bkt_versioning.enable()
    print("Bucket {} Versioning status is: {}".format(
        bucket_name, bkt_versioning.status), end="\n\n")


def delete_all_objects(bucket_name):
    res = []
    bucket = s3_resource.Bucket(bucket_name)
    for obj_version in bucket.object_versions.all():
        res.append({'Key': obj_version.object_key,
                    'VersionId': obj_version.id})
    bucket.delete_objects(Delete={'Objects': res})
    print("Delete versions {}: ".format(res), end="\n\n")


if __name__ == "__main__":
    s3_resource = boto3.resource('s3')
    s3_client = boto3.resource('s3')

    # create bucket
    first_bucket_name, first_response = create_bucket(
        bucket_prefix='firstpythonbucket', s3_connection=s3_resource.meta.client)
    second_bucket_name, second_response = create_bucket(
        bucket_prefix='secondpythonbucket', s3_connection=s3_resource)
    print("")
    enable_bucket_versioning(first_bucket_name)

    # create file
    first_file_name = create_temp_file(300, 'firstfile.txt', 'f')
    second_file_name = create_temp_file(400, 'secondfile.txt', 's')
    third_file_name = create_temp_file(300, 'thirdfile.txt', 't')
    print("")

    first_bucket = s3_resource.Bucket(name=first_bucket_name)
    first_object = s3_resource.Object(
        bucket_name=first_bucket_name, key=first_file_name)
    second_object = s3_resource.Object(first_bucket.name, second_file_name)
    third_object = s3_resource.Object(first_bucket_name, third_file_name)
    print("First Bucket: {}".format(first_bucket))
    print("First Object: {}".format(first_object))
    print("Second Object: {}".format(second_object))
    print("Third Object: {}".format(third_object), end="\n\n")

    # upload files and versions of files
    print("Uploading files to S3 bucket")
    first_object.upload_file(first_file_name)
    first_object.upload_file(third_file_name)
    print("Version of first file: {}".format(
        first_object.version_id), end="\n\n")

    second_object.upload_file(second_file_name, ExtraArgs={
                              'ACL': 'public-read'})
    third_object.upload_file(third_file_name, ExtraArgs={
        'ServerSideEncryption': 'AES256',
        'StorageClass': 'STANDARD_IA'})

    # download file
    s3_resource.Object(first_bucket_name, first_file_name).download_file(
        f'/tmp/{first_file_name}')
    print("Download file {} FROM bucket {} TO /tmp/".format(first_file_name,
                                                            first_bucket_name), end="\n\n")

    # copy file between buckets
    copy_to_bucket(first_bucket_name, second_bucket_name, first_file_name)
    print("")

    # print ACL
    second_object_acl = second_object.Acl()
    print("Second file Access Control List (Public) {}".format(
        second_object_acl.grants))
    response = second_object_acl.put(ACL='private')
    print("Second file Access Control List (Private) {}".format(
        second_object_acl.grants), end="\n\n")

    # print encryption
    print("Third file Encryption is: {}".format(
        third_object.server_side_encryption))

    # print storage class
    print("Third file Storage Class is: {}".format(
        third_object.storage_class), end="\n\n")

    # delete file - can use delete_all_objects instead but I did it to learn...
    print("Empty buckets...", end="\n\n")
    s3_resource.Object(first_bucket_name, first_file_name).delete()
    s3_resource.Object(first_bucket_name, second_file_name).delete()
    s3_resource.Object(first_bucket_name, third_file_name).delete()
    s3_resource.Object(second_bucket_name, first_file_name).delete()

    # delete versioning - delete files manually as done above is not enought if bucket has versioning
    # can be done on non version buckets as well
    delete_all_objects(first_bucket_name)

    # delete bucket
    print("Delete buckets!", end="\n\n")
    s3_resource.Bucket(first_bucket_name).delete()
    s3_resource.Bucket(second_bucket_name).delete()
