# Shodan Reconnaissance Report
## Target: holbertonschool.com

---

## 1. IP Ranges / Hosts

| IP Address       | Hostname                                   | Location        | Provider                  |
|-----------------|-------------------------------------------|----------------|---------------------------|
| 35.180.27.154   | ec2-35-180-27-154.eu-west-3.compute.amazonaws.com | Paris, France  | Amazon Data Services France |
| 52.47.143.83    | ec2-52-47-143-83.eu-west-3.compute.amazonaws.com / yriry2.holbertonschool.com | Paris, France  | Amazon Data Services France |

---

## 2. Subdomains and Technologies

| Subdomain                     | Web Server    | OS / Platform | SSL / TLS                   | Notes |
|--------------------------------|---------------|---------------|----------------------------|-------|
| yriry2.holbertonschool.com    | nginx 1.21.6 | Ubuntu        | TLSv1.2, TLSv1.3 (Let's Encrypt) | Redirects from HTTP to HTTPS |

**Technologies observed:**
- Web server: nginx
- Operating system: Ubuntu
- SSL certificate: Let's Encrypt
- TLS versions: TLSv1.2, TLSv1.3
- Cloud provider: Amazon AWS / EC2

---

## 3. Observations

- The holbertonschool.com infrastructure is hosted on **Amazon AWS EC2 instances**.  
- CloudFront / CDN not explicitly detected, but IPs belong to AWS.  
- Web servers consistently use **nginx** on **Ubuntu**.  
- HTTPS enforced on at least one subdomain (`yriry2.holbertonschool.com`).  
- Minimal open ports detected (80, 443).  
- No unusual or risky exposed services observed.

---

## 4. Conclusion

Holberton School domain is hosted in a secure cloud environment (AWS EC2), using nginx web servers on Ubuntu. TLS is properly configured and HTTP traffic is redirected to HTTPS. The attack surface is minimal based on current Shodan data.

