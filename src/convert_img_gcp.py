import functions_framework
from google.cloud import storage
from PIL import Image

# Triggered by a change in a storage bucket
@functions_framework.cloud_event
def convert_img(cloud_event):
    data = cloud_event.data

    event_id = cloud_event["id"]
    event_type = cloud_event["type"]

    bucket = data["bucket"]
    name = data["name"]

    if cloud_event.event_type != 'google.storage.object.finalize':
      print(f"Ignore event: {cloud_event.event_type}")
      return

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket)
    blob = bucket.blob(name)

    temp_dir = tempfile.mkdtemp()
    temp_file_path = os.path.join(temp_dir, 'downloaded_image.tiff')
    blob.download_to_filename(temp_file_path)

    processed_image_path = process_image(temp_file_path)

    processed_blob_name = f"{name.split('.')[0]}.jpg"
    processed_blob = bucket.blob(processed_blob_name)
    processed_blob.upload_from_filename(processed_image_path)

    metageneration = data["metageneration"]
    timeCreated = data["timeCreated"]
    updated = data["updated"]

def process_image(input_path)::
  output_path = tempfile.mktemp(suffix='.jpg')
  im = Image.open(input_path)
  im.save(output_path, "JPEG", quality=100)
  return output_path
