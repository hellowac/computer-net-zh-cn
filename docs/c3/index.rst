.. _c3:

第 3 章 传输层
============================================

Chapter 3 Transport Layer

Residing between the application and network layers, the transport layer is a central piece of the layered
network architecture. It has the critical role of providing communication services directly to the
application processes running on different hosts. The pedagogic approach we take in this chapter is to
alternate between discussions of transport-layer principles and discussions of how these principles are
implemented in existing protocols; as usual, particular emphasis will be given to Internet protocols, in
particular the TCP and UDP transport-layer protocols.

We’ll begin by discussing the relationship between the transport and network layers. This sets the stage
for examining the first critical function of the transport layer—extending the network layer’s delivery
service between two end systems to a delivery service between two application-layer processes running
on the end systems. We’ll illustrate this function in our coverage of the Internet’s connectionless
transport protocol, UDP.

We’ll then return to principles and confront one of the most fundamental problems in computer
networking—how two entities can communicate reliably over a medium that may lose and corrupt data.
Through a series of increasingly complicated (and realistic!) scenarios, we’ll build up an array of
techniques that transport protocols use to solve this problem. We’ll then show how these principles are
embodied in TCP, the Internet’s connection-oriented transport protocol.

We’ll next move on to a second fundamentally important problem in networking—controlling the
transmission rate of transport-layer entities in order to avoid, or recover from, congestion within the
network. We’ll consider the causes and consequences of congestion, as well as commonly used
congestion-control techniques. After obtaining a solid understanding of the issues behind congestion
control, we’ll study TCP’s approach to congestion control.

.. toggle::

    传输层位于应用层与网络层之间，是分层网络体系结构中的核心组成部分。它在不同主机上运行的应用进程之间提供通信服务，这一角色至关重要。在本章中，我们将采取一种交替式教学方法，穿插讲解传输层的基本原理以及这些原理在现有协议中的具体实现；一如既往，我们将特别强调因特网协议，尤其是传输层的 TCP 和 UDP 协议。

    我们将从讨论传输层与网络层之间的关系开始。这为我们探讨传输层的第一个关键功能奠定了基础——将网络层在两个终端系统之间提供的交付服务扩展为在两个终端系统上运行的应用层进程之间的交付服务。我们将在介绍因特网无连接传输协议 UDP 的过程中，阐明这一功能。

    随后我们将回到原理层面，直面计算机网络中的一个基本问题——两个实体如何在可能发生数据丢失和损坏的媒介上传输可靠的信息。通过一系列日益复杂（也更贴近现实！）的场景，我们将逐步构建传输协议用以解决该问题的各种技术方案。接着我们将展示这些原理是如何体现在因特网面向连接的传输协议 TCP 中的。

    接下来，我们将深入探讨网络中另一个根本性问题——如何控制传输层实体的发送速率，以避免或缓解网络中的拥塞。我们将分析拥塞的成因与后果，以及常见的拥塞控制技术。在对拥塞控制背后的关键问题形成扎实理解之后，我们将研究 TCP 的拥塞控制机制。



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