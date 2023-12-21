variable "ami_id" {
    type = string
  default = ""
}
variable "instance_type" {
    type  = string
    default = " "
}
variable "inst_name" {
    type  = string
    default = ""
}
variable "tags" {
    # default = " "
    default = {
        Name = "Roboshop"
    }
}