


Wireshark 实验室
=================

Wireshark Lab

Wireshark 实验：HTTP
----------------------
Wireshark Lab: HTTP

在第一个实验中初步接触了 Wireshark 报文嗅探器后，我们现在准备使用 Wireshark 来研究协议的实际运行情况。在本实验中，我们将探究 HTTP 协议的多个方面：基本的 GET/响应交互、HTTP 消息格式、获取大型 HTML 文件、获取包含嵌入式 URL 的 HTML 文件、持久连接与非持久连接、以及 HTTP 的认证与安全机制。

与所有 Wireshark 实验一样，本实验的完整描述可在本书网站上获取： `www.pearsonhighered.com/cs-resources <https://media.pearsoncmg.com/bc/abp/cs-resources/>`_。

.. toggle::

    Having gotten our feet wet with the Wireshark packet sniffer in Lab 1, we’re now ready to use Wireshark to investigate protocols in operation. In this lab, we’ll explore several aspects of the HTTP protocol: the basic GET/reply interaction, HTTP message formats, retrieving large HTML files, retrieving HTML files with embedded URLs, persistent and non-persistent connections, and HTTP authentication and security.

    As is the case with all Wireshark labs, the full description of this lab is available at this book’s Web site, `www.pearsonhighered.com/cs-resources <https://media.pearsoncmg.com/bc/abp/cs-resources/>`_.

Wireshark 实验：DNS
--------------------
Wireshark Lab: DNS

在本实验中，我们将更深入地研究 DNS 的客户端部分，即将 Internet 主机名转换为 IP 地址的协议。回顾 :ref:`第 2.5 节 <c2.5>` 所述，DNS 中客户端的角色相对简单 —— 客户端向其本地 DNS 服务器发送查询，并接收返回的响应。在底层中，分层 DNS 服务器之间可能会进行大量通信，以递归或迭代的方式解析客户端的 DNS 查询，但这些对 DNS 客户端是不可见的。对 DNS 客户端而言，协议相当简单 —— 构造查询发送至本地 DNS 服务器，并接收该服务器返回的响应。我们将在本实验中观察 DNS 的实际运行过程。

与所有 Wireshark 实验一样，本实验的完整描述可在本书网站上获取： `www.pearsonhighered.com/cs-resources <https://media.pearsoncmg.com/bc/abp/cs-resources/>`_。

.. toggle::

    In this lab, we take a closer look at the client side of the DNS, the protocol that translates Internet hostnames to IP addresses. Recall from :ref:`Section 2.5 <c2.5>` that the client’s role in the DNS is relatively simple —a client sends a query to its local DNS server and receives a response back. Much can go on under the covers, invisible to the DNS clients, as the hierarchical DNS servers communicate with each other to either recursively or iteratively resolve the client’s DNS query. From the DNS client’s standpoint, however, the protocol is quite simple—a query is formulated to the local DNS server and a response is received from that server. We observe DNS in action in this lab.

    As is the case with all Wireshark labs, the full description of this lab is available at this book’s Web site, `www.pearsonhighered.com/cs-resources <https://media.pearsoncmg.com/bc/abp/cs-resources/>`_.
