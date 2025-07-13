家庭作业问题和疑问
========================================

Homework Problems and Questions

SECTIONS 6.1–6.2
-----------------

R1. 考虑 :ref:`第 6.1.1 节 <c6.1.1>` 中的运输类比。如果乘客类比为数据报，那么什么可以类比为链路层帧？

R2. 如果互联网中的所有链路都能提供可靠传输服务，那么 TCP 的可靠传输服务是否就多余了？为什么或为什么不？

R3. 链路层协议可能为网络层提供哪些服务？这些链路层服务中，哪些在 IP 中有对应的服务？哪些在 TCP 中有对应的服务？

.. toggle::

    R1. Consider the transportation analogy in :ref:`Section 6.1.1 <c6.1.1>` . If the passenger is analagous to a datagram, what is analogous to the link layer frame?

    R2. If all the links in the Internet were to provide reliable delivery service, would the TCP reliable delivery service be redundant? Why or why not?

    R3. What are some of the possible services that a link-layer protocol can offer to the network layer? Which of these link-layer services have corresponding services in IP? In TCP?

SECTION 6.3
-----------------

R4. 假设两个节点同时在速率为 R 的广播信道上发送长度为 L 的分组。设两节点之间的传播时延为 :math:`d_{prop}` 。如果 :math:`d_{prop} < L/R`，是否会发生碰撞？为什么或为什么不？

R5. 在 :ref:`第 6.3 节 <c6.3>` 中，我们列出了广播信道的四个期望特性。哪些特性是时隙 ALOHA 拥有的？哪些特性是令牌传递拥有的？

R6. 在 CSMA/CD 中，第五次碰撞后，一个节点选择 K=4 的概率是多少？结果 K=4 对应于在 10 Mbps 的以太网上多少秒的延迟？

R7. 使用鸡尾酒会交流的类比，描述轮询和令牌传递协议。

R8. 如果一个 LAN 的周长非常大，为什么令牌环协议会变得低效？

.. toggle::

    R4. Suppose two nodes start to transmit at the same time a packet of length L over a broadcast channel of rate R. Denote the propagation delay between the two nodes as :math:`d_{prop}`. Will there be a collision if :math:`d_{prop} < L/R` ? Why or why not?

    R5. In :ref:`Section 6.3 <c6.3>` , we listed four desirable characteristics of a broadcast channel. Which of these characteristics does slotted ALOHA have? Which of these characteristics does token passing have?

    R6. In CSMA/CD, after the fifth collision, what is the probability that a node chooses K=4? The result K=4 corresponds to a delay of how many ­seconds on a 10 Mbps Ethernet?

    R7. Describe polling and token-passing protocols using the analogy of cocktail party interactions. R8. Why would the token-ring protocol be inefficient if a LAN had a very large perimeter?

SECTION 6.4
-----------------

R9. MAC 地址空间有多大？IPv4 地址空间呢？IPv6 地址空间呢？

R10. 假设节点 A、B 和 C 都通过它们的适配器连接到同一个广播 LAN。如果 A 向 B 发送成千上万个 IP 数据报，并将每个封装帧的目的 MAC 地址设为 B 的地址，C 的适配器会处理这些帧吗？如果会，C 的适配器会将这些帧中的 IP 数据报传递到 C 的网络层吗？如果 A 使用 MAC 广播地址发送帧，你的答案会有何变化？

R11. 为什么 ARP 查询要在广播帧中发送？为什么 ARP 响应要在具有特定目的 MAC 地址的帧中发送？

R12. 对于 :ref:`图 6.19 <Figure 6.19>` 中的网络，路由器有两个 ARP 模块，每个都有自己的 ARP 表。是否可能两个表中出现相同的 MAC 地址？

R13. 比较 10BASE-T、100BASE-T 和千兆以太网的帧结构。它们有何不同？

R14. 考虑 :ref:`图 6.15 <Figure 6.15>`。在 :ref:`第 4.3 节 <c4.3>` 所定义的寻址意义上，有多少个子网？

R15. 在支持 802.1Q 协议的交换机上，最多可以配置多少个 VLAN？为什么？

R16. 假设有 N 个支持 K 个 VLAN 组的交换机需要通过中继协议互联。需要多少端口来连接这些交换机？请说明理由。

.. toggle::

    R9. How big is the MAC address space? The IPv4 address space? The IPv6 address space?

    R10. Suppose nodes A, B, and C each attach to the same broadcast LAN (through their adapters). If A sends thousands of IP datagrams to B with each encapsulating frame addressed to the MAC address of B, will C’s adapter process these frames? If so, will C’s adapter pass the IP datagrams in these frames to the network layer C? How would your answers change if A sends frames with the MAC broadcast address?

    R11. Why is an ARP query sent within a broadcast frame? Why is an ARP response sent within a frame with a specific destination MAC address?

    R12. For the network in :ref:`Figure 6.19 <Figure 6.19>` , the router has two ARP modules, each with its own ARP table. Is it possible that the same MAC address appears in both tables?

    R13. Compare the frame structures for 10BASE-T, 100BASE-T, and Gigabit ­Ethernet. How do they differ?

    R14. Consider :ref:`Figure 6.15 <Figure 6.15>` . How many subnetworks are there, in the addressing sense of :ref:`Section 4.3 <c4.3>` ?

    R15. What is the maximum number of VLANs that can be configured on a switch supporting the 802.1Q protocol? Why?

    R16. Suppose that N switches supporting K VLAN groups are to be connected via a trunking protocol. How many ports are needed to connect the switches? Justify your answer.

Problems
-----------

P1. 假设一个分组的信息内容是比特模式 1110 0110 1001 1101，并且使用偶校验方案。在二维奇偶校验方案下，包含奇偶位字段的值应是多少？你的答案应使用最小长度的校验和字段。

.. toggle::

    P1. Suppose the information content of a packet is the bit pattern 1110 0110 1001 1101 and an even parity scheme is being used. What would the value of the field containing the parity bits be for the case of a two-dimensional parity scheme? Your answer should be such that a minimum- length checksum field is used.

P2. 请展示（给出一个不同于 :ref:`图 6.5 <Figure 6.5>` 的示例）二维奇偶校验可以检测和纠正单比特错误。再展示一个双比特错误的示例，它可以被检测但无法被纠正。

.. toggle::

    P2. Show (give an example other than the one in :ref:`Figure 6.5 <Figure 6.5>` ) that two-dimensional parity checks can correct and detect a single bit error. Show (give an example of) a double-bit error that can be detected but not corrected.

P3. 假设一个分组的信息部分（:ref:`图 6.3 <Figure 6.3>` 中的 D）包含 10 个字节，这些字节是字符串 “Networking” 的 8 位无符号二进制 ASCII 表示。请计算该数据的 Internet 校验和。

.. toggle::

    P3. Suppose the information portion of a packet (D in :ref:`Figure 6.3 <Figure 6.3>` ) contains 10 bytes consisting of the 8-bit unsigned binary ASCII representation of string “Networking.” Compute the Internet checksum for this data.

P4. 考虑前一题，但现在假设这 10 个字节分别包含：

a. 数字 1 到 10 的二进制表示。  
b. 大写字母 B 到 K 的 ASCII 表示。  
c. 小写字母 b 到 k 的 ASCII 表示。  
请计算该数据的 Internet 校验和。

.. toggle::

    P4. Consider the previous problem, but instead suppose these 10 bytes contain

    a. the binary representation of the numbers 1 through 10.
    b. the ASCII representation of the letters B through K (uppercase).
    c. the ASCII representation of the letters b through k (lowercase). Compute the Internet checksum for this data.

P5. 考虑一个 5 位的生成多项式 G=10011，假设 D 的值为 1010101010。R 的值是多少？

.. toggle::

    P5. Consider the 5-bit generator, G=10011, and suppose that D has the value 1010101010. What is the value of R?

P6. 考虑前一题，但假设 D 的值为：

a. ``1001010101``。  
b. ``0101101010``。  
c. ``1010100000``。

.. toggle::

    P6. Consider the previous problem, but suppose that D has the value 

    a. ``1001010101``.
    b. ``0101101010``. 
    c. ``1010100000``.

P7. 在本题中，我们探索 CRC 的某些性质。对于 :ref:`第 6.2.3 节 <c6.2.3>` 中给定的生成多项式 G (=1001)，回答以下问题：

a. 为什么它可以检测数据 D 中的任意单比特错误？  
b. 上述 G 是否可以检测任意奇数个比特错误？为什么？

.. toggle::

    P7. In this problem, we explore some of the properties of the CRC. For the ­generator G(=1001) given in :ref:`Section 6.2.3 <c6.2.3>` , answer the following questions.

    a. Why can it detect any single bit error in data D?
    b. Can the above G detect any odd number of bit errors? Why?

P8. 在 :ref:`第 6.3 节 <c6.3>` 中，我们概述了时隙 ALOHA 效率的推导过程。在本题中我们将完成该推导。

a. 回顾当有 N 个活跃节点时，时隙 ALOHA 的效率为 Np(1−p)ⁿ⁻¹。求使该表达式最大的 p 值。  
b. 使用 (a) 中求得的 p 值，在 N 趋于无穷大时计算时隙 ALOHA 的效率。提示：当 N 趋于无穷大时，(1−1/N)ⁿ 趋近于 1/e。

.. toggle::

    P8. In :ref:`Section 6.3 <c6.3>` , we provided an outline of the derivation of the efficiency of slotted ALOHA. In this problem we’ll complete the derivation.

    a. Recall that when there are N active nodes, the efficiency of slotted ALOHA is Np(1−p)N−1. Find the value of p that maximizes this expression.
    b. Using the value of p found in (a), find the efficiency of slotted ALOHA by letting N approach infinity. Hint: (1−1/N)N approaches 1/e as N approaches infinity.

P9. 证明纯 ALOHA 的最大效率为 1/(2e)。提示：如果你完成了上题，这道题将会很简单！

.. toggle::

    P9. Show that the maximum efficiency of pure ALOHA is 1/(2e). Note: This problem is easy if you have completed the problem above!

P10. 考虑两个使用时隙 ALOHA 协议争夺信道的节点 A 和 B。假设节点 A 有比节点 B 更多的数据需要传输，且节点 A 的重传概率 pA 大于节点 B 的重传概率 pB。

a. 写出节点 A 的平均吞吐量公式。这两个节点下协议的总效率是多少？  
b. 如果 pA=2pB，节点 A 的平均吞吐量是否是节点 B 的两倍？为什么或为什么不？如果不是，应如何选择 pA 和 pB 才能达到该效果？  
c. 更一般地，假设有 N 个节点，其中节点 A 的重传概率为 2p，其他所有节点的重传概率为 p。写出计算节点 A 和任意其他节点平均吞吐量的表达式。

.. toggle::

    P10. Consider two nodes, A and B, that use the slotted ALOHA protocol to contend for a channel. Suppose node A has more data to transmit than node B, and node A’s retransmission probability pA is greater than node B’s retransmission probability, pB.

    a. Provide a formula for node A’s average throughput. What is the total efficiency of the protocol with these two nodes?
    b. If pA=2pB, is node A’s average throughput twice as large as that of node B? Why or why not? If not, how can you choose pA and pB to make that happen?
    c. In general, suppose there are N nodes, among which node A has retransmission probability 2p and all other nodes have retransmission probability p. Provide expressions to compute the average throughputs of node A and of any other node.

P11. 假设有四个活跃节点——A、B、C 和 D——使用时隙 ALOHA 协议争用信道。假设每个节点都有无限个分组需要发送。每个节点在每个时隙中以概率 p 尝试发送。第一个时隙编号为 1，第二个为 2，依此类推。

a. 节点 A 第一次成功发送的概率是在第 5 个时隙是多少？  
b. 节点 A、B、C 或 D 中的某个节点在第 4 个时隙成功发送的概率是多少？  
c. 第一次成功发送发生在第 3 个时隙的概率是多少？  
d. 这个四节点系统的效率是多少？

.. toggle::

    P11. Suppose four active nodes—nodes A, B, C and D—are competing for access to a channel using slotted ALOHA. Assume each node has an infinite number of packets to send. Each node attempts to transmit in each slot with probability p. The first slot is numbered slot 1, the second slot is numbered slot 2, and so on.

    a. What is the probability that node A succeeds for the first time in slot 5?
    b. What is the probability that some node (either A, B, C or D) succeeds in slot 4? c. What is the probability that the first success occurs in slot 3?
    d. What is the efficiency of this four-node system?

P12. 绘制以下不同 N 值下，时隙 ALOHA 和纯 ALOHA 的效率随 p 变化的图像：

a. N=15。  
b. N=25。  
c. N=35。

.. toggle::

    P12. Graph the efficiency of slotted ALOHA and pure ALOHA as a function of p for the following values of N:

    a. N=15. 
    b. N=25. 
    c. N=35.

P13. 考虑一个具有 N 个节点和传输速率为 R bps 的广播信道。假设该信道使用轮询（带有一个额外的轮询节点）进行多路访问。假设从一个节点完成传输到下一个节点被允许传输之间的时间（即轮询延迟）为 dpoll。假设在一个轮询轮次中，一个节点最多可传输 Q 比特。该广播信道的最大吞吐量是多少？

.. toggle::

    P13. Consider a broadcast channel with N nodes and a transmission rate of R bps. Suppose the broadcast channel uses polling (with an additional polling node) for multiple access. Suppose the amount of time from when a node completes transmission until the subsequent node is permitted to transmit (that is, the polling delay) is dpoll. Suppose that within a polling round, a given node is allowed to transmit at most Q bits. What is the maximum throughput of the broadcast channel? 

P14. 考虑由两个路由器连接的三个 LAN，如 :ref:`图 6.33 <Figure 6.33>` 所示。

a. 为所有接口分配 IP 地址。子网 1 使用 192.168.1.xxx，子网 2 使用 192.168.2.xxx，子网 3 使用 192.168.3.xxx 格式的地址。  
b. 为所有适配器分配 MAC 地址。  
c. 考虑从主机 E 向主机 B 发送 IP 数据报。假设所有 ARP 表都是最新的。列出所有步骤，如 :ref:`第 6.4.1 节 <c6.4.1>` 中单路由器示例所示。  
d. 重复 (c)，现在假设发送主机中的 ARP 表为空（而其他表是最新的）。

.. toggle::

    P14. Consider three LANs interconnected by two routers, as shown in :ref:`Figure 6.33 <Figure 6.33>` .

    a. Assign IP addresses to all of the interfaces. For Subnet 1 use addresses of the form 192.168.1.xxx; for Subnet 2 uses addresses of the form 192.168.2.xxx; and for Subnet 3 use addresses of the form 192.168.3.xxx.
    b. Assign MAC addresses to all of the adapters.
    c. Consider sending an IP datagram from Host E to Host B. Suppose all of the ARP tables are up to date. Enumerate all the steps, as done for the single-router example in :ref:`Section 6.4.1 <c6.4.1>` .
    d. Repeat (c), now assuming that the ARP table in the sending host is empty (and the other
    tables are up to date).

P15. 考虑 :ref:`图 6.33 <Figure 6.33>`。现在我们将子网 1 和子网 2 之间的路由器替换为交换机 S1，并将子网 2 和子网 3 之间的路由器标记为 R1。

.. _Figure 6.33:

.. figure:: ../img/569-0.png
   :align: center 

**图 6.33 三个子网，由路由器互联**

a. 考虑从主机 E 向主机 F 发送 IP 数据报。主机 E 是否会请求路由器 R1 协助转发该数据报？为什么？在包含 IP 数据报的以太网帧中，源和目的的 IP 和 MAC 地址分别是什么？  
b. 假设 E 想要向 B 发送 IP 数据报，并假设 E 的 ARP 缓存中没有 B 的 MAC 地址。E 会发起 ARP 查询来获取 B 的 MAC 地址吗？为什么？在传送到路由器 R1 的以太网帧（包含发送到 B 的 IP 数据报）中，源和目的的 IP 和 MAC 地址分别是什么？  
c. 假设主机 A 想要向主机 B 发送 IP 数据报，且 A 的 ARP 缓存中没有 B 的 MAC 地址，B 的 ARP 缓存中也没有 A 的 MAC 地址。进一步假设交换机 S1 的转发表中仅有主机 B 和路由器 R1 的条目。因此，A 会广播 ARP 请求消息。一旦交换机 S1 收到 ARP 请求消息，它会执行什么操作？路由器 R1 是否也会收到该 ARP 请求消息？如果收到，它是否会将消息转发到子网 3？一旦主机 B 收到此 ARP 请求消息，它将向主机 A 返回一个 ARP 响应消息。但它是否也会发送一个 ARP 查询来请求 A 的 MAC 地址？为什么？一旦交换机 S1 收到来自主机 B 的 ARP 响应消息，它将执行什么操作？

.. toggle::

    P15. Consider :ref:`Figure 6.33 <Figure 6.33>` . Now we replace the router between subnets 1 and 2 with a switch S1, and label the router between subnets 2 and 3 as R1.

    .. figure:: ../img/569-0.png
    :align: center 

    **Figure 6.33 Three subnets, interconnected by routers**

    a. Consider sending an IP datagram from Host E to Host F. Will Host E ask router R1 to help forward the datagram? Why? In the Ethernet frame containing the IP datagram, what are the source and destination IP and MAC addresses?
    b. Suppose E would like to send an IP datagram to B, and assume that E’s ARP cache does not contain B’s MAC address. Will E perform an ARP query to find B’s MAC address? Why? In the Ethernet frame (containing the IP datagram destined to B) that is delivered to router R1, what are the source and destination IP and MAC addresses?
    c. Suppose Host A would like to send an IP datagram to Host B, and neither A’s ARP cache contains B’s MAC address nor does B’s ARP cache contain A’s MAC address. Further suppose that the switch S1’s forwarding table contains entries for Host B and router R1 only. Thus, A will broadcast an ARP request message. What actions will switch S1 perform once it receives the ARP request message? Will router R1 also receive this ARP request message? If so, will R1 forward the message to Subnet 3? Once Host B receives this ARP request message, it will send back to Host A an ARP response message. But will it send an ARP query message to ask for A’s MAC address? Why? What will switch S1 do once it receives an ARP response message from Host B? 

P16. 考虑前一题，但现在将子网 2 和子网 3 之间的路由器替换为交换机。在此新环境中回答前一题中的 (a)–(c) 问题。

.. toggle::

    P16. Consider the previous problem, but suppose now that the router between subnets 2 and 3 is replaced by a switch. Answer questions (a)–(c) in the previous problem in this new context.

P17. 回顾 CSMA/CD 协议，在发生冲突后，适配器会等待 K⋅512 比特时间，其中 K 是随机选取的。当 K=100 时，对于 10 Mbps 的广播信道，适配器在返回第 2 步前将等待多长时间？对于 100 Mbps 的广播信道又会等待多长时间？

.. toggle::

    P17. Recall that with the CSMA/CD protocol, the adapter waits K⋅512 bit times after a collision, where K is drawn randomly. For K=100, how long does the adapter wait until returning to Step 2 for a 10 Mbps broadcast channel? For a 100 Mbps broadcast channel?

P18. 假设节点 A 和 B 在同一个 10 Mbps 的广播信道上，它们之间的传播时延为 325 比特时间。假设该广播信道使用 CSMA/CD 和以太网分组。假设节点 A 开始发送一个帧，在未完成发送前，节点 B 也开始发送帧。A 是否可能在检测到 B 发送前完成发送？为什么？如果答案是“是”，那么 A 会错误地认为其帧已成功发送且未发生冲突。提示：假设在 t=0 比特时间，A 开始发送一个帧。在最坏情况下，A 发送一个最小长度帧，即 512+64 比特时间。因此，A 会在 t=512+64 比特时间完成发送。因此，如果 B 的信号在 t=512+64 比特时间前到达 A，那么答案就是“否”。在最坏情况下，B 的信号何时到达 A？

.. toggle::

    P18. Suppose nodes A and B are on the same 10 Mbps broadcast channel, and the propagation delay between the two nodes is 325 bit times. Suppose CSMA/CD and Ethernet packets are used for this broadcast channel. Suppose node A begins transmitting a frame and, before it finishes, node B begins transmitting a frame. Can A finish transmitting before it detects that B has transmitted? Why or why not? If the answer is yes, then A incorrectly believes that its frame was successfully transmitted without a collision. Hint: Suppose at time t=0 bits, A begins transmitting a frame. In the worst case, A transmits a minimum-sized frame of 512+64 bit times. So A would finish transmitting the frame at t=512+64 bit times. Thus, the answer is no, if B’s signal reaches A before bit time t=512+64 bits. In the worst case, when does B’s signal reach A?

P19. 假设节点 A 和 B 在同一个 10 Mbps 的广播信道上，它们之间的传播时延为 245 比特时间。假设 A 和 B 同时发送以太网帧，帧发生碰撞，然后 A 和 B 在 CSMA/CD 算法中选择了不同的 K 值。假设没有其他活跃节点，A 和 B 的重传是否会再次发生碰撞？为解答本题，请解决如下实例：假设 A 和 B 在 t=0 比特时间开始传输，它们在 t=245 比特时间检测到碰撞。假设 KA=0，KB=1。B 的重传时间安排在什么时候？A 开始传输的时间是什么？（注意：节点在返回第 2 步后必须等待信道空闲——参见协议。）A 的信号何时到达 B？B 是否会在其预定时间停止发送？

.. toggle::

    P19. Suppose nodes A and B are on the same 10 Mbps broadcast channel, and the propagation delay between the two nodes is 245 bit times. Suppose A and B send Ethernet frames at the same time, the frames collide, and then A and B choose different values of K in the CSMA/CD algorithm. Assuming no other nodes are active, can the retransmissions from A and B collide? For our purposes, it suffices to work out the following example. Suppose A and B begin transmission at t=0 bit times. They both detect collisions at t=245 t bit times. Suppose KA=0 and KB=1. At what time does B schedule its retransmission? At what time does A begin transmission? (Note: The nodes must wait for an idle channel after returning to Step 2—see protocol.) At what time does A’s signal reach B? Does B refrain from transmitting at its scheduled time?

P20. 本题将推导类似 CSMA/CD 的多路访问协议的效率。在此协议中，时间被分成时隙，所有适配器都与时隙同步。但与时隙 ALOHA 不同，时隙长度（秒）远小于帧的传输时间。设时隙长度为 S。假设所有帧长度为 L=kRS，其中 R 是信道传输速率，k 是一个大整数。设有 N 个节点，每个节点有无限个帧要发送。我们还假设 dprop<S，因此所有节点都能在一个时隙结束前检测到冲突。协议如下：

- 若在某个时隙中，没有节点拥有信道，则所有节点争用信道；具体地，每个节点以概率 p 在该时隙中发送。若恰有一个节点发送，则该节点占用接下来的 k−1 个时隙并发送其整个帧。
- 若某节点已占用信道，其他所有节点在该节点完成帧发送前不得发送。该节点发送完帧后，所有节点再次争用信道。

注意：信道在两种状态间交替：productive 状态持续 k 个时隙，nonproductive 状态持续若干随机时隙。信道效率显然为 k/(k+x)，其中 x 是连续 nonproductive 时隙的期望值。

a. 对于给定的 N 和 p，求此协议的效率。  
b. 对于给定的 N，求使效率最大的 p。  
c. 使用 (b) 中求得的 p（它是 N 的函数），当 N 趋近无穷大时，求该协议的效率。  
d. 证明当帧长度变大时，该效率趋近于 1。

.. toggle::

    P20. In this problem, you will derive the efficiency of a CSMA/CD-like multiple access protocol. In this protocol, time is slotted and all adapters are synchronized to the slots. Unlike slotted
    ALOHA, however, the length of a slot (in seconds) is much less than a frame time (the time to transmit a frame). Let S be the length of a slot. Suppose all frames are of constant length L=kRS, where R is the transmission rate of the channel and k is a large integer. Suppose there are N nodes, each with an infinite number of frames to send. We also assume that dprop<S, so that all nodes can detect a collision before the end of a slot time. The protocol is as follows:

    - If, for a given slot, no node has possession of the channel, all nodes contend for the channel; in particular, each node transmits in the slot with probability p. If exactly one node transmits in the slot, that node takes possession of the channel for the subsequent k−1 slots and transmits its entire frame.
    - If some node has possession of the channel, all other nodes refrain from transmitting until the node that possesses the channel has finished transmitting its frame. Once this node has transmitted its frame, all nodes contend for the channel.

    Note that the channel alternates between two states: the productive state, which lasts exactly k slots, and the nonproductive state, which lasts for a random number of slots. Clearly, the channel efficiency is the ratio of k/(k+x), where x is the expected number of consecutive unproductive slots.

    a. For fixed N and p, determine the efficiency of this protocol.
    b. For fixed N, determine the p that maximizes the efficiency.
    c. Using the p (which is a function of N) found in (b), determine the efficiency as N approaches infinity.
    d. Show that this efficiency approaches 1 as the frame length becomes large.

P21. 考虑第 P14 题中的 :ref:`图 6.33 <Figure 6.33>`。为主机 A、两个路由器和主机 F 的接口分配 MAC 和 IP 地址。假设主机 A 向主机 F 发送数据报。给出封装该 IP 数据报的帧在以下三个传输过程中使用的源和目的 MAC 地址：(i) 从 A 到左侧路由器，(ii) 从左侧路由器到右侧路由器，(iii) 从右侧路由器到 F。同时在每一传输过程中，给出封装在帧中的 IP 数据报的源和目的 IP 地址。

.. toggle::

    P21. Consider :ref:`Figure 6.33 <Figure 6.33>` in problem P14. Provide MAC addresses and IP addresses for the interfaces at Host A, both routers, and Host F. Suppose Host A sends a datagram to Host F. Give the source and destination MAC addresses in the frame encapsulating this IP datagram as the frame is transmitted (i) from A to the left router, (ii) from the left router to the right router, (iii) from the right router to F. Also give the source and destination IP addresses in the IP datagram encapsulated within the frame at each of these points in time.

P22. 现在假设在 :ref:`图 6.33 <Figure 6.33>` 中的最左侧路由器被一个交换机替代。主机 A、B、C、D 和右侧路由器均通过星型结构连接到此交换机。给出封装该 IP 数据报的帧在以下传输过程中的源和目的 MAC 地址：(i) 从 A 到交换机，(ii) 从交换机到右侧路由器，(iii) 从右侧路由器到 F。同时在每一传输过程中，给出封装在帧中的 IP 数据报的源和目的 IP 地址。

.. toggle::

    P22. Suppose now that the leftmost router in :ref:`Figure 6.33 <Figure 6.33>` is replaced by a switch. Hosts A, B, C, and D and the right router are all star-connected into this switch. Give the source and destination MAC addresses in the frame encapsulating this IP datagram as the frame is transmitted (i) from A to the switch, (ii) from the switch to the right router, (iii) from the right router to F. Also give the source and destination IP addresses in the IP datagram encapsulated within the frame at each of these points in time.

P23. 考虑 :ref:`图 6.15 <Figure 6.15>` 中的网络。假设所有链路速率为 100 Mbps。在此网络中的 9 个主机和 2 个服务器之间所能达到的最大总吞吐量是多少？你可以假设任意主机或服务器都可以与任意其他主机或服务器通信。为什么？

.. toggle::

    P23. Consider :ref:`Figure 6.15 <Figure 6.15>` . Suppose that all links are 100 Mbps. What is the maximum total aggregate throughput that can be achieved among the 9 hosts and 2 servers in this network? You can assume that any host or server can send to any other host or server. Why?

P24. 假设 :ref:`图 6.15 <Figure 6.15>` 中的三个部门交换机被集线器替代。所有链路为 100 Mbps。现在回答第 P23 题中的问题。

.. toggle::

    P24. Suppose the three departmental switches in :ref:`Figure 6.15 <Figure 6.15>` are replaced by hubs. All links are 100 Mbps. Now answer the questions posed in problem P23.

P25. 假设 :ref:`图 6.15 <Figure 6.15>` 中的所有交换机都被集线器替代。所有链路为 100 Mbps。现在回答第 P23 题中的问题。

.. toggle::

    P25. Suppose that all the switches in :ref:`Figure 6.15 <Figure 6.15>` are replaced by hubs. All links are 100 Mbps. Now answer the questions posed in problem P23.

P26. 让我们在一个有 6 个节点（A 到 F）星型连接到以太网交换机的网络中分析学习型交换机的操作。假设 (i) B 向 E 发送帧，(ii) E 向 B 回复帧，(iii) A 向 B 发送帧，(iv) B 向 A 回复帧。交换机表初始为空。展示每次事件前后的交换机表状态。对于每个事件，指出转发帧的链路，并简要说明理由。

.. toggle::

    P26. Let’s consider the operation of a learning switch in the context of a network in which 6 nodes labeled A through F are star connected into an Ethernet switch. Suppose that (i) B sends a frame to E, (ii) E replies with a frame to B, (iii) A sends a frame to B, (iv) B replies with a frame to A. The switch table is initially empty. Show the state of the switch table before and after each of these events. For each of these events, identify the link(s) on which the transmitted frame will be forwarded, and briefly justify your answers.

P27. 本题探讨在 VoIP 应用中使用小分组的问题。小分组的缺点之一是链接带宽的大部分被头部字节占用。假设一个分组包含 P 个字节，另有 5 个字节为头部。

a. 考虑直接发送数字编码语音源。假设该源以 128 kbps 的恒定速率编码。假设每个分组在发送前完全填满。填满一个分组所需的时间是 **分组化时延**。用 L 表示，求该时延（毫秒）。  
b. 分组化时延大于 20 毫秒会造成明显且不愉快的回声。求当 L=1,500 字节（约为最大以太网分组）和 L=50 字节（相当于 ATM 分组）时的分组化时延。  
c. 对于链路速率 R=622 Mbps，计算在单个交换节点处，L=1,500 字节和 L=50 字节时的存储转发延迟。  
d. 评论使用小分组的优势。

.. toggle::

    P27. In this problem, we explore the use of small packets for Voice-over-IP applications. One of the drawbacks of a small packet size is that a large fraction of link bandwidth is consumed by overhead bytes. To this end, suppose that the packet consists of P bytes and 5 bytes of header.

    a. Consider sending a digitally encoded voice source directly. Suppose the source is encoded at a constant rate of 128 kbps. Assume each packet is entirely filled before the source sends the packet into the network. The time required to fill a packet is the **packetization delay**. In terms of L, determine the packetization delay in milliseconds.
    b. Packetization delays greater than 20 msec can cause a noticeable and unpleasant echo. Determine the packetization delay for L=1,500 bytes (roughly corresponding to a maximum-sized Ethernet packet) and for L=50 (corresponding to an ATM packet).
    c. Calculate the store-and-forward delay at a single switch for a link rate of R=622 Mbps for L=1,500 bytes, and for L=50 bytes.
    d. Comment on the advantages of using a small packet size.

P28. 考虑 :ref:`图 6.25 <Figure 6.25>` 中的单交换机 VLAN，假设一个外部路由器连接到交换机端口 1。为 EE 和 CS 主机以及路由器接口分配 IP 地址。追踪从 EE 主机向 CS 主机传输 IP 数据报的网络层和链路层步骤（提示：重读正文中图 6.19 的讨论）。

.. toggle::

    P28. Consider the single switch VLAN in :ref:`Figure 6.25 <Figure 6.25>` , and assume an external router is connected to switch port 1. Assign IP addresses to the EE and CS hosts and router interface. Trace the steps taken at both the network layer and the link layer to transfer an IP datagram from an EE host to a CS host (Hint: Reread the discussion of Figure 6.19 in the text).

P29. 考虑 :ref:`图 6.29 <Figure 6.29>` 中的 MPLS 网络，假设路由器 R5 和 R6 现在启用了 MPLS。假设我们希望进行流量工程，使得从 R6 发往 A 的分组通过路径 R6-R4-R3-R1 转发，而从 R5 发往 A 的分组通过 R5-R4-R2-R1 转发。列出 R5 和 R6 的 MPLS 表以及修改后的 R4 表，使上述路径成为可能。

.. toggle::

    P29. Consider the MPLS network shown in :ref:`Figure 6.29 <Figure 6.29>` , and suppose that routers R5 and R6 are now MPLS enabled. Suppose that we want to perform traffic engineering so that packets from R6 destined for A are switched to A via R6-R4-R3-R1, and packets from R5 destined for A are switched via R5-R4-R2-R1. Show the MPLS tables in R5 and R6, as well as the modified table in R4, that would make this possible.

P30. 仍然考虑前一题中的场景，但假设从 R6 发往 D 的分组通过路径 R6-R4-R3 转发，而从 R5 发往 D 的分组通过 R4-R2-R1-R3 转发。列出所有路由器中的 MPLS 表，使得这些路径成为可能。

.. toggle::

    P30. Consider again the same scenario as in the previous problem, but suppose that packets from R6 destined for D are switched via R6-R4-R3, while packets from R5 destined to D are switched via R4-R2-R1-R3. Show the MPLS tables in all routers that would make this possible.

P31. 本题将综合你在互联网协议中学到的内容。假设你走进一个房间，连接到以太网，并希望下载一个网页。从开机开始到获取网页为止，会经历哪些协议步骤？假设开机时 DNS 和浏览器缓存均为空。（提示：涉及的协议包括 Ethernet、DHCP、ARP、DNS、TCP 和 HTTP。）在描述步骤时，明确说明你是如何获取网关路由器的 IP 和 MAC 地址的。

.. toggle::

    P31. In this problem, you will put together much of what you have learned about Internet protocols. Suppose you walk into a room, connect to Ethernet, and want to download a Web page. What are all the protocol steps that take place, starting from powering on your PC to getting the Web page? Assume there is nothing in our DNS or browser caches when you power on your PC. (Hint: The steps include the use of Ethernet, DHCP, ARP, DNS, TCP, and HTTP protocols.) Explicitly indicate in your steps how you obtain the IP and MAC addresses of a gateway router.

P32. 考虑 :ref:`图 6.30 <Figure 6.30>` 中的分层拓扑数据中心网络。现在假设有 80 对流，每对之间的流量为：第 1 与第 9 机架之间 10 对，第 2 与第 10 机架之间 10 对，以此类推。进一步假设除主机与顶级交换机（TOR）之间链路为 1 Gbps，其余网络链路均为 10 Gbps。

a. 每个流具有相同的数据速率；求一个流的最大速率。  
b. 对于相同流量模式，在 :ref:`图 6.31 <Figure 6.31>` 的高度互联拓扑下，求一个流的最大速率。  
c. 现在假设类似的流量模式，但每个机架有 20 个主机，共 160 对流。求这两种拓扑下流的最大速率。

.. toggle::

    P32. Consider the data center network with hierarchical topology in :ref:`Figure 6.30 <Figure 6.30>` . Suppose now there are 80 pairs of flows, with ten flows between the first and ninth rack, ten flows between the second and tenth rack, and so on. Further suppose that all links in the network are 10 Gbps, except for the links between hosts and TOR switches, which are 1 Gbps.

    a. Each flow has the same data rate; determine the maximum rate of a flow.
    b. For the same traffic pattern, determine the maximum rate of a flow for the highly interconnected topology in :ref:`Figure 6.31 <Figure 6.31>` .
    c. Now suppose there is a similar traffic pattern, but involving 20 hosts on each rack and 160 pairs of flows. Determine the maximum flow rates for the two topologies.

P33. 考虑 :ref:`图 6.30 <Figure 6.30>` 中的分层网络，假设数据中心需要支持电子邮件和视频分发等应用。假设四个服务器机架保留给电子邮件，四个机架保留给视频应用。对于每个应用，这四个机架必须位于同一个第 2 层交换机下，因为第 2 层到第 1 层的链路带宽不足以支持应用内流量。对于电子邮件应用，假设 99.9% 的时间只使用三个机架，视频应用使用模式相同。

a. 电子邮件应用在多少时间内需要使用第 4 个机架？视频应用呢？  
b. 假设电子邮件和视频的使用是独立的，两个应用都需要第 4 个机架的概率是多少？  
c. 假设应用出现服务器不足的容忍时间不超过 0.001%，请讨论如何利用 :ref:`图 6.31 <Figure 6.31>` 中的拓扑结构，使得两个应用总共仅分配七个机架（假设该拓扑可以支持所有流量）。

.. toggle::

    P33. Consider the hierarchical network in :ref:`Figure 6.30 <Figure 6.30>` and suppose that the data center needs to support e-mail and video distribution among other applications. Suppose four racks of servers are reserved for e-mail and four racks are reserved for video. For each of the applications, all four racks must lie below a single tier-2 switch since the tier-2 to tier-1 links do not have sufficient bandwidth to support the intra-application traffic. For the e-mail application, suppose that for 99.9 percent of the time only three racks are used, and that the video application has identical usage patterns.

    a. For what fraction of time does the e-mail application need to use a fourth rack? How about for the video application?
    b. Assuming e-mail usage and video usage are independent, for what fraction of time do (equivalently, what is the probability that) both applications need their fourth rack?
    c. Suppose that it is acceptable for an application to have a shortage of servers for 0.001 percent of time or less (causing rare periods of performance degradation for users). Discuss how the topology in :ref:`Figure 6.31 <Figure 6.31>` can be used so that only seven racks are collectively assigned to the two applications (assuming that the topology can support all the traffic).