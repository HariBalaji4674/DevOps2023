resource "aws_instance" "roboshop" {
    for_each = var.inst_names
    ami = var.ami_id
    instance_type = each.value
    tags = {
        Name = each.key
    } 
}

resource "aws_route53_record" "dns_names" {
    for_each = aws_instance.roboshop
    zone_id = var.zone_id
    name = "${each.key}.${var.domain_name}"
    type = "A"
    ttl = 1
    records = [each.key == "web" ? each.value.public_ip : each.value.private_ip]
}

resource "aws_security_group" "allow_tls" {
  name        = var.sg_name
  description = "Allow TLS inbound traffic"
  

  dynamic ingress {
    for_each = var.sgrules
    content {
    description      = ingress.value["description"]
    from_port        = ingress.value["from_port"]
    to_port          = ingress.value["to_port"]
    protocol         = ingress.value["protocol"]
    cidr_blocks      = ingress.value["cidr_blocks"]
  }
  }
  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  tags = {
    Name = var.sg_name
  }
}