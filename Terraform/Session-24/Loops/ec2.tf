resource "aws_instance" "first" {
    count = 10
    ami = var.ami_id
    instance_type = var.instance_type
    tags = var.tags
    security_groups = [aws_security_group.Allow_all.name]
}
