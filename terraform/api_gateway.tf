resource "yandex_api_gateway" "bot_api_gateway" {
  name        = "${var.bot_name}-gateway"
  description = "api gateway to manage traffic for ${var.bot_name}"
  labels      = {}
  spec = templatefile(
    "${path.module}/templates/gateway_spec.tftpl.yaml",
    {
      bot_name : var.bot_name,
      function_id : yandex_function.bot_function.id,
      service_account_id : yandex_iam_service_account.bot_service_account.id,
      bot_path : var.endpoint_path
    }
  )
}
