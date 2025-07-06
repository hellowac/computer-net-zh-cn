.. _c8:


第 8 章 计算机网络中的安全
============================================

Chapter 8 Security in Computer Networks

Way back in :ref:`Section 1.6 <c1.6>` we described some of the more prevalent and damaging classes of Internet
attacks, including malware attacks, denial of service, sniffing, source masquerading, and message
modification and deletion. Although we have since learned a tremendous amount about computer
networks, we still haven’t examined how to secure networks from those attacks. Equipped with our
newly acquired expertise in computer networking and Internet protocols, we’ll now study in-depth secure
communication and, in particular, how computer networks can be defended from those nasty bad guys.

Let us introduce Alice and Bob, two people who want to communicate and wish to do so “securely.” This
being a networking text, we should remark that Alice and Bob could be two routers that want to
exchange routing tables securely, a client and server that want to establish a secure transport
connection, or two e-mail applications that want to exchange secure e-mail—all case studies that we will
consider later in this chapter. Alice and Bob are well-known fixtures in the security community, perhaps
because their names are more fun than a generic entity named “A” that wants to communicate securely
with a generic entity named “B.” Love affairs, wartime communication, and business transactions are the
commonly cited human needs for secure communications; preferring the first to the latter two, we’re
happy to use Alice and Bob as our sender and receiver, and imagine them in this first scenario.

We said that Alice and Bob want to communicate and wish to do so “securely,” but what precisely does
this mean? As we will see, security (like love) is a many-splendored thing; that is, there are many facets
to security. Certainly, Alice and Bob would like for the contents of their communication to remain secret
from an eavesdropper. They probably would also like to make sure that when they are communicating,
they are indeed communicating with each other, and that if their communication is tampered with by an
eavesdropper, that this tampering is detected. In the first part of this chapter, we’ll cover the
fundamental cryptography techniques that allow for encrypting communication, authenticating the party
with whom one is communicating, and ensuring message integrity.

In the second part of this chapter, we’ll examine how the fundamental ­cryptography principles can be
used to create secure networking protocols. Once again taking a top-down approach, we’ll examine
secure protocols in each of the (top four) layers, beginning with the application layer. We’ll examine how
to secure e-mail, how to secure a TCP connection, how to provide blanket security at the network layer,
and how to secure a wireless LAN. In the third part of this chapter we’ll consider operational security,which is about protecting organizational networks from attacks. In particular, we’ll take a careful look at
how firewalls and intrusion detection systems can enhance the security of an organizational network.

.. toggle::

   早在 :ref:`第 1.6 节 <c1.6>` 中，我们描述了一些较为常见且危害严重的互联网攻击类型，包括恶意软件攻击、拒绝服务、嗅探、源伪装以及信息篡改和删除。尽管我们之后对计算机网络有了大量的学习，但尚未深入探讨如何防护网络免受这些攻击。现在，凭借我们在计算机网络和互联网协议方面新获得的专业知识，我们将深入研究安全通信，特别是如何防御那些恶意攻击者。

   让我们引入 Alice 和 Bob，两个人想要通信，并希望以“安全”的方式进行通信。由于这是一本网络教材，我们需要说明，Alice 和 Bob 也可以是两个希望安全交换路由表的路由器，是希望建立安全传输连接的客户端和服务器，或者是想要交换安全邮件的两个电子邮件应用程序——这些都是我们稍后将在本章中讨论的案例。Alice 和 Bob 是安全领域中的经典人物，或许是因为比起用泛泛的“A”和“B”来代表通信双方，这两个名字更加生动有趣。人们通常认为安全通信是为了满足恋爱、战争通讯和商业交易等人类需求；我们更偏向于用 Alice 和 Bob 来代表发送者和接收者，并在本章初始场景中想象他们的通信。

   我们说 Alice 和 Bob 想要通信并希望“安全”通信，但这究竟意味着什么呢？正如我们将看到的，安全（如同爱情）是多面性的；也就是说，安全有许多方面。当然，Alice 和 Bob 希望他们的通信内容对窃听者保持秘密。他们可能还希望确保他们在通信时确实是在相互通信，并且如果通信被窃听者篡改，可以检测出这种篡改。在本章的第一部分，我们将介绍实现通信加密、通信方身份验证以及确保消息完整性的基本密码学技术。

   在本章的第二部分，我们将探讨如何利用基本的密码学原理构建安全的网络协议。依旧采取自上而下的方法，我们将依次研究（前四层）中的安全协议，首先是应用层。我们将探讨如何保障电子邮件安全，如何保障 TCP 连接安全，如何在网络层实现全面安全，以及如何保护无线局域网。在本章的第三部分，我们将关注运营安全，即保护组织网络免受攻击。特别是，我们将详细考察防火墙和入侵检测系统如何增强组织网络的安全性。



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
   ./s9.rst
   ./summary.rst
   ./homework.rst
   ./wiresharklab.rst
   ./interview.rst

