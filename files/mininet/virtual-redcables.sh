#!/usr/bin/env bash

service openvswitch-switch start
ovs-vsctl set-manager ptcp:6640

#mn --topo=tree,1 --mac --controller=remote,ip=faucet.redcables.wand.nz,port=6653 --switch ovsk,protocols=OpenFlow13

while true; do
    sleep 1
done

service openvswitch-switch stop
