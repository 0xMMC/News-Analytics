variable "credentials" {
  description = "My credentials"
  default     = "news_analytics_service_acc.json"
}

variable "region" {
  description = "Region of the GCP Project"
  default     = "europe-west1-b"
}

variable "project_name" {
  description = "Name of the GCP Project"
  default     = "news-analytics-419010"
}

variable "location" {
  description = "Project Location"
  default     = "EU"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  default     = "demo_dataset"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  default     = "news-analytics-419010-terra-bucket"
}

variable "gcs_storage_class" {
  description = "Bucket Storage class"
  default     = "STANDARD"
}