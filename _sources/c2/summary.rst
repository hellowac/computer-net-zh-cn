.. _c2.9:


2.9 小结
=================
1.8 Summary

在本章中，我们学习了网络应用的概念层面和实现层面。我们了解了许多因特网应用所采用的无处不在的客户端-服务器架构，并在 HTTP、SMTP、POP3 和 DNS 协议中看到了这一架构的应用。我们详细学习了这些重要的应用层协议及其对应的相关应用（Web、文件传输、电子邮件和 DNS）。我们了解了 P2P 架构，以及它如何被应用于许多应用中。我们还学习了流媒体视频，以及现代视频分发系统如何利用 CDN。我们探讨了如何使用套接字 API 构建网络应用，并依次讲解了如何通过套接字来实现面向连接（TCP）和无连接（UDP）的端到端传输服务。我们对分层网络体系结构的第一步探索到此为止！

在本书一开始的 :ref:`第 1.1 节 <c1.1>` 中，我们给出了一个相当模糊、简化的协议定义：“在两个或多个通信实体之间交换的消息的格式与顺序，以及在消息传输和/或接收或其他事件发生时所采取的行为。”本章的内容，特别是我们对 HTTP、SMTP、POP3 和 DNS 协议的详细研究，为这个定义增添了丰富的内涵。协议是网络中的关键概念；我们对应用协议的学习使我们能够更直观地理解协议的本质。

在 :ref:`第 2.1 节 <c2.1>` 中，我们描述了 TCP 和 UDP 为调用它们的应用所提供的服务模型。当我们在 :ref:`第 2.7 节 <c2.7>` 中开发基于 TCP 和 UDP 的简单应用时，我们又更深入地研究了这些服务模型。然而，我们尚未详细说明 TCP 和 UDP 是如何实现这些服务模型的。例如，我们知道 TCP 提供可靠的数据服务，但我们尚未说明它是如何实现这一点的。在下一章中，我们将更深入地探讨传输协议的“是什么”、“如何做”以及“为什么这么做”。

在掌握了因特网应用结构和应用层协议相关知识之后，我们现在准备继续深入协议栈，在 :ref:`第 3 章 <c3>` 中研究传输层。

.. toggle::

    In this chapter, we’ve studied the conceptual and the implementation aspects of network applications. We’ve learned about the ubiquitous client-server architecture adopted by many Internet applications and seen its use in the HTTP, SMTP, POP3, and DNS protocols. We’ve studied these important application- level protocols, and their corresponding associated applications (the Web, file transfer, e-mail, and DNS) in some detail. We’ve learned about the P2P architecture and how it is used in many applications. We’ve also learned about streaming video, and how modern video distribution systems leverage CDNs. We’ve examined how the socket API can be used to build network applications. We’ve walked through the use of sockets for connection-oriented (TCP) and connectionless (UDP) end-to-end transport services. The first step in our journey down the layered network architecture is now complete!

    At the very beginning of this book, in :ref:`Section 1.1 <c1.1>`, we gave a rather vague, bare-bones definition of a protocol: “the format and the order of messages exchanged between two or more communicating entities, as well as the actions taken on the transmission and/or receipt of a message or other event.” The material in this chapter, and in particular our detailed study of the HTTP, SMTP, POP3, and DNS protocols, has now added considerable substance to this definition. Protocols are a key concept in networking; our study of application protocols has now given us the opportunity to develop a more intuitive feel for what protocols are all about.

    In :ref:`Section 2.1 <c2.1>`, we described the service models that TCP and UDP offer to applications that invoke them. We took an even closer look at these service models when we developed simple applications that run over TCP and UDP in :ref:`Section 2.7 <c2.7>`. However, we have said little about how TCP and UDP provide these service models. For example, we know that TCP provides a reliable data service, but we haven’t said yet how it does so. In the next chapter we’ll take a careful look at not only the what, but also the how and why of transport protocols.

    Equipped with knowledge about Internet application structure and application-level protocols, we’re now ready to head further down the protocol stack and examine the transport layer in :ref:`Chapter 3 <c3>`.