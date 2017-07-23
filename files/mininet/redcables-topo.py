"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class Redcables( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        host1 = self.addHost( 'h1' )
        host2 = self.addHost( 'h2' )
        host3 = self.addHost( 'h3' )

        ovs = self.addSwitch( 'ovs', dpid='0000000000000046' )
        at = self.addSwitch( 'at', dpid='0000eccd6df7d4aa' )
        aruba = self.addSwitch( 'aruba', dpid='0000285261a18100' )
        cisco = self.addSwitch( 'cisco', dpid='00019cdc7192a6c0' )

        # Add links
        self.addLink( ovs, at)
        self.addLink( ovs, aruba)
        self.addLink( ovs, cisco)
        self.addLink( at, host1 )
        self.addLink( aruba, host2 )
        self.addLink( cisco, host3 )

topos = { 'redcables': ( lambda: Redcables() ) }
