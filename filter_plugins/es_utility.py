# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

def ansible_ssh_host_list(hostnames, hostvars):
    result = []
    for hostname in hostnames:
        if hostname in hostvars:
            result.append(hostvars[hostname]['ansible_ssh_host'])

    return result

def es_ip_list(hostnames, hostvars):
    result = []
    for hostname in hostnames:
        if hostname in hostvars:
            ip = hostvars[hostname]['es_host'] or hostvars[hostname]['ansible_ssh_host']
            result.append(ip)

    return result

class FilterModule(object):
    ''''''

    def filters(self):
        return {
                'es_ip_list': es_ip_list,
                'ansible_ssh_host_list': ansible_ssh_host_list
                }
