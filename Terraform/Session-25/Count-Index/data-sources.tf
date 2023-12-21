data "aws_ami" "amiid" {
    most_recent = true
    owners = ["self"]
    filter{
        name = "name"
        values = ["amzn2-ami-kernel-5.10-hvm-*.0-x86_64-gp2"]
    }
}
output "ami_id" {
  value = data.aws_ami.amiid.id
}