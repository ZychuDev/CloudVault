from google.cloud import storage
from PIL import Image

def convert_img(input_tiff_path, output_jpg_path):
        tiff_image = Image.open(input_tiff_path)

        # Convert TIFF to JPEG
        tiff_image.convert("RGB").save(output_jpg_path, "JPEG")

def convert_img_gcp(event, context):
    file_name = event['name']
    bucket_name = event['bucket']

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_name)

    local_file_path = f"/tmp/{file_name}"
    local_target_path = f"/tmp/{file_name.split('.')[0]}.jpg"
    blob.download_to_filename(local_file_path)
    convert_img(local_file_path, local_target_path)
    target_bucket = storage_client.bucket("compressed_img_cloudvault")

    blob2 = target_bucket.blob(f"{file_name.split('.')[0]}.jpg")
    blob2.upload_from_filename(local_target_path)
