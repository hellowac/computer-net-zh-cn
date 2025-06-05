.. _c6:


第 6 章 链路层和 LAN
============================================

Chapter 6 The Link Layer and LANs

.. tab:: 中文



.. tab:: 英文

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

