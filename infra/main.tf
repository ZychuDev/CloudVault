#Enabling APIs
resource "google_project_service" "cloud_source_repositories" {
  project = var.gcp_project
  service = "sourcerepo.googleapis.com"

  disable_on_destroy = false
}

resource "google_project_service" "cloud_functions" {
  project = var.gcp_project
  service = "cloudfunctions.googleapis.com"

  disable_on_destroy = false
}

resource "google_project_service" "cloud_build" {
  project = var.gcp_project
  service = "cloudbuild.googleapis.com"

  disable_on_destroy = false
}


#Bucket to store raw images
resource "google_storage_bucket" "raw_img_bucket" {
  name = "raw_img_cloudvault"
  location = "europe-central2"
}

#Bucket to store ebook files
resource "google_storage_bucket" "ebook_bucket" {
  name = "ebook_cloudvault"
  location = "europe-central2"
}

#Bucket to store compressed img
resource "google_storage_bucket" "compressed_img_bucket" {
    name = "compressed_img_cloudvault"
    location = "europe-central2"
}

#Bucket to store cloud functions src
resource "google_storage_bucket" "src_bucket" {
  name     = "src_cloudvault"
  location = "US"
}

#Deploy functions
resource "google_storage_bucket_object" "archive" {
  name   = "convert_img_gcp_src.zip"
  bucket = google_storage_bucket.src_bucket.name
  source = "../src/functions/convert_img_gcp/convert_img_gcp.zip"
}

resource "google_cloudfunctions_function" "convert_function" {
  name        = "convert_img_gcp"
  description = "Convert files from .tiff to .jpg and uploads to according bucket."
  runtime     = "python39"

  available_memory_mb   = 256
  source_archive_bucket = google_storage_bucket.src_bucket.name
  source_archive_object = google_storage_bucket_object.archive.name
  entry_point           = "convert_img_gcp"
  event_trigger {
    resource = google_storage_bucket.raw_img_bucket.name
    event_type = "google.storage.object.finalize"
  }

  depends_on = [google_project_service.cloud_functions]
}

resource "google_storage_bucket_object" "archive2" {
  name   = "convert_epub_to_mobi_src.zip"
  bucket = google_storage_bucket.src_bucket.name
  source = "../src/functions/convert_epub_to_mobi/convert_epub_to_mobi.zip"
}

resource "google_cloudfunctions_function" "ebook" {
  name        = "convert_epub_to_mobi"
  description = "Convert files from .epub to .mobi and send it via email."
  runtime     = "python39"

  available_memory_mb   = 256
  source_archive_bucket = google_storage_bucket.src_bucket.name
  source_archive_object = google_storage_bucket_object.archive2.name
  entry_point           = "convert_epub_to_mobi"
  event_trigger {
    resource = google_storage_bucket.ebook_bucket.name
    event_type = "google.storage.object.finalize"
  }

  environment_variables = {
    SENDGRID_API_KEY = var.SENDGRID_API_KEY
  }

  depends_on = [google_project_service.cloud_functions]
}

#Create repository
resource "google_sourcerepo_repository" "website_repo" {
  name = "hugo_repo"
  project = var.gcp_project
  
  depends_on = [ google_project_service.cloud_source_repositories ]
}

#Build trigger
resource "google_cloudbuild_trigger" "my_trigger" {
  name     = "my-trigger"
  description = "My Cloud Build Trigger"
  trigger_template {
    branch_name = "master"
    repo_name   = google_sourcerepo_repository.website_repo.name
  }
  filename = "cloudbuild.yaml"

  depends_on = [ google_sourcerepo_repository.website_repo ]
}









