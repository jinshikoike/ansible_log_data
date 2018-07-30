# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

def __extract_ip_list(hostvars, hostnames, ip_field_name, default_ip_filed_name='ansible_ssh_host'):
    result = []
    for hostname in hostnames:
        if hostname in hostvars:
            if ip_field_name in hostvars[hostname]:
                ip = hostvars[hostname][ip_field_name]
            else:
                ip = hostvars[hostname][default_ip_filed_name]
            result.append(ip)
    return result

def ansible_ssh_host_list(hostnames, hostvars):
    result = []
    for hostname in hostnames:
        if hostname in hostvars:
            result.append(hostvars[hostname]['ansible_ssh_host'])

    return result

def es_ip_list(hostnames, hostvars):
    return __extract_ip_list(hostvars, hostnames, 'es_host')

def kibana_ip_list(hostnames, hostvars):
    return __extract_ip_list(hostvars, hostnames, 'kibana_host')

def kafka_ip_list(hostnames, hostvars):
    return __extract_ip_list(hostvars, hostnames, 'kafka_host')

def remove_prefix(targets, prefix):
    result = []
    for target in targets:
        result.append(target.split('/')[1])
    return result

def calc_default_workers(number_of_cpus, topics_length):
    number_of_cpus = number_of_cpus or 1
    topics_length = topics_length or 1

    result = number_of_cpus/topics_length
    if result < 1:
        result = 1
    return result

class FilterModule(object):
    ''''''

    def filters(self):
        return {
                'es_ip_list': es_ip_list,
                'kibana_ip_list': kibana_ip_list,
                'kafka_ip_list': kafka_ip_list,
                'ansible_ssh_host_list': ansible_ssh_host_list,
                'remove_prefix': remove_prefix,
                'calc_default_workers': calc_default_workers
                }
