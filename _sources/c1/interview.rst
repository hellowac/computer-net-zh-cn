访谈：Leonard Kleinrock
===================================

Interview: Leonard Kleinrock 

Leonard Kleinrock 是加州大学洛杉矶分校的计算机科学教授。1969 年，他在 UCLA 的计算机成为 Internet 的第一个节点。他于 1961 年创建的分组交换原理成为 Internet 背后的核心技术。他获得了纽约城市学院（CCNY）的电气工程学士学位，并在麻省理工学院（MIT）获得了电气工程的硕士和博士学位。

.. toggle::

   Leonard Kleinrock is a professor of computer science at the University of California, Los
   Angeles. In 1969, his computer at UCLA became the first node of the Internet. His creation of
   packet-switching principles in 1961 became the technology behind the Internet. He received his
   B.E.E. from the City College of New York (CCNY) and his masters and PhD in electrical
   engineering from MIT.

.. figure:: ../img/109-0.png
   :align: center


是什么促使您专注于网络/互联网技术？
------------------------------------
What made you decide to specialize in networking/Internet technology?

1959 年，我在 MIT 攻读博士时，环顾四周，发现大多数同学都在研究信息论和编码理论。在 MIT，有一位伟大的研究者 Claude Shannon，他开启了这些领域，并且已经解决了其中大多数重要问题。剩下的问题非常困难，而且意义不大。所以我决定开辟一个全新的方向——一个尚未有人涉足的领域。请记住，在 MIT 我被大量计算机包围，我很清楚不久之后这些机器将需要彼此通信。而当时并没有一种有效的通信方式，因此我决定开发一种能够创建高效、可靠数据网络的技术。

.. toggle::

   As a PhD student at MIT in 1959, I looked around and found that most of my classmates were
   doing research in the area of information theory and coding theory. At MIT, there was the great
   researcher, Claude Shannon, who had launched these fields and had solved most of the
   important problems already. The research problems that were left were hard and of lesser
   consequence. So I decided to launch out in a new area that no one else had yet conceived of.
   Remember that at MIT I was surrounded by lots of computers, and it was clear to me that soon
   these machines would need to communicate with each other. At the time, there was no effective
   way for them to do so, so I decided to develop the technology that would permit efficient and
   reliable data networks to be created.

您在计算机行业的第一份工作是什么？具体做了什么？
---------------------------------------------------------------------------
What was your first job in the computer industry? What did it entail?

我在 1951 年至 1957 年期间在 CCNY 的夜校学习，攻读电气工程学士学位。白天，我先是在一家名为 Photobell 的小型工业电子公司担任技术员，后来成为工程师。在那儿，我将数字技术引入了他们的产品线。本质上，我们使用光电设备来检测特定物体的存在（如箱子、人等），并使用当时称为双稳态多谐振荡器的电路将数字处理引入这一检测领域。这些电路恰好是计算机的基本构件，今天通常被称为触发器或开关。

.. toggle::

   I went to the evening session at CCNY from 1951 to 1957 for my bachelor’s degree in electrical
   engineering. During the day, I worked first as a technician and then as an engineer at a small,
   industrial electronics firm called Photobell. While there, I introduced digital technology to their
   product line. Essentially, we were using photoelectric devices to detect the presence of certain
   items (boxes, people, etc.) and the use of a circuit known then as a bistable multivibrator was
   just the kind of technology we needed to bring digital processing into this field of detection.
   These circuits happen to be the building blocks for computers, and have come to be known as
   flip-flops or switches in today’s vernacular.

当您发送第一条主机到主机的消息（从 UCLA 到 Stanford Research Institute）时，您的心里在想什么？
-------------------------------------------------------------------------------------------------------------------------------------------
What was going through your mind when you sent the first host-to-host message (from UCLA to the Stanford Research Institute)?

坦率地说，我们完全没有意识到那个事件的重要性。我们没有准备什么具有历史意义的特殊消息，就像许多过去的发明者那样（Samuel Morse 的 “What hath God wrought.”，Alexander Graham Bell 的 “Watson, come here! I want you.”，或者 Neil Armstrong 的 “That’s one small step for a man, one giant leap for mankind.”）。那些人真聪明！他们懂得媒体和公关。我们当时只是想登录到 SRI 的计算机。因此我们键入了 “L”，它被正确接收；接着输入 “o”，也被接收；然后输入 “g”，结果导致 SRI 主机宕机！所以，我们的消息成了有史以来最简短，也许也是最有预兆性的消息：“Lo！”——正如 “Lo and behold!” 所暗示的那样。

那年早些时候，我在 UCLA 的一份新闻稿中曾被引用说：“一旦网络投入运行，我们将可以像使用电力和电话一样，从家中和办公室方便地访问计算机资源。” 因此我当时的设想是，Internet 将无处不在、始终在线、始终可用，任何人可以使用任何设备在任何地点接入，它将是“隐形”的。然而，我从未预料到我的 99 岁老母亲也会使用 Internet——而她的确做到了！

.. toggle::

   Frankly, we had no idea of the importance of that event. We had not prepared a special
   message of historic significance, as did so many inventors of the past (Samuel Morse with “What
   hath God wrought.” or Alexander Graham Bell with “Watson, come here! I want you.” or Neal
   Amstrong with “That’s one small step for a man, one giant leap for mankind.”) Those guys were
   smart! They understood media and public relations. All we wanted to do was to login to the SRI
   computer. So we typed the “L”, which was correctly received, we typed the “o” which was
   received, and then we typed the “g” which caused the SRI host computer to crash! So, it turned
   out that our message was the shortest and perhaps the most prophetic message ever, namely
   “Lo!” as in “Lo and behold!”

   Earlier that year, I was quoted in a UCLA press release saying that once the network was up
   and running, it would be possible to gain access to computer utilities from our homes and offices
   as easily as we gain access to electricity and telephone connectivity. So my vision at that time
   was that the Internet would be ubiquitous, always on, always available, anyone with any device
   could connect from any location, and it would be invisible. However, I never anticipated that my
   99-year-old mother would use the Internet—and indeed she did!

您对网络的未来有何愿景？
------------------------------------------------------
What is your vision for the future of networking?

对基础设施进行预测是比较容易的部分。我预计我们会看到流动计算、移动设备和智能空间的大量部署。实际上，轻量级、廉价、高性能、便携的计算与通信设备（再加上 Internet 的无处不在）已使我们成为“数字游牧者”。流动计算指的是一种技术，使得用户可以在各处自由移动时无缝地访问 Internet 服务，无论走到哪里，无论使用什么设备。

更难预测的是应用和服务，这些往往以戏剧性的方式让我们大吃一惊（例如电子邮件、搜索技术、万维网、博客、社交网络、用户内容生成，以及音乐、照片、视频的共享等）。我们正处在一类全新、令人惊喜的移动应用即将爆发的临界点，这些应用将传送至我们的手持设备中。

下一步将是从网络的虚拟世界迈入“智能空间”的物理世界。我们的环境（办公桌、墙壁、车辆、手表、腰带等）将通过执行器、传感器、逻辑处理器、存储器、摄像头、麦克风、扬声器、显示屏和通信模块等技术“活”起来。这些嵌入式技术将使得我们的环境能够提供我们想要的 IP 服务。当我走进一个房间时，房间会知道我进来了。我将能以自然语言（如英语）与环境对话；我的请求将以网页形式呈现，显示在墙面、眼镜中，甚至通过语音、全息影像等方式展现。

再往远一点看，我设想网络的未来将包括以下关键组成部分：我看到智能软件代理被部署在整个网络中，它们将挖掘数据、处理数据、观察趋势，并动态、适应性地执行任务。我看到网络中产生的流量将越来越多地来自这些嵌入设备和智能代理，而非人类用户。我看到由大量自组织系统构成的网络来管理这一庞大、高速的网络。我看到海量信息在网络中瞬时传播，并经历强大的处理与过滤。Internet 将成为全球范围内无处不在的神经系统。我看到这一切，也看到更多，我们正加速奔向 21 世纪的未来。

.. toggle::

   The easy part of the vision is to predict the infrastructure itself. I anticipate that we see
   considerable deployment of nomadic computing, mobile devices, and smart spaces. Indeed, the
   availability of lightweight, inexpensive, high-performance, portable computing, and
   communication devices (plus the ubiquity of the Internet) has enabled us to become nomads.
   Nomadic computing refers to the technology that enables end users who travel from place to
   place to gain access to Internet services in a transparent fashion, no matter where they travel
   and no matter what device they carry or gain access to. The harder part of the vision is to predict
   the applications and services, which have consistently surprised us in dramatic ways (e-mail,
   search technologies, the World Wide Web, blogs, social networks, user generation, and sharing
   of music, photos, and videos, etc.). We are on the verge of a new class of surprising and
   innovative mobile applications delivered to our hand-held devices.

   The next step will enable us to move out from the netherworld of cyberspace to the physical
   world of smart spaces. Our environments (desks, walls, vehicles, watches, belts, and so on) will
   come alive with technology, through actuators, sensors, logic, processing, storage, cameras,
   microphones, speakers, displays, and communication. This embedded technology will allow our
   environment to provide the IP services we want. When I walk into a room, the room will know I
   entered. I will be able to communicate with my environment naturally, as in spoken English; my
   requests will generate replies that present Web pages to me from wall displays, through my
   eyeglasses, as speech, holograms, and so forth.

   Looking a bit further out, I see a networking future that includes the following additional key
   components. I see intelligent software agents deployed across the network whose function it is
   to mine data, act on that data, observe trends, and carry out tasks dynamically and adaptively. I
   see considerably more network traffic generated not so much by humans, but by these
   embedded devices and these intelligent software agents. I see large collections of self-
   organizing systems controlling this vast, fast network. I see huge amounts of information flashing
   across this network instantaneously with this information undergoing enormous processing and
   filtering. The Internet will essentially be a pervasive global nervous system. I see all these things
   and more as we move headlong through the twenty-first century.

在职业上，哪些人对您产生了影响？
-----------------------------------------------------------------------------------
What people have inspired you professionally?

最重要的是 MIT 的 Claude Shannon，他是一位才华横溢的研究者，擅长以高度直观的方式将其数学思想与物理世界联系起来。他曾是我博士论文委员会的成员。

.. toggle::

   By far, it was Claude Shannon from MIT, a brilliant researcher who had the ability to relate his
   mathematical ideas to the physical world in highly intuitive ways. He was on my PhD thesis
   committee.

您对正在进入网络/互联网领域的学生有何建议？
-----------------------------------------------------------------------------------
Do you have any advice for students entering the networking/Internet field?

Internet 及其所带来的一切是一个广阔的新前沿，充满了令人惊叹的挑战。在这里，有巨大的创新空间。不要被现有技术所限制。放手去想象你想实现的未来——然后让它成真。

.. toggle::

   The Internet and all that it enables is a vast new frontier, full of amazing challenges. There is
   room for great innovation. Don’t be constrained by today’s technology. Reach out and imagine
   what could be and then make it happen.