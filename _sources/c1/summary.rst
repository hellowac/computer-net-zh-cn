.. _c1.8:


1.8 小结
=================

1.8 Summary

在本章中，我们涵盖了大量的内容！我们考察了构成互联网（特别是）和计算机网络（总体而言）的各种硬件和软件组成部分。我们从网络的边缘开始，研究了终端系统和应用程序，以及为这些终端系统上的应用程序提供的传输服务。我们还研究了接入网络中常见的链路层技术和物理介质。接着我们深入网络内部，探讨了网络核心，将分组交换和电路交换识别为电信网络中传输数据的两种基本方式，并分析了每种方式的优缺点。我们还研究了全球互联网的结构，了解到互联网是由许多网络组成的网络。我们看到，互联网的分层结构由高层和低层 ISP 构成，这种结构使其可以扩展到成千上万个网络。

在本章的后半部分，我们考察了计算机网络领域的若干核心主题。我们首先分析了分组交换网络中延迟、吞吐量和分组丢失的原因。我们建立了传输、传播和排队延迟以及吞吐量的简单定量模型；我们将在本书的习题中广泛使用这些延迟模型。接下来，我们探讨了协议分层和服务模型，这是网络架构中的关键原则，后续章节中也会频繁引用。我们还概览了当前互联网上一些常见的安全攻击。最后，我们以计算机网络的简史结束了本章的介绍。第一章本身就构成了一个关于计算机网络的微型课程。

因此，我们在第一章中确实涵盖了大量内容！如果你感到有些信息量过大，不必担心。在接下来的章节中，我们将重新讨论所有这些概念，并以更深入的方式进行讲解（这是一种承诺，而不是威胁！）。此时，我们希望你能带着对构成网络的各种组成部分的逐步形成的直觉、对网络术语的逐步掌握（不要害羞，随时回来看这一章），以及不断增长的学习网络的兴趣结束本章。这将是我们在本书剩余部分的任务。

.. toggle::

    In this chapter we’ve covered a tremendous amount of material! We’ve looked at the various pieces of
    hardware and software that make up the Internet in particular and computer networks in general. We
    started at the edge of the network, looking at end systems and applications, and at the transport service
    provided to the applications running on the end systems. We also looked at the link-layer technologies
    and physical media typically found in the access network. We then dove deeper inside the network, into
    the network core, identifying packet switching and circuit switching as the two basic approaches for
    transporting data through a telecommunication network, and we examined the strengths and
    weaknesses of each approach. We also examined the structure of the global Internet, learning that the
    Internet is a network of networks. We saw that the Internet’s hierarchical structure, consisting of higher-
    and lower-tier ISPs, has allowed it to scale to include thousands of networks.

    In the second part of this introductory chapter, we examined several topics central to the field of
    computer networking. We first examined the causes of delay, throughput and packet loss in a packet-
    switched network. We developed simple quantitative models for transmission, propagation, and queuing
    delays as well as for throughput; we’ll make extensive use of these delay models in the homework
    problems throughout this book. Next we examined protocol layering and service models, key
    architectural principles in networking that we will also refer back to throughout this book. We also
    surveyed some of the more prevalent security attacks in the Internet day. We finished our introduction to
    networking with a brief history of computer networking. The first chapter in itself constitutes a mini-
    course in computer networking.

    So, we have indeed covered a tremendous amount of ground in this first chapter! If you’re a bit
    overwhelmed, don’t worry. In the following chapters we’ll revisit all of these ideas, covering them in
    much more detail (that’s a promise, not a threat!). At this point, we hope you leave this chapter with a
    still-developing intuition for the pieces that make up a network, a still-developing command of the
    vocabulary of networking (don’t be shy about referring back to this chapter), and an ever-growing desire
    to learn more about networking. That’s the task ahead of us for the rest of this book.

路线图：本书的结构
-----------------------------
Road-Mapping This Book

在开始任何一次旅行之前，你都应该先看看路线图，以便熟悉接下来的主要道路和关键节点。对于我们即将展开的这段旅程，其最终目标是深入理解计算机网络的“如何做”、“做什么”以及“为什么这么做”。我们的路线图就是本书各章节的顺序：

1. 计算机网络与互联网  
2. 应用层  
3. 运输层  
4. 网络层：数据平面  
5. 网络层：控制平面  
6. 链路层与局域网  
7. 无线与移动网络  
8. 计算机网络中的安全  
9. 多媒体网络  

:ref:`第 2 章 <c2>` 到 :ref:`第 6 章 <c6>` 是本书的五个核心章节。你会注意到这些章节围绕五层互联网协议栈中的前四层组织。此外，请注意我们的旅程将从互联网协议栈的顶层——即应用层——开始，然后逐层向下。这种自顶向下的安排是有道理的：一旦我们理解了应用，就可以理解为支持这些应用所需的网络服务；进而，我们可以探讨网络架构实现这些服务的各种方式。因此，早期讨论应用为整本书的其余内容提供了动机。

本书后半部分——:ref:`第 7 章 <c7>` 到 :ref:`第 9 章 <c9>`——聚焦于现代计算机网络中三个极为重要（且相对独立）的话题。在 :ref:`第 7 章 <c7>` 中，我们将研究无线与移动网络，包括无线局域网（WiFi 和蓝牙）、蜂窝网络（GSM、3G 和 4G）以及移动性（包括 IP 和 GSM 网络中的移动性）。:ref:`第 8 章 <c8>` 探讨计算机网络中的安全问题，首先介绍加密与网络安全的基础知识，然后考察这些基础理论在广泛互联网环境中的应用。最后一章，即多媒体网络部分，将研究音频与视频应用，如网络电话、视频会议和媒体流播放。我们还将探讨分组交换网络如何设计，以便为音频与视频应用提供一致的服务质量。


.. toggle::

    Before starting any trip, you should always glance at a road map in order to become familiar with the
    major roads and junctures that lie ahead. For the trip we are about to embark on, the ultimate
    destination is a deep understanding of the how, what, and why of computer networks. Our road map is
    the sequence of chapters of this book:

    1. Computer Networks and the Internet
    2. Application Layer
    3. Transport Layer
    4. Network Layer: Data Plane
    5. Network Layer: Control Plane
    6. The Link Layer and LANs
    7. Wireless and Mobile Networks
    8. Security in Computer Networks
    9. Multimedia Networking

    :ref:`Chapters 2 <c2>` through :ref:`6 <c6>` are the five core chapters of this book. You should notice that these chapters are
    organized around the top four layers of the five-layer Internet protocol. Further note that our journey will
    begin at the top of the Internet protocol stack, namely, the application layer, and will work its way
    downward. The rationale behind this top-down journey is that once we understand the applications, we
    can understand the network services needed to support these applications. We can then, in turn,
    examine the various ways in which such services might be implemented by a network architecture.
    Covering applications early thus provides motivation for the remainder of the text.

    The second half of the book— :ref:`Chapters 7 <c7>` through :ref:`9 <c9>` —zooms in on three enormously important (and
    somewhat independent) topics in modern computer networking. In :ref:`Chapters 7 <c7>`, we examine wireless and
    mobile networks, including wireless LANs (including WiFi and Bluetooth), Cellular telephony networks
    (including GSM, 3G, and 4G), and mobility (in both IP and GSM networks). :ref:`Chapters 8 <c8>`, which addresses
    security in computer networks, first looks at the underpinnings of encryption and network security, and
    then we examine how the basic theory is being applied in a broad range of Internet contexts. The last
    chapter, which addresses multimedia networking, examines audio and video applications such as
    Internet phone, video conferencing, and streaming of stored media. We also look at how a packet-
    switched network can be designed to provide consistent quality of service to audio and video
    applications.