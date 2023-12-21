module "this" {
  source = "../VPC-Module"
  cidr_block = var.cidr_block
  enable_dns_hostnames = var.enable_dns_hostnames
  enable_dns_support = var.enable_dns_support
  common_tags = var.common_tags
  vpc_tags = var.vpc_tags
  project_name = var.project_name
}