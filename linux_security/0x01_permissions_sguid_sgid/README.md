# Linux Permissions, SUID & SGID

This project focuses on understanding Linux file permissions, privilege escalation risks, and special permission bits such as SUID and SGID.

## Project Overview

The tasks in this directory explore:

- Creating users and groups
- Managing sudo privileges
- Searching for files with SUID/SGID bits
- Identifying potential privilege escalation vectors
- Switching users securely
- File permission auditing
- Ownership and access control concepts

The objective of this project was to understand how Linux permission systems work and how misconfigurations can introduce security vulnerabilities.

⚠️ All privilege-related experiments were conducted in a controlled lab environment for educational purposes.

## Files Description

- 0-add_user.sh: Adds a new system user.
- 1-add_group.sh: Creates a new group.
- 2-sudo_nopass.sh: Configures passwordless sudo (lab simulation).
- 3-find_files.sh: Searches for specific files.
- 4-find_suid.sh: Finds files with SUID bit set.
- 5-find_sgid.sh: Finds files with SGID bit set.
- 6-check_files.sh: Checks file permissions.
- 7-file_read.sh: Demonstrates file access control.
- 8-change_user.sh: Switches user context.
- 9-empty_file.sh: Creates and manages empty files securely.

## Technologies Used

- Bash scripting
- Linux
- chmod / chown / sudo
- find command
- Permission bits (SUID, SGID)

## Key Concepts Practiced

- Linux permission model
- User and group management
- Privilege escalation awareness
- Security auditing techniques
- Access control best practices

## Author

Sahil Asgarov
