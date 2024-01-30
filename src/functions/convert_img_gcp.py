from google.cloud import storage
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
def convert_img_gcp(event, context):
    file_name = event['name']
    bucket_name = event['bucket']

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_name)

    local_file_path = f"tmp/{file_name}"

    blob.download_to_filename(local_file_path)

    target_bucket = storage_client.bucket("compressed_img_cloudvault")

    blob2 = target_bucket.blob(f"{file_name}2")
    blob2.upload_from_filename(local_file_path)
