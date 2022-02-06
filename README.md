## Automatically block IPs in CloudFlare Firewall Rules
This is run in an AWS lambda function and intended to be automated as a Slack Bot, where we key `/block <ip>` in a channel and it would block that IP in CloudFlare. This could also be in a SIEM Orchestration pipeline when there is a high fidelity signal that a malicious IP has had abnormal behaviour, it could be blocked in CloudFlare.

Improvements such as deleting the block IP after 30 mins could be baked in, essentially making the IP block as a temporary ban based on behavior and the investigation from the Ops team.