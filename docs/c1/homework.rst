


家庭作业问题和疑问
========================================

Homework Problems and Questions

第 1 章 复习问题
--------------------------------
Chapter 1 Review Questions

SECTION 1.1
~~~~~~~~~~~~~~~

R1. 主机和终端系统之间有什么区别？列举几种不同类型的终端系统。Web 服务器是终端系统吗？

R2. 单词“protocol（协议）”经常被用来描述外交关系。维基百科是如何描述外交协议的？

R3. 为什么协议的标准化很重要？

.. toggle::

    R1. What is the difference between a host and an end system? List several different types of end systems. Is a Web server an end system?

    R2. The word protocol is often used to describe diplomatic relations. How does Wikipedia describe diplomatic protocol?

    R3. Why are standards important for protocols?

SECTION 1.2
~~~~~~~~~~~~~~~

R4. 列举六种接入技术。将每种技术分类为家庭接入、企业接入或广域无线接入。

R5. HFC 的传输速率是专用的还是在用户之间共享的？在下行 HFC 信道中是否可能发生碰撞？为什么或为什么不？

R6. 列出你所在城市可用的家庭接入技术。对于每种接入类型，提供其标称下行速率、上行速率以及每月价格。

R7. 以太网 LAN 的传输速率是多少？

R8. 以太网可以运行在哪些物理介质上？

R9. 拨号调制解调器、HFC、DSL 和 FTTH 都用于家庭接入。对于这些接入技术中的每一种，给出其传输速率范围，并说明传输速率是共享的还是专用的。

R10. 描述当前最流行的无线互联网接入技术。对比它们之间的异同。

.. toggle::

    R4. List six access technologies. Classify each one as home access, enterprise access, or wide-area wireless access.
    
    R5. Is HFC transmission rate dedicated or shared among users? Are collisions possible in adownstream HFC channel? Why or why not?
    
    R6. List the available residential access technologies in your city. For each type of access,provide the advertised downstream rate, upstream rate, and monthly price.
    
    R7. What is the transmission rate of Ethernet LANs?
    
    R8. What are some of the physical media that Ethernet can run over?
    
    R9. Dial-up modems, HFC, DSL and FTTH are all used for residential access. For each of theseaccess technologies, provide a range of ­transmission rates and comment on whether thetransmission rate is shared or dedicated.
    
    R10. Describe the most popular wireless Internet access technologies today. ­Compare andcontrast them.

SECTION 1.3
~~~~~~~~~~~~~~~

R11. 假设在发送主机和接收主机之间只有一个分组交换机。发送主机到交换机之间的传输速率为 R1，交换机到接收主机之间的传输速率为 R2。假设交换机使用存储转发分组交换，发送一个长度为 L 的分组的端到端总延迟是多少？（忽略排队延迟、传播延迟和处理延迟。）

R12. 电路交换网络相对于分组交换网络有什么优势？在电路交换网络中，TDM 相对于 FDM 有哪些优势？

R13. 假设用户共享一个 2 Mbps 的链路。又假设每个用户在传输时持续以 1 Mbps 的速率传输，但每个用户只在 20% 的时间内进行传输。（参见 :ref:`第 1.3 节 <c1.3>` 中对统计复用的讨论。）

a. 在使用电路交换时，最多能支持多少个用户？  
b. 在以下问题中，假设使用分组交换。当同时有两个或更少用户传输时，为什么在链路前几乎不会有排队延迟？当有三个用户同时传输时，为什么会出现排队延迟？  
c. 求某个给定用户正在传输的概率。  
d. 假设现在有三个用户。求在任意给定时刻三个用户同时传输的概率。求队列增长的时间比例。

R14. 为什么在层级结构中处于同一级别的两个 ISP 经常会互联（peer）？一个 IXP 是如何盈利的？

R15. 一些内容提供商创建了自己的网络。描述 Google 的网络。是什么促使内容提供商构建这些网络的？

.. toggle::

    R11. Suppose there is exactly one packet switch between a sending host and a receiving host. The transmission rates between the sending host and the switch and between the switch and the receiving host are R1 and R2, respectively. Assuming that the switch uses store-and-forward packet switching, what is the total end-to-end delay to send a packet of length L? (Ignore queuing, propagation delay, and processing delay.)

    R12. What advantage does a circuit-switched network have over a packet-switched network? What advantages does TDM have over FDM in a circuit-switched network?
    
    R13. Suppose users share a 2 Mbps link. Also suppose each user transmits continuously at 1 Mbps when transmitting, but each user transmits only 20 percent of the time. (See the discussion of statistical multiplexing in :ref:`Section 1.3 <c1.3>` .)
    
    a. When circuit switching is used, how many users can be supported?
    b. For the remainder of this problem, suppose packet switching is used. Why will there be essentially no queuing delay before the link if two or fewer users transmit at the same time? Why will there be a queuing delay if three users transmit at the same time?
    c. Find the probability that a given user is transmitting.
    d. Suppose now there are three users. Find the probability that at any given time, all three users are transmitting simultaneously. Find the fraction of time during which the queue grows.
    
    R14. Why will two ISPs at the same level of the hierarchy often peer with each other? How does an IXP earn money?

    R15. Some content providers have created their own networks. Describe Google’s network. What motivates content providers to create these networks?

SECTION 1.4
~~~~~~~~~~~~~~~

R16. 考虑从源主机向目的主机通过一条固定路径发送分组。列出端到端延迟的组成部分。其中哪些延迟是恒定的，哪些是可变的？

R17. 访问配套网站上的“Transmission Versus Propagation Delay”小程序。在提供的速率、传播延迟和分组大小中，找出一个组合，使得发送方在分组的第一个比特到达接收方之前完成发送。再找出一个组合，使得分组的第一个比特在发送方完成发送之前就已到达接收方。

R18. 一个长度为 1000 字节的分组在传播距离为 2500 公里、传播速度为 2.5⋅10⁸ 米/秒、传输速率为 2 Mbps 的链路上传播需要多长时间？更一般地说，一个长度为 L 的分组在距离为 d、传播速度为 s、传输速率为 R bps 的链路上传播需要多长时间？这个延迟是否取决于分组长度？是否取决于传输速率？

R19. 假设主机 A 想向主机 B 发送一个大文件。从 A 到 B 的路径上有三个链路，其速率分别为 R1=500 kbps，R2=2 Mbps，R3=1 Mbps。

a. 假设网络中没有其他流量，文件传输的吞吐量是多少？  
b. 假设文件大小为 400 万字节。将文件大小除以吞吐量，大约需要多少时间才能将文件传输到主机 B？  
c. 重复 (a) 和 (b)，但此时 R2 降低为 100 kbps。

R20. 假设终端系统 A 想向终端系统 B 发送一个大文件。从宏观角度描述终端系统 A 如何将文件分成多个分组。当这些分组中的一个到达路由器时，路由器使用分组中的哪些信息来决定该分组要转发到哪个链路？为什么互联网中的分组交换类似于从一个城市开车到另一个城市并一路询问路线？

R21. 访问配套网站上的“Queuing and Loss”小程序。最大发送速率和最小传输速率分别是多少？在这些速率下，流量强度是多少？运行小程序并确定发生分组丢失所需的时间。然后再次重复实验，再次确定发生分组丢失所需的时间。这两个结果是否不同？为什么或为什么不？

.. toggle::

    R16. Consider sending a packet from a source host to a destination host over a fixed route. List the delay components in the end-to-end delay. Which of these delays are constant and which are variable?

    R17. Visit the Transmission Versus Propagation Delay applet at the companion Web site. Among the rates, propagation delay, and packet sizes available, find a combination for which the sender finishes transmitting before the first bit of the packet reaches the receiver. Find another combination for which the first bit of the packet reaches the receiver before the sender finishes transmitting.

    R18. How long does it take a packet of length 1,000 bytes to propagate over a link of distance 2,500 km, propagation speed 2.5⋅108 m/s, and transmission rate 2 Mbps? More generally, how long does it take a packet of length L to propagate over a link of distance d, propagation speed s, and transmission rate R bps? Does this delay depend on packet length? Does this delay depend on transmission rate?

    R19. Suppose Host A wants to send a large file to Host B. The path from Host A to Host B has three links, of rates R1=500 kbps, R2=2 Mbps, and R3=1 Mbps.

    a. Assuming no other traffic in the network, what is the throughput for the file transfer?
    b. Suppose the file is 4 million bytes. Dividing the file size by the throughput, roughly how long will it take to transfer the file to Host B?
    c. Repeat (a) and (b), but now with R2 reduced to 100 kbps.

    R20. Suppose end system A wants to send a large file to end system B. At a very high level, describe how end system A creates packets from the file. When one of these packets arrives to a router, what information in the packet does the router use to determine the link onto which the packet is forwarded? Why is packet switching in the Internet analogous to driving from one city to another and asking directions along the way?

    R21. Visit the Queuing and Loss applet at the companion Web site. What is the maximum emission rate and the minimum transmission rate? With those rates, what is the traffic intensity? Run the applet with these rates and determine how long it takes for packet loss to occur. Then repeat the experiment a second time and determine again how long it takes for packet loss to occur. Are the values different? Why or why not?

SECTION 1.5
~~~~~~~~~~~~~~~

R22. 列举一层可以执行的五项任务。是否可能有一项或多项任务可由两个或多个层共同执行？

R23. 互联网协议栈有哪五层？每一层的主要职责是什么？

R24. 什么是应用层消息？传输层报文段？网络层数据报？链路层帧？

R25. 路由器处理互联网协议栈中的哪些层？链路层交换机处理哪些层？主机处理哪些层？

.. toggle::
    
    R22. List five tasks that a layer can perform. Is it possible that one (or more) of these tasks could be performed by two (or more) layers?

    R23. What are the five layers in the Internet protocol stack? What are the principal responsibilities of each of these layers?

    R24. What is an application-layer message? A transport-layer segment? A network-layer datagram? A link-layer frame?

    R25. Which layers in the Internet protocol stack does a router process? Which layers does a link-layer switch process? Which layers does a host process?

SECTION 1.6
~~~~~~~~~~~~~~~

R26. 病毒和蠕虫之间有什么区别？

R27. 描述如何创建一个僵尸网络（botnet）以及它如何被用于 DDoS 攻击。

R28. 假设 Alice 和 Bob 通过计算机网络互相发送分组。假设 Trudy 把自己安置在网络中的一个位置，可以捕获 Alice 发送的所有分组并向 Bob 发送任意内容；她也可以捕获 Bob 发送的所有分组并向 Alice 发送任意内容。从这个位置 Trudy 可以做出哪些恶意行为？

.. toggle::

    R26. What is the difference between a virus and a worm?

    R27. Describe how a botnet can be created and how it can be used for a DDoS attack.

    R28. Suppose Alice and Bob are sending packets to each other over a computer network. Suppose Trudy positions herself in the network so that she can capture all the packets sent by Alice and send whatever she wants to Bob; she can also capture all the packets sent by Bob and send whatever she wants to Alice. List some of the malicious things Trudy can do from this position.

Problems
-----------

P1. 设计并描述一个应用层协议，用于自动取款机与银行中心计算机之间的通信。你的协议应支持验证用户的卡片和密码、查询账户余额（该余额由中心计算机维护）、以及进行账户取款操作（即向用户支付现金）。你的协议实体应能处理一种常见情况：账户中余额不足以覆盖取款金额。通过列出交互消息以及自动取款机和银行中心计算机在发送与接收消息时所执行的操作来指定你的协议。用类似于 :ref:`图 1.2 <Figure 1.2>` 的图示勾画该协议在无错误的简单取款情形下的操作流程。明确指出该协议对底层端到端传输服务所作的假设。

.. toggle::

    P1. Design and describe an application-level protocol to be used between an automatic teller machine and a bank’s centralized computer. Your protocol should allow a user’s card and password to be verified, the account balance (which is maintained at the centralized computer) to be queried, and an account withdrawal to be made (that is, money disbursed to the user).
    Your protocol entities should be able to handle the all-too-common case in which there is not enough money in the account to cover the withdrawal. Specify your protocol by listing the messages exchanged and the action taken by the automatic teller machine or the bank’s centralized computer on transmission and receipt of messages. Sketch the operation of your protocol for the case of a simple withdrawal with no errors, using a diagram similar to that in :ref:`Figure 1.2 <Figure 1.2>` . Explicitly state the assumptions made by your protocol about the underlying end-to- end transport service.

P2. :ref:`公式 1.1 <Equation 1.1>` 给出了将一个长度为 L 的分组通过 N 条传输速率为 R 的链路发送时的端到端延迟。请将该公式推广到将 P 个分组连续发送通过 N 条链路的情形。

.. toggle::

    P2. :ref:`Equation 1.1 <Equation 1.1>` gives a formula for the end-to-end delay of sending one packet of length L over N links of transmission rate R. Generalize this formula for sending P such packets back-to- back over the N links.

P3. 考虑一个以稳定速率传输数据的应用（例如，发送方每 k 个时间单位生成一个 N 比特的数据单元，其中 k 很小且固定）。此外，该应用一旦开始运行，将持续相对较长时间。请回答下列问题，并简要说明你的理由：

a. 分组交换网络还是电路交换网络更适合该应用？为什么？  
b. 假设使用的是分组交换网络，且该网络中唯一的流量来自如上所述的此类应用。进一步假设应用的数据总速率小于任意链路的容量。此时是否仍需要某种形式的拥塞控制？为什么？

.. toggle::

    P3. Consider an application that transmits data at a steady rate (for example, the sender generates an N-bit unit of data every k time units, where k is small and fixed). Also, when such an application starts, it will continue running for a relatively long period of time. Answer the following questions, briefly justifying your answer:

    a. Would a packet-switched network or a circuit-switched network be more appropriate for this application? Why?
    b. Suppose that a packet-switched network is used and the only traffic in this network comes from such applications as described above. Furthermore, assume that the sum of the application data rates is less than the capacities of each and every link. Is some form of congestion control needed? Why?

P4. 考虑 :ref:`图 1.13 <Figure 1.13>` 中的电路交换网络。回忆每条链路上有 4 条电路。按顺时针方向将四个交换机标记为 A、B、C 和 D。

a. 在该网络中任意时刻最多可并发多少条连接？  
b. 假设所有连接均在交换机 A 和 C 之间。此时最多可并发多少条连接？  
c. 假设我们要建立 A 与 C 之间的四条连接，以及 B 与 D 之间的另外四条连接。是否可以通过四条链路对这八条连接进行路由？

.. toggle::

    P4. Consider the circuit-switched network in :ref:`Figure 1.13 <Figure 1.13>` . Recall that there are 4 circuits on each link. Label the four switches A, B, C, and D, going in the clockwise direction.

    a. What is the maximum number of simultaneous connections that can be in progress at any one time in this network?
    b. Suppose that all connections are between switches A and C. What is the maximum number of simultaneous connections that can be in progress?
    c. Suppose we want to make four connections between switches A and C, and another four connections between switches B and D. Can we route these calls through the four links to accommodate all eight ­connections?

P5. 回顾 :ref:`第 1.4 节 <c1.4>` 中的汽车车队类比。假设传播速度为 100 公里/小时。

a. 假设车队行驶 150 公里，从第一个收费站前出发，经过第二个收费站，最后在第三个收费站后结束。端到端延迟是多少？  
b. 重复 (a)，但此时车队中有 8 辆车而不是 10 辆。

.. toggle::

    P5. Review the car-caravan analogy in :ref:`Section 1.4 <c1.4>` . Assume a propagation speed of 100 km/hour.

    a. Suppose the caravan travels 150 km, beginning in front of one tollbooth, passing through a second tollbooth, and finishing just after a third tollbooth. What is the end-to-end delay?
    b. Repeat (a), now assuming that there are eight cars in the caravan instead of ten.

P6. 本题将探讨传播延迟和传输延迟这两个数据网络中的核心概念。考虑两个主机 A 和 B，它们通过一条速率为 R bps 的链路连接。假设两主机之间相距 m 米，链路上的传播速度为 s 米/秒。主机 A 要向主机 B 发送一个长度为 L 比特的分组。

.. image:: ../img/101-0.png

探讨传播延迟和传输延迟

a. 用 m 和 s 表示传播延迟 :math:`d_{prop}`。  
b. 用 L 和 R 表示传输时间 :math:`d_{trans}`。  
c. 忽略处理和排队延迟，给出端到端延迟的表达式。  
d. 假设主机 A 在 t=0 时刻开始发送分组。在 t= :math:`d_{trans}` 时刻，分组的最后一位在哪？  
e. 假设 :math:`d_{prop}` 大于 :math:`d_{trans}`。在 t= :math:`d_{trans}` 时刻，分组的第一位在哪？  
f. 假设 :math:`d_{prop}` 小于 :math:`d_{trans}`。在 t= :math:`d_{trans}` 时刻，分组的第一位在哪？  
g. 假设 s=2.5⋅10⁸，L=120 比特，R=56 kbps。求使得 :math:`d_{prop}` 等于 :math:`d_{trans}` 时的距离 m。

.. toggle::

    P6. This elementary problem begins to explore propagation delay and transmission delay, two central concepts in data networking. Consider two hosts, A and B, connected by a single link of rate R bps. Suppose that the two hosts are separated by m meters, and suppose thepropagation speed along the link is s meters/sec. Host A is to send a packet of size L bits to Host B.

    .. image:: ../img/101-0.png
        
    Exploring propagation delay and transmission delay

    a. Express the propagation delay, :math:`d_{prop}`, in terms of m and s.
    b. Determine the transmission time of the packet, :math:`d_{trans}`, in terms of L and R.
    c. Ignoring processing and queuing delays, obtain an expression for the end-to-end delay.
    d. Suppose Host A begins to transmit the packet at time t=0. At time t= :math:`d_{trans}`, where is the last bit of the packet?
    e. Suppose :math:`d_{prop}` is greater than :math:`d_{trans}`. At time t=dtrans, where is the first bit of the packet?
    f. Suppose :math:`d_{prop}` is less than :math:`d_{trans}`. At time t=dtrans, where is the first bit of the packet?
    g. Suppose s=2.5⋅108, L=120 bits, and R=56 kbps. Find the distance m so that :math:`d_{prop}` equals :math:`d_{trans}`.

P7. 本题考虑在分组交换网络上传输实时语音（VoIP），从主机 A 到主机 B。主机 A 将模拟语音实时转换为 64 kbps 的比特流，然后将比特打包成 56 字节的分组。主机 A 与主机 B 之间只有一条链路，其传输速率为 2 Mbps，传播延迟为 10 毫秒。主机 A 每生成一个分组即发送出去。主机 B 每接收一个完整分组即将其内容转换为模拟信号。从主机 A 产生一个比特开始到主机 B 解码该比特为模拟信号为止，经历的时间是多少？

.. toggle::

    P7. In this problem, we consider sending real-time voice from Host A to Host B over a packet- switched network (VoIP). Host A converts analog voice to a digital 64 kbps bit stream on the fly. Host A then groups the bits into 56-byte packets. There is one link between Hosts A and B; its transmission rate is 2 Mbps and its propagation delay is 10 msec. As soon as Host A gathers a packet, it sends it to Host B. As soon as Host B receives an entire packet, it converts the packet’s bits to an analog signal. How much time elapses from the time a bit is created (from the original analog signal at Host A) until the bit is decoded (as part of the analog signal at Host B)?

P8. 假设用户共享一条 3 Mbps 的链路。每个用户在传输时需要 150 kbps，但仅在 10% 的时间内处于传输状态。（参见 :ref:`第 1.3 节 <c1.3>` 中关于分组交换与电路交换的讨论。）

a. 若采用电路交换，最多可支持多少个用户？  
b. 在以下问题中，假设使用分组交换。求一个给定用户正在传输的概率。  
c. 假设有 120 个用户。求任意时刻正好有 n 个用户同时传输的概率。（提示：使用二项分布。）  
d. 求在任意时刻有 21 个或更多用户同时传输的概率。

.. toggle::

    P8. Suppose users share a 3 Mbps link. Also suppose each user requires 150 kbps when transmitting, but each user transmits only 10 percent of the time. (See the discussion of packet switching versus circuit switching in :ref:`Section 1.3 <c1.3>` .)

    a. When circuit switching is used, how many users can be supported?
    b. For the remainder of this problem, suppose packet switching is used. Find the probability
    that a given user is transmitting.
    c. Suppose there are 120 users. Find the probability that at any given time, exactly n users
    are transmitting simultaneously. (Hint: Use the binomial distribution.)
    d. Find the probability that there are 21 or more users transmitting ­simultaneously.

P9. 考虑 :ref:`第 1.3 节 <c1.3>` 中关于分组交换与电路交换的讨论，其中提供了一个 1 Mbps 链路的例子。用户在繁忙时以 100 kbps 速率生成数据，但只有概率 p=0.1 处于繁忙状态。假设 1 Mbps 链路被 1 Gbps 链路替代。

a. 在电路交换下，能同时支持的最大用户数 N 是多少？  
b. 现在考虑分组交换，并假设有 M 个用户。请给出一个关于 p、M 和 N 的公式，计算有超过 N 个用户同时发送数据的概率。

.. toggle::

    P9. Consider the discussion in :ref:`Section 1.3 <c1.3>` of packet switching versus circuit switching in which an example is provided with a 1 Mbps link. Users are generating data at a rate of 100 kbps when busy, but are busy generating data only with probability p=0.1. Suppose that the 1 Mbps link is replaced by a 1 Gbps link.

    a. What is N, the maximum number of users that can be supported simultaneously under circuit switching?
    b. Now consider packet switching and a user population of M users. Give a formula (in terms of p, M, N) for the probability that more than N users are sending data.

P10. 考虑一个长度为 L 的分组从终端系统 A 出发，经过三条链路到达目的终端系统。三条链路之间由两个分组交换机连接。令 di、si 和 Ri 分别表示第 i 条链路的长度、传播速度和传输速率（i=1,2,3）。每个分组交换机会对分组产生 dproc 的处理延迟。假设无排队延迟，用 di、si、Ri (i=1,2,3) 和 L 表示该分组的总端到端延迟。现在假设分组长度为 1500 字节，三条链路上的传播速度为 2.5⋅10⁸ m/s，传输速率均为 2 Mbps，分组交换处理延迟为 3 毫秒，第一条链路长 5000 公里，第二条链路长 4000 公里，第三条链路长 1000 公里。在这些条件下，总端到端延迟是多少？

.. toggle::

    P10. Consider a packet of length L that begins at end system A and travels over three links to a destination end system. These three links are connected by two packet switches. Let di, si, and Ri denote the length, propagation speed, and the transmission rate of link i, for i=1,2,3. The packet switch delays each packet by dproc. Assuming no queuing delays, in terms of di, si, Ri, (i=1,2,3), and L, what is the total end-to-end delay for the packet? Suppose now the packet is 1,500 bytes, the propagation speed on all three links is 2.5⋅108m/s, the transmission rates of all three links are 2 Mbps, the packet switch processing delay is 3 msec, the length of the first link is 5,000 km, the length of the second link is 4,000 km, and the length of the last link is 1,000 km. For these values, what is the end-to-end delay?

P11. 在上述问题中，假设 R1=R2=R3=R 且 dproc=0。进一步假设分组交换机不使用存储转发机制，而是在接收到每个比特后立即进行转发，而无需等待整个分组到达。此时总端到端延迟是多少？

.. toggle::

    P11. In the above problem, suppose R1=R2=R3=R and dproc=0. Further suppose the packet switch does not store-and-forward packets but instead immediately transmits each bit it receives before waiting for the entire packet to arrive. What is the end-to-end delay?

P12. 一个分组交换机收到一个分组，并决定该分组应转发到哪个出链路。当该分组到达时，出链路上已有一个分组正在传输，其传输进度为一半，另外还有 4 个分组正在排队等待传输。分组按照到达顺序进行传输。假设所有分组均为 1500 字节，链路速率为 2 Mbps。该分组的排队延迟是多少？更一般地说，若所有分组长度为 L，传输速率为 R，当前正在传输的分组已传输 x 比特，队列中已有 n 个分组，则排队延迟是多少？

.. toggle::

    P12. A packet switch receives a packet and determines the outbound link to which the packet should be forwarded. When the packet arrives, one other packet is halfway done being transmitted on this outbound link and four other packets are waiting to be transmitted. Packets are transmitted in order of arrival. Suppose all packets are 1,500 bytes and the link rate is 2 Mbps. What is the queuing delay for the packet? More generally, what is the queuing delay when all packets have length L, the transmission rate is R, x bits of the currently-being-transmitted packet have been transmitted, and n packets are already in the queue?

P13.

a. 假设 N 个分组同时到达一条链路，该链路当前没有分组正在传输或排队。每个分组长度为 L，链路传输速率为 R。这 N 个分组的平均排队延迟是多少？  
b. 现在假设每隔 LN/R 秒有 N 个这样的分组到达该链路。每个分组的平均排队延迟是多少？

.. toggle::

    P13.

    a. Suppose N packets arrive simultaneously to a link at which no packets are currently being transmitted or queued. Each packet is of length L and the link has transmission rate R. What is the average queuing delay for the N packets?
    b. Now suppose that N such packets arrive to the link every LN/R seconds. What is the average queuing delay of a packet?

P14. 考虑路由器缓冲区中的排队延迟。令 I 表示流量强度，即 I=La/R。假设排队延迟的形式为 IL/R(1−I)，当 I<1 时成立。

a. 给出总延迟（即排队延迟加上传输延迟）的公式。  
b. 绘制总延迟关于 L /R 的函数图像。

.. toggle::

    P14. Consider the queuing delay in a router buffer. Let I denote traffic intensity; that is, I=La/R. Suppose that the queuing delay takes the form IL/R(1−I) for I<1.

    a. Provide a formula for the total delay, that is, the queuing delay plus the transmission delay.
    b. Plot the total delay as a function of L /R.

P15. 令 a 表示到达链路的分组速率（单位：分组/秒），µ 表示链路的传输速率（单位：分组/秒）。根据上题中得到的总延迟公式，推导出关于 a 和 µ 的总延迟公式。

.. toggle::

    P15. Let a denote the rate of packets arriving at a link in packets/sec, and let µ denote the link’s transmission rate in packets/sec. Based on the formula for the total delay (i.e., the queuing delay plus the transmission delay) derived in the previous problem, derive a formula for the total delay in terms of a and µ.

P16. 考虑一个出链路前的路由器缓冲区。在本题中你将使用 Little 定理，这是排队论中的一个著名公式。令 N 表示缓冲区中平均分组数（包括当前正在传输的分组），a 表示到达该链路的分组速率，d 表示分组经历的平均总延迟（即排队延迟加上传输延迟）。Little 定理为 N=a⋅d。假设缓冲区中平均有 10 个分组，平均排队延迟为 10 毫秒，链路传输速率为 100 个分组/秒。使用 Little 定理，若无分组丢失，求平均分组到达速率。

.. toggle::

    P16. Consider a router buffer preceding an outbound link. In this problem, you will use Little’s formula, a famous formula from queuing theory. Let N denote the average number of packets in the buffer plus the packet being transmitted. Let a denote the rate of packets arriving at the link. Let d denote the average total delay (i.e., the queuing delay plus the transmission delay) experienced by a packet. Little’s formula is N=a⋅d. Suppose that on average, the buffer contains 10 packets, and the average packet queuing delay is 10 msec. The link’s transmission rate is 100 packets/sec. Using Little’s formula, what is the average packet arrival rate, assuming there is no packet loss?

P17.

a. 将 :ref:`公式 1.2 <Equation 1.2>` （见 :ref:`第 1.4.3 节 <c1.4.3>`）推广到异构处理速率、传输速率和传播延迟的情形。  
b. 重复 (a)，但现在还假设每个节点有平均排队延迟 dqueue。

.. toggle::

    P17.

    a. Generalize :ref:`Equation 1.2 <Equation 1.2>` in :ref:`Section 1.4.3 <c1.4.3>` for heterogeneous processing rates, transmission rates, and propagation delays.
    b. Repeat (a), but now also suppose that there is an average queuing delay of dqueue at each node.

P18. 在同一大陆的源和目的地之间进行三次 Traceroute，时间选择为一天中的三个不同时间点。

.. image:: ../img/103-0.png

**使用 Traceroute 探索网络路径和测量网络延迟**

a. 在每个时间点上，计算往返延迟的平均值和标准差。  
b. 统计每个时间点路径中的路由器数量。路径在不同时间点是否有变化？  
c. 尝试识别从源到目的地的 Traceroute 分组所经过的 ISP 网络数量。具有相似名称和/或相似 IP 地址的路由器应视为属于同一 ISP。在你的实验中，最大延迟是否发生在相邻 ISP 之间的互联点？  
d. 针对位于不同大陆的源和目的地重复上述实验。比较同一大陆与跨大陆的实验结果。

.. toggle::

    P18. Perform a Traceroute between source and destination on the same continent at three different hours of the day.

    .. image:: ../img/103-0.png

    **Using Traceroute to discover network paths and measure network delay**

    a. Find the average and standard deviation of the round-trip delays at each of the three hours.
    b. Find the number of routers in the path at each of the three hours. Did the paths change during any of the hours?
    c. Try to identify the number of ISP networks that the Traceroute packets pass through from source to destination. Routers with similar names and/or similar IP addresses should be considered as part of the same ISP. In your experiments, do the largest delays occur at the peering interfaces between adjacent ISPs?
    d. Repeat the above for a source and destination on different continents. Compare the intra-continent and inter-continent results.
    
P19.

a. 访问网站 `www.traceroute.org <http://www.traceroute.org/>`_，从法国两个不同城市分别对美国的同一目标主机执行 traceroute。两次 traceroute 有多少条链路是相同的？跨大西洋链路是否相同？  
b. 重复 (a)，但这次选择一个法国城市和一个德国城市。  
c. 选择美国的一个城市，对中国两个不同城市的主机分别执行 traceroute。这两个 traceroute 有多少条链路是相同的？这两条路径在进入中国之前是否已经分叉？

.. toggle::

    P19.

    a. Visit the site `www.traceroute.org <http://www.traceroute.org/>`_ and perform traceroutes from two different cities in France to the same destination host in the United States. How many links are the same in the two traceroutes? Is the transatlantic link the same?
    b. Repeat (a) but this time choose one city in France and another city in Germany.
    c. Pick a city in the United States, and perform traceroutes to two hosts, each in a different city in China. How many links are common in the two traceroutes? Do the two traceroutes diverge before reaching China?

P20. 考虑 :ref:`图 1.20(b) <Figure 1.20>` 中的吞吐量示例。现在假设有 M 对客户端-服务器，而不是 10 对。用 :math:`R_s`、:math:`R_c` 和 R 分别表示服务器链路速率、客户端链路速率和网络链路速率。假设所有其他链路容量充足，并且网络中除了这 M 对客户端-服务器对产生的流量之外没有其他流量。推导出一个关于 :math:`R_s`、:math:`R_c`、R 和 M 的通用吞吐量表达式。

.. toggle::

    P20. Consider the throughput example corresponding to :ref:`Figure 1.20(b) <Figure 1.20>` . Now suppose that there are M client-server pairs rather than 10. Denote :math:`R_s`, :math:`R_c`, and R for the rates of the server links, client links, and network link. Assume all other links have abundant capacity and that there is no other traffic in the network besides the traffic generated by the M client-server pairs. Derive a general expression for throughput in terms of :math:`R_s`, :math:`R_c`, R, and M.

P21. 考虑 :ref:`图 1.19(b) <Figure 1.19>`。现在假设服务器与客户端之间有 M 条路径，且这些路径之间没有任何共享链路。第 k 条路径（k=1,…,M）由 N 条链路组成，其传输速率为 R1k、R2k、…、RNk。如果服务器只能使用一条路径向客户端发送数据，那么其最大吞吐量是多少？如果服务器可以使用所有 M 条路径发送数据，其最大吞吐量是多少？

.. toggle::

    P21. Consider :ref:`Figure 1.19(b) <Figure 1.19>` . Now suppose that there are M paths between the server and the client. No two paths share any link. Path k(k=1,…,M) consists of N links with transmission rates R1k,R2k,…,RNk. If the server can only use one path to send data to the client, what is the maximum throughput that the server can achieve? If the server can use all M paths to send data, what is the maximum throughput that the server can achieve?

P22. 考虑 :ref:`图 1.19(b) <Figure 1.19>`。假设服务器与客户端之间的每条链路都有一个分组丢失概率 p，且这些链路的丢包概率是独立的。一个（由服务器发送的）分组被接收方成功接收的概率是多少？如果一个分组在从服务器到客户端的路径上丢失，服务器将重新发送该分组。平均而言，服务器需要重新发送多少次才能让客户端成功接收到该分组？

.. toggle::

    P22. Consider :ref:`Figure 1.19(b) <Figure 1.19>` . Suppose that each link between the server and the client has a packet loss probability p, and the packet loss probabilities for these links are independent. What is the probability that a packet (sent by the server) is successfully received by the receiver? If a packet is lost in the path from the server to the client, then the server will re-transmit the packet. On average, how many times will the server re-transmit the packet in order for the client to successfully receive the packet?

P23. 考虑 :ref:`图 1.19(a) <Figure 1.19>`。假设我们知道从服务器到客户端路径上的瓶颈链路是第一条速率为 Rs bits/sec 的链路。假设我们从服务器向客户端背靠背发送两个分组，且此路径上没有其他流量。假设每个分组的大小为 L 比特，且两条链路具有相同的传播延迟 dprop。

a. 目的地的分组到达间隔时间是多少？也就是说，第一个分组的最后一个比特到达后到第二个分组的最后一个比特到达之间的时间是多少？  
b. 现在假设第二条链路是瓶颈链路（即 Rc<Rs）。第二个分组是否可能在第二条链路的输入队列中排队？解释。现在假设服务器在发送第一个分组后 T 秒发送第二个分组。T 应该至少多大才能确保在第二条链路前不发生排队？解释说明。

.. toggle::

    P23. Consider :ref:`Figure 1.19(a) <Figure 1.19>` . Assume that we know the bottleneck link along the path from the server to the client is the first link with rate Rs bits/sec. Suppose we send a pair of packets back to back from the server to the client, and there is no other traffic on this path. Assume each packet of size L bits, and both links have the same propagation delay dprop.

    a. What is the packet inter-arrival time at the destination? That is, how much time elapses from when the last bit of the first packet arrives until the last bit of the second packet arrives?
    b. Now assume that the second link is the bottleneck link (i.e., Rc<Rs). Is it possible that the second packet queues at the input queue of the second link? Explain. Now suppose that the server sends the second packet T seconds after sending the first packet. How large must T be to ensure no queuing before the second link? Explain.

P24. 假设你想紧急从波士顿向洛杉矶传送 40 TB 的数据。你可以使用一条 100 Mbps 的专用链路进行数据传输。你会选择通过该链路传送数据，还是使用 FedEx 隔夜快递？请解释。

.. toggle::

    P24. Suppose you would like to urgently deliver 40 terabytes data from Boston to Los Angeles. You have available a 100 Mbps dedicated link for data transfer. Would you prefer to transmit the data via this link or instead use FedEx over-night delivery? Explain.

P25. 假设两个主机 A 和 B 相距 20,000 公里，并通过一条速率为 R=2 Mbps 的链路直接连接。假设该链路上的传播速度为 2.5⋅10⁸ 米/秒。

a. 计算带宽-时延乘积 R⋅dprop。  
b. 考虑从主机 A 向主机 B 发送一个 800,000 比特的文件。假设该文件作为一个大消息连续发送。该链路上任何时刻最多会有多少比特？  
c. 给出带宽-时延乘积的含义解释。  
d. 在该链路上一个比特的“宽度”（单位：米）是多少？是否比一个橄榄球场还长？  
e. 推导一个关于传播速度 s、传输速率 R 和链路长度 m 的比特宽度通用表达式。

.. toggle::

    P25. Suppose two hosts, A and B, are separated by 20,000 kilometers and are connected by a direct link of R=2 Mbps. Suppose the propagation speed over the link is 2.5⋅108 meters/sec.

    a. Calculate the bandwidth-delay product, R⋅dprop.
    b. Consider sending a file of 800,000 bits from Host A to Host B. Suppose the file is sent continuously as one large message. What is the maximum number of bits that will be in the link at any given time?
    c. Provide an interpretation of the bandwidth-delay product.
    d. What is the width (in meters) of a bit in the link? Is it longer than a football field?
    e. Derive a general expression for the width of a bit in terms of the propagation speed s, the transmission rate R, and the length of the link m.

P26. 参照问题 P25，假设我们可以修改 R。求 R 的取值，使得一个比特的宽度正好等于链路长度。

.. toggle::

    P26. Referring to problem P25, suppose we can modify R. For what value of R is the width of a bit as long as the length of the link?

P27. 考虑问题 P25，但现在链路速率为 R=1 Gbps。

a. 计算带宽-时延乘积 R⋅dprop。  
b. 考虑从主机 A 向主机 B 发送一个 800,000 比特的文件。假设该文件作为一个大消息连续发送。该链路上任何时刻最多会有多少比特？  
c. 链路上一个比特的宽度（以米计）是多少？

.. toggle::

    P27. Consider problem P25 but now with a link of R=1 Gbps.

    a. Calculate the bandwidth-delay product, R⋅dprop.
    b. Consider sending a file of 800,000 bits from Host A to Host B. Suppose the file is sent continuously as one big message. What is the maximum number of bits that will be in the link at any given time?
    c. What is the width (in meters) of a bit in the link?

P28. 再次参考问题 P25。

a. 假设文件连续发送，发送该文件需要多长时间？  
b. 现在假设该文件被分成 20 个分组，每个分组包含 40,000 比特。假设每个分组都需由接收方确认，确认分组的传输时间可忽略不计。最后，假设发送方在前一个分组未被确认前不能发送下一个分组。发送该文件需要多长时间？  
c. 比较 (a) 和 (b) 中的结果并进行评论。

.. toggle::

    P28. Refer again to problem P25.

    a. How long does it take to send the file, assuming it is sent continuously?
    b. Suppose now the file is broken up into 20 packets with each packet containing 40,000 bits. Suppose that each packet is acknowledged by the receiver and the transmission time of an acknowledgment packet is negligible. Finally, assume that the sender cannot send a packet until the preceding one is acknowledged. How long does it take to send the file?
    c. Compare the results from (a) and (b).

P29. 假设一颗地球同步卫星与地面基站之间存在一条 10 Mbps 的微波链路。每分钟卫星拍摄一张数字照片并发送到地面基站。假设传播速度为 2.4⋅10⁸ 米/秒。

a. 链路的传播延迟是多少？  
b. 带宽-时延乘积 R⋅dprop 是多少？  
c. 设 x 表示照片大小。要使该微波链路持续传输，x 的最小值是多少？

.. toggle::

    P29. Suppose there is a 10 Mbps microwave link between a geostationary satellite and its base station on Earth. Every minute the satellite takes a digital photo and sends it to the base station. Assume a propagation speed of 2.4⋅108 meters/sec.

    a. What is the propagation delay of the link?
    b. What is the bandwidth-delay product, R⋅dprop?
    c. Let x denote the size of the photo. What is the minimum value of x for the microwave link to be continuously transmitting?

P30. 考虑我们在 :ref:`第 1.5 节 <c1.5>` 中关于分层的航空旅行类比，以及协议数据单元在协议栈下传时附加报头的过程。是否存在类似的报头信息概念被添加到乘客和行李上，当它们在航空协议栈中“下行”时？

.. toggle::

    P30. Consider the airline travel analogy in our discussion of layering in :ref:`Section 1.5 <c1.5>` , and the addition of headers to protocol data units as they flow down the protocol stack. Is there an equivalent notion of header information that is added to passengers and baggage as they move down the airline protocol stack?

P31. 在现代分组交换网络（包括互联网）中，源主机会将长的应用层消息（例如图像或音乐文件）分段为较小的分组，并将这些分组发送到网络中。接收方随后会将这些分组重新组合为原始消息。我们将这一过程称为消息分段。:ref:`图 1.27 <Figure 1.27>` 展示了在有无消息分段的情况下端到端传输一条消息的过程。考虑要从源发送一条 8⋅10⁶ 比特的消息到目的地，如 :ref:`图 1.27 <Figure 1.27>` 所示。假设图中每条链路的速率为 2 Mbps。忽略传播、排队和处理延迟。

a. 考虑不使用消息分段将消息从源发送到目的地。从源主机将消息移动到第一个分组交换机需要多长时间？考虑到每个交换机使用存储-转发分组交换，从源主机到目的主机的总耗时是多少？  
b. 现在假设该消息被分为 800 个分组，每个分组为 10,000 比特。从源主机将第一个分组移动到第一个交换机需要多长时间？当第一个分组从第一个交换机发送到第二个交换机时，第二个分组正在从源主机发送到第一个交换机。第二个分组完全到达第一个交换机的时间是什么时候？  
c. 在使用消息分段的情况下，从源主机到目的主机传输整个文件需要多长时间？将该结果与你在 (a) 中的答案进行比较并评论。  

.. _Figure 1.27:

.. figure:: ../img/106-0.png
    :align: center 

.. figure:: ../img/106-1.png
    :align: center 

**图 1.27 端到端消息传输：(a) 无消息分段；(b) 有消息分段**

d. 除了减少延迟外，还有哪些使用消息分段的原因？  
e. 讨论使用消息分段的缺点。

.. toggle::

    P31. In modern packet-switched networks, including the Internet, the source host segments long, application-layer messages (for example, an image or a music file) into smaller packets and sends the packets into the network. The receiver then reassembles the packets back into the original message. We refer to this process as message segmentation. :ref:`Figure 1.27 <Figure 1.27>` illustrates the end-to-end transport of a message with and without message segmentation. Consider a message that is 8⋅106 bits long that is to be sent from source to destination in :ref:`Figure 1.27 <Figure 1.27>` . Suppose each link in the figure is 2 Mbps. Ignore propagation, queuing, and processing delays.

    a. Consider sending the message from source to destination without message segmentation. How long does it take to move the message from the source host to the first packet switch? Keeping in mind that each switch uses store-and-forward packet switching, what is the total time to move the message from source host to destination host?
    b. Now suppose that the message is segmented into 800 packets, with each packet being 10,000 bits long. How long does it take to move the first packet from source host to the first switch? When the first packet is being sent from the first switch to the second switch, the second packet is being sent from the source host to the first switch. At what time will the second packet be fully received at the first switch?
    c. How long does it take to move the file from source host to destination host when message segmentation is used? Compare this result with your answer in part (a) and comment.

    .. figure:: ../img/106-0.png
        :align: center 

    .. figure:: ../img/106-1.png
        :align: center 

    **Figure 1.27 End-to-end message transport: (a) without message ­segmentation; (b) with message segmentation**

    d. In addition to reducing delay, what are reasons to use message ­segmentation?
    e. Discuss the drawbacks of message segmentation.

P32. 在本书网站上尝试 Message Segmentation 小程序。小程序中的延迟是否与前一题中的延迟一致？链路传播延迟如何影响使用分组交换（带消息分段）与使用消息交换的端到端总延迟？

.. toggle::

    P32. Experiment with the Message Segmentation applet at the book’s Web site. Do the delays in the applet correspond to the delays in the previous problem? How do link propagation delays affect the overall end-to-end delay for packet switching (with message segmentation) and for message switching?

P33. 考虑从主机 A 向主机 B 发送一个大小为 F 比特的大文件。A 与 B 之间有三条链路（和两个交换机），链路无拥塞（即无排队延迟）。主机 A 将文件分段为每段 S 比特，并为每段添加 80 比特报头，形成长度为 L=80+S 比特的分组。每条链路的传输速率为 R bps。找出使得文件从 A 移动到 B 的延迟最小的 S 值。忽略传播延迟。

.. toggle::

    P33. Consider sending a large file of F bits from Host A to Host B. There are three links (and two switches) between A and B, and the links are uncongested (that is, no queuing delays). Host Asegments the file into segments of S bits each and adds 80 bits of header to each segment, forming packets of L=80 + S bits. Each link has a transmission rate of R bps. Find the value of S that minimizes the delay of moving the file from Host A to Host B. Disregard propagation delay. 

P34. Skype 提供一个服务，允许你从 PC 拨打电话到普通电话。这意味着语音通话必须同时通过互联网和电话网络。请讨论这是如何实现的。

.. toggle::

    P34. Skype offers a service that allows you to make a phone call from a PC to an ordinary phone. This means that the voice call must pass through both the Internet and through a telephone network. Discuss how this might be done.