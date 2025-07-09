.. _c4.5:


4.5 小结
=================
4.5 Summary

在本章中，我们讲解了网络层的 **数据平面** 功能 —— 即每台路由器上的功能，这些功能决定了如何将到达某个输入链路的分组转发到该路由器的某个输出链路。我们首先详细考察了路由器的内部操作，研究了输入和输出端口的功能以及基于目的地址的转发机制、路由器的内部交换结构、分组队列管理等内容。我们涵盖了传统的 IP 转发（其中转发基于数据报的目的地址）以及通用转发（其中转发和其他功能可基于数据报首部中的多个不同字段值执行），并看到了后一种方式的灵活性。我们还详细研究了 IPv4 和 IPv6 协议，以及互联网地址机制，这一机制比我们原先预期的更深入、更微妙，也更有趣。

通过对网络层数据平面的深入理解，我们现在已准备好进入 :ref:`第 5 章 <c5>`，探索网络层的控制平面！

.. toggle::

    In this chapter we’ve covered the **data plane** functions of the network layer—the per-router functions that determine how packets arriving on one of a router’s input links are forwarded to one of that router’s output links. We began by taking a detailed look at the internal operations of a router, studying input and output port functionality and destination-based forwarding, a router’s internal switching mechanism, packet queue management and more. We covered both traditional IP forwarding (where forwarding is based on a datagram’s destination address) and generalized forwarding (where forwarding and other functions may be performed using values in several different fields in the datagram’s header) and seen the versatility of the latter approach. We also studied the IPv4 and IPv6 protocols in detail, and Internet addressing, which we found to be much deeper, subtler, and more interesting than we might have expected.

    With our newfound understanding of the network-layer’s data plane, we’re now ready to dive into the network layer’s control plane in :ref:`Chapter 5 <c5>`!