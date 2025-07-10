


家庭作业问题和疑问
========================================

Homework Problems and Questions

第 5.1 节
-----------
SECTION 5.1

R1. 什么是基于每路由器控制的控制平面？在这种情况下，当我们说网络控制平面和数据平面是“单片式”实现时，这是什么意思？

R2. 什么是基于逻辑集中控制的控制平面？在这种情况下，数据平面和控制平面是在同一设备中实现，还是在不同设备中实现？请解释。

.. toggle::

   R1. What is meant by a control plane that is based on per-router control? In such cases, when we say the network control and data planes are implemented “monolithically,” what do we mean?

   R2. What is meant by a control plane that is based on logically centralized control? In such cases, are the data plane and the control plane implemented within the same device or in separate devices? Explain.

第 5.2 节
-----------
SECTION 5.2

R3. 比较并对比集中式和分布式路由算法的属性。请给出一个采用集中式方法和一个采用分布式方法的路由协议的示例。

R4. 比较并对比链路状态和距离向量路由算法。

R5. 什么是距离向量路由中的“计数到无穷”问题？

R6. 是否有必要每个自治系统都使用相同的域内路由算法？为什么或为什么不？

.. toggle::

   R3. Compare and contrast the properties of a centralized and a distributed routing algorithm. Give an example of a routing protocol that takes a centralized and a decentralized approach.

   R4. Compare and contrast link-state and distance-vector routing algorithms. R5. What is the “count to infinity” problem in distance vector routing?

   R6. Is it necessary that every autonomous system use the same intra-AS routing algorithm? Why or why not?

第 5.3–5.4 节
--------------
SECTIONS 5.3–5.4

R7. 为什么在因特网中使用不同的域间（inter-AS）和域内（intra-AS）协议？

R8. 判断正误：当一个 OSPF 路由器发送其链路状态信息时，它只发送给那些直接连接的邻居节点。请解释。

R9. 在 OSPF 自治系统中，什么是区域（area）？为什么引入区域的概念？

R10. 定义并对比以下术语：子网（subnet）、前缀（prefix）和 BGP 路由（BGP route）。

R11. BGP 如何使用 NEXT-HOP 属性？它如何使用 AS-PATH 属性？

R12. 上层 ISP 的网络管理员在配置 BGP 时如何实现策略？

R13. 判断正误：当一个 BGP 路由器从其邻居接收到一个已通告的路径时，它必须将自己的身份添加到该路径中，并将这个新路径发送给它的所有邻居。请解释。

.. toggle::

   R7. Why are different inter-AS and intra-AS protocols used in the Internet?

   R8. True or false: When an OSPF route sends its link state information, it is sent only to those nodes directly attached neighbors. Explain.

   R9. What is meant by an area in an OSPF autonomous system? Why was the concept of an area introduced?

   R10. Define and contrast the following terms: subnet, prefix, and BGP route.

   R11. How does BGP use the NEXT-HOP attribute? How does it use the AS-PATH attribute?

   R12. Describe how a network administrator of an upper-tier ISP can implement policy when configuring BGP.

   R13. True or false: When a BGP router receives an advertised path from its neighbor, it must add its own identity to the received path and then send that new path on to all of its neighbors. Explain.

第 5.5 节
----------------------------------------------------------------------------
SECTIONS 5.5

R14. 描述 SDN 控制器中通信层、网络范围状态管理层以及网络控制应用层的主要作用。

R15. 假设你想在 SDN 控制平面中实现一个新的路由协议。你会在控制器的哪一层实现该协议？请解释。

R16. 在 SDN 控制器的北向和南向 API 上传递了哪些类型的消息？这些从控制器南向接口发送的消息的接收者是谁？谁向控制器北向接口发送消息？

R17. 描述两个从被控制设备发送到控制器的 OpenFlow 消息的用途（任选）。再描述两个从控制器发送到被控制设备的 OpenFlow 消息的用途（任选）。

R18. OpenDaylight SDN 控制器中服务抽象层的用途是什么？

.. toggle::

   R14. Describe the main role of the communication layer, the network-wide state-­management layer, and the network-control application layer in an SDN controller.

   R15. Suppose you wanted to implement a new routing protocol in the SDN control plane. At which layer would you implement that protocol? Explain.

   R16. What types of messages flow across an SDN controller’s northbound and southbound APIs? Who is the recipient of these messages sent from the controller across the southbound interface, and who sends messages to the controller across the northbound interface?

   R17. Describe the purpose of two types of OpenFlow messages (of your choosing) that are sent from a controlled device to the controller. Describe the purpose of two types of Openflow messages (of your choosing) that are send from the controller to a controlled device.

   R18. What is the purpose of the service abstraction layer in the OpenDaylight SDN controller?


第 5.6–5.7 节
----------------------------------------------------------------------------
SECTIONS 5.6–5.7

R19. 写出四种不同类型的 ICMP 消息。

R20. 在执行 Traceroute 程序的发送主机上，会接收到哪两种类型的 ICMP 消息？

R21. 在 SNMP 的上下文中，定义以下术语：管理服务器（managing server）、被管理设备（managed device）、网络管理代理（network management agent）和 MIB。

R22. SNMP 的 GetRequest 和 SetRequest 消息的用途是什么？

R23. SNMP trap 消息的用途是什么？

.. toggle::

   R19. Names four different types of ICMP messages

   R20. What two types of ICMP messages are received at the sending host executing the Traceroute program?

   R21. Define the following terms in the context of SNMP: managing server, ­managed device, network management agent and MIB.

   R22. What are the purposes of the SNMP GetRequest and SetRequest messages? R23. What is the purpose of the SNMP trap message?

问题
----------
Problems

P1. 查看 :ref:`图 5.3 <Figure 5.3>`，枚举从 y 到 u 不包含任何环的路径。

.. toggle::

   P1. Looking at :ref:`Figure 5.3 <Figure 5.3>` , enumerate the paths from y to u that do not contain any loops. 

P2. 重复问题 P1，列出从 x 到 z，z 到 u，以及 z 到 w 的路径。

.. toggle::

   P2. Repeat Problem P1 for paths from x to z, z to u, and z to w.

P3. 考虑如下所示的网络。根据所给的链路代价，使用 Dijkstra 最短路径算法计算从 x 到所有网络节点的最短路径。通过计算类似于 :ref:`表 5.1 <Table 5.1>` 的表格来展示算法的执行过程。

.. figure:: ../img/videonote.png
   :align: center

**Dijkstra 算法：讨论与示例**

.. figure:: ../img/484-0.png
   :align: center

.. toggle::

   P3. Consider the following network. With the indicated link costs, use Dijkstra’s shortest-path algorithm to compute the shortest path from x to all network nodes. Show how the algorithm works by computing a table similar to :ref:`Table 5.1 <Table 5.1>` .

   .. figure:: ../img/videonote.png
      :align: center

   **Dijkstra’s algorithm: discussion and example**

   .. figure:: ../img/484-0.png
      :align: center

P4. 考虑问题 P3 中所示的网络。使用 Dijkstra 算法，并通过类似于 :ref:`表 5.1 <Table 5.1>` 的表格展示你的计算过程，完成以下内容：

a. 计算从 t 到所有网络节点的最短路径。  
b. 计算从 u 到所有网络节点的最短路径。  
c. 计算从 v 到所有网络节点的最短路径。  
d. 计算从 w 到所有网络节点的最短路径。  
e. 计算从 y 到所有网络节点的最短路径。  
f. 计算从 z 到所有网络节点的最短路径。

.. toggle::

   P4. Consider the network shown in Problem P3. Using Dijkstra’s algorithm, and showing your work using a table similar to :ref:`Table 5.1 <Table 5.1>` , do the following:

   a. Compute the shortest path from t to all network nodes. 
   b. Compute the shortest path from u to all network nodes. 
   c. Compute the shortest path from v to all network nodes. 
   d. Compute the shortest path from w to all network nodes. 
   e. Compute the shortest path from y to all network nodes.
   f. Compute the shortest path from z to all network nodes.

P5. 考虑下图所示的网络，并假设每个节点最初只知道其相邻节点的代价。考虑距离向量算法，并展示节点 z 的距离表项。

.. figure:: ../img/484-1.png
   :align: center

.. toggle::

   P5. Consider the network shown below, and assume that each node initially knows the costs to each of its neighbors. Consider the distance-vector algorithm and show the distance table entries at node z.

   .. figure:: ../img/484-1.png
      :align: center

P6. 考虑一个一般拓扑（即，不是上述具体网络）以及一个同步版本的距离向量算法。假设每轮迭代中，一个节点会与其邻居交换距离向量，并接收来自邻居的距离向量。假设算法开始时每个节点只知道与直接邻居的代价，分布式算法收敛所需的最大迭代次数是多少？请证明你的答案。

.. toggle::

   P6. Consider a general topology (that is, not the specific network shown above) and a synchronous version of the distance-vector algorithm. Suppose that at each iteration, a node exchanges its distance vectors with its neighbors and receives their distance vectors. Assuming that the algorithm begins with each node knowing only the costs to its immediate neighbors, what is the maximum number of iterations required before the distributed algorithm converges? Justify your answer.

P7. 考虑下图所示的网络片段。x 只有两个相邻节点，w 和 y。w 到目标 u（未显示）有一条最小代价路径为 5，y 到 u 的最小代价路径为 6。w 和 y 到 u 的完整路径（以及 w 和 y 之间）未显示。网络中所有链路代价均为正整数。

.. figure:: ../img/485-0.png
   :align: center

a. 给出 x 对于目标 w、y 和 u 的距离向量。  
b. 给出一个链路代价变更（c(x, w) 或 c(x, y)），使得 x 在执行距离向量算法后会通知其邻居一条新的最小代价路径到 u。  
c. 给出一个链路代价变更（c(x, w) 或 c(x, y)），使得 x 在执行距离向量算法后不会通知其邻居新的最小代价路径到 u。

.. toggle::

   P7. Consider the network fragment shown below. x has only two attached neighbors, w and y. w has a minimum-cost path to destination u (not shown) of 5, and y has a minimum-cost path to u of 6. The complete paths from w and y to u (and between w and y) are not shown. All link costs in the network have strictly positive integer values.

   .. figure:: ../img/485-0.png
      :align: center

   a. Give x’s distance vector for destinations w, y, and u.
   b. Give a link-cost change for either c(x, w) or c(x, y) such that x will inform its neighbors of a new minimum-cost path to u as a result of executing the distance-vector algorithm.
   c. Give a link-cost change for either c(x, w) or c(x, y) such that x will not inform its neighbors of a new minimum-cost path to u as a result of executing the distance-vector algorithm.

P8. 考虑 :ref:`图 5.6 <Figure 5.6>` 所示的三节点拓扑。将其链路代价改为 c(x,y)=3，c(y,z)=6，c(z,x)=4。请计算初始化步骤之后及每轮同步版本距离向量算法迭代后的距离表（与我们之前讨论 :ref:`图 5.6 <Figure 5.6>` 的方式相同）。

.. toggle::

   P8. Consider the three-node topology shown in :ref:`Figure 5.6 <Figure 5.6>` . Rather than having the link costs shown in :ref:`Figure 5.6 <Figure 5.6>` , the link costs are c(x,y)=3, c(y,z)=6, c(z,x)=4. Compute the distance tables after the initialization step and after each iteration of a synchronous version of the distance-vector algorithm (as we did in our earlier discussion of :ref:`Figure 5.6 <Figure 5.6>` ).

P9. 考虑距离向量路由中的“计数到无穷”问题。如果我们减少链路的代价，这个问题还会发生吗？为什么？如果我们连接两个原本没有连接的节点呢？

.. toggle::

   P9. Consider the count-to-infinity problem in the distance vector routing. Will the count-to-infinity problem occur if we decrease the cost of a link? Why? How about if we connect two nodes which do not have a link?

P10. 论证在图 5.6 中距离向量算法的情况下，D(x) 中的每个值是单调不增的，并将在有限步内稳定。

.. toggle::

   P10. Argue that for the distance-vector algorithm in Figure 5.6 , each value in the distance vector D(x) is non-increasing and will eventually stabilize in a finite number of steps.

P11. 考虑 :ref:`图 5.7 <Figure 5.7>`。假设存在另一个路由器 w，连接到路由器 y 和 z。所有链路代价如下：c(x,y)=4，c(x,z)=50，c(y,w)=1，c(z,w)=1，c(y,z)=3。假设在距离向量路由算法中使用了毒性逆转（poisoned reverse）。

a. 当距离向量路由稳定时，路由器 w、y 和 z 将彼此告知它们到 x 的距离。它们分别会告诉彼此哪些距离值？  
b. 假设链路代价 c(x,y) 增加到 60。即使使用毒性逆转，也会出现“计数到无穷”问题吗？为什么或为什么不？如果会出现，距离向量路由达到稳定状态需要多少轮迭代？请证明你的答案。  
c. 如何修改 c(y,z)，使得当 c(y,x) 从 4 变为 60 时完全不会出现“计数到无穷”问题？

.. toggle::

   P11. Consider :ref:`Figure 5.7 <Figure 5.7>`. Suppose there is another router w, connected to router y and z. The costs of all links are given as follows: c(x,y)=4, c(x,z)=50, c(y,w)=1, c(z,w)=1, c(y,z)=3. Suppose that poisoned reverse is used in the distance-vector routing algorithm.

   a. When the distance vector routing is stabilized, router w, y, and z inform their distances to x to each other. What distance values do they tell each other?
   b. Now suppose that the link cost between x and y increases to 60. Will there be a count-to- infinity problem even if poisoned reverse is used? Why or why not? If there is a count-to-infinity problem, then how many iterations are needed for the distance-vector routing to reach a stable state again? Justify your answer.
   c. How do you modify c(y, z) such that there is no count-to-infinity problem at all if c(y,x) changes from 4 to 60?

P12. 描述 BGP 中如何检测路径中的环路。

.. toggle::

   P12. Describe how loops in paths can be detected in BGP.

P13. 一个 BGP 路由器是否总是选择具有最短 AS 路径长度的无环路路径？请证明你的答案。

.. toggle::

   P13. Will a BGP router always choose the loop-free route with the shortest ASpath length? Justify your answer.

P14. 考虑下图所示的网络。假设 AS3 和 AS2 使用 OSPF 作为它们的域内路由协议，AS1 和 AS4 使用 RIP 作为它们的域内路由协议。假设使用 eBGP 和 iBGP 作为域间路由协议。最初假设 AS2 和 AS4 之间没有物理链路。

a. 路由器 3c 是通过哪种路由协议学习前缀 x 的：OSPF、RIP、eBGP 或 iBGP？  
b. 路由器 3a 是通过哪种路由协议学习 x 的？  
c. 路由器 1c 是通过哪种路由协议学习 x 的？  
d. 路由器 1d 是通过哪种路由协议学习 x 的？

.. figure:: ../img/486-0.png
   :align: center

.. toggle::

   P14. Consider the network shown below. Suppose AS3 and AS2 are running OSPF for their intra-AS routing protocol. Suppose AS1 and AS4 are running RIP for their intra-AS routing protocol. Suppose eBGP and iBGP are used for the inter-AS routing protocol. Initially suppose there is no physical link between AS2 and AS4.

   a. Router 3c learns about prefix x from which routing protocol: OSPF, RIP, eBGP, or iBGP? b. Router 3a learns about x from which routing protocol?
   c. Router 1c learns about x from which routing protocol?
   d. Router 1d learns about x from which routing protocol?

   .. figure:: ../img/486-0.png
      :align: center

P15. 参考上一个问题，一旦路由器 1d 学习到 x，它将在其转发表中添加条目 (x, I)。

a. 对于该条目，I 是 I1 还是 I2？请用一句话解释理由。  
b. 现在假设 AS2 和 AS4 之间存在一条物理链路，如虚线所示。假设路由器 1d 学到 x 可通过 AS2 以及通过 AS3 到达。I 将被设置为 I1 还是 I2？请用一句话解释理由。  
c. 现在假设存在另一个 AS，称为 AS5，位于 AS2 和 AS4 之间（图中未显示）。假设路由器 1d 学到 x 可通过 AS2 AS5 AS4 以及通过 AS3 AS4 到达。I 将被设置为 I1 还是 I2？请用一句话解释理由。

.. toggle::

   P15. Referring to the previous problem, once router 1d learns about x it will put an entry (x, I) in its forwarding table.

   a. Will I be equal to I1 or I2 for this entry? Explain why in one sentence.
   b. Now suppose that there is a physical link between AS2 and AS4, shown by the dotted line. Suppose router 1d learns that x is accessible via AS2 as well as via AS3. Will I be set to I1 or I2? Explain why in one sentence.
   c. Now suppose there is another AS, called AS5, which lies on the path between AS2 and AS4 (not shown in diagram). Suppose router 1d learns that x is accessible via AS2 AS5 AS4 as well as via AS3 AS4. Will I be set to I1 or I2? Explain why in one sentence.

P16. 考虑如下网络。ISP B 为区域 ISP A 提供全国骨干服务。ISP C 为区域 ISP D 提供全国骨干服务。每个 ISP 都由一个 AS 构成。B 和 C 在两个地点使用 BGP 互联。考虑从 A 到 D 的流量。B 更希望在西海岸将该流量转交给 C（这样 C 就需要承担跨国传输的代价），而 C 更希望在其与 B 的东海岸对等点接收流量（这样 B 将承担跨国传输代价）。C 可以使用什么 BGP 机制来促使 B 在东海岸对等点交付 A 到 D 的流量？要回答该问题，你需要深入研究 BGP 规范。

.. figure:: ../img/487-0.png
   :align: center

.. toggle::

   P16. Consider the following network. ISP B provides national backbone service to regional ISP A. ISP C provides national backbone service to regional ISP D. Each ISP consists of one AS. B and C peer with each other in two places using BGP. Consider traffic going from A to D. B would prefer to hand that traffic over to C on the West Coast (so that C would have to absorb the cost of carrying the traffic cross-country), while C would prefer to get the traffic via its East Coast peering point with B (so that B would have carried the traffic across the country). What BGP mechanism might C use, so that B would hand over A-to-D traffic at its East Coast peering point? To answer this question, you will need to dig into the BGP ­specification.

   .. figure:: ../img/487-0.png
      :align: center

P17. 在 :ref:`图 5.13 <Figure 5.13>` 中，考虑到达存根网络 W、X 和 Y 的路径信息。基于 W 和 X 所能获得的信息，它们对网络拓扑的看法分别是怎样的？请说明理由。Y 的拓扑视图如下所示。

.. figure:: ../img/487-1.png
   :align: center

.. toggle::

   P17. In :ref:`Figure 5.13 <Figure 5.13>` , consider the path information that reaches stub networks W, X, and Y. Based on the information available at W and X, what are their respective views of the network topology? Justify your answer. The topology view at Y is shown below.

   .. figure:: ../img/487-1.png
      :align: center

P18. 考虑 :ref:`图 5.13 <Figure 5.13>`。根据 BGP 路由，B 永远不会通过 X 将目的地为 Y 的流量转发过去。但对于某些非常流行的应用，数据包会先到达 X 然后再流向 Y。请指出其中一种应用，并描述数据包是如何遵循非 BGP 路由路径的。

.. toggle::

   P18. Consider :ref:`Figure 5.13 <Figure 5.13>` . B would never forward traffic destined to Y via X based on BGP routing. But there are some very popular applications for which data packets go to X first and then flow to Y. Identify one such application, and describe how data packets follow a path not given by BGP routing.

P19. 在 :ref:`图 5.13 <Figure 5.13>` 中，假设还有一个存根网络 V，它是 ISP A 的客户。假设 B 和 C 是对等关系，A 是 B 和 C 的客户。假设 A 希望所有发往 W 的流量只能来自 B，但发往 V 的流量可以来自 B 或 C。A 应该如何向 B 和 C 广告它的路由？C 接收到哪些 AS 路由？

.. toggle::

   P19. In :ref:`Figure 5.13 <Figure 5.13>` , suppose that there is another stub network V that is a customer of ISP A. Suppose that B and C have a peering relationship, and A is a customer of both B and C. Suppose that A would like to have the traffic destined to W to come from B only, and the traffic destined to V from either B or C. How should A advertise its routes to B and C? What AS routes does C receive?

P20. 假设 AS X 和 Z 并没有直接连接，而是通过 AS Y 连接。进一步假设 X 与 Y 有对等协议，Y 与 Z 有对等协议。最后假设 Z 想转发所有来自 Y 的流量，但不希望转发来自 X 的流量。BGP 是否允许 Z 实现该策略？

.. toggle::

   P20. Suppose ASs X and Z are not directly connected but instead are connected by AS Y. Further suppose that X has a peering agreement with Y, and that Y has a peering agreement with Z. Finally, suppose that Z wants to transit all of Y’s traffic but does not want to transit X’s traffic. Does BGP allow Z to implement this policy?

P21. 考虑管理实体与被管理设备之间通信的两种方式：请求-响应模式和陷阱（trapping）。从以下三个方面分析这两种方法的优缺点：(1) 开销；(2) 当出现异常事件时的通知时间；(3) 管理实体与设备之间信息丢失时的鲁棒性。

.. toggle::

   P21. Consider the two ways in which communication occurs between a managing entity and a managed device: request-response mode and trapping. What are the pros and cons of these two approaches, in terms of (1) overhead, (2) notification time when exceptional events occur, and (3) robustness with respect to lost messages between the managing entity and the device?

P22. 在 :ref:`第 5.7 节 <c5.7>` 中我们看到将 SNMP 消息封装在不可靠的 UDP 数据报中更可取。你认为 SNMP 的设计者为什么选择 UDP 而不是 TCP 作为其首选传输协议？

.. toggle::

   P22. In :ref:`Section 5.7 <c5.7>` we saw that it was preferable to transport SNMP messages in unreliable UDP datagrams. Why do you think the designers of SNMP chose UDP rather than TCP as the transport protocol of choice for SNMP?

套接字编程作业
------------------------------------------
Socket Programming Assignment

在 :ref:`第 2 章 <c2>` 结尾，有四个套接字编程任务。下面是第五个作业，它使用了本章讨论过的 ICMP 协议。

.. toggle::

   At the end of :ref:`Chapter 2 <c2>`, there are four socket programming assignments. Below, you will find a fifth assignment which employs ICMP, a protocol discussed in this chapter.

作业 5：ICMP Ping
-------------------------
Assignment 5: ICMP Ping

Ping 是一个流行的网络应用，用于从远程位置测试某主机是否处于运行状态并且可达。它也常用于测量客户端主机与目标主机之间的延迟。其工作方式是向目标主机发送 ICMP “回显请求” 数据包（即 ping 包），并监听 ICMP “回显响应” 回复（即 pong 包）。Ping 会测量 RTT、记录丢包情况，并对多次 ping-pong 交互进行统计汇总（包括最小值、平均值、最大值和往返时间的标准差）。

在本实验中，你将用 Python 编写你自己的 Ping 应用程序。你的应用程序将使用 ICMP。但为了保持程序简单，你不需要完全遵循 RFC 1739 中的官方规范。请注意，你只需要编写程序的客户端部分，因为服务器端所需的功能几乎已经内置于所有操作系统中。你可以在网站 http://www.pearsonhighered.com/cs-resources 上找到本作业的全部细节和重要的 Python 代码片段。

.. toggle::

   Ping is a popular networking application used to test from a remote location whether a particular host is up and reachable. It is also often used to measure latency between the client host and the target host. It works by sending ICMP “echo request” packets (i.e., ping packets) to the target host and listening for ICMP “echo response” replies (i.e., pong packets). Ping measures the RRT, records packet loss, and calculates a statistical summary of multiple ping-pong exchanges (the minimum, mean, max, and standard deviation of the round-trip times).

   In this lab, you will write your own Ping application in Python. Your application will use ICMP. But in order to keep your program simple, you will not exactly follow the official specification in RFC 1739. Note that you will only need to write the client side of the program, as the functionality needed on the server side is built into almost all operating systems. You can find full details of this assignment, as well as important snippets of the Python code, at the Web site http://www.pearsonhighered.com/cs-resources.


编程作业
----------------------
Programming Assignment

在本次编程作业中，你将编写一组“分布式”过程，这些过程将在本作业所提供的仿真环境中异步执行，用以实现一个分布式异步距离向量路由算法，目标拓扑如下图所示。

你需要编写以下子程序，这些子程序将在仿真器环境中异步运行。对于节点 0，你需要编写以下程序：

.. figure:: ../img/489-0.png
   :align: center

- rtinit0()。该过程将在仿真开始时被调用一次。rtinit0() 没有参数。它应当初始化节点 0 的距离表，以反映到节点 1、2 和 3 的直接代价分别为 1、3 和 7。上图中，所有链路是双向的，并且两个方向的代价相同。在初始化距离表和节点 0 所需的其他数据结构之后，它应当向其直接连接的邻居（本例中是 1、2 和 3）发送其到所有其他网络节点的最小代价路径。这些最小代价信息通过调用 tolayer2() 函数以路由更新包的形式发送给邻居，更新包的格式在完整作业描述中有说明。
- rtupdate0(struct rtpkt *rcvdpkt)。当节点 0 接收到由其直接邻居发送的路由包时，该过程会被调用。参数 *rcvdpkt 是指向所接收包的指针。rtupdate0() 是距离向量算法的“核心”。它从某个节点 i 接收到的路由更新包中包含了 i 到所有其他网络节点的当前最短路径代价。rtupdate0() 使用这些值来更新自己的距离表（依据距离向量算法的定义）。如果更新后它自己到其他某节点的最小代价发生了变化，则节点 0 会通过发送路由包通知其直接连接的邻居该变化。请注意，在距离向量算法中，只有直接相连的节点才会交换路由包。因此，节点 1 和 2 会互相通信，但节点 1 和 3 不会互相通信。

节点 1、2 和 3 的相应函数也需要定义。因此，你将总共编写八个过程：rtinit0()、rtinit1()、rtinit2()、rtinit3()、rtupdate0()、rtupdate1()、rtupdate2() 和 rtupdate3()。这些过程将共同实现该拓扑及链路代价下距离表的分布式、异步计算。

你可以在 http://www.pearsonhighered.com/cs-resource 找到完整的编程作业描述以及为创建模拟硬件/软件环境所需的 C 语言代码。此外，该作业也提供 Java 版本。

.. toggle::
      
   In this programming assignment, you will be writing a “distributed” set of procedures that implements a distributed asynchronous distance-vector routing for the network shown below.

   You are to write the following routines that will “execute” asynchronously within the emulated environment provided for this assignment. For node 0, you will write the routines:

   .. figure:: ../img/489-0.png
      :align: center

   - rtinit0(). This routine will be called once at the beginning of the emulation. rtinit0() has no arguments. It should initialize your distance table in node 0 to reflect the direct costs of 1, 3, and 7 to nodes 1, 2, and 3, respectively. In the figure above, all links are bidirectional and the costs in both directions are identical. After initializing the distance table and any other data structures needed by your node 0 routines, it should then send its directly connected neighbors (in this case, 1, 2, and 3) the cost of its minimum-cost paths to all other network nodes. This minimum-cost information is sent to neighboring nodes in a routing update packet by calling the routine tolayer2(), as described in the full assignment. The format of the routing update packet is also described in the full assignment.
   - rtupdate0(struct rtpkt *rcvdpkt). This routine will be called when node 0 receives a routing packet that was sent to it by one of its directly connected neighbors. The parameter *rcvdpkt is a pointer to the packet that was received. rtupdate0() is the “heart” of the distance-vector algorithm. The values it receives in a routing update packet from some other node i contain i’s current shortest-path costs to all other network nodes. rtupdate0() uses these received values to update its own distance table (as specified by the distance-vector algorithm). If its own minimum cost to another node changes as a result of the update, node 0 informs its directly connected neighbors of this change in minimum cost by sending them a routing packet. Recall that in the distance-vector algorithm, only directly connected nodes will exchange routing packets. Thus, nodes 1 and 2 will communicate with each other, but nodes 1 and 3 will not communicate with each other.

   Similar routines are defined for nodes 1, 2, and 3. Thus, you will write eight procedures in all: rtinit0(), rtinit1(), rtinit2(), rtinit3(), rtupdate0(), rtupdate1(), rtupdate2(), and rtupdate3(). These routines will together implement a distributed, asynchronous computation of the distance tables for the topology and costs shown in the figure on the preceding page.

   You can find the full details of the programming assignment, as well as C code that you will need to create the simulated hardware/software environment, at http://www.pearsonhighered.com/cs-resource. A Java version of the assignment is also available.
   