module "ec2_instance" {
  source  = "terraform-aws-modules/ec2-instance/aws"

  name = "WORKSTATION"

  ami = "ami-03265a0778a880afb"
  instance_type          = "t3.medium"
  vpc_security_group_ids = [aws_security_group.allow_all.id]
  subnet_id              = "subnet-08779672161084a23"
  user_data = file("docker.sh")

  tags = {
    Terraform   = "true"
    Environment = "dev"
  }
}

resource "aws_security_group" "allow_all" {
    name = "Allow-All"
    description = "Allowing all traffic from Outside & Inside"
    ingress {
        description = "workstation"
        from_port = 0
        to_port = 0
        protocol = "-1"
        cidr_blocks = ["0.0.0.0/0"]

    }
    egress {
        description = "workstation"
        from_port = 0
        to_port = 0
        protocol = "-1"
        cidr_blocks = ["0.0.0.0/0"]

    }
  
}