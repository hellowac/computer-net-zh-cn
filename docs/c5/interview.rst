访谈: Jennifer Rexford
===================================
Interview: Jennifer Rexford

Jennifer Rexford 是普林斯顿大学计算机科学系的教授。她的研究目标是让计算机网络更易于设计和管理，特别关注路由协议。从 1996 年到 2004 年，她曾在 AT&T Labs–Research 的网络管理与性能部门工作。在 AT&T 工作期间，她设计了用于网络测量、流量工程和路由器配置的技术和工具，这些技术和工具被部署在 AT&T 的骨干网络中。Jennifer 是《Web Protocols and Practice: Networking Protocols, Caching, and Traffic Measurement》一书的合著者，该书由 Addison-Wesley 于 2001 年 5 月出版。她曾于 2003 年至 2007 年担任 ACM SIGCOMM 主席。她于 1991 年获得普林斯顿大学电气工程学士学位，并于 1996 年获得密歇根大学电气工程与计算机科学博士学位。2004 年，Jennifer 获得 ACM 的 Grace Murray Hopper 奖，以表彰其作为杰出青年计算机专业人士的成就，并入选 MIT 的 TR-100（35 岁以下的百位顶尖创新者）名单。

.. figure:: ../img/490-0.png
   :align: center

.. toggle::

   Jennifer Rexford is a Professor in the Computer Science department at Princeton University. Her research has the broad goal of making computer networks easier to design and manage, with particular emphasis on routing protocols. From 1996–2004, she was a member of the Network Management and Performance department at AT&T Labs–Research. While at AT&T, she designed techniques and tools for network measurement, traffic engineering, and router configuration that were deployed in AT&T’s backbone network. Jennifer is co-author of the book “Web Protocols and Practice: Networking Protocols, Caching, and Traffic Measurement,” published by Addison-Wesley in May 2001. She served as the chair of ACM SIGCOMM from 2003 to 2007. She received her BSE degree in electrical engineering from Princeton University in 1991, and her PhD degree in electrical engineering and computer science from the University of Michigan in 1996. In 2004, Jennifer was the winner of ACM’s Grace Murray Hopper Award for outstanding young computer professional and appeared on the MIT TR-100 list of top innovators under the age of 35.

   .. figure:: ../img/490-0.png
      :align: center

请描述你职业生涯中最令人兴奋的一两个项目。其中最大的挑战是什么？
------------------------------------------------------------------------------------------------------------------------------------
Please describe one or two of the most exciting projects you have worked on during your career. What were the biggest challenges?

当我还是 AT&T 的研究员时，我们团队设计了一种在互联网服务提供商骨干网络中管理路由的新方法。传统上，网络运营人员需要单独配置每台路由器，这些路由器运行分布式协议以计算网络中的路径。我们认为，如果网络运营人员能够基于对网络拓扑和流量的全局视图，直接控制路由器的转发行为，网络管理将更加简单和灵活。我们设计并构建的路由控制平台（RCP）可以在一台普通计算机上计算 AT&T 骨干网中所有路由器的路径，并且可以在无需修改的情况下控制传统路由器。对我来说，这个项目令人兴奋，因为我们提出了一个富有挑战性的想法，实现了一个可工作的系统，最终还在实际运行的网络中得到了部署。几年之后，软件定义网络（SDN）成为主流技术，像 OpenFlow 这样的标准协议让告诉底层交换机“该做什么”变得容易许多。

.. toggle::

   When I was a researcher at AT&T, a group of us designed a new way to manage routing in Internet Service Provider backbone networks. Traditionally, network operators configure each router individually, and these routers run distributed protocols to compute paths through the network. We believed that network management would be simpler and more flexible if network operators could exercise direct control over how routers forward traffic based on a network-wide view of the topology and traffic. The Routing Control Platform (RCP) we designed and built could compute the routes for all of AT&T’s backbone on a single commodity computer, and could control legacy routers without modification. To me, this project was exciting because we had a provocative idea, a working system, and ultimately a real deployment in an operational network. Fast forward a few years, and software-defined networking (SDN) has become a mainstream technology, and standard protocols (like OpenFlow) have made it much easier to tell the underlying switches what to do.

你认为软件定义网络未来应该如何发展？
------------------------------------------------------------------------------
How do you think software-defined networking should evolve in the future?

与以往的重大转变相比，控制平面软件现在可以由许多不同的程序员创建，而不仅仅是销售网络设备的公司开发。然而，与服务器或智能手机上运行的应用程序不同，控制器应用必须协同处理相同的流量。网络运营人员并不希望对一部分流量做负载均衡，对另一部分流量做路由；他们希望对相同的流量同时进行负载均衡和路由。因此，未来的 SDN 控制器平台应当提供良好的编程抽象，便于将独立编写的多个控制器应用组合在一起。更广泛来说，良好的编程抽象可以让开发控制器应用变得更简单，无需关心如流表项、流量计数器、包头中的比特模式等底层细节。此外，虽然 SDN 控制器在逻辑上是集中式的，网络仍由一组分布式设备组成。未来的控制器应当提供良好的抽象机制以便在整个网络中更新流表，这样应用可以在设备更新过程中推理数据包在途中的行为。针对控制平面软件的编程抽象是一个令人激动的跨学科研究领域，融合了计算机网络、分布式系统和编程语言，并有望在未来几年产生现实影响。

.. toggle::

   In a major break from the past, control-plane software can be created by many different programmers, not just at companies selling network equipment. Yet, unlike the applications running on a server or a smart phone, controller apps must work together to handle the same traffic. Network operators do not want to perform load balancing on some traffic and routing on
   other traffic; instead, they want to perform load balancing and routing, together, on the same traffic. Future SDN controller platforms should offer good programming abstractions for
   composing independently written multiple controller applications together. More broadly, good programming abstractions can make it easier to create controller applications, without having to
   worry about low-level details like flow table entries, traffic counters, bit patterns in packet headers, and so on. Also, while an SDN controller is logically centralized, the network still consists of a distributed collection of devices. Future controllers should offer good abstractions for updating the flow tables across the network, so apps can reason about what happens to packets in flight while the devices are updated. Programming abstractions for control-plane software is an exciting area for interdisciplinary research between computer networking, distributed systems, and programming languages, with a real chance for practical impact in the years ahead.

你如何看待网络和互联网的未来？
------------------------------------------------------------------------------
Where do you see the future of networking and the Internet?

网络是一个令人振奋的领域，因为应用和底层技术始终在变化。我们一直在不断“自我重塑”！即使在十年前，谁能预见到智能手机的主导地位，让移动用户可以访问现有应用和新的基于位置的服务？云计算的出现从根本上改变了用户与其所运行应用之间的关系，而联网传感器和执行器（即“物联网”）正在启用大量新的应用（以及安全漏洞！）。技术创新的速度令人鼓舞。

网络是所有这些创新的关键组成部分。然而，网络又以“妨碍”著称——限制性能、影响可靠性、约束应用部署并使服务管理复杂化。我们应当努力让未来的网络像空气一样“隐形”，永远不阻碍新思想和有价值的服务的实现。为此，我们需要提升抽象层次，超越具体的网络设备和协议（及其伴随的缩略词！），从整体上考虑网络及用户的高层目标。

.. toggle::

   Networking is an exciting field because the applications and the underlying technologies change all the time. We are always reinventing ourselves! Who would have predicted even ten years ago the dominance of smart phones, allowing mobile users to access existing applications as well as new location-based services? The emergence of cloud computing is fundamentally changing the relationship between users and the applications they run, and networked sensors and actuators (the “Internet of Things”) are enabling a wealth of new applications (and security vulnerabilities!). The pace of innovation is truly inspiring.

   The underlying network is a crucial component in all of these innovations. Yet, the network is notoriously “in the way”—limiting performance, compromising reliability, constraining applications, and complicating the deployment and management of services. We should strive to make the network of the future as invisible as the air we breathe, so it never stands in the way of new ideas and valuable services. To do this, we need to raise the level of abstraction above individual network devices and protocols (and their attendant acronyms!), so we can reason about the network and the user’s high-level goals as a whole.

哪些人曾在专业上激励你？
-------------------------------------------
What people inspired you professionally?

我长期以来一直受到 Sally Floyd（国际计算机科学研究所）的激励。她的研究总是有明确的目标，专注于互联网面临的重要挑战。她深入研究困难问题，直到彻底理解问题和解决方案空间，并全力推动“真正的改变”，例如推动她的理念进入协议标准和网络设备。此外，她也积极回馈社区，在多个标准和研究组织中参与专业服务，并创建了如广泛使用的 ns-2 和 ns-3 模拟器这样的工具，帮助其他研究人员取得成功。她于 2009 年退休，但她对该领域的影响将持续多年。

.. toggle::

   I’ve long been inspired by Sally Floyd at the International Computer Science Institute. Her research is always purposeful, focusing on the important challenges facing the Internet. She digs deeply into hard questions until she understands the problem and the space of solutions completely, and she devotes serious energy into “making things happen,” such as pushing her ideas into protocol standards and network equipment. Also, she gives back to the community, through professional service in numerous standards and research organizations and by creating tools (such as the widely used ns-2 and ns-3 simulators) that enable other researchers to succeed. She retired in 2009 but her influence on the field will be felt for years to come.

你对希望从事计算机科学与网络事业的学生有何建议？
---------------------------------------------------
What are your recommendations for students who want careers in computer science and networking?

网络本质上是一个跨学科领域。将其他学科的技术应用到网络中可以带来突破，这些技术来自排队论、博弈论、控制论、分布式系统、网络优化、编程语言、机器学习、算法、数据结构等多个领域。我认为，熟悉一个相关领域，或与该领域的专家密切合作，是加强网络研究基础的绝佳方式，有助于我们构建值得社会信赖的网络。除了理论学科之外，网络令人兴奋的地方在于我们可以构建真正供人使用的系统。通过学习操作系统、计算机体系结构等知识，掌握系统设计与构建经验，是另一个拓展网络知识、助力社会进步的极好途径。

.. toggle::

   Networking is an inherently interdisciplinary field. Applying techniques from other disciplines breakthroughs in networking come from such diverse areas as queuing theory, game theory, control theory, distributed systems, network optimization, programming languages, machine learning, algorithms, data structures, and so on. I think that becoming conversant in a related field, or collaborating closely with experts in those fields, is a wonderful way to put networking on a stronger foundation, so we can learn how to build networks that are worthy of society’s trust. Beyond the theoretical disciplines, networking is exciting because we create real artifacts that real people use. Mastering how to design and build systems—by gaining experience in operating systems, computer architecture, and so on—is another fantastic way to amplify your knowledge of networking to help make the world a better place.