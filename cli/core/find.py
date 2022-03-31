from ipaddress import IPv4Network

from cli.settings import Settings, load_settings
from cli.utils import query_sw

settings: Settings = load_settings()


def search_mac(mac: str) -> list[dict[str, str | int]]:
    devices = get_devices_from_mac(mac)
    for device in devices:
        get_device_switch(device)
    return devices


def get_devices_from_mac(mac: str):
    query = """
        SELECT IPNode.IpNodeId as nodeid, IPNode.IPAddress as ip, Subnet.Address as network, Subnet.CIDR as cidr, IPNode.MAC as mac, IPNode.DhcpClientName as hostname
        FROM IPAM.IPNode
        INNER JOIN IPAM.Subnet ON IPNode.SubnetId = Subnet.SubnetId
        WHERE MAC LIKE @m
    """
    parameters = {"m": f"%{mac}%"}

    if settings.ENVIRONMENT == "test":
        devices = [
            {
                "nodeid": 1,
                "ip": "10.10.1.1",
                "network": "10.10.1.0",
                "cidr": 24,
                "mac": "52-54-00-18-8B-85",
                "hostname": "PC1011",
            }
        ]
    else:
        devices = query_sw(query, parameters)
        for device in devices:
            device["hostname"] = device["hostname"].split(".")[0]
    return devices


def get_device_switch(device: dict):
    if settings.ENVIRONMENT == "test":
        device.update({"ip": "10.10.1.254", "hostname": "SW1011"})
    else:
        query = """
            SELECT Nodes.NodeId as nodeid, Nodes.IPAddress as ip, Nodes.SysName as hostname
            FROM Orion.Nodes
            INNER JOIN Orion.NodeIPAddresses ON Nodes.NodeId = NodeIPAddresses.NodeId
            WHERE NodeIPAddresses.IPAddress = @i
        """
        parameters = {
            "i": str(IPv4Network(f"{device['network']}/{device['cidr']}")[-2]),
        }
        switch = query_sw(query, parameters)[0]
        device.update({"switch": switch["hostname"].split(".")[0], "switch_ip": switch["ip"]})
