module "ec2" {
  source = "../module-dev"
  ami_id = var.ami_id
  instance_type = var.instance_type
  inst_name = var.inst_name
}