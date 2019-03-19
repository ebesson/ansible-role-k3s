import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('k3s-agent')


def test_k3s_service(host):
    k3s = host.service("k3s")
    assert k3s.is_running
