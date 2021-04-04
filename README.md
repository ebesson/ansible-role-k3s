# Ansible Role: k3s

[![Build Status](https://travis-ci.org/ebesson/ansible-role-k3s.svg?branch=master)](https://travis-ci.org/ebesson/ansible-role-k3s)

An Ansible Role that installs [k3s](https://k3s.io/).

## Requirements
None.

## Role Variables
Available variables are listed below, along with default values (see `defaults/main.yml`):

    k3s_state: present

State of role: `present`, `start`, `stop`

    k3s_version: 1.20.5+k3s1

Version of k3s

    k3s_type: master

Node type `master` or `agent`

    k3s_addtionnal_config:

Additional config for k3s start command

    k3s_master_node_address:

Address of master node

    k3s_cluster_token:

Token

## Dependencies
None.

## Example Playbook

```yaml
- hosts: k3s-master
  become: True
  vars:
    k3s_type: master
  roles:
    - ebesson.k3s

- hosts: k3s-agent
  become: True
  vars:
    k3s_type: agent
  roles:
    - ebesson.k3s
```

## License
Apache 2
