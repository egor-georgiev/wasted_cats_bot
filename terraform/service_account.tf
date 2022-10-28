resource "yandex_iam_service_account" "bot_service_account" {
  name        = "${var.bot_name}-service-account"
  description = "service account to manage ${var.bot_name} lambda"
}

resource "yandex_resourcemanager_folder_iam_binding" "bot_service_account_role" {
  # https://cloud.yandex.ru/docs/iam/operations/sa/assign-role-for-sa
  for_each  = toset(var.lambda_sa_roles)
  folder_id = var.folder_id
  role      = each.key
  members = [
    "serviceAccount:${yandex_iam_service_account.bot_service_account.id}",
  ]
}