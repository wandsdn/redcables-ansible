# Ansible Role: bearwall2

An ansible role that installs [bearwall2](https://bearwall.org) on Debian/Ubuntu.

## Role Variables

Available variables are listed below, see `defaults/main.yml` for default values.

  * For NAT to work properly with bearwall2 a recent version of the linux kernel
    and nftables is required. Setting the below variables to true will cause
    the right versions to be installed on Debian Buster. On Ubuntu please use
    version 20.04+.

        bearwall2_enable_backports: true
        bearwall2_backport_kernel_nftables: true

  * Bearwall2 rulesets can be defined by adding them to `bearwall2_rulesets`:

        bearwall2_rulesets:
          - name: martians
            policies:
              - policy_log ip saddr {192.168.0.0/16, 10.0.0.0/8, 172.16.0.0/12} reject
              - policy_log ip daddr {192.168.0.0/16, 10.0.0.0/8, 172.16.0.0/12} reject

  * Bearwall2 classes can be defined by adding them to `bearwall2_classes`:

        bearwall2_classes:
          - name: internal
            policies: |
              policy inout accept
              policy forward accept
            if_features:
              disable_ipv6: 0
              autoconf: 1
              rp_filter: 1
              accept_redirects: 1
              accept_source_route: 1
              bootp_relay: 0
              accept_ra: 0
              forwarding: 1
              log_martians: 0
              send_redirects: 1

  * Bearwall2 options (/etc/bearwall2/bearwall2.conf) can be defined by adding
    them to `bearwall2_options`:

        bearwall2_options:
            logging: "nflog"
            conntrack: "stateful"
            missing: "withhold"
            rollback_delay: "30"

  * Bearwall2 interfaces can be defined by adding them to `bearwall2_interfaces`.
    An interface can be defined in two different ways.

    1. By inheriting from a class:

           bearwall2_interfaces:
             - name: eth0
               class: internal
             - name: eth1
               class: external

    2. By defining a custom set of policies for that interface:

           bearwall2_interfaces:
             - name: eth0
               policies: |
                 policy inout accept
               if_features:
                 disable_ipv6: 0
                 autoconf: 0
                 rp_filter: 1
                 accept_redirects: 0
                 accept_source_route: 0
                 bootp_relay: 0
                 accept_ra: 0
                 forwarding: 0
                 log_martians: 0
                 send_redirects: 0
