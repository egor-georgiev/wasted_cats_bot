# not managed:
#  * project
#  * project global access (0.0.0.0/0)
#  * user

resource "mongodbatlas_advanced_cluster" "bot_mongodb_cluster" {
  project_id     = var.mongo_project_id
  name           = "${var.bot_name}-cluster"
  cluster_type   = "REPLICASET"
  backup_enabled = false

  #   provider_name = "TENANT"
  #   backing_provider_name = "AWS"
  #   provider_region_name = "EU_WEST_1"
  #   provider_instance_size_name = "M0"
  replication_specs {
    num_shards = 1
    region_configs {
      electable_specs {
        disk_iops     = 0
        instance_size = "M0"
        node_count    = 0
      }
      priority      = 7
      backing_provider_name = "AWS"
      provider_name = "TENANT"
      region_name   = "EU_WEST_1"
    }
  }
}
