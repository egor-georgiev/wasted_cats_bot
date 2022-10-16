output "api_gateway_domain" {
  value = yandex_api_gateway.bot_api_gateway.domain
}

output "mongo_srv" {
  value = mongodbatlas_advanced_cluster.bot_mongodb_cluster.connection_strings.0.standard_srv
}