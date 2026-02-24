# Mandatory Access Control (MAC) & SELinux

This project focuses on understanding Mandatory Access Control (MAC) mechanisms in Linux systems, including SELinux configuration and firewall management.

## Project Overview

The tasks in this directory explore:

- Analysing SELinux modes
- Configuring firewall rules with iptables
- Security context matching
- Listing HTTP-related rules
- Managing SELinux ports
- Inspecting system users
- Working with SELinux booleans
- Configuring secure service policies

The objective of this project was to understand how Mandatory Access Control enhances system security beyond traditional discretionary permissions.

⚠️ All configurations and modifications were performed in a controlled lab environment.

## Files Description

- 0-analyse_mode.sh: Analyzes current SELinux mode.
- 0-iptables.sh: Displays or configures iptables rules.
- 1-security_match.sh: Matches security contexts.
- 2-list_http.sh: Lists HTTP-related security rules.
- 3-add_port.sh: Adds custom port to SELinux policy.
- 4-list_user.sh: Lists SELinux users.
- 5-add_selinux.sh: Adds new SELinux configuration.
- 6-list_booleans.sh: Lists available SELinux booleans.
- 7-set_sendmail.sh: Configures SELinux boolean for sendmail service.

## Technologies Used

- Linux
- SELinux
- iptables
- Bash scripting
- Security policies

## Key Concepts Practiced

- Mandatory Access Control (MAC)
- SELinux modes (Enforcing, Permissive, Disabled)
- Security contexts
- Policy management
- Firewall configuration
- Service-level security control

## Author

Sahil Asgarov
