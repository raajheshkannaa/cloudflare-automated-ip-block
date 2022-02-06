import CloudFlare
import boto3
from time import sleep

#accountid = [event['accountID']]
#email = event['email']

ssm = boto3.client('ssm',region_name='us-east-1')
response = ssm.get_parameters(
		Names=[
			'/Cloudflare/Token', '/Cloudflare/zones/' + env
		],
		WithDecryption=True
)
token = response['Parameters'][0]['Value']
zone = response['Parameters'][1]['Value']

# Global
cf = CloudFlare.CloudFlare(token=token)

def block_ip(ip):
	cf = CloudFlare.CloudFlare(token=token)
	#ip = '244.233.222.211'

	post_filters_data = [{
		"expression": "ip.src eq " + str(ip),
		"description": "Automatically block malicious IP: " + str(ip)
		}]
	
	post_filters = cf.zones.filters.post(zone,data=post_filters_data)
	length = len(post_filters)
	for filter in range(length):
		id = post_filters[filter]['id']
		expr = post_filters[filter]['expression']
		#print(id, expr)
		post_rules_data = [
			{
				"filter": {
					"id": id
				},
				"action": "block",
				"description": "Automatically block malcious IP " + str(ip)
			}
		]
		posts_rule = cf.zones.firewall.rules.post(zone,data=post_rules_data)
		print(posts_rule)    

'''
def delete_filter():
	delete_filter = cf.zones.filters.delete(zone,'<key in filter id here>')
	print(delete_filter)
'''    

def get_filters():
	get_filters = cf.zones.filters.get(zone)
	length = len(get_filters)
	for filter in range(length):
		id = get_filters[filter]['id']
		expr = get_filters[filter]['expression']
		print(id, expr)
		#sleep(1)
		#delete_filter = cf.zones.filters.delete(zone,id)
		#print(delete_filter)


def main(event, handler):

	ip = event['src_ip']
	global env
	env = event['environment']
	block_ip(ip)
	get_filters()
	#delete_filter()