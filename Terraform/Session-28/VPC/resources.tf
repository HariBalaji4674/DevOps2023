resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
  tags = var.tags
}

resource "aws_subnet" "public" {
  vpc_id     = aws_vpc.main.id
  cidr_block = "10.0.1.0/24"
  tags = {Name = "Public-Roboshop"}
}

resource "aws_subnet" "private" {
  vpc_id     = aws_vpc.main.id
  cidr_block = "10.0.2.0/24"
  tags = {Name = "Private-Roboshop"}
}

resource "aws_internet_gateway" "gw" {
  vpc_id = aws_vpc.main.id
  tags = var.tags
}

resource "aws_route_table" "public" {
  vpc_id = aws_vpc.main.id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.gw.id
  }
  tags = {Name = "Public-Roboshop"}
}

resource "aws_route_table" "private" {
  vpc_id = aws_vpc.main.id
  tags = {Name = "Private-Roboshop"}
}

resource "aws_route_table_association" "public" {
  subnet_id      = aws_subnet.public.id
  route_table_id = aws_route_table.public.id
}

resource "aws_route_table_association" "a" {
  subnet_id      = aws_subnet.private.id
  route_table_id = aws_route_table.private.id
}

resource "aws_security_group" "ssh" {
  name   = "ssh"
  vpc_id = aws_vpc.main.id

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    description = "access to my laptop"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = -1
    cidr_blocks = ["0.0.0.0/0"]
  }
  tags = {Name = "Security-Gr"}
}

resource "aws_instance" "public" {
    ami = var.ami_id
    instance_type = var.instance_type
    tags = var.tags
    subnet_id = aws_subnet.public.id
    associate_public_ip_address = true
    vpc_security_group_ids = [ aws_security_group.ssh.id ]
}
