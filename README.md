[![Build Status](https://travis-ci.org/rahul0705/ansible-rtorrent.svg?branch=master)](https://travis-ci.org/rahul0705/ansible-rtorrent)

Ansible rTorrent
=========

Ansible role to install and configure rTorrent

Requirements
------------

Debian LTS
Ubuntu LTS

Role Variables
--------------

```yaml
rtorrent_user: rtorrent
rtorrent_group: rtorrent
rtorrent_user_home: /home/{{ rtorrent_user }}

rtorrent_min_peers: 40
rtorrent_max_peers: 100
rtorrent_min_peers_seed: 10
rtorrent_max_peers_seed: 50
rtorrent_max_uploads: 15
rtorrent_download_rate: 0
rtorrent_upload_rate: 0

rtorrent_default_directories:
  download:
    path: "{{ rtorrent_user_home }}/download"
    user: "{{ rtorrent_user }}"
    group: "{{ rtorrent_group }}"
  session:
    path: "{{ rtorrent_user_home }}/session"
    user: "{{ rtorrent_user }}"
    group: "{{ rtorrent_group }}"
  watch:
    path: "{{ rtorrent_user_home }}/watch"
    user: "{{ rtorrent_user }}"
    group: "{{ rtorrent_group }}"

rtorrent_schedule_watch_directory: watch_directory,5,5,load.start={{ rtorrent_directory_watch }}/*.torrent
rtorrent_schedule_untied_directory: untied_directory,5,5,stop_untied=

rtorrent_port_range: 46157-47169
rtorrent_port_random: "yes"

rtorrent_check_hash: "no"
rtorrent_use_udp_trackers: "yes"
rtorrent_encryption: allow_incoming,enable_retry,prefer_plaintext
rtorrent_dht: disable
rtorrent_dht_port: 6881
rtorrent_peer_exchange: "yes"

rtorrent_scgi_set: True
rtorrent_scgi_ip: 127.0.0.1
rtorrent_scgi_port: 5001
```

Dependencies
------------

None

Example Playbook
----------------

1) Install rTorrent with default settings

```yaml
- hosts: all
  roles:
    - role: rtorrent
```

2) Install rTorrent with custom settings

```yaml
- hosts: all
  roles:
    - role: rtorrent
      rtorrent_user: rahul
      rtorrent_user_home: /opt/rahul
      rtorrent_scgi_set: False
```

License
-------

MIT
