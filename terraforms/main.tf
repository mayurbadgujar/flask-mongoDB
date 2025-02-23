provider "aws" {
  region = "us-east-1"
  access_key=var.access_key
  secret_key=var.secret_key
}

resource "aws_instance" "app_server" {
    ami=var.ami_id
    instance_type ="t2.micro"
    key_name = var.key_name

    vpc_security_group_ids = [aws_security_group.app_sg.id]
    user_data = file("user-data.sh")
    tags = {
    Name = "app-server"
  }
}

resource "aws_security_group" "app_sg" {
  name        = "flask_express_sg"
  description = "Allow HTTP and SSH traffic"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 3000
    to_port     = 3000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 5000
    to_port     = 5000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
