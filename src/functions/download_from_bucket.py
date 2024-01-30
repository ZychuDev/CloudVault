from google.cloud import storage

def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)

    blob.download_to_filename(destination_file_name)

    print(f'File {source_blob_name} downloaded to {destination_file_name}.')

if __name__ == "__main__":
    bucket_name = 'raw-images-cloudvault-bucket'
    source_blob_name = 'krajobraz2.tif'
    destination_file_name = '../../assets/from_storage.tif'

    download_blob(bucket_name, source_blob_name, destination_file_name)