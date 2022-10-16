## about
This Terraform module manages:
* mongodb cluster
* yandex cloud function
* api gateway for the function above
* integration between telegram, api gateway and cloud function

## running this module

1. obtain bot token from telegram botfather and `export TG_TOKEN="<token value>"`
2. obtain bearer token: `export YC_TOKEN=$(yc iam create-token)`
3. one-time init: `terraform init`
4. apply: `terraform apply -var-file envs/default.tfvars -var tg_token=$TG_TOKEN`
