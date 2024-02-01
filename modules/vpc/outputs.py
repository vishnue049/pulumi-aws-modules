import pulumi
from pulumi_aws import ec2

def get_vpc_id_output(vpc: ec2.Vpc) -> pulumi.Output[str]:
    return vpc.id

def get_public_subnet_ids_output(vpc: ec2.Vpc) -> pulumi.Output[list]:
    public_subnet_ids = pulumi.Output.all(vpc.id).apply(lambda args: ec2.getSubnetIds(vpc_id=args[0], tags={"Tier": "public"}))
    return public_subnet_ids.ids

def get_private_subnet_ids_output(vpc: ec2.Vpc) -> pulumi.Output[list]:
    private_subnet_ids = pulumi.Output.all(vpc.id).apply(lambda args: ec2.getSubnetIds(vpc_id=args[0], tags={"Tier": "private"}))
    return private_subnet_ids.ids
