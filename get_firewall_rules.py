import CloudFlare


token = '' # API Token
zone = '' # Zone ID

def main():
    cf = CloudFlare.CloudFlare(token=token)
    zones = cf.zones.firewall.rules.get(zone)
    print(zones)

if __name__ == '__main__':
    main()
