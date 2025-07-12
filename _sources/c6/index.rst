.. _c6:


第 6 章 链路层与局域网（LANs）
============================================

Chapter 6 The Link Layer and LANs

在前两章中，我们了解到网络层提供了任意两个网络主机之间的通信服务。在这两个主机之间，数据报通过一系列通信链路（包括有线和无线链路）传输，从源主机开始，经过一系列分组交换设备（交换机和路由器），最终抵达目标主机。当我们继续沿着协议栈向下，从网络层进入链路层时，我们自然会好奇：分组究竟是如何在构成端到端通信路径的各个链路上传输的？网络层数据报是如何被封装进链路层帧中，以便在单个链路上传输的？在通信路径的不同链路中，是否使用不同的链路层协议？广播链路中传输冲突是如何解决的？链路层是否也有地址机制？如果有，它与我们在 :ref:`第 4 章 <c4>` 学到的网络层地址机制又是如何协作的？交换机和路由器到底有什么区别？本章将解答这些重要问题。

在讨论链路层时，我们将看到链路层信道主要分为两种基本类型。第一类是广播信道，它连接多个主机，常见于无线局域网、卫星网络以及混合光纤同轴电缆（HFC）接入网络。由于多个主机共享同一广播通信信道，因此需要一种所谓的“介质访问协议”来协调帧的发送。在某些情况下，会使用中心控制器协调传输；而在其他情况下，则由主机之间自行协调。第二类链路层信道是点对点通信链路，例如两个路由器之间通过长距离链路相连，或用户办公电脑与附近以太网交换机之间的连接。在这种情况下，访问协调更为简单；本书网站上的参考资料中提供了对点对点协议（PPP）的详细讨论，该协议可用于从拨号电话线服务到光纤高速点对点帧传输的各种场景。

在本章中，我们将探讨多个重要的链路层概念与技术。我们将更深入地研究差错检测与纠正，这是我们在 :ref:`第 3 章 <c3>` 中简要提到的一个主题。我们还将研究多路访问网络和交换式局域网，包括以太网——迄今为止最广泛使用的有线局域网技术。此外，我们还将介绍虚拟局域网（VLAN）和数据中心网络。尽管 WiFi 以及更广义的无线局域网也是链路层主题，但我们会将这部分重要内容留待 :ref:`第 7 章 <c7>` 进一步讨论。

.. toggle::

   In the previous two chapters we learned that the network layer provides a communication service
   between any two network hosts. Between the two hosts, datagrams travel over a series of
   communication links, some wired and some wireless, starting at the source host, passing through a
   series of packet switches (switches and routers) and ending at the destination host. As we continue
   down the protocol stack, from the network layer to the link layer, we naturally wonder how packets are
   sent across the individual links that make up the end-to-end communication path. How are the network-
   layer datagrams encapsulated in the link-layer frames for transmission over a single link? Are different
   link-layer protocols used in the different links along the communication path? How are transmission
   conflicts in broadcast links resolved? Is there addressing at the link layer and, if so, how does the link-
   layer addressing operate with the network-layer addressing we learned about in :ref:`Chapter 4 <c4>` ? And what
   exactly is the difference between a switch and a router? We’ll answer these and other important
   questions in this chapter.

   In discussing the link layer, we’ll see that there are two fundamentally ­different types of link-layer
   channels. The first type are broadcast channels, which connect multiple hosts in wireless LANs, satellite
   networks, and hybrid fiber-coaxial cable (HFC) access networks. Since many hosts are connected to the
   same broadcast communication channel, a so-called medium access protocol is needed to coordinate
   frame transmission. In some cases, a central controller may be used to coordinate transmissions; in
   other cases, the hosts themselves coordinate transmissions. The second type of link-layer channel is
   the point-to-point communication link, such as that often found between two routers connected by a
   long-distance link, or between a user’s office computer and the nearby Ethernet switch to which it is
   connected. Coordinating access to a point-to-point link is simpler; the reference material on this book’s
   Web site has a detailed discussion of the Point-to-Point Protocol (PPP), which is used in settings
   ranging from dial-up service over a telephone line to high-speed point-to-point frame transport over
   fiber-optic links.

   We’ll explore several important link-layer concepts and technologies in this ­chapter. We’ll dive deeper
   into error detection and correction, a topic we touched on briefly in :ref:`Chapter 3 <c3>` . We’ll consider multiple
   access networks and switched LANs, including Ethernet—by far the most prevalent wired LAN
   technology. We’ll also look at virtual LANs, and data center networks. Although WiFi, and more
   generally wireless LANs, are link-layer topics, we’ll postpone our study of these important topics until
   :ref:`Chapter 7 <c7>` .


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

