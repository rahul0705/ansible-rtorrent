import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_rtorrent_is_installed(host):
    rtorrent = host.package('rtorrent')

    assert rtorrent.is_installed


def test_rtorrent_running_and_enabled(host):
    rtorrent = host.service('rtorrent')

    assert rtorrent.is_running
    assert rtorrent.is_enabled


def test_tmux_is_installed(host):
    tmux = host.package('tmux')

    assert tmux.is_installed
