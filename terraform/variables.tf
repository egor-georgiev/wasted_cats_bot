# env-dependent
variable "cloud_id" {
  type = string
}

variable "folder_id" {
  type = string
}

variable "zone" {
  type = string
}

variable "tg_bot_token" {
  type        = string
  description = "token received from botfather"
}

variable "mongo_project_id" {
  type = string
}

variable "mongo_public_key" {
  type = string
}

variable "mongo_private_key" {
  type = string
}

variable "cat_api_key" {
  type = string
}

variable "mongo_db_user" {
  type = string
}

variable "mongo_db_password" {
  type = string
}

# env-agnostic
variable "bot_name" {
  type    = string
  default = "wasted-cats-bot"
}

variable "lambda_sa_roles" {
  type        = list(string)
  description = "roles to assign for the service account"
  default     = ["editor", "serverless.functions.invoker"]
}

variable "entrypoint" {
  type    = string
  default = "main.handler"
}

variable "endpoint_path" {
  type    = string
  default = "bot"
}
