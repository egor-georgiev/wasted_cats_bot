## about
This Terraform module manages:
* mongodb cluster
* yandex cloud function
* api gateway for the function above
* integration between telegram, api gateway and cloud function

## running this module

1. obtain bearer token: `export YC_TOKEN=$(yc iam create-token)`
2. one-time init: `terraform init`
3. apply: `terraform apply -var-file envs/default.tfvars`
