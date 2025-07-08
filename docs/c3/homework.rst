


家庭作业问题和疑问
========================================

Homework Problems and Questions

SECTIONS 3.1–3.3
------------------

R1. 假设网络层提供如下服务。源主机中的网络层从传输层接收最大为 1200 字节的报文段和目标主机地址。随后网络层保证将该报文段传送到目标主机中的传输层。假设目标主机上可以运行多个网络应用进程。

a. 设计一个尽可能简单的传输层协议，以将应用数据传送到目标主机中的目标进程。假设目标主机操作系统为每个正在运行的应用进程分配一个 4 字节端口号。
b. 修改该协议，使其向目标进程提供一个“返回地址”。
c. 在你的协议中，传输层是否需要在计算机网络核心中“做任何事情”？

R2. 考虑一个星球，每个人都属于一个六人家庭，每个家庭住在自己的房子中，每栋房子有一个唯一地址，每个家庭成员在该房子中有唯一的名字。假设该星球有一个邮件服务，能够将信件从源房子送到目标房子。邮件服务要求：(1) 信件必须放在信封中，(2) 信封上必须清晰写明目标房子的地址（且只能写这个地址）。假设每个家庭都有一个代表成员，负责收发全家的信件。信件本身不一定包含收信人的信息。

a. 参照上述问题 R1 的解决方案，描述代表成员如何使用某种协议将信件从发送家庭成员传送给接收家庭成员。
b. 在你的协议中，邮件服务是否需要打开信封并检查信件内容来提供其服务？

R3. 考虑主机 A 和主机 B 之间的一个 TCP 连接。假设从主机 A 到主机 B 的 TCP 报文段的源端口号为 x，目标端口号为 y。那么从主机 B 到主机 A 的报文段的源端口号和目标端口号分别是什么？

R4. 说明为什么某个应用开发者可能选择通过 UDP 而不是 TCP 来运行应用程序。

R5. 为什么在当今互联网中，语音和视频流量常常通过 TCP 而不是 UDP 发送？（提示：我们想要的答案与 TCP 的拥塞控制机制无关。）

R6. 当应用运行于 UDP 之上时，是否仍可能实现可靠的数据传输？如果可以，如何实现？

R7. 假设主机 C 中的一个进程拥有一个端口号为 6789 的 UDP 套接字。假设主机 A 和主机 B 分别向主机 C 发送一个目标端口为 6789 的 UDP 报文段。是否这两个报文段都会被定向到主机 C 上的同一个套接字？如果是，主机 C 上的进程如何知道这两个报文段来自两个不同的主机？

R8. 假设主机 C 上运行着一个 Web 服务器，其监听端口为 80。假设该 Web 服务器使用持久连接，并正接收来自两个不同主机 A 和 B 的请求。这些请求是否都通过主机 C 上的同一个套接字传送？如果是不同套接字，它们是否都使用端口 80？请讨论并解释。

.. toggle::

   R1. Suppose the network layer provides the following service. The network layer in the source host accepts a segment of maximum size 1,200 bytes and a destination host address from the transport layer. The network layer then guarantees to deliver the segment to the transport layer at the destination host. Suppose many network application processes can be running at the destination host.

   a. Design the simplest possible transport-layer protocol that will get application data to the desired process at the destination host. Assume the operating system in the destination host has assigned a 4-byte port number to each running application process.
   b. Modify this protocol so that it provides a “return address” to the destination process.
   c. In your protocols, does the transport layer “have to do anything” in the core of the computer network?

   R2. Consider a planet where everyone belongs to a family of six, every family lives in its own house, each house has a unique address, and each person in a given house has a unique name. Suppose this planet has a mail service that delivers letters from source house to destination house. The mail service requires that (1) the letter be in an envelope, and that (2) the address of the destination house (and nothing more) be clearly written on the envelope. Suppose each family has a delegate family member who collects and distributes letters for the other family members. The letters do not necessarily provide any indication of the recipients of the letters.

   a. Using the solution to Problem R1 above as inspiration, describe a protocol that the delegates can use to deliver letters from a sending family member to a receiving family member.
   b. In your protocol, does the mail service ever have to open the envelope and examine the letter in order to provide its service?

   R3. Consider a TCP connection between Host A and Host B. Suppose that the TCP segments traveling from Host A to Host B have source port number x and destination port number y. What are the source and destination port numbers for the segments traveling from Host B to Host A?

   R4. Describe why an application developer might choose to run an application over UDP rather than TCP.

   R5. Why is it that voice and video traffic is often sent over TCP rather than UDP in today’s Internet? (Hint: The answer we are looking for has nothing to do with TCP’s congestion-control mechanism.)

   R6. Is it possible for an application to enjoy reliable data transfer even when the application runs over UDP? If so, how?

   R7. Suppose a process in Host C has a UDP socket with port number 6789. Suppose both Host A and Host B each send a UDP segment to Host C with destination port number 6789. Will both of these segments be directed to the same socket at Host C? If so, how will the process at Host C know that these two segments originated from two different hosts?

   R8. Suppose that a Web server runs in Host C on port 80. Suppose this Web server uses persistent connections, and is currently receiving requests from two different Hosts, A and B. Are all of the requests being sent through the same socket at Host C? If they are being passed through different sockets, do both of the sockets have port 80? Discuss and explain.

SECTION 3.4
-------------

R9. 在我们的 ``rdt`` 协议中，为什么需要引入序列号？

R10. 在我们的 ``rdt`` 协议中，为什么需要引入定时器？

R11. 假设发送方和接收方之间的往返延迟是恒定且已知的。在协议 ``rdt 3.0`` 中（假设报文可能丢失），是否仍然需要定时器？请解释。

R12. 访问配套网站上的 Go-Back-N Java 小程序。

a. 让源端发送五个分组，然后在这五个分组到达目标之前暂停动画。杀死第一个分组后恢复动画。描述发生了什么。
b. 重复实验，但允许第一个分组到达目标并杀死第一个确认。再次描述发生了什么。
c. 最后，尝试发送六个分组。会发生什么？

R13. 重复 R12，但使用 Selective Repeat Java 小程序。Selective Repeat 与 Go-Back-N 有何不同？

.. toggle::

   R9. In our ``rdt`` protocols, why did we need to introduce sequence numbers?

   R10. In our ``rdt`` protocols, why did we need to introduce timers?

   R11. Suppose that the roundtrip delay between sender and receiver is constant and known to the sender. Would a timer still be necessary in protocol ``rdt 3.0``, assuming that packets can be lost? Explain.

   R12. Visit the Go-Back-N Java applet at the companion Web site.

   a. Have the source send five packets, and then pause the animation before any of the five packets reach the destination. Then kill the first packet and resume the animation. Describe what happens.
   b. Repeat the experiment, but now let the first packet reach the destination and kill the first acknowledgment. Describe again what happens.
   c. Finally, try sending six packets. What happens?

   R13. Repeat R12, but now with the Selective Repeat Java applet. How are Selective Repeat and Go-Back-N different?

SECTION 3.5
--------------

R14. 判断对错：

a. 主机 A 正通过 TCP 连接向主机 B 发送一个大文件。假设主机 B 没有数据要发给主机 A。由于主机 B 无法在数据上附加确认，因此不会向主机 A 发送确认。
b. TCP 的 ``rwnd`` 大小在整个连接期间永远不变。
c. 假设主机 A 正通过 TCP 连接向主机 B 发送一个大文件。A 发送的未确认字节数不能超过接收缓存大小。
d. 假设主机 A 正通过 TCP 连接向主机 B 发送一个大文件。如果该连接中某个报文段的序列号为 m，那么下一个报文段的序列号必定是 m+1。
e. TCP 报文段在其首部中有一个 ``rwnd`` 字段。
f. 假设一个 TCP 连接中的最后一个 ``SampleRTT`` 为 1 秒。该连接当前的 ``TimeoutInterval`` 值一定 ≥ 1 秒。
g. 假设主机 A 在 TCP 连接中发送了一个序列号为 38、含 4 字节数据的报文段给主机 B。在该报文段中，确认号必定为 42。

R15. 假设主机 A 通过 TCP 连接向主机 B 连续发送两个报文段。第一个报文段的序列号为 90；第二个为 110。

a. 第一个报文段中有多少数据？
b. 假设第一个报文段丢失而第二个到达 B。在 B 向 A 发送的确认中，确认号是多少？

R16. 考虑 :ref:`第3.5节 <c3.5>` 中讨论的 Telnet 示例。在用户输入字母 ‘C’ 几秒后又输入字母 ‘R’。在输入字母 ‘R’ 后，发送了多少个报文段？这些报文段的序列号和确认号字段分别是什么？

.. toggle::

   R14. True or false?

   a. Host A is sending Host B a large file over a TCP connection. Assume Host B has no data to send Host A. Host B will not send acknowledgments to Host A because Host B cannot piggyback the acknowledgments on data.
   b. The size of the TCP ``rwnd`` never changes throughout the duration of the connection.
   c. Suppose Host A is sending Host B a large file over a TCP connection. The number of unacknowledged bytes that A sends cannot exceed the size of the receive buffer.
   d. Suppose Host A is sending a large file to Host B over a TCP connection. If the sequence number for a segment of this connection is m, then the sequence number for the subsequent segment will necessarily be m+1.
   e. The TCP segment has a field in its header for ``rwnd``.
   f. Suppose that the last ``SampleRTT`` in a TCP connection is equal to 1 sec. The current value of ``TimeoutInterval`` for the connection will necessarily be ≥1 sec.
   g. Suppose Host A sends one segment with sequence number 38 and 4 bytes of data over a TCP connection to Host B. In this same segment the acknowledgment number is necessarily 42.

   R15. Suppose Host A sends two TCP segments back to back to Host B over a TCP connection. The first segment has sequence number 90; the second has sequence number 110.

   a. How much data is in the first segment?
   b. Suppose that the first segment is lost but the second segment arrives at B. In the acknowledgment that Host B sends to Host A, what will be the acknowledgment number?

   R16. Consider the Telnet example discussed in :ref:`Section 3.5 <c3.5>` . A few seconds after the user types the letter ‘C,’ the user types the letter ‘R.’ After typing the letter ‘R,’ how many segments are sent, and what is put in the sequence number and acknowledgment fields of the segments?

SECTION 3.7
--------------

R17. 假设两个 TCP 连接共享一个速率为 R bps 的瓶颈链路。两个连接都有大量文件要发送（沿瓶颈链路同一方向）。文件传输同时开始。TCP 会希望为每个连接分配多少传输速率？

R18. 判断对错：考虑 TCP 中的拥塞控制。当发送方的定时器超时时，``ssthresh`` 的值被设置为其先前值的一半。

R19. 在 :ref:`第3.7节 <c3.7>` 的边栏中关于 TCP 拆分的讨论中，提到使用 TCP 拆分的响应时间约为 4⋅RTTFE+RTTBE+处理时间。请为该说法提供理由。

.. toggle::

   R17. Suppose two TCP connections are present over some bottleneck link of rate R bps. Both connections have a huge file to send (in the same direction over the bottleneck link). The transmissions of the files start at the same time. What transmission rate would TCP like to give to each of the connections?

   R18. True or false? Consider congestion control in TCP. When the timer expires at the sender, the value of ``ssthresh`` is set to one half of its previous value.

   R19. In the discussion of TCP splitting in the sidebar in :ref:`Section 3.7 <c3.7>` , it was claimed that the response time with TCP splitting is approximately 4⋅RTTFE+RTTBE+processing time. Justify this claim.

Problems
-----------

P1. 假设客户端 A 启动了一个与服务器 S 的 Telnet 会话。大约在同一时间，客户端 B 也启动了一个与服务器 S 的 Telnet 会话。请为以下各项提供可能的源端口号和目标端口号：

a. 从 A 到 S 发送的报文段。
b. 从 B 到 S 发送的报文段。
c. 从 S 到 A 发送的报文段。
d. 从 S 到 B 发送的报文段。
e. 如果 A 和 B 是不同的主机，是否可能从 A 到 S 的报文段和从 B 到 S 的报文段具有相同的源端口号？
f. 如果 A 和 B 是同一台主机呢？

.. toggle::

   P1. Suppose Client A initiates a Telnet session with Server S. At about the same time, Client B also initiates a Telnet session with Server S. Provide possible source and destination port numbers for

   a. The segments sent from A to S.
   b. The segments sent from B to S.
   c. The segments sent from S to A.
   d. The segments sent from S to B.
   e. If A and B are different hosts, is it possible that the source port number in the segments from A to S is the same as that from B to S?
   f. How about if they are the same host?

P2. 考虑 :ref:`图 3.5 <Figure 3.5>`。从服务器返回到客户端进程的报文段中的源端口和目标端口的值分别是什么？承载这些传输层报文段的网络层数据报中的 IP 地址又分别是什么？

.. toggle::

   P2. Consider :ref:`Figure 3.5 <Figure 3.5>` . What are the source and destination port values in the segments flowing from the server back to the clients’ processes? What are the IP addresses in the network-layer datagrams carrying the transport-layer segments?

P3. UDP 和 TCP 使用一补码进行校验和。假设你有以下三个 8 位字节：01010011、01100110、01110100。这三个字节之和的一补码是多少？（注意：尽管 UDP 和 TCP 在计算校验和时使用的是 16 位字，但本题要求你用 8 位进行计算。）请展示所有步骤。为什么 UDP 要取一补码而不是直接使用和？在一补码机制下，接收方如何检测错误？一个 1 位的错误是否有可能不被检测出来？那 2 位的错误呢？

.. toggle::

   P3. UDP and TCP use 1s complement for their checksums. Suppose you have the following three 8-bit bytes: 01010011, 01100110, 01110100. What is the 1s complement of the sum of these 8-bit bytes? (Note that although UDP and TCP use 16-bit words in computing the checksum, for this problem you are being asked to consider 8-bit sums.) Show all work. Why is it that UDP takes the 1s complement of the sum; that is, why not just use the sum? With the 1s complement scheme, how does the receiver detect errors? Is it possible that a 1-bit error will go undetected? How about a 2-bit error?

P4.

a. 假设你有以下两个字节：01011100 和 01100101。这两个字节之和的一补码是多少？
b. 假设你有以下两个字节：11011010 和 01100101。这两个字节之和的一补码是多少？
c. 对于 (a) 中的字节，举一个例子，其中每个字节中有一位被翻转，但一补码并未改变。

.. toggle::

   P4.

   a. Suppose you have the following 2 bytes: 01011100 and 01100101. What is the 1s complement of the sum of these 2 bytes?
   b. Suppose you have the following 2 bytes: 11011010 and 01100101. What is the 1s complement of the sum of these 2 bytes?
   c. For the bytes in part (a), give an example where one bit is flipped in each of the 2 bytes and yet the 1s complement doesn’t change.

P5. 假设 UDP 接收方计算接收到的 UDP 报文段的 Internet 校验和，并发现其与报文段中校验和字段的值匹配。那么接收方是否可以完全确定没有位错误发生？请解释。

.. toggle::

   P5. Suppose that the UDP receiver computes the Internet checksum for the received UDP segment and finds that it matches the value carried in the checksum field. Can the receiver be absolutely certain that no bit errors have occurred? Explain.

P6. 考虑我们修正 rdt2.1 协议的动机。请说明当使用 :ref:`图 3.57 <Figure 3.57>` 中所示的接收方与 :ref:`图 3.11 <Figure 3.11>` 中所示的发送方配合使用时，可能导致发送方和接收方进入死锁状态，即双方都在等待一个永远不会发生的事件。

.. toggle::

   P6. Consider our motivation for correcting protocol rdt2.1. Show that the receiver, shown in :ref:`Figure 3.57 <Figure 3.57>` , when operating with the sender shown in :ref:`Figure 3.11 <Figure 3.11>` , can lead the sender and receiver to enter into a deadlock state, where each is waiting for an event that will never occur.

P7. 在 rdt3.0 协议中，从接收方到发送方发送的 ACK 报文段没有序列号（虽然它们包含 ACK 字段，用于指出其确认的报文段的序列号）。为什么 ACK 报文段不需要自己的序列号？

.. figure:: ../img/334-0.png
   :align: center

.. _Figure 3.57:

**图 3.57 rdt 2.1 协议的错误接收方**

.. toggle::

   P7. In protocol rdt3.0, the ACK packets flowing from the receiver to the sender do not have sequence numbers (although they do have an ACK field that contains the sequence number of the packet they are acknowledging). Why is it that our ACK packets do not require sequence numbers?

   .. figure:: ../img/334-0.png
      :align: center

   **Figure 3.57 An incorrect receiver for protocol rdt 2.1**

P8. 为 ``rdt3.0`` 协议的接收方绘制状态机（FSM）。

.. toggle::

   P8. Draw the FSM for the receiver side of protocol ``rdt3.0``.

P9. 给出当数据报文段和确认报文段发生损坏时 ``rdt3.0`` 协议的运行轨迹。你的轨迹应类似于 :ref:`图 3.16 <Figure 3.16>` 中所使用的形式。

.. toggle::

   P9. Give a trace of the operation of protocol ``rdt3.0`` when data packets and acknowledgment packets are garbled. Your trace should be similar to that used in :ref:`Figure 3.16 <Figure 3.16>` .

P10. 考虑一个可能丢失报文但其最大延迟是已知的信道。修改 ``rdt2.1`` 协议，加入发送方超时与重传功能。请非正式地论证你的协议如何能在该信道上正确通信。

.. toggle::

   P10. Consider a channel that can lose packets but has a maximum delay that is known. Modify protocol ``rdt2.1`` to include sender timeout and retransmit. Informally argue why your protocol can communicate correctly over this channel.

P11. 考虑 :ref:`图 3.14 <Figure 3.14>` 中的 ``rdt2.2`` 接收方，以及在 Wait-for-0-from-below 和 Wait-for-1-from-below 状态中的自迁移中创建新报文段的行为：``sndpkt=make_pkt(ACK, 1, checksum)`` 和 ``sndpkt=make_pkt(ACK, 0, checksum)``。如果从 Wait-for-1-from-below 状态的自迁移中移除此操作，协议是否还能正确工作？请说明理由。如果从 Wait-for-0-from-below 状态的自迁移中移除此事件呢？[提示：在后一种情况下，考虑当第一个从发送方到接收方的报文段被损坏时会发生什么。]

.. toggle::

   P11. Consider the ``rdt2.2`` receiver in :ref:`Figure 3.14 <Figure 3.14>` , and the creation of a new packet in the self-transition (i.e., the transition from the state back to itself) in the Wait-for-0-from-below and the Wait-for-1-from-below states: ``sndpkt=make_pkt(ACK, 1, checksum)`` and ``sndpkt=make_pkt(ACK, 0, checksum)``. Would the protocol work correctly if this action were removed from the self-transition in the Wait-for-1-from-below state? Justify your answer. What if this event were removed from the self-transition in the Wait-for-0-from-below state? [Hint: In this latter case, consider what would happen if the first sender-to-receiver packet were corrupted.]

P12. ``rdt3.0`` 协议的发送方会忽略（即不采取任何操作）所有接收到的损坏的报文段或 ACK 报文段中 ``acknum`` 字段值不正确的报文段。假设在这种情况下，``rdt3.0`` 改为重传当前的数据报文段。该协议仍然能工作吗？（提示：考虑当只有比特错误存在、没有报文段丢失但可能出现过早超时时会发生什么。考虑第 n 个报文段最终被发送的次数，在 n 趋于无穷时。）

.. toggle::

   P12. The sender side of ``rdt3.0`` simply ignores (that is, takes no action on) all received packets that are either in error or have the wrong value in the ``acknum`` field of an acknowledgment packet. Suppose that in such circumstances, ``rdt3.0`` were simply to retransmit the current data packet. Would the protocol still work? (Hint: Consider what would happen if there were only bit errors; there are no packet losses but premature timeouts can occur. Consider how many times the nth packet is sent, in the limit as n approaches infinity.)

P13. 考虑 ``rdt 3.0`` 协议。请画出一个图示，说明如果发送方和接收方之间的网络连接可以重排序消息（即，在介质中传播的两个消息可以被重新排序），那么交替位协议将无法正确工作（请明确指出其无法正确工作的具体含义）。你的图应以发送方在左、接收方在右，并沿页面向下表示时间轴，展示数据（D）和确认（A）消息的交换。请确保为每个数据或确认段标明其序列号。

.. toggle::

   P13. Consider the ``rdt 3.0`` protocol. Draw a diagram showing that if the network connection between the sender and receiver can reorder messages (that is, that two messages propagating in the medium between the sender and receiver can be reordered), then the alternating-bit protocol will not work correctly (make sure you clearly identify the sense in which it will not work correctly). Your diagram should have the sender on the left and the receiver on the right, with the time axis running down the page, showing data (D) and acknowledgment (A) message exchange. Make sure you indicate the sequence number associated with any data or acknowledgment segment.

P14. 考虑一个仅使用否定确认（NAK）的可靠数据传输协议。假设发送方很少发送数据。在这种情况下，NAK-only 协议是否优于使用 ACK 的协议？请说明理由。现在假设发送方有大量数据要发送，端到端连接中几乎没有丢失。在这种情况下，NAK-only 协议是否优于使用 ACK 的协议？请说明理由。

.. toggle::

   P14. Consider a reliable data transfer protocol that uses only negative acknowledgments. Suppose the sender sends data only infrequently. Would a NAK-only protocol be preferable to a protocol that uses ACKs? Why? Now suppose the sender has a lot of data to send and the end- to-end connection experiences few losses. In this second case, would a NAK-only protocol be preferable to a protocol that uses ACKs? Why?

P15. 考虑 :ref:`图 3.17 <Figure 3.17>` 中展示的跨国场景。为了让信道利用率大于 98%，窗口大小应该多大？假设每个分组大小为 1500 字节（包括首部和数据）。

.. toggle::

   P15. Consider the cross-country example shown in :ref:`Figure 3.17 <Figure 3.17>` . How big would the window size have to be for the channel utilization to be greater than 98 percent? Suppose that the size of a packet is 1,500 bytes, including both header fields and data.

P16. 假设某应用程序使用 ``rdt 3.0`` 作为其传输层协议。由于停止等待协议的信道利用率非常低（在跨国示例中有所体现），该应用程序的设计者让接收方即使尚未收到对应的数据，也不断发送多个交替的 ACK 0 和 ACK 1。这种设计是否能提高信道利用率？为什么？这种方法是否存在潜在问题？请解释。

.. toggle::

   P16. Suppose an application uses ``rdt 3.0`` as its transport layer protocol. As the stop-and-wait protocol has very low channel utilization (shown in the cross-country example), the designers of this application let the receiver keep sending back a number (more than two) of alternating ACK 0 and ACK 1 even if the corresponding data have not arrived at the receiver. Would this application design increase the channel utilization? Why? Are there any potential problems with this approach? Explain.

P17. 考虑两个网络实体 A 和 B，它们通过一个完美的双向信道连接（即任何消息发送后都能正确接收；该信道不会损坏、丢失或重排序报文段）。A 和 B 需交替向对方传递数据消息：首先 A 向 B 发送一个消息，然后 B 向 A，再接着是 A 向 B，依此类推。如果某实体当前处于不应尝试发送消息的状态，但从上层收到 ``rdt_send(data)`` 调用试图发送数据，该调用应被忽略，同时调用 ``rdt_unable_to_send(data)``，通知上层当前不能发送数据。[注意：该简化假设意在避免处理数据缓冲问题。]请绘制该协议的 FSM 规范（一份用于 A，一份用于 B）。不需要处理可靠性机制；本题重点是构建体现两实体同步行为的 FSM。你应使用与 :ref:`图 3.9 <Figure 3.9>` 中 ``rdt1.0`` 协议相同含义的事件与操作： ``rdt_send(data), packet = make_pkt(data), udt_send(packet), rdt_rcv(packet), extract(packet, data), deliver_data(data)`` 。请确保你的协议体现 A 和 B 之间严格的交替发送行为，并标明 FSM 的初始状态。

.. toggle::

   P17. Consider two network entities, A and B, which are connected by a perfect bi-directional channel (i.e., any message sent will be received correctly; the channel will not corrupt, lose, or re-order packets). A and B are to deliver data messages to each other in an alternating manner: First, A must deliver a message to B, then B must deliver a message to A, then A must deliver a message to B and so on. If an entity is in a state where it should not attempt to deliver a message to the other side, and there is an event like ``rdt_send(data)`` call from above that attempts to pass data down for transmission to the other side, this call from above can simply be ignored with a call to ``rdt_unable_to_send(data)``, which informs the higher layer that it is currently not able to send data. [Note: This simplifying assumption is made so you don’t have to worry about buffering data.] Draw a FSM specification for this protocol (one FSM for A, and one FSM for B!). Note that you do not have to worry about a reliability mechanism here; the main point of this question is to create a FSM specification that reflects the synchronized behavior of the two entities. You should use the following events and actions that have the same meaning as protocol rdt1.0 in :ref:`Figure 3.9 <Figure 3.9>` : ``rdt_send(data), packet = make_pkt(data), udt_send(packet), rdt_rcv(packet), extract(packet, data), deliver_data(data)``. Make sure your protocol reflects the strict alternation of sending between A and B. Also, make sure to indicate the initial states for A and B in your FSM descriptions.

P18. 在我们于 :ref:`第 3.4.4 节 <c3.4.4>` 中学习的通用 SR 协议中，发送方在数据可用且位于窗口范围内时立即发送，而不等待确认。现在我们希望构建一个 SR 协议，使其每次发送两个消息，即发送方每次发送一对消息，且仅在确定这对消息都被正确接收后才发送下一对。假设信道可能丢失消息但不会损坏或重排序消息。请为单向可靠消息传输设计一个差错控制协议，给出发送方和接收方的 FSM 说明。描述发送方与接收方之间报文段的格式。如你使用了除 :ref:`第 3.4 节 <c3.4>` 中介绍的过程调用（如 ``udt_send()``、 ``start_timer()``、 ``rdt_rcv()`` 等）以外的函数，请明确其行为。请给出一个示例（发送方和接收方的时间线轨迹），展示你的协议如何从报文丢失中恢复。

.. toggle::
 
   P18. In the generic SR protocol that we studied in :ref:`Section 3.4.4 <c3.4.4>` , the sender transmits a message as soon as it is available (if it is in the window) without waiting for an acknowledgment. Suppose now that we want an SR protocol that sends messages two at a time. That is, the sender will send a pair of messages and will send the next pair of messages only when it knows that both messages in the first pair have been received correctly. Suppose that the channel may lose messages but will not corrupt or reorder messages. Design an error-control protocol for the unidirectional reliable transfer of messages. Give an FSM description of the sender and receiver. Describe the format of the packets sent between sender and receiver, and vice versa. If you use any procedure calls other than those in :ref:`Section 3.4 <c3.4>` (for example, ``udt_send()``, ``start_timer()``, ``rdt_rcv()``, and so on), clearly state their actions. Give an example (a timeline trace of sender and receiver) showing how your protocol recovers from a lost packet.

P19. 考虑一个场景，主机 A 需要同时向主机 B 和主机 C 发送报文。A 通过一个广播信道与 B 和 C 相连——A 发送的报文会被该信道同时传送给 B 和 C。假设连接 A、B、C 的广播信道可能独立地丢失或损坏报文（例如，A 发送的一个报文可能被 B 正确接收，但 C 却未接收）。请设计一个类似停止等待的差错控制协议，使得 A 能可靠地将报文发送至 B 和 C，并且在确认 B 和 C 都已正确接收当前报文前，A 不会从上层获取新数据。给出 A 和 C 的 FSM 说明。（提示：B 的 FSM 应与 C 基本相同。）同时，说明所使用的报文格式。

.. toggle::

   P19. Consider a scenario in which Host A wants to simultaneously send packets to Hosts B and C. A is connected to B and C via a broadcast channel—a packet sent by A is carried by the channel to both B and C. Suppose that the broadcast channel connecting A, B, and C can independently lose and corrupt packets (and so, for example, a packet sent from A might be correctly received by B, but not by C). Design a stop-and-wait-like error-control protocol for reliably transferring packets from A to B and C, such that A will not get new data from the upper layer until it knows that both B and C have correctly received the current packet. Give FSM descriptions of A and C. (Hint: The FSM for B should be essentially the same as for C.) Also, give a description of the packet format(s) used.

P20. 考虑一个场景，主机 A 和主机 B 需要向主机 C 发送消息。A 和 C 之间通过一个可能丢失和损坏（但不重排序）消息的信道连接；B 和 C 之间通过另一条独立的、具有相同属性的信道连接。C 的传输层应按交替顺序将来自 A 和 B 的消息传递给上层（即：先传递一个来自 A 的报文的数据，然后是 B，再是 A，如此交替）。

.. toggle::

   P20. Consider a scenario in which Host A and Host B want to send messages to Host C. Hosts A and C are connected by a channel that can lose and corrupt (but not reorder) messages. Hosts B and C are connected by another channel (independent of the channel connecting A and C) with the same properties. The transport layer at Host C should alternate in delivering messages from A and B to the layer above (that is, it should first deliver the data from a packet from A, then the data from a packet from B, and so on). Design a stop-and-wait-like error-control protocol for reliably transferring packets from A and B to C, with alternating delivery at C as described above. Give FSM descriptions of A and C. (Hint: The FSM for B should be essentially the same as for A.) Also, give a description of the packet format(s) used.

P21. 假设我们有两个网络实体 A 和 B。B 拥有一组数据消息，将按以下方式发送给 A。当 A 从上层收到请求获取 B 的下一个数据（D）消息的请求时，A 必须在 A 到 B 的信道上发送一个请求（R）消息。只有当 B 收到 R 消息时，才能在 B 到 A 的信道上回传一个 D 消息。A 应确保仅向上层交付每条 D 消息的一份副本。A 到 B 的信道中，R 消息可能丢失（但不会损坏）；D 消息一旦发送，则必定被正确接收。两条信道的延迟未知且变化不定。请设计一个协议（给出 FSM 描述），实现上述所需机制，并将消息传递至 A 上层。仅使用绝对必要的机制。

.. toggle::

   P21. Suppose we have two network entities, A and B. B has a supply of data messages that will be sent to A according to the following conventions. When A gets a request from the layer above to get the next data (D) message from B, A must send a request (R) message to B on the A-to-B channel. Only when B receives an R message can it send a data (D) message back to A on the B-to-A channel. A should deliver exactly one copy of each D message to the layer above. R messages can be lost (but not corrupted) in the A-to-B channel; D messages, once sent, are always delivered correctly. The delay along both channels is unknown and variable. Design (give an FSM description of) a protocol that incorporates the appropriate mechanisms to compensate for the loss-prone A-to-B channel and implements message passing to the layer above at entity A, as discussed above. Use only those mechanisms that are absolutely necessary.

P22. 考虑一个 GBN 协议，发送窗口大小为 4，序列号范围为 1024。假设在时刻 t，接收方下一个期望的按序报文段的序列号为 k。假设信道不会重排序消息。请回答以下问题：

a. 在时刻 t，发送方窗口中可能包含哪些序列号的报文段？请说明理由。
b. 在所有可能正在向发送方传播的消息中，ACK 字段可能有哪些值？请说明理由。

.. toggle::

   P22. Consider the GBN protocol with a sender window size of 4 and a sequence number range of 1,024. Suppose that at time t, the next in-order packet that the receiver is expecting has a sequence number of k. Assume that the medium does not reorder messages. Answer the following questions:

   a. What are the possible sets of sequence numbers inside the sender’s window at time t? Justify your answer.
   b. What are all possible values of the ACK field in all possible messages currently propagating back to the sender at time t? Justify your answer.

P23. 考虑 GBN 和 SR 协议。假设序列号空间大小为 k。在每种协议中，为避免发生类似 :ref:`图 3.27 <Figure 3.27>` 中的问题，允许的最大发送窗口大小是多少？

.. toggle::

   p23. Consider the GBN and SR protocols. Suppose the sequence number space is of size k. What is the largest allowable sender window that will avoid the occurrence of problems such as that in :ref:`Figure 3.27 <Figure 3.27>` for each of these protocols?

P24. 对以下问题回答“对”或“错”，并简要说明理由：

a. 在 SR 协议中，发送方有可能收到一个不在其当前窗口内的分组的 ACK。
b. 在 GBN 协议中，发送方有可能收到一个不在其当前窗口内的分组的 ACK。
c. 交替位协议等价于发送方和接收方窗口大小均为 1 的 SR 协议。
d. 交替位协议等价于发送方和接收方窗口大小均为 1 的 GBN 协议。

.. toggle::

   P24. Answer true or false to the following questions and briefly justify your answer:

   a. With the SR protocol, it is possible for the sender to receive an ACK for a packet that falls outside of its current window.
   b. With GBN, it is possible for the sender to receive an ACK for a packet that falls outside of its current window.
   c. The alternating-bit protocol is the same as the SR protocol with a sender and receiver window size of 1.
   d. The alternating-bit protocol is the same as the GBN protocol with a sender and receiver window size of 1.

P25. 我们曾说应用程序可能会选择 UDP 作为其传输协议，因为与 TCP 相比，UDP 提供了对报文段中数据内容与发送时机更精细的应用层控制。

a. 为什么应用程序对报文段中发送的数据具有更多控制权？
b. 为什么应用程序对报文段何时发送具有更多控制权？

.. toggle::

   P25. We have said that an application may choose UDP for a transport protocol because UDP offers finer application control (than TCP) of what data is sent in a segment and when.

   a. Why does an application have more control of what data is sent in a segment? 
   b. Why does an application have more control on when the segment is sent?

P26. 考虑将一个巨大的长度为 L 字节的文件从主机 A 传输到主机 B。假设 MSS 为 536 字节。
a. L 的最大值是多少，以使得 TCP 的序列号不会耗尽？回忆 TCP 序列号字段为 4 字节。
b. 对于 (a) 中得到的 L，计算传输该文件所需的时间。假设每个分段在发送之前都要附加 66 字节的传输层、网络层和数据链路层首部，并通过一条 155 Mbps 的链路发送。忽略流量控制和拥塞控制，因此 A 可以持续不断地连续发送分段。

.. toggle::

   P26. Consider transferring an enormous file of L bytes from Host A to Host B. Assume an MSS of 536 bytes.
   
   a. What is the maximum value of L such that TCP sequence numbers are not exhausted? Recall that the TCP sequence number field has 4 bytes.
   b. For the L you obtain in (a), find how long it takes to transmit the file. Assume that a total of 66 bytes of transport, network, and data-link header are added to each segment before the resulting packet is sent out over a 155 Mbps link. Ignore flow control and congestion control so A can pump out the segments back to back and continuously.

P27. 主机 A 和主机 B 正通过 TCP 连接通信，主机 B 已经从 A 收到了字节 126 及之前的所有字节。假设主机 A 接着连续发送两个分段给 B。第一个和第二个分段分别包含 80 字节和 40 字节的数据。在第一个分段中，序列号为 127，源端口号为 302，目标端口号为 80。主机 B 每收到来自 A 的一个分段都会发送一个确认。

a. 在 A 发往 B 的第二个分段中，序列号、源端口号和目标端口号分别是多少？
b. 如果第一个分段先到达，在对第一个到达分段的确认中，确认号、源端口号和目标端口号分别是多少？
c. 如果第二个分段先到达，在对第一个到达分段的确认中，确认号是多少？
d. 假设 A 发送的两个分段按顺序到达 B。第一个确认丢失，第二个确认在第一次超时之后到达。请绘制一个时序图，显示这些分段及所有其他发送的分段和确认。（假设没有额外的分组丢失。）对于图中的每个分段，给出其序列号和数据字节数；对于每个确认，给出确认号。

.. toggle::

   P27. Host A and B are communicating over a TCP connection, and Host B has already received from A all bytes up through byte 126. Suppose Host A then sends two segments to Host B back-to-back. The first and second segments contain 80 and 40 bytes of data, respectively. In the first segment, the sequence number is 127, the source port number is 302, and the destination port number is 80. Host B sends an acknowledgment whenever it receives a segment from Host A.

   a. In the second segment sent from Host A to B, what are the sequence number, source port number, and destination port number?
   b. If the first segment arrives before the second segment, in the acknowledgment of the first arriving segment, what is the acknowledgment number, the source port number, and the destination port number?
   c. If the second segment arrives before the first segment, in the acknowledgment of the first arriving segment, what is the acknowledgment number?
   d. Suppose the two segments sent by A arrive in order at B. The first acknowledgment is lost and the second acknowledgment arrives after the first timeout interval. Draw a timing diagram, showing these segments and all other segments and acknowledgments sent. (Assume there is no additional packet loss.) For each segment in your figure, provide the sequence number and the number of bytes of data; for each acknowledgment that you add, provide the acknowledgment number.

P28. 主机 A 和主机 B 通过一条 100 Mbps 的链路直接连接。两主机之间有一个 TCP 连接，主机 A 正通过该连接向主机 B 发送一个巨大文件。主机 A 可以以最高 120 Mbps 的速率将应用数据写入其 TCP 套接字，而主机 B 最多只能以 50 Mbps 的速率从 TCP 接收缓冲区中读取数据。请描述 TCP 流量控制的效果。

.. toggle::

   P28. Host A and B are directly connected with a 100 Mbps link. There is one TCP connection between the two hosts, and Host A is sending to Host B an enormous file over this connection. Host A can send its application data into its TCP socket at a rate as high as 120 Mbps but Host B can read out of its TCP receive buffer at a maximum rate of 50 Mbps. Describe the effect of TCP flow control.

P29. SYN cookies 在 :ref:`第 3.5.6 节 <c3.5.6>` 中讨论过。

a. 为什么服务器需要在 SYNACK 中使用一个特殊的初始序列号？
b. 假设攻击者知道目标主机使用 SYN cookies。攻击者是否可以通过仅发送 ACK 报文给目标主机来建立半开连接或完全连接？为什么？
c. 假设攻击者收集了大量服务器发送的初始序列号。攻击者是否可以通过使用这些初始序列号发送 ACK 来使服务器创建大量完全打开的连接？为什么？

.. toggle::

   P29. SYN cookies were discussed in :ref:`Section 3.5.6 <c3.5.6>`.

   a. Why is it necessary for the server to use a special initial sequence number in the SYNACK?
   b. Suppose an attacker knows that a target host uses SYN cookies. Can the attacker create half-open or fully open connections by simply sending an ACK packet to the target? Why or why not?
   c. Suppose an attacker collects a large amount of initial sequence numbers sent by the server. Can the attacker cause the server to create many fully open connections by sending ACKs with those initial sequence numbers? Why?

P30. 考虑 :ref:`第 3.6.1 节 <c3.6.1>` 中场景 2 所示的网络。假设发送主机 A 和 B 都使用固定的超时时间值。

a. 请论证：增加路由器有限缓冲区的大小可能会降低吞吐量（λout）。
b. 现在假设两个主机根据路由器的缓冲延迟动态调整其超时时间（类似 TCP 的方式）。增加缓冲区大小是否有助于提高吞吐量？请说明理由。

.. toggle::

   P30. Consider the network shown in Scenario 2 in :ref:`Section 3.6.1 <c3.6.1>` . Suppose both sending hosts A and B have some fixed timeout values.

   a. Argue that increasing the size of the finite buffer of the router might possibly decrease the throughput (λout).
   b. Now suppose both hosts dynamically adjust their timeout values (like what TCP does) based on the buffering delay at the router. Would increasing the buffer size help to increase the throughput? Why?

P31. 假设测得的五个 ``SampleRTT`` 值为 106 ms、120 ms、140 ms、90 ms 和 115 ms。使用 α=0.125，并假设在获得这五个样本之前， ``EstimatedRTT`` 的初始值为 100 ms。请在每个样本获取后计算 ``EstimatedRTT``。同时使用 β=0.25，且假设 ``DevRTT`` 的初始值为 5 ms，计算每个样本后的 ``DevRTT``。最后，计算每个样本后的 TCP ``TimeoutInterval``。

.. toggle::

   P31. Suppose that the five measured ``SampleRTT`` values (see :ref:`Section 3.5.3 <c3.5.3>` ) are 106 ms, 120 ms, 140 ms, 90 ms, and 115 ms. Compute the ``EstimatedRTT`` after each of these SampleRTT values is obtained, using a value of α=0.125 and assuming that the value of ``EstimatedRTT`` was 100 ms just before the first of these five samples were obtained. Compute also the ``DevRTT`` after each sample is obtained, assuming a value of β=0.25 and assuming the value of ``DevRTT`` was 5 ms just before the first of these five samples was obtained. Last, compute the TCP ``TimeoutInterval`` after each of these samples is obtained.

P32. 考虑 TCP 的 RTT 估计过程。假设 α=0.1。令 ``SampleRTT1`` 为最新采样 RTT， ``SampleRTT2`` 为次新的采样 RTT，依此类推。

a. 对于某个 TCP 连接，假设返回了四个确认，对应的 SampleRTT 分别为： ``SampleRTT4``、 ``SampleRTT3``、 ``SampleRTT2`` 和 ``SampleRTT1``。请用这些值表示 ``EstimatedRTT``。
b. 将你的公式推广为 n 个 SampleRTT。
c. 对于 (b) 中的公式，令 n 趋于无穷。请评论为何该平均过程被称为指数加权移动平均。

.. toggle::

   P32. Consider the TCP procedure for estimating RTT. Suppose that α=0.1. Let ``SampleRTT1`` be the most recent sample RTT, let ``SampleRTT2`` be the next most recent sample RTT, and so on.

   a. For a given TCP connection, suppose four acknowledgments have been returned with corresponding sample RTTs: ``SampleRTT4``, ``SampleRTT3``, ``SampleRTT2``, and
   ``SampleRTT1``. Express ``EstimatedRTT`` in terms of the four sample RTTs.
   b. Generalize your formula for n sample RTTs.
   c. For the formula in part (b) let n approach infinity. Comment on why this averaging procedure is called an exponential moving average.

P33. 在 :ref:`第 3.5.3 节 <c3.5.3>` 中，我们讨论了 TCP 对 RTT 的估计。你认为为什么 TCP 避免对重传的报文段测量 SampleRTT？

.. toggle::

   P33. In :ref:`Section 3.5.3 <c3.5.3>` , we discussed TCP’s estimation of RTT. Why do you think TCP avoids measuring the SampleRTT for retransmitted segments?

P34. 第 3.5.4 节中的变量 SendBase 与 :ref:`第 3.5.5 节 <c3.5.5>` 中的变量 LastByteRcvd 之间是什么关系？

.. toggle::

   P34. What is the relationship between the variable SendBase in Section 3.5.4 and the variable LastByteRcvd in :ref:`Section 3.5.5 <c3.5.5>` ?

P35. 第 3.5.5 节中的变量 LastByteRcvd 与 :ref:`第 3.5.4 节 <c3.5.4>` 中的变量 y 之间是什么关系？

.. toggle::

   P35. What is the relationship between the variable LastByteRcvd in Section 3.5.5 and the variable y in :ref:`Section 3.5.4 <c3.5.4>`?

P36. 在 :ref:`第 3.5.4 节 <c3.5.4>` 中我们看到，TCP 要在收到三个重复 ACK 后才执行快速重传。你认为为什么 TCP 设计者没有在收到第一个重复 ACK 时就进行快速重传？

.. toggle::

   P36. In :ref:`Section 3.5.4 <c3.5.4>` , we saw that TCP waits until it has received three duplicate ACKs before performing a fast retransmit. Why do you think the TCP designers chose not to perform a fast retransmit after the first duplicate ACK for a segment is received?

P37. 比较 GBN、SR 和 TCP（不使用延迟确认）。假设三种协议的超时时间都足够长，使得接收主机（主机 B）和发送主机（主机 A）能够接收到（如果在信道中未丢失）连续的 5 个数据分段及其对应的 ACK。假设主机 A 向主机 B 发送了 5 个数据分段，而第 2 个分段在传输中丢失。最终，主机 B 成功接收了全部 5 个数据分段。

a. 主机 A 总共发送了多少个分段？主机 B 总共发送了多少个 ACK？它们的序列号分别是多少？请对三种协议分别回答。
b. 如果三种协议的超时时间都远大于 5 个 RTT，那么哪种协议在最短的时间内成功传送所有 5 个数据分段？

.. toggle::

   P37. Compare GBN, SR, and TCP (no delayed ACK). Assume that the timeout values for all three protocols are sufficiently long such that 5 consecutive data segments and their corresponding ACKs can be received (if not lost in the channel) by the receiving host (Host B) and the sending host (Host A) respectively. Suppose Host A sends 5 data segments to Host B, and the 2nd segment (sent from A) is lost. In the end, all 5 data segments have been correctly received by Host B.

   a. How many segments has Host A sent in total and how many ACKs has Host B sent in total? What are their sequence numbers? Answer this question for all three protocols.
   b. If the timeout values for all three protocol are much longer than 5 RTT, then which protocol successfully delivers all five data segments in shortest time interval?

P38. 在我们对 TCP 的描述中（见 :ref:`图 3.53 <Figure 3.53>`），在多个位置中都设置阈值 ``ssthresh=cwnd/2``，即在发生丢包事件时，``ssthresh`` 设置为窗口大小的一半。当丢包事件发生时，发送方的发送速率是否必定约等于 cwnd 个分段每 RTT？请解释你的答案。如果答案是否定的，你是否能提出一个设置 ``ssthresh`` 的替代方式？

.. toggle::

   P38. In our description of TCP in :ref:`Figure 3.53 <Figure 3.53>` , the value of the threshold, ``ssthresh``, is set as ``ssthresh=cwnd/2`` in several places and ``ssthresh`` value is referred to as being set to half the window size when a loss event occurred. Must the rate at which the sender is sending when the loss event occurred be approximately equal to cwnd segments per RTT? Explain your answer. If your answer is no, can you suggest a different manner in which ``ssthresh`` should be set?

P39. 考虑 :ref:`图 3.46(b) <Figure 3.46>`。如果 λ′in 增加到超过 R/2，λout 是否可以增加到超过 R/3？请解释。现在考虑 :ref:`图 3.46(c) <Figure 3.46>`。若假设从路由器转发到接收方的平均跳数为两跳，如果 λ′in 增加到超过 R/2，λout 是否能超过 R/4？请解释。

.. toggle::

   P39. Consider :ref:`Figure 3.46(b) <Figure 3.46>` . If λ′in increases beyond R/2, can λout increase beyond R/3?

   Explain. Now consider :ref:`Figure 3.46(c) <Figure 3.46>` . If λ′in increases beyond R/2, can λout increase beyond R/4 under the assumption that a packet will be forwarded twice on average from the router to the receiver? Explain.

P40. 考虑 :ref:`图 3.58 <Figure 3.58>`。假设 TCP Reno 是当前表现出的协议行为，请回答以下问题。在所有情况下，你都应简要说明理由。

.. figure:: ../img/videonote.png
   :align: center

**分析 TCP 的行为**

a. 标出 TCP 处于慢启动状态的时间区间。
b. 标出 TCP 处于拥塞避免状态的时间区间。
c. 第 16 轮传输之后，段丢失是通过三次重复 ACK 还是超时检测到的？
d. 第 22 轮传输之后，段丢失是通过三次重复 ACK 还是超时检测到的？

   .. figure:: ../img/340-1.png
      :align: center

   .. _Figure 3.58:

   **图 3.58 TCP 窗口大小随时间的变化**

e. 第 1 轮传输中 ssthresh 的初始值是多少？
f. 第 18 轮传输中 ssthresh 的值是多少？
g. 第 24 轮传输中 ssthresh 的值是多少？
h. 第 70 个分段在第几轮传输中被发送？
i. 假设第 26 轮之后通过接收三次重复 ACK 检测到分组丢失，此时的拥塞窗口大小和 ssthresh 的值分别是多少？
j. 假设使用 TCP Tahoe（而非 Reno），并且在第 16 轮收到了三次重复 ACK。第 19 轮时的 ssthresh 和拥塞窗口大小分别是多少？
k. 同样假设使用 TCP Tahoe，并且在第 22 轮发生了超时事件。从第 17 轮到第 22 轮（包含）期间，一共发送了多少个分段？

.. toggle::

   P40. Consider :ref:`Figure 3.58 <Figure 3.58>` . Assuming TCP Reno is the protocol experiencing the behavior shown above, answer the following questions. In all cases, you should provide a short discussion justifying your answer.

   .. figure:: ../img/videonote.png
      :align: center

   **Examining the behavior of TCP**

   a. Identify the intervals of time when TCP slow start is operating.
   b. Identify the intervals of time when TCP congestion avoidance is operating.
   c. After the 16th transmission round, is segment loss detected by a triple duplicate ACK or by a timeout?
   d. After the 22nd transmission round, is segment loss detected by a triple duplicate ACK or by a timeout?

      .. figure:: ../img/340-1.png
         :align: center
      
      **Figure 3.58 TCP window size as a function of time**

   e. What is the initial value of ssthresh at the first transmission round?
   f. What is the value of ssthresh at the 18th transmission round?
   g. What is the value of ssthresh at the 24th transmission round?
   h. During what transmission round is the 70th segment sent?
   i. Assuming a packet loss is detected after the 26th round by the receipt of a triple duplicate ACK, what will be the values of the congestion window size and of
   ssthresh ?
   j. Suppose TCP Tahoe is used (instead of TCP Reno), and assume that triple duplicate ACKs are received at the 16th round. What are the ssthresh and the congestion window size at the 19th round?
   k. Again suppose TCP Tahoe is used, and there is a timeout event at 22nd round. How many packets have been sent out from 17th round till 22nd round, inclusive?

P41. 参见 :ref:`图 3.55 <Figure 3.55>`，该图展示了 TCP 的 AIMD 算法的收敛过程。假设 TCP 不再使用乘性减小，而是每次将窗口大小减小一个固定值。那么由此产生的 AIAD 算法是否会收敛到一个公平分配算法？请使用类似 :ref:`图 3.55 <Figure 3.55>` 的图来证明你的答案。

.. toggle::

   P41. Refer to :ref:`Figure 3.55 <Figure 3.55>` , which illustrates the convergence of TCP’s AIMD algorithm. Suppose that instead of a multiplicative decrease, TCP decreased the window size by a constant amount.

   Would the resulting AIAD algorithm converge to an equal share algorithm? Justify your answer using a diagram similar to :ref:`Figure 3.55 <Figure 3.55>` .

P42. 在 :ref:`第 3.5.4 节 <c3.5.4>` 中，我们讨论了在发生超时事件后将超时时间加倍的机制。该机制是一种拥塞控制形式。为什么 TCP 除了这个超时加倍机制外，还需要一个基于窗口的拥塞控制机制（参见 :ref:`第 3.7 节 <c3.7>`）？

.. toggle::

   P42. In :ref:`Section 3.5.4 <c3.5.4>` , we discussed the doubling of the timeout interval after a timeout event. This mechanism is a form of congestion control. Why does TCP need a window-based congestion-control mechanism (as studied in :ref:`Section 3.7 <c3.7>` ) in addition to this doubling-timeout- interval mechanism?

P43. 主机 A 通过 TCP 连接向主机 B 发送一个巨大文件。在该连接上传输过程中没有任何分组丢失，也没有定时器超时。设连接主机 A 到因特网的链路速率为 R bps。假设主机 A 中的进程可以以 S bps 的速率将数据写入其 TCP 套接字，其中 S=10⋅R。进一步假设 TCP 接收缓冲区足够大，可以容纳整个文件，而发送缓冲区只能容纳文件的 1%。是什么阻止主机 A 中的进程以 S bps 的速率持续不断地向其 TCP 套接字传输数据？是 TCP 的流量控制？TCP 的拥塞控制？还是其他原因？请详细说明。

.. toggle::

   P43. Host A is sending an enormous file to Host B over a TCP connection. Over this connection there is never any packet loss and the timers never expire. Denote the transmission rate of the link connecting Host A to the Internet by R bps. Suppose that the process in Host A is capable of sending data into its TCP socket at a rate S bps, where S=10⋅R. Further suppose that the TCP receive buffer is large enough to hold the entire file, and the send buffer can hold only one percent of the file. What would prevent the process in Host A from continuously passing data to its TCP socket at rate S bps? TCP flow control? TCP congestion control? Or something else? Elaborate.

P44. 考虑通过一个无丢包的 TCP 连接从一台主机向另一台主机发送一个大文件。

a. 假设 TCP 使用 AIMD 拥塞控制而不使用慢启动。假设每次收到一批 ACK 时 cwnd 增加 1 MSS，且往返时间（RTT）大致恒定，那么 cwnd 从 6 MSS 增长到 12 MSS 需要多长时间（假设无丢包）？
b. 在 t=6 RTT 之前，该连接的平均吞吐量是多少（以 MSS 和 RTT 表示）？

.. toggle::

   P44. Consider sending a large file from a host to another over a TCP connection that has no loss.

   a. Suppose TCP uses AIMD for its congestion control without slow start. Assuming cwnd increases by 1 MSS every time a batch of ACKs is received and assuming approximately constant round-trip times, how long does it take for cwnd increase from 6 MSS to 12 MSS (assuming no loss events)?
   b. What is the average throughout (in terms of MSS and RTT) for this connection up through time=6 RTT?

P45. 回顾 TCP 吞吐量的宏观描述。从连接速率从 W/(2·RTT) 变化到 W/RTT 的时间段内，仅发生一个分组丢失（在该时间段的末尾）。

a. 证明丢包率（丢失分组所占的比例）为 L=loss rate=138W²+34W
b. 使用上述结果证明：如果某连接的丢包率为 L，则其平均速率大致为 ≈1.22⋅MSS/RTT⋅√(1/L)

.. toggle::

   P45. Recall the macroscopic description of TCP throughput. In the period of time from when the connection’s rate varies from W/(2 · RTT) to W/RTT, only one packet is lost (at the very end of the period).

   a. Show that the loss rate (fraction of packets lost) is equal to L=loss rate=138W2+34W
   b. Use the result above to show that if a connection has loss rate L, then its average rate is approximately given by ≈1.22⋅MSSRTTL

P46. 假设仅一个 TCP（Reno）连接使用一条 10 Mbps 的链路，且该链路不缓冲任何数据。假设这是发送方和接收方之间唯一拥塞的链路。假设 TCP 发送方有一个巨大的文件要发送，接收方的接收缓冲区远大于拥塞窗口。我们还做出如下假设：每个 TCP 分段大小为 1500 字节；该连接的双向传播延迟为 150 毫秒；该 TCP 连接始终处于拥塞避免阶段，即忽略慢启动。

a. 该 TCP 连接能达到的最大窗口大小（以分段为单位）是多少？
b. 该 TCP 连接的平均窗口大小（以分段为单位）和平均吞吐量（以 bps 为单位）是多少？
c. 在发生分组丢失后，该 TCP 连接需要多长时间才能再次达到其最大窗口？

.. toggle::

   P46. Consider that only a single TCP (Reno) connection uses one 10Mbps link which does not buffer any data. Suppose that this link is the only congested link between the sending and receiving hosts. Assume that the TCP sender has a huge file to send to the receiver, and the receiver’s receive buffer is much larger than the congestion window. We also make the following assumptions: each TCP segment size is 1,500 bytes; the two-way propagation delay of this connection is 150 msec; and this TCP connection is always in congestion avoidance phase, that is, ignore slow start.

   a. What is the maximum window size (in segments) that this TCP connection can achieve?
   b. What is the average window size (in segments) and average throughput (in bps) of this TCP connection?
   c. How long would it take for this TCP connection to reach its maximum window again after recovering from a packet loss?

P47. 考虑上题中描述的场景。假设该 10 Mbps 链路可以缓冲有限数量的分段。请论证：为了使链路始终保持繁忙地发送数据，我们希望选择一个至少等于链路速率 C 与发送方和接收方之间双向传播时延之积的缓冲区大小。

.. toggle::

   P47. Consider the scenario described in the previous problem. Suppose that the 10Mbps link can buffer a finite number of segments. Argue that in order for the link to always be busy sending data, we would like to choose a buffer size that is at least the product of the link speed C and the two-way propagation delay between the sender and the receiver.

P48. 重复第 46 题，但将 10 Mbps 链路替换为 10 Gbps 链路。注意在你对 c 部分的回答中，你会发现从丢包恢复到再次达到最大窗口大小需要非常长的时间。请草拟一个解决方案来解决这个问题。

.. toggle::

   P48. Repeat Problem 46, but replacing the 10 Mbps link with a 10 Gbps link. Note that in your answer to part c, you will realize that it takes a very long time for the congestion window size to reach its maximum window size after recovering from a packet loss. Sketch a solution to solve this problem.

P49. 设 T（以 RTT 为单位）表示一个 TCP 连接将其拥塞窗口大小从 W/2 增加到 W 所需的时间，其中 W 是最大拥塞窗口大小。请论证 T 是 TCP 平均吞吐量的函数。

.. toggle::

   P49. Let T (measured by RTT) denote the time interval that a TCP connection takes to increase its congestion window size from W/2 to W, where W is the maximum congestion window size. Argue that T is a function of TCP’s average throughput.

P50. 考虑一个简化的 TCP AIMD 算法，其中拥塞窗口大小以分段数衡量，而不是字节数。在加性增加中，拥塞窗口每 RTT 增加一个分段；在乘性减少中，拥塞窗口减半（若结果不是整数，则向下取整）。假设两个 TCP 连接 C1 和 C2 共享一条速率为 30 段/秒的拥塞链路。假设 C1 和 C2 都处于拥塞避免阶段。连接 C1 的 RTT 为 50 毫秒，连接 C2 的 RTT 为 100 毫秒。假设当链路上的数据速率超过链路速率时，所有 TCP 连接都会经历分段丢失。

a. 如果 C1 和 C2 在时刻 t0 的拥塞窗口都为 10 段，那么在 1000 毫秒后它们的窗口大小分别是多少？
b. 从长期来看，这两个连接是否会获得相同的链路带宽份额？请说明理由。

.. toggle::

   P50. Consider a simplified TCP’s AIMD algorithm where the congestion window size is measured in number of segments, not in bytes. In additive increase, the congestion window size increases by one segment in each RTT. In multiplicative decrease, the congestion window size decreases by half (if the result is not an integer, round down to the nearest integer). Suppose that two TCP connections, C1 and C2, share a single congested link of speed 30 segments per second. Assume that both C1 and C2 are in the congestion avoidance phase. Connection C1’s RTT is 50 msec and connection C2’s RTT is 100 msec. Assume that when the data rate in the link exceeds the link’s speed, all TCP connections experience data segment loss.

   a. If both C1 and C2 at time t0 have a congestion window of 10 segments, what are their congestion window sizes after 1000 msec?
   b. In the long run, will these two connections get the same share of the bandwidth of the congested link? Explain.

P51. 考虑上题中的网络。现在假设两个 TCP 连接 C1 和 C2 的 RTT 均为 100 毫秒。假设在时刻 t0，C1 的拥塞窗口为 15 段，C2 为 10 段。

a. 在 2200 毫秒后，它们的拥塞窗口大小分别是多少？
b. 从长期来看，这两个连接是否会获得大致相同的链路带宽份额？
c. 如果两个连接在相同时间达到其最大窗口并在相同时间达到其最小窗口，我们称这两个连接是同步的。从长期来看，这两个连接最终会同步吗？若会，它们的最大窗口大小是多少？
d. 这种同步是否有助于提升共享链路的利用率？为什么？请简述一种打破同步的方法。

.. toggle::

   P51. Consider the network described in the previous problem. Now suppose that the two TCP connections, C1 and C2, have the same RTT of 100 msec. Suppose that at time t0, C1’s congestion window size is 15 segments but C2’s congestion window size is 10 segments.

   a. What are their congestion window sizes after 2200 msec?
   b. In the long run, will these two connections get about the same share of the bandwidth of the congested link?
   c. We say that two connections are synchronized, if both connections reach their maximum window sizes at the same time and reach their minimum window sizes at the same time. In the long run, will these two connections get synchronized eventually? If so, what are their maximum window sizes?
   d. Will this synchronization help to improve the utilization of the shared link? Why? Sketch some idea to break this synchronization.

P52. 考虑对 TCP 拥塞控制算法的修改。我们用乘性增加代替加性增加。每当收到一个有效的 ACK，TCP 发送方将其窗口大小增加一个小的正数 a（0<a<1）。请找出丢包率 L 与最大拥塞窗口 W 之间的函数关系。请论证：对于该修改版 TCP，不论其平均吞吐量如何，TCP 连接从 W/2 增长到 W 总花费相同的时间。

.. toggle::

   P52. Consider a modification to TCP’s congestion control algorithm. Instead of additive increase, we can use multiplicative increase. A TCP sender increases its window size by a small positive constant a(0<a<1) whenever it receives a valid ACK. Find the functional relationship between loss rate L and maximum congestion window W. Argue that for this modified TCP, regardless of TCP’s average throughput, a TCP connection always spends the same amount of time to increase its congestion window size from W/2 to W.

P53. 在我们对 TCP 未来的讨论中（见 :ref:`第 3.7 节 <c3.7>`），我们指出，为实现 10 Gbps 的吞吐量，TCP 只能容忍 2⋅10⁻¹⁰ 的分段丢失概率（等价于每 5,000,000,000 个分段发生一次丢失）。请基于 :ref:`第 3.7 节 <c3.7>` 中给出的 RTT 和 MSS 值，推导出 2⋅10⁻¹⁰（即每 5,000,000 个分段 1 次）这一数值。如果 TCP 需要支持 100 Gbps 的连接，那么可容忍的丢包率是多少？

.. toggle::

   P53. In our discussion of TCP futures in :ref:`Section 3.7 <c3.7>` , we noted that to achieve a throughput of 10 Gbps, TCP could only tolerate a segment loss probability of 2⋅10−10 (or equivalently, one loss event for every 5,000,000,000 segments). Show the derivation for the values of 2⋅10−10 (1 out of 5,000,000) for the RTT and MSS values given in :ref:`Section 3.7 <c3.7>` . If TCP needed to support a 100 Gbps connection, what would the tolerable loss be?

P54. 在我们对 TCP 拥塞控制的讨论中（见 :ref:`第 3.7 节 <c3.7>`），我们默认 TCP 发送方总是有数据可发。现在考虑另一种情况：TCP 发送方发送大量数据后，在 t1 时刻变为空闲（因为没有数据可发）。TCP 保持空闲较长时间，然后在 t2 时刻重新开始发送数据。若在 t2 开始发送数据时使用 t1 时的 ``cwnd`` 和 ``ssthresh`` 值，有何利弊？你推荐的替代方案是什么？为什么？

.. toggle::

   P54. In our discussion of TCP congestion control in :ref:`Section 3.7 <c3.7>` , we implicitly assumed that the TCP sender always had data to send. Consider now the case that the TCP sender sends a large amount of data and then goes idle (since it has no more data to send) at t1. TCP remains idle for a relatively long period of time and then wants to send more data at t2. What are the advantages and disadvantages of having TCP use the ``cwnd`` and ``ssthresh`` values from t1 when starting to send data at t2? What alternative would you recommend? Why?

P55. 本题探讨 UDP 或 TCP 是否提供某种程度的端点认证。

a. 考虑一个服务器，它在接收到一个包含请求的 UDP 报文后，以 UDP 报文进行响应（例如 DNS 服务器）。如果一个客户端使用 IP 地址 X，并将其地址伪装为地址 Y，服务器将把响应发送到哪里？
b. 假设服务器收到一个源 IP 地址为 Y 的 SYN，在响应一个 SYNACK 后收到一个同样源地址为 Y 且具有正确确认号的 ACK。假设服务器选择了一个随机的初始序列号，且不存在“中间人”攻击，服务器是否可以确定客户端确实位于 Y 地址（而非其他伪装成 Y 的地址 X）？

.. toggle::

   P55. In this problem we investigate whether either UDP or TCP provides a degree of end-point authentication.

   a. Consider a server that receives a request within a UDP packet and responds to that request within a UDP packet (for example, as done by a DNS server). If a client with IP address X spoofs its address with address Y, where will the server send its response?
   b. Suppose a server receives a SYN with IP source address Y, and after responding with a SYNACK, receives an ACK with IP source address Y with the correct acknowledgment number. Assuming the server chooses a random initial sequence number and there is no “man-in-the-middle,” can the server be certain that the client is indeed at Y (and not at some other address X that is spoofing Y)?

P56. 本题中我们考虑 TCP 慢启动阶段引入的延迟。考虑客户端与 Web 服务器之间由一条速率为 R 的链路直接连接。假设客户端希望获取一个大小正好为 15 S 的对象，其中 S 为最大报文段大小（MSS）。设客户端与服务器之间的往返时间为 RTT（假设恒定）。忽略协议首部，计算获取该对象所需的总时间（包括建立 TCP 连接的时间），在下列情况下：

a. 4 S/R > S/R + RTT > 2 S/R  
b. S/R + RTT > 4 S/R  
c. S/R > RTT

.. toggle::

   P56. In this problem, we consider the delay introduced by the TCP slow-start phase. Consider a client and a Web server directly connected by one link of rate R. Suppose the client wants to retrieve an object whose size is exactly equal to 15 S, where S is the maximum segment size (MSS). Denote the round-trip time between client and server as RTT (assumed to be constant). Ignoring protocol headers, determine the time to retrieve the object (including TCP connection establishment) when

   a. 4 S/R>S/R+RTT>2S/R 
   b. S/R+RTT>4 S/R
   c. S/R>RTT.

编程作业
-------------------------
Programming Assignments

实现一个可靠的传输协议
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Implementing a Reliable Transport Protocol

在本实验编程作业中，你将编写发送端和接收端的传输层代码，用于实现一个简单的可靠数据传输协议。该实验有两个版本：交替位协议版本和 GBN 版本。这个实验应该很有趣——你所实现的内容与现实中所需的协议几乎没有差别。

由于你可能没有可供修改操作系统的独立机器，你的代码需要在一个模拟的软硬件环境中执行。然而，提供给你实现代码的编程接口——即上层和下层调用你代码的方式——与实际 UNIX 环境非常相似。（事实上，本实验中描述的软件接口远比许多教材中描述的无限循环发送器和接收器更现实。）定时器的启动与停止也是模拟实现的，定时器中断将激活你的定时器处理函数。

完整的实验说明以及你需要与之编译的代码可在本书网站获得： `www.pearsonhighered.com/cs-resources <https://www.pearsonhighered.com/cs-resources>`_。

.. toggle::

   In this laboratory programming assignment, you will be writing the sending and receiving transport-level code for implementing a simple reliable data transfer protocol. There are two versions of this lab, the alternating-bit-protocol version and the GBN version. This lab should be fun—your implementation will differ very little from what would be required in a real-world situation.

   Since you probably don’t have standalone machines (with an OS that you can modify), your code will have to execute in a simulated hardware/software environment. However, the programming interface provided to your routines—the code that would call your entities from above and from below—is very close to what is done in an actual UNIX environment. (Indeed, the software interfaces described in this programming assignment are much more realistic than the infinite loop senders and receivers that many texts describe.) Stopping and starting timers are also simulated, and timer interrupts will cause your timer handling routine to be activated.

   The full lab assignment, as well as code you will need to compile with your own code, are available at this book’s Web site: `www.pearsonhighered.com/cs-resources <https://www.pearsonhighered.com/cs-resources>`_.