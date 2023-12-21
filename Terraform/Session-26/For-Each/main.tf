resource "aws_instance" "inst1" {
    for_each = var.inst_names
    ami = var.ami_id
    instance_type = each.value
    tags = {
        Name = each.key
    } 
}

resource "aws_route53_record" "dns_names" {
    for_each = aws_instance.inst1
    zone_id = var.zone_id
    name = "${each.key}.${var.domain_name}"
    type = "A"
    ttl = 1
    records = [each.key == "web" ? each.value.public_ip : each.value.private_ip]
}