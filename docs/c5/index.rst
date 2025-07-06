.. _c5:


第 5 章 网络层：控制平面
============================================

Chapter 5 The Network Layer: Control Plane

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

.. toggle::

   在本章中，我们将完成对网络层的探索，重点介绍网络层中的 **控制平面（control-plane）** 组件——即网络范围内的逻辑，用于控制数据报如何从源主机沿着端到端路径被路由器转发到目标主机，同时也负责网络层组件与服务的配置和管理。在 :ref:`第 5.2 节 <c5.2>` 中，我们将介绍用于在图中计算最小代价路径的传统路由算法；这些算法构成了两个广泛部署的因特网路由协议——OSPF 和 BGP（我们将在 :ref:`第 5.3 节 <c5.3>` 和 :ref:`第 5.4 节 <c5.4>` 中分别介绍）的基础。

   正如我们将看到的，OSPF 是一种在单个 ISP 网络内部运行的路由协议。而 BGP 是用于连接因特网中所有网络的路由协议；因此 BGP 通常被称为“连接因特网的胶水”。传统上，控制平面中的路由协议与数据平面中的转发功能是作为整体在路由器中实现的。如我们在 :ref:`第 4 章 <c4>` 引言中所学到的，软件定义网络（SDN）将数据平面与控制平面明确分离，将控制平面功能实现为独立的“控制器”服务，该控制器不同于并且远离它所控制的路由器中的转发组件。我们将在 :ref:`第 5.5 节 <c5.5>` 中介绍 SDN 控制器。

   在 :ref:`第 5.6 节 <c5.6>` 和 :ref:`第 5.7 节 <c5.7>` 中，我们将介绍管理 IP 网络的一些具体机制：包括 ICMP（因特网控制报文协议）和 SNMP（简单网络管理协议）。


.. toctree::
   :maxdepth: 2
   :caption: 内容

   ./s1.rst
   ./s2.rst
   ./s3.rst
   ./s4.rst
   ./s5.rst
   ./s6.rst
   ./s7.rst
   ./summary.rst
   ./homework.rst
   ./wiresharklab.rst
   ./interview.rst
