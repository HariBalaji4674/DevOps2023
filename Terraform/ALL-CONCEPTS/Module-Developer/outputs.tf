output "vpc_id" {
    value = aws_vpc.main.id
}
output "igw_id" {
  value = aws_internet_gateway.main.id
}
# output "azs" {
#   value = data.aws_availability_zone.available
# }