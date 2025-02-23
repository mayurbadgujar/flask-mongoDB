variable "access_key"{
}
variable "secret_key"{
}
variable "ami_id" {
  description = "AMI ID for the EC2 instance"
  default     = "ami-04b4f1a9cf54c11d0"
}
variable "key_name" {
  description = "Key pair name for SSH access"
  default ="test"
}