resource "aws_instance" "first" {
    ami = var.ami_id
    instance_type = var.instance_name == "mongodb" ? "t3.micro":"t2.micro"
    tags = var.tags
    security_groups = [aws_security_group.Allow_all.name]
}
