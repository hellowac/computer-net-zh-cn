.. _c5:

Chapter 5 The Network Layer: Control Plane
============================================

Chapter 5 The Network Layer: Control Plane

.. tab:: 中文



.. tab:: 英文

   In this chapter, we’ll complete our journey through the network layer by covering the **control-plane**
   component of the network layer—the network-wide logic that controls not only how a datagram is
   forwarded among routers along an end-to-end path from the source host to the destination host, but also
   how network-layer components and services are configured and managed. In :ref:`Section 5.2 <c5.2>`, we’ll cover
   traditional routing algorithms for computing least cost paths in a graph; these algorithms are the basis
   for two widely deployed Internet routing protocols: OSPF and BGP, that we’ll cover in :ref:`Sections 5.3 <c5.3>` and
   :ref:`5.4 <c5.4>`, respectively. As we’ll see, OSPF is a routing protocol that operates within a single ISP’s network.
   BGP is a routing protocol that serves to interconnect all of the networks in the Internet; BGP is thus
   often referred to as the “glue” that holds the Internet together. Traditionally, control-plane routing
   protocols have been implemented together with data-plane forwarding functions, monolithically, within a
   router. As we learned in the introduction to :ref:`Chapter 4 <c4>`, software-defined networking (SDN) makes a
   clear separation between the data and control planes, implementing control-plane functions in a
   separate “controller” service that is distinct, and remote, from the forwarding components of the routers
   it controls. We’ll cover SDN controllers in :ref:`Section 5.5 <c5.5>`.

   In :ref:`Sections 5.6 <c5.6>` and :ref:`5.7 <c5.7>` we’ll cover some of the nuts and bolts of managing an IP network: ICMP (the
   Internet Control Message Protocol) and SNMP (the Simple Network Management Protocol).


.. toctree::
   :maxdepth: 2
   :caption: 内容

   ./s1.rst
   ./s2.rst
   ./s3.rst
   ./s5.rst
   ./s4.rst
   ./s6.rst
   ./s7.rst
   ./summary.rst
   ./homework.rst
   ./wiresharklab.rst
   ./interview.rst
