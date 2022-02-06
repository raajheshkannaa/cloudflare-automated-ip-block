import CloudFlare


token = '' # API Token
zone = '' # Zone ID

def main():
    cf = CloudFlare.CloudFlare(token=token)
    zones = cf.zones.get()
    for zone in zones:
        zone_id = zone['id']
        zone_name = zone['name']
        print(zone_id, zone_name)


if __name__ == '__main__':
    main()
