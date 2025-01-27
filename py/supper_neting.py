import ipaddress

def supernet_ips(ip_range_start, ip_range_end):
    """Supernets a range of IP addresses."""
    try:
        start_ip = ipaddress.ip_address(ip_range_start)
        end_ip = ipaddress.ip_address(ip_range_end)

        if start_ip > end_ip:
            raise ValueError("Start IP must be less than or equal to end IP")

        networks = []
        current_ip = start_ip
        while current_ip <= end_ip:
            for prefixlen in range(32, 0, -1):
                network = ipaddress.ip_network(f"{current_ip}/{prefixlen}", strict=False)
                if end_ip in network:
                    networks.append(network)
                    current_ip = network[-1] + 1
                    break
        return networks

    except ValueError as e:
        print(f"Invalid IP address input: {e}")
        return None

def main():
    """Gets IP range input from the user and performs supernetting."""
    while True:  # Input validation loop
        ip_range = input("Enter the IP range (e.g., 10.110.2.2-10.110.6.254): ")
        try:
            start_ip_str, end_ip_str = ip_range.split("-")
            start_ip_str = start_ip_str.strip() #remove white space
            end_ip_str = end_ip_str.strip() #remove white space
            ipaddress.ip_address(start_ip_str)
            ipaddress.ip_address(end_ip_str)
            break  # Exit loop if input is valid
        except (ValueError, AttributeError):
            print("Invalid IP range format. Please use the format IP1-IP2.")

    supernet = supernet_ips(start_ip_str, end_ip_str)

    if supernet:
        print("Supernet(s):")
        for net in supernet:
            print(net)
    else:
        print("Could not find a suitable supernet.")

if __name__ == "__main__":
    main()