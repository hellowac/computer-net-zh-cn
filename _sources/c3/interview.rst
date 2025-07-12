



访谈: Van Jacobson
===================================

Interview: Van Jacobson

Van Jacobson 目前在 Google 工作，此前曾是 PARC 的研究员。在那之前，他是 Packet Design 的联合创始人和首席科学家。再早前，他担任 Cisco 的首席科学家。在加入 Cisco 之前，他曾担任劳伦斯伯克利国家实验室网络研究组的负责人，并在加州大学伯克利分校和斯坦福大学任教。Van 于 2001 年获得 ACM SIGCOMM 奖，以表彰其在通信网络领域的杰出终身贡献，并于 2002 年获得 IEEE Kobayashi 奖，表彰其“对网络拥塞理解的贡献以及所开发的拥塞控制机制促进了互联网的成功扩展”。他于 2004 年当选为美国国家工程院院士。

.. figure:: ../img/346-0.png
   :align: center

.. toggle::

   Van Jacobson works at Google and was previously a Research Fellow at PARC. Prior to that, he was co-founder and Chief Scientist of Packet Design. Before that, he was Chief Scientist at Cisco. Before joining Cisco, he was head of the Network Research Group at Lawrence Berkeley National Laboratory and taught at UC Berkeley and Stanford. Van received the ACM SIGCOMM Award in 2001 for outstanding lifetime contribution to the field of communication networks and the IEEE Kobayashi Award in 2002 for “contributing to the understanding of network congestion and developing congestion control mechanisms that enabled the successful scaling of the Internet”. He was elected to the U.S. National Academy of Engineering in 2004.

   .. figure:: ../img/346-0.png
      :align: center

请描述你职业生涯中参与的一个或两个最令人兴奋的项目。其中最大的挑战是什么？
----------------------------------------------------------------------------------------------------------------------------------
Please describe one or two of the most exciting projects you have worked on during your career. What were the biggest challenges?

学校教会我们很多寻找答案的方法。而我参与的每一个有趣问题中，最大的挑战都是找到“正确的问题”。当 Mike Karels 和我开始研究 TCP 拥塞时，我们花了好几个月盯着协议和数据包的抓包记录发问：“为什么它会失败？”有一天，在 Mike 的办公室里，我们其中一个人说：“我之所以搞不懂它为什么失败，是因为我根本不明白它是怎么成功过的。”这才是那个“正确的问题”，它迫使我们去搞懂让 TCP 运作的“ack 定时”。之后，剩下的事情就容易多了。

.. toggle::

   School teaches us lots of ways to find answers. In every interesting problem I’ve worked on, the challenge has been finding the right question. When Mike Karels and I started looking at TCP congestion, we spent months staring at protocol and packet traces asking “Why is it failing?”. One day in Mike’s office, one of us said “The reason I can’t figure out why it fails is because I don’t understand how it ever worked to begin with.” That turned out to be the right question and it forced us to figure out the “ack clocking” that makes TCP work. After that, the rest was easy.

更广义地说，你认为网络和互联网的未来是什么？
-----------------------------------------------------------------------------
More generally, where do you see the future of networking and the Internet?

对大多数人来说，Web 就是互联网。网络工程师礼貌地微笑，因为我们知道 Web 是运行在互联网上的一个应用程序，但如果他们是对的呢？互联网的核心是实现一对主机之间的通信。而 Web 的核心是分布式的信息生产与消费。“信息传播”是一种非常通用的通信视角，而“一对一通信”只是其中一个极小的子集。我们需要进入那个更大的范畴。今天的网络在处理广播媒介（无线电、无源光网络等）时，假装它们是一根点对点的电缆。这种方式极其低效。如今，世界各地正通过 U 盘或智能手机传输每秒数太比特的数据，但我们却不知道如何把这些行为视为“网络”。ISP 正忙着部署缓存和 CDN，以可扩展地分发视频和音频。缓存是解决方案中必不可少的一部分，但今天的网络体系——从信息、排队或流量理论到互联网协议规范——没有任何部分告诉我们如何设计和部署这些机制。我认为，也希望，在接下来的几年中，网络技术将逐步发展为拥抱支持 Web 的那个更宏大的通信愿景。

.. toggle::

   For most people, the Web is the Internet. Networking geeks smile politely since we know the Web is an application running over the Internet but what if they’re right? The Internet is about enabling conversations between pairs of hosts. The Web is about distributed information production and consumption. “Information propagation” is a very general view of communication of which “pairwise conversation” is a tiny subset. We need to move into the larger tent. Networking today deals with broadcast media (radios, PONs, etc.) by pretending it’s a point-to- point wire. That’s massively inefficient. Terabits-per-second of data are being exchanged all over the World via thumb drives or smart phones but we don’t know how to treat that as “networking”. ISPs are busily setting up caches and CDNs to scalably distribute video and audio. Caching is a necessary part of the solution but there’s no part of today’s networking—from Information, Queuing or Traffic Theory down to the Internet protocol specs—that tells us how to engineer and deploy it. I think and hope that over the next few years, networking will evolve to embrace the much larger vision of communication that underlies the Web.

哪些人曾在专业上激励了你？
------------------------------------------
What people inspired you professionally?

我在读研究生时，Richard Feynman 来做过一次学术报告。他谈到的是我整整一学期都在努力理解的一段量子理论，他的解释如此简单明了，让我之前眼中毫无逻辑、难以理解的东西变得显而易见、不可避免。那种能够看透并传达我们复杂世界背后本质简单性的能力，对我来说是一种罕见而美妙的天赋。

.. toggle::

   When I was in grad school, Richard Feynman visited and gave a colloquium. He talked about a piece of Quantum theory that I’d been struggling with all semester and his explanation was so simple and lucid that what had been incomprehensible gibberish to me became obvious and inevitable. That ability to see and convey the simplicity that underlies our complex world seems to me a rare and wonderful gift.

你对那些希望从事计算机科学与网络事业的学生有什么建议？
------------------------------------------------------------------------------------------------
What are your recommendations for students who want careers in computer science and networking?

这是一个极棒的领域——自从有了书籍以来，计算机和网络可能是对社会影响最深远的发明。网络的本质是连接各种事物，而研究它能帮助你建立各种知识上的联系：蚂蚁觅食和蜜蜂舞蹈比 RFC 更好地展示了协议设计，交通堵塞或人群离开体育场才是真正的拥塞本质，而感恩节后暴风雪中学生寻找返校航班的情形就是动态路由的核心。如果你对很多事情感兴趣，并希望产生影响力，那很难想象有比这个更好的领域了。

.. toggle::

   It’s a wonderful field—computers and networking have probably had more impact on society than any invention since the book. Networking is fundamentally about connecting stuff, and studying it helps you make intellectual connections: Ant foraging & Bee dances demonstrate protocol design better than RFCs, traffic jams or people leaving a packed stadium are the essence of congestion, and students finding flights back to school in a post-Thanksgiving blizzard are the core of dynamic routing. If you’re interested in lots of stuff and want to have an impact, it’s hard to imagine a better field.