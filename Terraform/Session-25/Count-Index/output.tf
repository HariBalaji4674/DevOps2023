output "publicip" {
  value = aws_instance.Count_index[*].public_ip
}
output "privateip" {
  value = aws_instance.Count_index[*].private_ip
}

