import pulumi
from pulumi_aws import ec2

def create_vpc(vpc_name: str, cidr_block: str = "10.0.0.0/16") -> ec2.Vpc:
    # Create VPC
    vpc = ec2.Vpc(
        vpc_name,
        cidr_block=cidr_block,
        enable_dns_support=True,
        enable_dns_hostnames=True,
    )

    # Create Internet Gateway
    internet_gateway = ec2.InternetGateway(f"{vpc_name}-igw", vpc_id=vpc.id)

    # Create Route Table for Internet access
    route_table = ec2.RouteTable(f"{vpc_name}-rt", vpc_id=vpc.id)
    route = ec2.Route(
        f"{vpc_name}-route",
        route_table_id=route_table.id,
        destination_cidr_block="0.0.0.0/0",
        gateway_id=internet_gateway.id,
    )

    # Create Public Subnet in each Availability Zone
    for az in range(2):  # Adjust the range based on the number of availability zones in your region
        public_subnet = ec2.Subnet(
            f"{vpc_name}-public-subnet-{az}",
            vpc_id=vpc.id,
            cidr_block=f"10.0.{az}.0/24",
            availability_zone=f"us-east-1a" if az == 0 else f"us-east-1b",  # Replace with your region and zones
            map_public_ip_on_launch=True,
            tags={"Name": f"{vpc_name}-public-subnet-{az}"},
        )
        ec2.RouteTableAssociation(f"{vpc_name}-public-rta-{az}", route_table_id=route_table.id, subnet_id=public_subnet.id)

        # Create Private Subnet in each Availability Zone
    for az in range(2):  # Adjust the range based on the number of availability zones in your region
        private_subnet = ec2.Subnet(
            f"{vpc_name}-private-subnet-{az}",
            vpc_id=vpc.id,
            cidr_block=f"10.0.{az + 1}.0/24",  # Offset by 1 to avoid overlapping with public subnets
            availability_zone=f"us-east-1a" if az == 0 else f"us-east-1b",  # Replace with your region and zones
            map_public_ip_on_launch=True,
            tags={"Name": f"{vpc_name}-private-subnet-{az}"},
        )
        ec2.RouteTableAssociation(f"{vpc_name}-private-rta-{az}", route_table_id=route_table.id, subnet_id=private_subnet.id)

    return vpc
