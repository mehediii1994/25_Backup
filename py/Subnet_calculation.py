import ipaddress

def subnet_info(ip_network_str):
    """Calculates subnet information, including host range.

    Args:
        ip_network_str: The IP network string (e.g., "192.168.0.0/16").

    Returns:
        A dictionary containing subnet information, or None if there's an error.
    """
    try:
        network = ipaddress.ip_network(ip_network_str, strict=False)
        prefix_len = network.prefixlen
        ip_version = network.version

        if ip_version == 4:
            max_prefix_len = 32
        elif ip_version == 6:
            max_prefix_len = 128
        else:
            return None

        if prefix_len == max_prefix_len:  # /32 or /128 means a single host
            return {
                "num_subnets": 1,
                "hosts_per_subnet": 1,
                "first_host": str(network.network_address),
                "last_host": str(network.network_address),
            }

        num_subnets = 2**(max_prefix_len - prefix_len)
        hosts_per_subnet = 2**(max_prefix_len - prefix_len) - 2

        hosts = list(network.hosts())
        first_host = str(hosts[0]) if hosts else "N/A"
        last_host = str(hosts[-1]) if hosts else "N/A"

        return {
            "num_subnets": num_subnets,
            "hosts_per_subnet": hosts_per_subnet,
            "first_host": first_host,
            "last_host": last_host,
        }

    except ValueError:
        print("Invalid IP network string.")
        return None

def main():
    while True:
        ip_network_str = input("Enter the IP network (e.g., 192.168.0.0/16): ")
        result = subnet_info(ip_network_str)

        if result:
            print("\nNetwork Information:")
            print(f"Number of Subnets: {result['num_subnets']}")
            print(f"Valid Hosts per Subnet: {result['hosts_per_subnet']}")
            print(f"First Host: {result['first_host']}")
            print(f"Last Host: {result['last_host']}")
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()