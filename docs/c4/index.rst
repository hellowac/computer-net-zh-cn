.. _c4:


第 4 章 网络层：数据平面
============================================

Chapter 4 The Network Layer: Data Plane

We learned in the previous chapter that the transport layer provides various forms of process-to-process
communication by relying on the network layer’s host-to-host communication service. We also learned
that the transport layer does so without any knowledge about how the network layer actually implements
this service. So perhaps you’re now wondering, what’s under the hood of the host-to-host
communication service, what makes it tick?

In this chapter and the next, we’ll learn exactly how the network layer can provide its host-to-host
communication service. We’ll see that unlike the transport and application layers, there is a piece of the
network layer in each and every host and router in the network. Because of this, network-layer protocols
are among the most challenging (and therefore among the most interesting!) in the protocol stack.

Since the network layer is arguably the most complex layer in the protocol stack, we’ll have a lot of
ground to cover here. Indeed, there is so much to cover that we cover the network layer in two chapters.
We’ll see that the network layer can be decomposed into two interacting parts, the **data plane** and the
**control plane**. In :ref:`Chapter 4 <c4>` , we’ll first cover the data plane functions of the network layer—the per-
router functions in the network layer that determine how a datagram (that is, a network-layer packet)
arriving on one of a router’s input links is forwarded to one of that router’s output links. We’ll cover both
traditional IP forwarding (where forwarding is based on a datagram’s destination address) and
generalized forwarding (where forwarding and other functions may be performed using values in several
different fields in the datagram’s header). We’ll study the IPv4 and IPv6 protocols and addressing in
detail. In :ref:`Chapter 5 <c5>` , we’ll cover the control plane functions of the network layer—the network-wide logic
that controls how a datagram is routed among routers along an end-to-end path from the source host to
the destination host. We’ll cover routing algorithms, as well as routing protocols, such as OSPF and
BGP, that are in widespread use in today’s Internet. Traditionally, these control-plane routing protocols
and data-plane forwarding functions have been implemented together, monolithically, within a router.
Software-defined networking (SDN) explicitly separates the data plane and control plane by
implementing these control plane functions as a separate service, typically in a remote “controller.” We’ll
also cover SDN controllers in :ref:`Chapter 5 <c5>` .

This distinction between data-plane and control-plane functions in the network layer is an important
concept to keep in mind as you learn about the network layer —it will help structure your thinking aboutthe network layer and reflects a modern view of the network layer’s role in computer networking.

.. toggle::

    在上一章中我们了解到，传输层依赖网络层提供的主机到主机通信服务，来实现多种形式的进程到进程通信。我们还了解到，传输层在实现这些服务时，并不需要了解网络层具体是如何提供这些服务的。那么，也许你现在会好奇：主机到主机通信服务的“引擎盖下”究竟是什么？又是什么机制让它运转起来？

    在本章及下一章中，我们将深入学习网络层是如何实现主机到主机通信服务的。我们将看到，与传输层和应用层不同，网络层的组件存在于网络中的每一台主机和路由器中。正因为如此，网络层的协议是整个协议栈中最具挑战性（因此也最有趣！）的一部分。

    由于网络层可以说是协议栈中最复杂的一层，因此我们需要讨论的内容也很多。实际上，内容之多使得我们将网络层分为两章进行讲解。我们将看到，网络层可以被分解为两个相互协作的部分： **数据平面（data plane）** 与 **控制平面（control plane）**。在 :ref:`第 4 章 <c4>` 中，我们首先介绍网络层的数据平面功能——即在每台路由器中执行的功能，用于决定到达某一输入链路的数据报（即网络层分组）将被转发到该路由器的哪一输出链路。我们将介绍传统的 IP 转发方式（基于数据报的目的地址进行转发），以及更通用的转发方式（即根据数据报头中多个字段的值执行转发及其他功能）。我们还将详细讲解 IPv4 和 IPv6 协议及其地址结构。

    而在 :ref:`第 5 章 <c5>` 中，我们将介绍网络层的控制平面功能——也就是控制数据报在源主机与目标主机之间的路由器路径上如何被路由的网络范围内的逻辑。我们将讲解路由算法，以及在当今因特网中广泛使用的路由协议，如 OSPF 和 BGP。传统上，这些控制平面的路由协议与数据平面的转发功能是作为整体在路由器中实现的。而软件定义网络（SDN）则显式地将数据平面与控制平面分离，将控制平面功能实现为一个独立服务，通常运行在远程的“控制器”中。我们将在 :ref:`第 5 章 <c5>` 中进一步介绍 SDN 控制器。

    在学习网络层的过程中，牢记网络层中数据平面与控制平面功能的区分，是一个非常重要的概念。它不仅能帮助你更清晰地构建对网络层的理解，也体现了对网络层在现代计算机网络中角色的前沿认知。


.. toctree::
   :maxdepth: 2
   :caption: 内容

   ./s1.rst
   ./s2.rst
   ./s3.rst
   ./s4.rst
   ./summary.rst
   ./homework.rst
   ./wiresharklab.rst
   ./interview.rst