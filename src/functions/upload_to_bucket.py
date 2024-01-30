from google.cloud import storage

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(f'File {source_file_name} uploaded to {destination_blob_name} in {bucket_name}.')

if __name__ == "__main__":
    bucket_name = 'raw-images-cloudvault-bucket'
    source_file_name = '../../assets/from_storage.tif'
    destination_blob_name = 'upload_krajobraz2.tif'

    upload_blob(bucket_name, source_file_name, destination_blob_name)