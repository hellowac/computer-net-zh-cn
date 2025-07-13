访谈：Simon S. Lam
===================================
Interview: Simon S. Lam

Simon S. Lam 是德克萨斯大学奥斯汀分校计算机科学系的教授和校务委员会讲席教授。1971 年至 1974 年间，他在加州大学洛杉矶分校（UCLA）的 ARPA 网络测量中心工作，从事卫星和无线分组交换方面的研究。他领导的研究团队在 1993 年发明了安全套接字并完成了第一个名为 Secure Network Programming 的安全套接字层原型，这项工作荣获了 2004 年 ACM 软件系统奖。他的研究兴趣包括网络协议和安全服务的设计与分析。他获得了华盛顿州立大学的电气工程学士学位，并在 UCLA 获得了硕士和博士学位。2007 年，他当选为美国国家工程院院士。

.. figure:: ../img/574-0.png 
   :align: center

.. toggle::
   
   Simon S. Lam is Professor and Regents Chair in Computer Sciences at the University of Texas at Austin. From 1971 to 1974, he was with the ARPA Network Measurement Center at UCLA, where he worked on satellite and radio packet switching. He led a research group that invented secure sockets and prototyped, in 1993, the first secure sockets layer named Secure Network Programming, which won the 2004 ACM Software System Award. His research interests are in design and analysis of network protocols and security services. He received his BSEE from Washington State University and his MS and PhD from UCLA. He was elected to the National Academy of Engineering in 2007.

   .. figure:: ../img/574-0.png 
      :align: center

你为什么决定专攻网络领域？
-------------------------------------------------
Why did you decide to specialize in networking?

1969 年秋我作为新研究生来到 UCLA 时，原本打算学习控制理论。后来我上了 Leonard Kleinrock 的排队理论课，他给我留下了非常深刻的印象。有一段时间，我在研究排队系统的自适应控制，作为可能的论文课题。1972 年初，Larry Roberts 启动了 ARPAnet 卫星系统项目（后来称为 Packet Satellite）。Kleinrock 教授邀请我加入该项目。我们做的第一件事是将一个简单但现实的退避算法引入到时隙 ALOHA 协议中。不久之后，我发现了许多有趣的研究问题，例如 ALOHA 的不稳定性问题和对自适应退避机制的需求，这些问题最终构成了我的博士论文核心。

.. toggle::

   When I arrived at UCLA as a new graduate student in Fall 1969, my intention was to study control theory. Then I took the queuing theory classes of Leonard Kleinrock and was very impressed by him. For a while, I was working on adaptive control of queuing systems as a possible thesis topic. In early 1972, Larry Roberts initiated the ARPAnet Satellite System project (later called Packet Satellite). Professor Kleinrock asked me to join the project. The first thing we did was to introduce a simple, yet realistic, backoff algorithm to the slotted ALOHA protocol. Shortly thereafter, I found many interesting research problems, such as ALOHA’s instability problem and need for adaptive backoff, which would form the core of my thesis.

你在 1970 年代互联网的早期就已经活跃起来了，从 UCLA 学生时期开始。当时是什么样的？人们是否预见到互联网会发展成今天这个样子？
--------------------------------------------------------------------------------------------------------------
You were active in the early days of the Internet in the 1970s, beginning with your student days at UCLA. What was it like then? Did people have any inkling of what the Internet would become?

当时的氛围其实与我后来在工业界和学术界见过的其他系统建设项目没什么不同。ARPAnet 最初设定的目标是相当朴素的——让远程用户可以访问昂贵的计算机，以便更多的科学家能够使用这些资源。然而，随着 1972 年 Packet Satellite 项目和 1973 年 Packet Radio 项目的启动，ARPA 的目标大大扩展了。到 1973 年，ARPA 同时在构建三个不同的分组网络，这使得 Vint Cerf 和 Bob Kahn 必须开发一种互联策略。

回顾当时，我相信所有这些在网络方面的渐进式发展被看作是逻辑上的必然而非魔术般的奇迹。没有人能预见如今互联网的规模以及个人计算机的强大功能。当时距离第一台个人电脑问世还有整整十年。为了让你有个概念，大多数学生提交程序是通过打孔卡片进行批处理。只有少数学生能直接访问计算机，而计算机通常被安置在限制区域。调制解调器很慢，也很罕见。作为研究生，我的办公桌上只有一部电话，大多数工作都是用铅笔和纸完成的。

.. toggle::

   The atmosphere was really no different from other system-building projects I have seen in industry and academia. The initially stated goal of the ARPAnet was fairly modest, that is, to provide access to expensive computers from remote locations so that many more scientists could use them. However, with the startup of the Packet Satellite project in 1972 and the Packet Radio project in 1973, ARPA’s goal had expanded substantially. By 1973, ARPA was building three different packet networks at the same time, and it became necessary for Vint Cerf and Bob Kahn to develop an interconnection strategy.

   Back then, all of these progressive developments in networking were viewed (I believe) as logical rather than magical. No one could have envisioned the scale of the Internet and power of personal computers today. It was a decade before appearance of the first PCs. To put things in perspective, most students submitted their computer programs as decks of punched cards for batch processing. Only some students had direct access to computers, which were typically housed in a restricted area. Modems were slow and still a rarity. As a graduate student, I had only a phone on my desk, and I used pencil and paper to do most of my work.
 
你认为网络和互联网领域未来会朝什么方向发展？
-------------------------------------------------------------------------------------
Where do you see the field of networking and the Internet heading in the future?

过去，互联网 IP 协议的简单性是其最大的优势，使其战胜竞争对手，成为事实上的互联标准。与 1980 年代的 X.25 和 1990 年代的 ATM 等竞争技术不同，IP 可以运行在任何链路层网络技术之上，因为它只提供尽力而为的分组服务。因此，任何分组网络都可以连接到互联网。

而今天，IP 最大的优势反而变成了一个限制。IP 就像一件紧身衣，把互联网的发展限制在特定方向上。近年来，许多研究人员已将精力转向仅限于应用层的研究。同时，关于无线自组织网络、传感器网络和卫星网络的研究也在迅速发展。这些网络既可以被视为独立系统，也可以看作是链路层系统，它们之所以能够发展，是因为不受 IP 限制的束缚。

许多人对 P2P 系统作为新型互联网应用平台的潜力感到兴奋。然而，P2P 系统在利用互联网资源方面效率极低。我担心的是，随着互联网连接设备种类日益增多，并需支持未来基于 P2P 的应用，互联网核心的传输和交换能力是否能够持续以快于流量增长的速度扩展。若无大幅的带宽超额配置，要在面对恶意攻击和拥塞的情况下保障网络稳定性将持续成为重大挑战。

互联网的爆炸式增长也要求迅速向全球的网络运营商和企业分配新的 IP 地址。按当前的分配速度，IPv4 的未分配地址池将在几年内耗尽。届时，只有从 IPv6 地址空间中分配大块连续地址才成为可能。由于早期采用 IPv6 缺乏激励，IPv6 的推广进展缓慢，因此 IPv4 和 IPv6 很可能在互联网中并存多年。从以 IPv4 为主的互联网成功迁移到以 IPv6 为主的互联网将需要全球范围的大力协作。

.. toggle::

   In the past, the simplicity of the Internet’s IP protocol was its greatest strength in vanquishing competition and becoming the de facto standard for internetworking. Unlike competitors, such as X.25 in the 1980s and ATM in the 1990s, IP can run on top of any link-layer networking technology, because it offers only a best-effort datagram service. Thus, any packet network can connect to the Internet.

   Today, IP’s greatest strength is actually a shortcoming. IP is like a straitjacket that confines the Internet’s development to specific directions. In recent years, many researchers have redirected their efforts to the application layer only. There is also a great deal of research on wireless ad hoc networks, sensor networks, and satellite networks. These networks can be viewed either as stand-alone systems or link-layer systems, which can flourish because they are outside of the IP straitjacket.

   Many people are excited about the possibility of P2P systems as a platform for novel Internet applications. However, P2P systems are highly inefficient in their use of Internet resources. A concern of mine is whether the transmission and switching capacity of the Internet core will continue to increase faster than the traffic demand on the Internet as it grows to interconnect all kinds of devices and support future P2P-enabled applications. Without substantial overprovisioning of capacity, ensuring network stability in the presence of malicious attacks and congestion will continue to be a significant challenge.

   The Internet’s phenomenal growth also requires the allocation of new IP addresses at a rapid rate to network operators and enterprises worldwide. At the current rate, the pool of unallocated IPv4 addresses would be depleted in a few years. When that happens, large contiguous blocks of address space can only be allocated from the IPv6 address space. Since adoption of IPv6 is off to a slow start, due to lack of incentives for early adopters, IPv4 and IPv6 will most likely co- exist on the Internet for many years to come. Successful migration from an IPv4-dominant Internet to an IPv6-dominant Internet will require a substantial global effort.

你工作中最具挑战性的部分是什么？
------------------------------------------------------
What is the most challenging part of your job?

作为一名教授，我工作中最具挑战性的部分是要教授并激励班上每一位学生和我指导的每一位博士生，而不仅仅是那些成绩优异者。那些聪明又积极的学生可能只需要一点点指导，不需要太多帮助。事实上，我常常从这些学生那里学到的比他们从我这里学到的还多。而教育并激励那些表现不佳的学生，才是真正的挑战。

.. toggle::

   The most challenging part of my job as a professor is teaching and motivating every student in my class, and every doctoral student under my supervision, rather than just the high achievers. The very bright and motivated may require a little guidance but not much else. I often learn more from these students than they learn from me. Educating and motivating the underachievers present a major challenge.

你认为技术未来会对学习产生什么影响？
-----------------------------------------------------------------------------
What impacts do you foresee technology having on learning in the future?


最终，几乎所有人类知识都将可通过互联网获得，互联网将成为最强大的学习工具。这个庞大的知识库有可能在全球范围内为学生创造平等的学习机会。例如，任何国家的有动力的学生都可以访问最优质的网站、多媒体讲座和教学材料。有人曾说，IEEE 和 ACM 的数字图书馆已经加速了中国计算机科学研究人员的发展。随着时间推移，互联网将跨越所有地理障碍，推动学习的发展。

.. toggle::

   Eventually, almost all human knowledge will be accessible through the Internet, which will be the most powerful tool for learning. This vast knowledge base will have the potential of leveling the playing field for students all over the world. For example, motivated students in any country will be able to access the best-class Web sites, multimedia lectures, and teaching materials. Already, it was said that the IEEE and ACM digital libraries have accelerated the development of computer science researchers in China. In time, the Internet will transcend all geographic barriers to learning.
   

