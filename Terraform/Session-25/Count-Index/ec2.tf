resource "aws_instance" "Count_index" {
    count = 10
    ami = local.ami_id
    instance_type = var.instance_names[count.index] == "mongodb" || var.instance_names[count.index] == "mysql" ? "t3.medium" : "t2.micro"
    tags = {
      Name = var.instance_names[count.index]
    }
}
resource "aws_route53_record" "roboshop" {
    count = 10
    zone_id = var.zone_id
    name    = "${var.instance_names[count.index]}.${var.domain_name}"
    type    = "A"
    ttl     = 300
    records = [aws_instance.Count_index[count.index].private_ip]

# var.instance_names[count.index] == "mongodb" || var.instance_names[count.index] == "mysql" ? aws_instance.Count_index[count.index].private_ip : aws_instance.Count_index[count.index].public_ip
}