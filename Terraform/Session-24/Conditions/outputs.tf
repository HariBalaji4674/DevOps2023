output "Public_IP" {
  value = aws_instance.first.public_ip
}
output "Private_IP" {
  value = aws_instance.first.private_ip
}
output "ami_id" {
  value = aws_instance.first.ami  
}
