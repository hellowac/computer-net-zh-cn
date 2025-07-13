.. _c7:


第 7 章 无线与移动网络
=========================

Chapter 7 Wireless and Mobile Networks

在电话通信领域，过去的 20 年可以说是蜂窝电话的黄金时代。全球移动蜂窝用户数量从 1993 年的 3400 万增加到 2014 年的近 70 亿，蜂窝用户数量现已超过有线电话线数量。现在，移动电话订阅数甚至超过了地球上的人口总数。手机的诸多优势显而易见——随时随地通过高度便携、轻量化的设备，无线接入全球电话网络。近年来，笔记本电脑、智能手机和平板电脑通过蜂窝网络或 WiFi 无线连接到互联网。越来越多的设备，如游戏主机、温控器、家庭安防系统、家电、手表、眼镜、汽车、交通控制系统等，也正在无线连接到互联网。

从网络角度来看，这些无线和移动设备带来的挑战，尤其是在链路层和网络层，与传统有线计算机网络的差异极大，因此专门设立一章来研究无线与移动网络（即本章）是非常合适的。

本章开始将讨论移动用户、无线链路和网络，以及它们与所连接的更大规模（通常是有线）网络的关系。我们将区分无线链路的无线特性带来的挑战和这些无线链路所实现的移动性带来的挑战。明确区分“无线”和“移动”这两个重要概念，将有助于我们更好地隔离、识别并掌握各自领域的关键概念。需要注意的是，确实存在许多网络环境中网络节点是无线的，但并不移动（例如无线家用或办公网络中的固定工作站和大型显示设备），也存在不需要无线链路的有限形式的移动性（例如员工在家使用有线笔记本电脑，关闭电脑后开车上班，再将笔记本接入公司有线网络）。当然，许多最令人兴奋的网络环境是用户既无线又移动的场景——比如一个移动用户（如汽车后座的乘客）以每小时 160 公里的速度在高速公路上保持语音 IP 通话和多个 TCP 连接的场景，未来还可能是在自动驾驶车辆中。正是在无线与移动交汇之处，我们将面临最有趣的技术挑战！

我们将以示例说明考虑无线通信和移动性的环境——无线（可能是移动的）用户通过网络边缘的无线链路连接到更大的网络基础设施。随后在 :ref:`第 7.2 节 <c7.2>` 中，我们将讨论该无线链路的特性。我们在 :ref:`第 7.2 节 <c7.2>` 中简要介绍码分多址（CDMA），这是一种常用于无线网络的共享介质访问协议。在 :ref:`第 7.3 节 <c7.3>` 中，我们将深入探讨 IEEE 802.11（WiFi）无线局域网标准的链路层方面；同时也会简要介绍蓝牙及其他无线个人区域网络。在 :ref:`第 7.4 节 <c7.4>` 中，我们将概述蜂窝互联网接入，包括提供语音和高速互联网接入的 3G 及新兴 4G 蜂窝技术。在 :ref:`第 7.5 节 <c7.5>` 中，我们将关注移动性，重点讨论定位移动用户、向移动用户路由以及动态将移动用户从一个网络连接点“切换”到另一个连接点的问题。我们将在 :ref:`第 7.6 节 <c7.6>` 和 :ref:`第 7.7 节 <c7.7>` 中，分别考察这些移动性服务在企业 802.11 网络的移动 IP 标准和 LTE 蜂窝网络中的实现。最后，在 :ref:`第 7.8 节 <c7.8>` 中，我们将讨论无线链路和移动性对传输层协议和网络应用的影响。

.. toggle::

   In the telephony world, the past 20 years have arguably been the golden years of cellular telephony.
   The number of worldwide mobile cellular subscribers increased from 34 million in 1993 to nearly 7.0
   billion subscribers by 2014, with the number of cellular subscribers now surpassing the number of wired
   telephone lines. There are now a larger number of mobile phone subscriptions than there are people on
   our planet. The many advantages of cell phones are evident to all—anywhere, anytime, untethered
   access to the global telephone network via a highly portable lightweight device. More recently, laptops,
   smartphones, and tablets are wirelessly connected to the Internet via a cellular or WiFi network. And
   increasingly, devices such as gaming consoles, thermostats, home security systems, home appliances,
   watches, eye glasses, cars, traffic control systems and more are being wirelessly connected to the
   Internet.

   From a networking standpoint, the challenges posed by networking these wireless and mobile devices,
   particularly at the link layer and the network layer, are so different from traditional wired computer
   networks that an individual chapter devoted to the study of wireless and mobile networks (i.e., this
   chapter) is appropriate.

   We’ll begin this chapter with a discussion of mobile users, wireless links, and networks, and their
   relationship to the larger (typically wired) networks to which they connect. We’ll draw a distinction
   between the challenges posed by the ­wireless nature of the communication links in such networks,
   and by the mobility that these wireless links enable. Making this important distinction—between wireless
   and mobility—will allow us to better isolate, identify, and master the key concepts in each area. Note
   that there are indeed many networked environments in which the network nodes are wireless but not
   mobile (e.g., wireless home or office networks with stationary workstations and large displays), and that
   there are limited forms of mobility that do not require wireless links (e.g., a worker who uses a wired
   laptop at home, shuts down the laptop, drives to work, and attaches the laptop to the company’s wired
   network). Of course, many of the most exciting networked environments are those in which users are
   both wireless and mobile—for example, a scenario in which a mobile user (say in the back seat of car)
   maintains a Voice-over-IP call and multiple ongoing TCP connections while racing down the autobahn at
   160 kilometers per hour, soon in an autonomous vehicle. It is here, at the intersection of wireless and
   mobility, that we’ll find the most interesting technical challenges!

   We’ll begin by illustrating the setting in which we’ll consider wireless communication and mobility—a
   network in which wireless (and possibly mobile) users are connected into the larger network
   infrastructure by a wireless link at the network’s edge. We’ll then consider the characteristics of this
   wireless link in :ref:`Section 7.2 <c7.2>`. We include a brief introduction to code division multiple access (CDMA), a
   shared-medium access protocol that is often used in wireless networks, in :ref:`Section 7.2 <c7.2>`. In :ref:`Section 7.3 <c7.3>`,
   we’ll examine the link-level aspects of the IEEE 802.11 (WiFi) wireless LAN standard in some depth;
   we’ll also say a few words about Bluetooth and other wireless personal area networks. In :ref:`Section 7.4 <c7.4>`,
   we’ll provide an overview of cellular Internet access, including 3G and emerging 4G cellular
   technologies that provide both voice and high-speed Internet access. In :ref:`Section 7.5 <c7.5>`, we’ll turn our
   attention to mobility, focusing on the problems of locating a mobile user, routing to the mobile user, and
   “handing off” the mobile user who dynamically moves from one point of attachment to the network to
   another. We’ll examine how these mobility services are implemented in the mobile IP standard in
   enterprise 802.11 networks, and in LTE cellular networks in :ref:`Section 7.6 <c7.6>` and :ref:`7.7 <c7.7>` , respectively. Finally,
   we’ll consider the impact of wireless links and mobility on transport-layer protocols and networked
   applications in :ref:`Section 7.8 <c7.8>`.


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
   ./s8.rst
   ./summary.rst
   ./homework.rst
   ./wiresharklab.rst
   ./interview.rst