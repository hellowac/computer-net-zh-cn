


Wireshark 实验室
=================
Wireshark Lab

在本实验中（可从本书网站获取），我们将研究安全套接层（SSL）协议。回顾 :ref:`第 8.6 节 <c8.6>`，SSL 用于保护 TCP 连接的安全，并且在实际中被广泛用于安全的互联网交易。在本实验中，我们将关注通过 TCP 连接发送的 SSL 记录。我们将尝试划分和分类每条记录，目的是理解每条记录的原因与作用。我们将研究各种 SSL 记录类型以及 SSL 消息中的字段。为此，我们将分析你的主机与某电子商务服务器之间发送的 SSL 记录的跟踪数据。

.. toggle::

    In this lab (available from the book Web site), we investigate the Secure Sockets Layer (SSL) protocol. Recall from :ref:`Section 8.6 <c8.6>` that SSL is used for securing a TCP connection, and that it is extensively used in practice for secure Internet transactions. In this lab, we will focus on the SSL records sent over the TCP connection. We will attempt to delineate and classify each of the records, with a goal of understanding the why and how for each record. We investigate the various SSL record types as well as the fields in the SSL messages. We do so by analyzing a trace of the SSL records sent between your host and an e-commerce server.

IPsec 实验
----------
IPsec Lab

在本实验中（可从本书网站获取），我们将探讨如何在 Linux 主机之间创建 IPsec 安全关联（SA）。实验的第一部分你可以使用两台普通的 Linux 主机，每台配有一个以太网适配器。但在实验的第二部分中，你需要四台 Linux 主机，其中两台配备两个以太网适配器。在实验的后半部分，你将使用 ESP 协议的隧道模式创建 IPsec 安全关联。你将首先手动创建这些 SA，然后使用 IKE 自动创建这些 SA。

.. toggle::

    In this lab (available from the book Web site), we will explore how to create IPsec SAs between linux boxes. You can do the first part of the lab with two ordinary linux boxes, each with one Ethernet adapter. But for the second part of the lab, you will need four linux boxes, two of which having two Ethernet adapters. In the second half of the lab, you will create IPsec SAs using the ESP protocol in the tunnel mode. You will do this by first manually creating the SAs, and then by having IKE create the SAs.
