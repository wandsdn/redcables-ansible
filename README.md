### NZNOG Network Ansible Playbooks

This repo contains a set of ansible playbooks and roles for deploying your own
SDN/NFV conference network in a box. This repo was used to deploy the conference
wifi for the [NZNOG17](http://www.nznog.org/) conference.

For a high level overview of the architecture of this network and a set of
hardware requirements see our [conference-sdn-nfv-network](https://github.com/wandsdn/conference-sdn-nfv-network) repo.

### Playbook structure

The structure of this repo is based on the [Ansible Best Practices](https://docs.ansible.com/ansible/playbooks_best_practices.html)
documentation, they explain how each file is used and how inventory and roles work.

### Customisation

To customise how the network is deployed you can modify the roles assigned to
each VM in the **site.yaml** file, or modify the configs individually in the various
**roles/\*/files** directories.

The **production** file is your inventory file that tells ansible how to login
to each machine via SSH for deploys.

### Machine setup

First you will need a host machine to run the ALLBIRDS network, this machine
will have your DPDK NICs to provide an interface to the outside world. On this
host deploy 2 VMs (**FAUCET** and **NAT64**) for providing the various network
services. I've tested against ubuntu 16.10 (but other versions should also work).
These machines need to have python installed and you need to be able to SSH to
them so that ansible can work its magic.

### Deploying

These playbooks make use of features only available in Ansible 2.2 so make sure
you are using an up to date version installed from pip.

Run this command to deploy all the various network roles:

```bash
ansible-playbook -i production site.yaml
```

You can also provide the -l option to ansible-playbook to filter which machines
are deployed.
