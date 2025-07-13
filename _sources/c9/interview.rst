访谈：Henning Schulzrinne
===================================
Interview: Henning Schulzrinne

Henning Schulzrinne 是哥伦比亚大学计算机科学系教授、系主任，并担任该校互联网实时实验室主任。他是 RTP、RTSP、SIP 和 GIST 协议的共同作者——这些协议是互联网上音视频通信的关键协议。Henning 在德国达姆施塔特工业大学获得电气与工业工程学士学位，在辛辛那提大学获得电气与计算机工程硕士学位，并在马萨诸塞大学阿默斯特分校获得电气工程博士学位。

.. figure:: ../img/811-0.png 
   :align: center

.. toggle::

   Henning Schulzrinne is a professor, chair of the Department of Computer Science, and head of the Internet Real-Time Laboratory at Columbia University. He is the co-author of RTP, RTSP, SIP, and GIST—key protocols for audio and video communications over the Internet. Henning received his BS in electrical and industrial engineering at TU Darmstadt in Germany, his MS in electrical and computer engineering at the University of Cincinnati, and his PhD in electrical engineering at the University of Massachusetts, Amherst.

   .. figure:: ../img/811-0.png 
      :align: center

你为什么决定专攻多媒体网络？
-------------------------------------------------------------
What made you decide to specialize in multimedia networking?

这几乎是一个偶然的事件。作为一名博士生，我参与了 DARTnet 项目，这是一个使用 T1 线路跨越美国的实验性网络。DARTnet 被用作多播和互联网实时工具的试验场。这促使我编写了第一个音频工具 NeVoT。通过一些 DARTnet 参与者，我开始参与 IETF，当时刚成立的音视频传输工作组。这个工作组后来标准化了 RTP。

.. toggle::

   This happened almost by accident. As a PhD student, I got involved with DARTnet, an experimental network spanning the United States with T1 lines. DARTnet was used as a proving ground for multicast and Internet real-time tools. That led me to write my first audio tool, NeVoT. Through some of the DARTnet participants, I became involved in the IETF, in the then-nascent Audio Video Transport working group. This group later ended up standardizing RTP.

你在计算机行业的第一份工作是什么？包括哪些内容？
------------------------------------------------------------------------
What was your first job in the computer industry? What did it entail?

我在计算机行业的第一份工作是高中时在加州利弗莫尔焊接 Altair 计算机套件。回到德国后，我创办了一家小型咨询公司，为一家旅行社开发地址管理程序——我们在 TRS-80 上将数据存储在磁带上，并使用带有自制硬件接口的 IBM Selectric 打字机作为打印机。

我第一份真正的工作是在 AT&T 贝尔实验室，开发一个用于在实验室环境中构建实验网络的网络仿真器。


.. toggle::

   My first job in the computer industry was soldering together an Altair computer kit when I was a high school student in Livermore, California. Back in Germany, I started a little consulting company that devised an address management program for a travel agency—storing data on cassette tapes for our TRS-80 and using an IBM Selectric typewriter with a home-brew hardware interface as a printer.

   My first real job was with AT&T Bell Laboratories, developing a network emulator for constructing experimental networks in a lab environment.

互联网实时实验室的目标是什么？
-------------------------------------------------------
What are the goals of the Internet Real-Time Lab?

我们的目标是为互联网作为未来唯一通信基础设施提供组件和构建模块。这包括开发新协议，如 GIST（用于网络层信令）和 LoST（用于按位置查找资源），或改进我们早期参与的协议，如通过丰富状态信息、对等系统、下一代紧急呼叫和服务创建工具增强 SIP。最近，我们还广泛研究了 VoIP 的无线系统，因为 802.11b 和 802.11n 网络以及可能的 WiMax 网络很可能成为电话服务的重要“最后一公里”技术。我们也尝试通过名为 DYSWIS（Do You See What I See）的对等故障诊断系统，大大改善用户诊断复杂提供商与设备网络故障的能力。

我们力求做具有实际意义的工作，通过构建原型和开源系统、测量真实系统性能，并为 IETF 标准做出贡献。

.. toggle::

   Our goal is to provide components and building blocks for the Internet as the single future communications infrastructure. This includes developing new protocols, such as GIST (for network-layer signaling) and LoST (for finding resources by location), or enhancing protocols that we have worked on earlier, such as SIP, through work on rich presence, peer-to-peer systems, next-generation emergency calling, and service creation tools. Recently, we have also looked extensively at wireless systems for VoIP, as 802.11b and 802.11n networks and maybe WiMax networks are likely to become important last-mile technologies for telephony. We are also trying to greatly improve the ability of users to diagnose faults in the complicated tangle of providers and equipment, using a peer-to-peer fault diagnosis system called DYSWIS (Do You See What I See).

   We try to do practically relevant work, by building prototypes and open source systems, by measuring performance of real systems, and by contributing to IETF standards.

你对多媒体网络未来的愿景是什么？
-------------------------------------------------------------
What is your vision for the future of multimedia networking?

我们正处于一个过渡阶段，距离 IP 成为 IPTV 到 VoIP 等多媒体服务的通用平台只有几年时间。人们希望在暴风雪和地震期间仍能收听广播、使用电话和观看电视，因此当互联网取代这些专用网络的角色时，用户也会期望同样的可靠性水平。

我们将必须学会为由竞争运营商、服务和内容提供商组成的生态系统设计网络技术，同时服务于大量技术不精的用户，并保护他们免受少数恶意和犯罪用户的破坏。改变协议越来越困难，协议也越来越复杂，因为它们需要考虑相互竞争的商业利益、安全性、隐私性，以及防火墙和网络地址转换器导致的网络透明性缺失。

由于多媒体网络正逐步成为几乎所有消费者娱乐的基础，因此将强调以低成本管理非常大的网络。用户会期望使用方便，例如在所有设备上找到相同的内容。

.. toggle::

   We are now in a transition phase; just a few years shy of when IP will be the universal platform for multimedia services, from IPTV to VoIP. We expect radio, telephone, and TV to be available even during snowstorms and earthquakes, so when the Internet takes over the role of these dedicated networks, users will expect the same level of reliability.

   We will have to learn to design network technologies for an ecosystem of competing carriers, service and content providers, serving lots of technically untrained users and defending them against a small, but destructive, set of malicious and criminal users. Changing protocols is becoming increasingly hard. They are also becoming more complex, as they need to take into account competing business interests, security, privacy, and the lack of transparency of networks caused by firewalls and network address translators.

   Since multimedia networking is becoming the foundation for almost all of consumer entertainment, there will be an emphasis on managing very large networks, at low cost. Users will expect ease of use, such as finding the same content on all of their devices.

为什么 SIP 拥有光明的前景？
------------------------------------------
Why does SIP have a promising future?

随着当前无线网络升级到 3G 网络的进程，希望能够拥有一个跨所有网络类型（从有线调制解调器到企业电话网络和公共无线网络）的单一多媒体信令机制。结合软件无线电，未来一个设备可以在家庭网络中作为无线蓝牙电话使用，在企业网络中通过 802.11 使用，在广域中通过 3G 网络使用。即便在我们拥有这种单一通用无线设备之前，个人移动机制也使我们可以隐藏不同网络之间的差异。一个标识符将成为联系某人的通用手段，而不是记住或传播半打基于技术或位置的电话号码。

SIP 也将语音（比特）传输与语音服务分离开来。现在在技术上可以打破本地电话的垄断：一家公司提供中立的比特传输，而其他公司则提供 IP“拨号音”以及传统的电话服务，如网关、呼叫转移和来电显示。

超越多媒体信令，SIP 还提供了一种互联网中一直缺失的新服务：事件通知。我们曾尝试用 HTTP 临时方案和电子邮件近似实现这种服务，但效果始终不理想。由于事件是分布式系统中的常见抽象机制，这或许能简化新服务的构建。

.. toggle::

   As the current wireless network upgrade to 3G networks proceeds, there is the hope of a single multimedia signaling mechanism spanning all types of networks, from cable modems, to corporate telephone networks and public wireless networks. Together with software radios, this will make it possible in the future that a single device can be used on a home network, as a cordless BlueTooth phone, in a corporate network via 802.11 and in the wide area via 3G networks. Even before we have such a single universal wireless device, the personal mobility mechanisms make it possible to hide the differences between networks. One identifier becomes the universal means of reaching a person, rather than remembering or passing around half a dozen technology- or location-specific telephone numbers.

   SIP also breaks apart the provision of voice (bit) transport from voice services. It now becomes technically possible to break apart the local telephone monopoly, where one company provides neutral bit transport, while others provide IP “dial tone” and the classical telephone services, such as gateways, call forwarding, and caller ID.

   Beyond multimedia signaling, SIP offers a new service that has been missing in the Internet: event notification. We have approximated such services with HTTP kludges and e-mail, but this was never very satisfactory. Since events are a common abstraction for distributed systems, this may simplify the construction of new services.

你对准备进入网络领域的学生有什么建议？
------------------------------------------------------------------------
Do you have any advice for students entering the networking field?

网络研究是一个跨学科领域。它涉及电气工程、计算机科学的所有方面、运筹学、统计学、经济学及其他学科。因此，网络研究人员必须熟悉远远超出协议和路由算法的内容。鉴于网络正成为日常生活的重要组成部分，希望在该领域有所作为的学生应当思考网络中的新型资源限制：人的时间与精力，而不仅仅是带宽或存储。

从事网络研究可以极富成就感，因为它致力于让人们进行交流和思想交换，这正是人类本质的一部分。互联网已经成为继交通系统和能源分配之后的第三大全球基础设施。几乎没有哪个经济领域可以在没有高性能网络的情况下正常运作，因此在可预见的未来，该领域应当充满机遇。

.. toggle::

   Networking bridges disciplines. It draws from electrical engineering, all aspects of computer science, operations research, statistics, economics, and other disciplines. Thus, networking researchers have to be familiar with subjects well beyond protocols and routing algorithms. Given that networks are becoming such an important part of everyday life, students wanting to make a difference in the field should think of the new resource constraints in networks: human time and effort, rather than just bandwidth or storage.

   Work in networking research can be immensely satisfying since it is about allowing people to communicate and exchange ideas, one of the essentials of being human. The Internet has become the third major global infrastructure, next to the transportation system and energy distribution. Almost no part of the economy can work without high-performance networks, so there should be plenty of opportunities for the foreseeable future.