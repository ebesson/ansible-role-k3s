import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('k3s-master')


def test_k3s_service(host):
    k3s = host.service("k3s")
    assert k3s.is_running


def test_kubectl_get_nodes(host):
    kubectl_get_nodes = host.run("kubectl get nodes")
    assert kubectl_get_nodes.rc == 0
    assert "master   Ready" in kubectl_get_nodes.stdout
#    assert "agent1   Ready" in kubectl_get_nodes.stdout
