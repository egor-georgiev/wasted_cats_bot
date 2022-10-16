resource "null_resource" "example1" {
  # make a call to telegram api to link cloud function gateway
  # note: request is idempotent
  provisioner "local-exec" {
    command     = "curl -X POST https://api.telegram.org/bot${var.tg_bot_token}/setwebhook?url=https://${yandex_api_gateway.bot_api_gateway.domain}/bot"
    interpreter = ["bash", "-c"]
  }
  depends_on = [
    yandex_api_gateway.bot_api_gateway,
    yandex_function.bot_function
  ]
  # trigger provisioner every time
  triggers = {
    build_time : timestamp()
  }
}