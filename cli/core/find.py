from cli.settings import Settings, load_settings
from cli.utils import query_sw

settings: Settings = load_settings()


def search_mac(mac: str) -> list[dict[str, str | int]]:
    query = """
        SELECT IPNode.IpNodeId as nodeid, IPNode.IPAddress as ip, Subnet.CIDR as cidr, IPNode.MAC as mac, IPNode.DhcpClientName as hostname
        FROM IPAM.IPNode
        INNER JOIN IPAM.Subnet ON IPNode.SubnetId = Subnet.SubnetId
        WHERE MAC LIKE @m
    """
    parameters = {"m": f"%{mac}%"}

    if settings.ENVIRONMENT in ["test", "develop"]:
        results = [
            {
                "nodeid": 1,
                "ip": "10.101.10.1",
                "network": "10.101.10.0",
                "cidr": 24,
                "mac": "52-54-00-1D-DA-08",
                "hostname": "PC1011.lab.local",
            }
        ]
    else:
        results = query_sw(query, parameters)

    return results
