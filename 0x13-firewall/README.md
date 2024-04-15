# Firewall Configuration Project

## Introduction

This project contains configuration files for setting up a firewall using `ufw` on an Ubuntu server.

## Files

### Configuration File: 0-block_all_incoming_traffic_but

This file contains instructions to configure the firewall to block all incoming traffic, except for specific TCP ports:
- Port 22 (SSH)
- Port 443 (HTTPS SSL)
- Port 80 (HTTP)

To apply this configuration, run the following commands:
```bash
sudo ufw default deny incoming
sudo ufw allow 22/tcp
sudo ufw allow 443/tcp
sudo ufw allow 80/tcp

### Configuration File: 100-port_forwarding
Configure web-01 so that its firewall redirects port 8080/TCP to port 80/TCP.
