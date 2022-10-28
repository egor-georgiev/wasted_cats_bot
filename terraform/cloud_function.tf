data "archive_file" "bot_source_code" {
  type        = "zip"
  source_dir  = "${path.module}/../src"
  output_path = "${path.module}/${var.bot_name}.zip"
  excludes = [
    "venv"
  ]

}

resource "yandex_function" "bot_function" {
  # https://cloud.yandex.com/en/docs/functions/operations/function/function-create
  name               = "${var.bot_name}-function"
  user_hash          = data.archive_file.bot_source_code.output_md5
  runtime            = "python39"
  entrypoint         = var.entrypoint
  memory             = "128"
  execution_timeout  = "10"
  service_account_id = yandex_iam_service_account.bot_service_account.id
  environment = {
    TG_TOKEN       = var.tg_bot_token
    CAT_API_KEY    = var.cat_api_key
    MONGO_SRV      = mongodbatlas_advanced_cluster.bot_mongodb_cluster.connection_strings.0.standard_srv
    MONGO_USER     = var.mongo_db_user
    MONGO_PASSWORD = var.mongo_db_password
  }
  content {
    zip_filename = data.archive_file.bot_source_code.output_path
  }
}