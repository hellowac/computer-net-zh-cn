.. _c7:

Chapter 7 Wireless and Mobile Networks
============================================

Chapter 7 Wireless and Mobile Networks

.. tab:: 中文



.. tab:: 英文

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
   ./summary.rst
   ./homework.rst
   ./wiresharklab.rst
   ./interview.rst