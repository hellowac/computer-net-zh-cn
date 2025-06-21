.. _c5.8:


5.8 总结
=================

5.8 Summary

.. tab:: 中文

.. tab:: 英文

We have now completed our two-chapter journey into the network core—a journey that began with our study of the network layer’s data plane in :ref:`Chapter 4 <c4>` and finished here with our study of the network layer’s control plane. We learned that the control plane is the network-wide logic that controls not only how a datagram is forwarded among routers along an end-to-end path from the source host to the destination host, but also how network-layer components and services are configured and managed.

We learned that there are two broad approaches towards building a control plane: traditional per-router control (where a routing algorithm runs in each and every router and the routing component in the router communicates with the routing components in other routers) and software-defined networking (SDN) control (where a logically centralized controller computes and distributes the forwarding tables to be used by each and every router). We studied two fundamental routing algorithms for computing least cost paths in a graph—link-state routing and distance-vector routing—in :ref:`Section 5.2 <c5.2>`; these algorithms find application in both per-router control and in SDN control. These algorithms are the basis for two widely- deployed Internet routing protocols, OSPF and BGP, that we covered in :ref:`Sections 5.3 <c5.3>` and :ref:`5.4 <c5.4>`. We covered the SDN approach to the network-layer control plane in :ref:`Section 5.5 <c5.5>`, investigating SDN network-control applications, the SDN controller, and the OpenFlow protocol for communicating between the controller and SDN-controlled devices. In :ref:`Sections 5.6 <c5.6>` and :ref:`5.7 <c5.7>`, we covered some of the nuts and bolts of managing an IP network: ICMP (the Internet Control Message Protocol) and SNMP (the Simple Network Management Protocol).

Having completed our study of the network layer, our journey now takes us one step further down the protocol stack, namely, to the link layer. Like the network layer, the link layer is part of each and every network-connected device. But we will see in the next chapter that the link layer has the much more localized task of moving packets between nodes on the same link or LAN. Although this task may appear on the surface to be rather simple compared with that of the network layer’s tasks, we will see that the link layer involves a number of important and fascinating issues that can keep us busy for a long time.