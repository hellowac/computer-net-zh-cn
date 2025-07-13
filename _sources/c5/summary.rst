.. _c5.8:


5.8 小结
=================
5.8 Summary

我们已经完成了对网络核心层的两章学习之旅——这一旅程始于我们在 :ref:`第 4 章 <c4>` 对网络层数据平面的学习，并在本章对网络层控制平面的学习中画上句号。我们了解到，控制平面是网络范围内的逻辑，用于控制不仅数据报如何在路由器之间沿端到端路径从源主机转发到目的主机，还包括网络层组件和服务的配置与管理方式。

我们了解到，构建控制平面有两种广义方法：传统的每路由器控制（在每一个路由器中运行路由算法，并使路由器中的路由组件与其他路由器中的路由组件通信）和软件定义网络（SDN）控制（由逻辑上集中式的控制器计算并分发用于每个路由器的转发表）。我们在 :ref:`第 5.2 节 <c5.2>` 中学习了两种用于计算图中最小代价路径的基本路由算法——链路状态路由和距离向量路由；这两种算法在每路由器控制和 SDN 控制中均有应用。这些算法是我们在 :ref:`第 5.3 节 <c5.3>` 和 :ref:`第 5.4 节 <c5.4>` 中介绍的两个广泛部署的互联网路由协议——OSPF 和 BGP——的基础。

我们在 :ref:`第 5.5 节 <c5.5>` 中讲解了网络层控制平面的 SDN 方法，研究了 SDN 网络控制应用、SDN 控制器以及用于控制器与 SDN 控制设备之间通信的 OpenFlow 协议。在 :ref:`第 5.6 节 <c5.6>` 和 :ref:`第 5.7 节 <c5.7>` 中，我们讲解了管理 IP 网络的一些基础机制：ICMP（Internet 控制消息协议）和 SNMP（简单网络管理协议）。

在完成了网络层的学习之后，我们的学习之旅将进一步深入协议栈，进入链路层。与网络层类似，链路层也是每一个网络连接设备的一部分。但我们将在下一章看到，链路层承担的任务更加局部化，即在同一链路或局域网（LAN）上的节点之间移动数据包。尽管与网络层的任务相比，这一任务表面上看起来相对简单，但我们将看到链路层涉及许多重要且引人入胜的问题，这些问题足以让我们研究很长一段时间。

.. toggle::

    We have now completed our two-chapter journey into the network core—a journey that began with our study of the network layer’s data plane in :ref:`Chapter 4 <c4>` and finished here with our study of the network layer’s control plane. We learned that the control plane is the network-wide logic that controls not only how a datagram is forwarded among routers along an end-to-end path from the source host to the destination host, but also how network-layer components and services are configured and managed.

    We learned that there are two broad approaches towards building a control plane: traditional per-router control (where a routing algorithm runs in each and every router and the routing component in the router communicates with the routing components in other routers) and software-defined networking (SDN) control (where a logically centralized controller computes and distributes the forwarding tables to be used by each and every router). We studied two fundamental routing algorithms for computing least cost paths in a graph—link-state routing and distance-vector routing—in :ref:`Section 5.2 <c5.2>`; these algorithms find application in both per-router control and in SDN control. These algorithms are the basis for two widely- deployed Internet routing protocols, OSPF and BGP, that we covered in :ref:`Sections 5.3 <c5.3>` and :ref:`5.4 <c5.4>`. We covered the SDN approach to the network-layer control plane in :ref:`Section 5.5 <c5.5>`, investigating SDN network-control applications, the SDN controller, and the OpenFlow protocol for communicating between the controller and SDN-controlled devices. In :ref:`Sections 5.6 <c5.6>` and :ref:`5.7 <c5.7>`, we covered some of the nuts and bolts of managing an IP network: ICMP (the Internet Control Message Protocol) and SNMP (the Simple Network Management Protocol).

    Having completed our study of the network layer, our journey now takes us one step further down the protocol stack, namely, to the link layer. Like the network layer, the link layer is part of each and every network-connected device. But we will see in the next chapter that the link layer has the much more localized task of moving packets between nodes on the same link or LAN. Although this task may appear on the surface to be rather simple compared with that of the network layer’s tasks, we will see that the link layer involves a number of important and fascinating issues that can keep us busy for a long time.