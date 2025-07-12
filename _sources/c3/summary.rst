.. _c3.8:


3.8 小结
=================

1.8 Summary

本章开始时，我们研究了传输层协议能够为网络应用提供的服务。在一个极端，传输层协议可以非常简单，只为应用提供复用/解复用功能，以支持通信进程。互联网的 UDP 协议就是这种简单无修饰的传输层协议的例子。另一极端，传输层协议可以向应用提供各种保证，比如可靠的数据传输、延迟保证和带宽保证。然而，传输协议所能提供的服务往往受到底层网络层协议服务模型的限制。如果网络层协议无法为传输层数据段提供延迟或带宽保证，那么传输层协议也无法为进程间发送的消息提供延迟或带宽保证。

我们在 :ref:`第3.4节 <c3.4>` 中了解到，即使底层网络层不可靠，传输层协议仍可提供可靠数据传输。我们看到，提供可靠数据传输有许多细节，但通过谨慎结合确认、定时器、重传和序列号，这一任务是可以实现的。

尽管本章涵盖了可靠数据传输，我们应牢记可靠传输可以由链路层、网络层、传输层或应用层协议来实现。协议栈中的任何四个上层都可以实现确认、定时器、重传和序列号，并向上层提供可靠数据传输。实际上，多年来，工程师和计算机科学家已独立设计并实现了链路层、网络层、传输层和应用层的可靠传输协议（尽管其中许多协议已默默消失）。

在 :ref:`第3.5节 <c3.5>` 中，我们详细研究了 TCP，互联网的面向连接且可靠的传输层协议。我们了解到 TCP 结构复杂，涉及连接管理、流量控制和往返时间估计，以及可靠数据传输。实际上，TCP 比我们的描述更复杂——我们刻意没有讨论各种广泛实现的 TCP 补丁、修复和改进。但所有这些复杂性都被隐藏在网络应用背后。如果一台主机上的客户端想可靠地向另一主机上的服务器发送数据，只需打开到服务器的 TCP 套接字并往里写数据。客户端-服务器应用完全无感知 TCP 的复杂性。

在 :ref:`第3.6节 <c3.6>`，我们从宏观角度考察了拥塞控制，且在 :ref:`第3.7节 <c3.7>` 中展示了 TCP 如何实现拥塞控制。我们了解到拥塞控制对网络健康至关重要。没有拥塞控制，网络极易瘫痪，端到端几乎无法传输数据。在 :ref:`第3.7节 <c3.7>` 中，我们学习了 TCP 实现了端到端拥塞控制机制，当路径判断无拥塞时，TCP 以加法方式增加传输速率，发生丢包时以乘法方式减少传输速率。该机制还力求让通过拥塞链路的每条 TCP 连接平分该链路带宽。我们还深入探讨了 TCP 连接建立和慢启动对延迟的影响。观察发现，在许多重要场景中，连接建立和慢启动显著增加了端到端延迟。我们再次强调，尽管 TCP 拥塞控制多年来不断演进，它仍是一个活跃的研究领域，未来可能持续发展。

本章对具体互联网传输协议的讨论集中于 UDP 和 TCP——互联网传输层的两大“主力军”。然而，二十年的经验显示这两者均非在所有情况下理想。研究者因此致力于开发新的传输层协议，其中几个已成为 IETF 提出的标准。

数据报拥塞控制协议（DCCP）[:rfc:`4340`] 提供低开销、面向消息的类似 UDP 的不可靠服务，但具有应用可选的拥塞控制，且兼容 TCP。如果应用需要可靠或半可靠数据传输，则在应用层实现，可能使用我们在 :ref:`第3.4节 <c3.4>` 学习的机制。DCCP 设想用于如流媒体（见 :ref:`第9章 <c9>`）等可利用数据传递及时性与可靠性权衡，但又希望对网络拥塞响应的应用。

谷歌的 QUIC（快速 UDP 互联网连接）协议 :ref:`[Iyengar 2016] <Iyengar 2016>`，由谷歌 Chromium 浏览器实现，通过重传和错误纠正提供可靠性，支持快速连接建立，以及基于速率的拥塞控制算法，旨在与 TCP 友好——所有这些作为基于 UDP 的应用层协议实现。2015 年初，谷歌报告称大约一半 Chrome 向谷歌服务器的请求通过 QUIC 服务。

DCTCP（数据中心 TCP） :ref:`[Alizadeh 2010] <Alizadeh 2010>` 是专为数据中心网络设计的 TCP 版本，使用 ECN 更好地支持数据中心负载特征中的短时和长时流混合。

流控制传输协议（SCTP）[:rfc:`4960`，:rfc:`3286`] 是一种可靠的面向消息的协议，允许多个不同的应用层“流”通过单一 SCTP 连接复用（称为“多流”）。从可靠性角度看，连接内不同流独立处理，某一流的丢包不会影响其他流的数据传送。QUIC 也提供类似多流语义。SCTP 还支持当主机连接到两个或更多网络时，通过两条出站路径传输数据，可选的乱序数据交付，以及其他多种特性。SCTP 的流量控制和拥塞控制算法基本与 TCP 相同。

TCP 友好速率控制协议（TFRC）[:rfc:`5348`] 是一种拥塞控制协议，而非完整的传输层协议。它定义了一种拥塞控制机制，可在其他传输协议中使用，如 DCCP（DCCP 中两种应用可选协议之一即为 TFRC）。TFRC 目标是平滑 TCP 拥塞控制中的“锯齿”行为（见 :ref:`图3.53 <Figure 3.53>`），同时维持长期发送速率与 TCP 相“近”。由于发送速率较 TCP 更平滑，TFRC 适合多媒体应用，如 IP 电话或流媒体，在这类应用中，平滑速率很重要。TFRC 是一种“基于方程”的协议，使用测得的丢包率作为输入，依据 :ref:`[Padhye 2000] <Padhye 2000>` 提出的方程估算若 TCP 会话经历该丢包率时的吞吐量，随后以此速率作为 TFRC 的目标发送速率。

未来是否会广泛部署 DCCP、SCTP、QUIC 或 TFRC 尚不得而知。尽管这些协议显然在功能上优于 TCP 和 UDP，TCP 和 UDP 多年来已证明“足够好”。“更好”是否能胜出“足够好”，取决于技术、社会和商业等复杂因素。

在 :ref:`第1章 <c1>` 中，我们提到计算机网络可分为“网络边缘”和“网络核心”。网络边缘涵盖终端系统中的所有活动。现已覆盖应用层和传输层，我们对网络边缘的讨论已完成。是时候探索网络核心了！这段旅程将在接下来的两章开始，我们将学习网络层，并在 :ref:`第6章 <c6>` 继续研究链路层。


.. toggle::

    We began this chapter by studying the services that a transport-layer protocol can provide to network applications. At one extreme, the transport-layer protocol can be very simple and offer a no-frills service to applications, providing only a multiplexing/demultiplexing function for communicating processes. The Internet’s UDP protocol is an example of such a no-frills transport-layer protocol. At the other extreme, a transport-layer protocol can provide a variety of guarantees to applications, such as reliable delivery of data, delay guarantees, and bandwidth guarantees. Nevertheless, the services that a transport protocol can provide are often constrained by the service model of the underlying network-layer protocol. If the network-layer protocol cannot provide delay or bandwidth guarantees to transport-layer segments, then the transport-layer protocol cannot provide delay or bandwidth guarantees for the messages sent between processes.

    We learned in :ref:`Section 3.4 <c3.4>` that a transport-layer protocol can provide reliable data transfer even if the underlying network layer is unreliable. We saw that providing reliable data transfer has many subtle points, but that the task can be accomplished by carefully combining acknowledgments, timers, retransmissions, and sequence numbers.

    Although we covered reliable data transfer in this chapter, we should keep in mind that reliable data transfer can be provided by link-, network-, transport-, or application-layer protocols. Any of the upper four layers of the protocol stack can implement acknowledgments, timers, retransmissions, and sequence numbers and provide reliable data transfer to the layer above. In fact, over the years, engineers and computer scientists have independently designed and implemented link-, network-, transport-, and application-layer protocols that provide reliable data transfer (although many of these protocols have quietly disappeared).

    In :ref:`Section 3.5 <c3.5>`, we took a close look at TCP, the Internet’s connection-oriented and reliable transport- layer protocol. We learned that TCP is complex, involving connection management, flow control, and
    round-trip time estimation, as well as reliable data transfer. In fact, TCP is actually more complex than our description—we intentionally did not discuss a variety of TCP patches, fixes, and improvements that are widely implemented in various versions of TCP. All of this complexity, however, is hidden from the network application. If a client on one host wants to send data reliably to a server on another host, it simply opens a TCP socket to the server and pumps data into that socket. The client-server application is blissfully unaware of TCP’s complexity.

    In :ref:`Section 3.6 <c3.6>`, we examined congestion control from a broad perspective, and in :ref:`Section 3.7 <c3.7>`, we showed how TCP implements congestion control. We learned that congestion control is imperative for
    the well-being of the network. Without congestion control, a network can easily become gridlocked, with
    little or no data being transported end-to-end. In :ref:`Section 3.7 <c3.7>` we learned that TCP implements an end- to-end congestion-control mechanism that additively increases its transmission rate when the TCP
    connection’s path is judged to be congestion-free, and multiplicatively decreases its transmission rate when loss occurs. This mechanism also strives to give each TCP connection passing through a congested link an equal share of the link bandwidth. We also examined in some depth the impact of TCP connection establishment and slow start on latency. We observed that in many important scenarios, connection establishment and slow start significantly contribute to end-to-end delay. We emphasize once more that while TCP congestion control has evolved over the years, it remains an area of intensive research and will likely continue to evolve in the upcoming years.

    Our discussion of specific Internet transport protocols in this chapter has focused on UDP and TCP—the two “work horses” of the Internet transport layer. However, two decades of experience with these two protocols has identified circumstances in which neither is ideally suited. Researchers have thus been busy developing additional transport-layer protocols, several of which are now IETF proposed standards.

    The Datagram Congestion Control Protocol (DCCP) :ref:`[RFC 4340] <RFC 4340>` provides a low-overhead, message- oriented, UDP-like unreliable service, but with an application-selected form of congestion control that is compatible with TCP. If reliable or semi-reliable data transfer is needed by an application, then this would be performed within the application itself, perhaps using the mechanisms we have studied in :ref:`Section 3.4 <c3.4>`. DCCP is envisioned for use in applications such as streaming media (see :ref:`Chapter 9 <c9>`) that can exploit the tradeoff between timeliness and reliability of data delivery, but that want to be responsive to network congestion.

    Google’s QUIC (Quick UDP Internet Connections) protocol [Iyengar 2016], implemented in Google’s Chromium browser, provides reliability via retransmission as well as error correction, fast-connection setup, and a rate-based congestion control algorithm that aims to be TCP friendly—all implemented as an application-level protocol on top of UDP. In early 2015, Google reported that roughly half of all requests from Chrome to Google servers are served over QUIC.

    DCTCP (Data Center TCP) :ref:`[Alizadeh 2010] <Alizadeh 2010>` is a version of TCP designed specifically for data center networks, and uses ECN to better support the mix of short- and long-lived flows that characterize data center workloads. 

    The Stream Control Transmission Protocol (SCTP) [:ref:`RFC 4960 <RFC 4960>`, :ref:`RFC 3286 <RFC 3286>`] is a reliable, message- oriented protocol that allows several different application-level “streams” to be multiplexed through a
    single SCTP connection (an approach known as “multi-streaming”). From a reliability standpoint, the different streams within the connection are handled separately, so that packet loss in one stream does not affect the delivery of data in other streams. QUIC provides similar multi-stream semantics. SCTP also allows data to be transferred over two outgoing paths when a host is connected to two or more networks, optional delivery of out-of-order data, and a number of other features. SCTP’s flow-and congestion-control algorithms are essentially the same as in TCP.

    The TCP-Friendly Rate Control (TFRC) protocol :ref:`[RFC 5348] <RFC 5348>` is a congestion-control protocol rather than a full-fledged transport-layer protocol. It specifies a congestion-control mechanism that could be used in another transport protocol such as DCCP (indeed one of the two application-selectable protocols available in DCCP is TFRC). The goal of TFRC is to smooth out the “saw tooth” behavior (see :ref:`Fig­ure 3.53 <Figure 3.53>` ) in TCP congestion control, while maintaining a long-term sending rate that is “reasonably” close to that of TCP. With a smoother sending rate than TCP, TFRC is well-suited for multimedia applications such as IP telephony or streaming media where such a smooth rate is important. TFRC is an “equation-based” protocol that uses the measured packet loss rate as input to an equation :ref:`[Padhye 2000] <Padhye 2000>` that estimates what TCP’s throughput would be if a TCP session experiences that loss rate. This rate is then taken as TFRC’s target sending rate.

    Only the future will tell whether DCCP, SCTP, QUIC, or TFRC will see widespread deployment. While these protocols clearly provide enhanced capabilities over TCP and UDP, TCP and UDP have proven themselves “good enough” over the years. Whether “better” wins out over “good enough” will depend on a complex mix of technical, social, and business considerations.

    In :ref:`Chapter 1 <c1>`, we said that a computer network can be partitioned into the “network edge” and the “network core.” The network edge covers everything that happens in the end systems. Having now covered the application layer and the transport layer, our discussion of the network edge is complete. It is time to explore the network core! This journey begins in the next two chapters, where we’ll study the network layer, and continues into :ref:`Chapter 6 <c6>`, where we’ll study the link layer.