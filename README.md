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
rtorrent_home: /home/{{ rtorrent_user }}

rtorrent_min_peers: 40
rtorrent_max_peers: 100
rtorrent_min_peers_seed: 10
rtorrent_max_peers_seed: 50
rtorrent_max_uploads: 15
rtorrent_download_rate: 0
rtorrent_upload_rate: 0

rtorrent_directory_download: "{{ rtorrent_home }}/download"
rtorrent_directory_session: "{{ rtorrent_home }}/session"
rtorrent_directory_watch: "{{ rtorrent_home }}/watch"

rtorrent_schedule_watch_directory: watch_directory,5,5,load_start={{ rtorrent_directory_watch }}/*.torrent
rtorrent_schedule_untied_directory: untied_directory,5,5,stop_untied=

rtorrent_port_range: 46157-47169
rtorrent_port_random: "yes"

rtorrent_check_hash: "no"
rtorrent_use_udp_trackers: "yes"
rtorrent_encryption: allow_incoming,enable_retry,prefer_plaintext
rtorrent_dht: disable
rtorrent_dht_port: 6881
rtorrent_peer_exchange: "yes"
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
      rtorrent_home: /opt/rahul
```

License
-------

MIT
