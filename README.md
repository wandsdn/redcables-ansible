### Redcables Network Ansible Playbooks

This repo contains the set of ansible playbooks and roles for managing
the Redcables network, at the University of Waikato.

It was originally based on a deployment at wifi for the
[NZNOG17](http://www.nznog.org/) conference. You can find out
more about that deployment at
[conference-sdn-nfv-network](https://github.com/wandsdn/conference-sdn-nfv-network) repo.

To learn how ansible works the [Ansible Getting Started](https://docs.ansible.com/ansible/intro_getting_started.html)
guide is a good place to start.

### Playbook structure

The structure of this repo is based on the [Ansible Best Practices](https://docs.ansible.com/ansible/playbooks_best_practices.html)
documentation, they explain how each file is used and how inventory and roles work.

### Customisation

To customise how the network is deployed you can modify the roles assigned to
each VM in the **site.yaml** file, you will also want to modify the user-customisable
configurations in the [files](files) directory.

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
