# Creaing S3 bucket for flowlogs
import pulumi
from modules.s3.s3_module import create_s3_bucket

# Create an S3 bucket using the module function
bucket = create_s3_bucket('flowlogs')

# Export the name of the bucket
pulumi.export('bucket_name', bucket.id)


# Creating VPC
import pulumi
from modules.vpc.vpc_module import create_vpc
from modules.vpc.outputs import get_vpc_id_output, get_public_subnet_ids_output, get_private_subnet_ids_output

# Create VPC using the module function
my_vpc = create_vpc('kridge')

# Retrieve exported VPC and subnet information
vpc_id_output = get_vpc_id_output(my_vpc)
public_subnet_ids_output = get_public_subnet_ids_output(my_vpc)
private_subnet_ids_output = get_private_subnet_ids_output(my_vpc)

# Use the VPC and subnet information as needed
print(f"VPC ID: {vpc_id_output}")
print(f"Public Subnet IDs: {public_subnet_ids_output}")
print(f"Private Subnet IDs: {private_subnet_ids_output}")
