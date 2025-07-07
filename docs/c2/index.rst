.. _c2:

第 2 章 应用层
============================================

Chapter 2 Application Layer 

网络应用是计算机网络存在的理由（raison d’être）——如果我们无法设想出任何有用的应用程序，那就没有必要构建支持这些应用的网络基础设施和协议。自因特网诞生以来，确实涌现了大量有用且富有娱乐性的应用。这些应用推动了因特网的成功，激励了家庭、学校、政府和企业将因特网融入他们的日常活动之中。

因特网应用包括 20 世纪 70 至 80 年代流行的经典文本应用：文本电子邮件、远程计算机访问、文件传输和新闻组；也包括 90 年代中期的“杀手级应用”——万维网，涵盖网页浏览、搜索和电子商务。进入千禧年之后，出现了即时通讯和 P2P 文件共享这两大杀手级应用。新千年中，又有许多新颖且极具吸引力的应用不断涌现，包括 IP 语音和视频会议（如 Skype、Facetime 和 Google Hangouts）、用户生成视频（如 YouTube）、按需电影服务（如 Netflix）、大型多人在线游戏（如 Second Life 和魔兽世界）。同期，我们还见证了新一代社交网络应用的兴起——如 Facebook、Instagram、Twitter 和微信——这些应用在人类社会网络之上，建立在因特网的路由器和通信链路之上。而最 近几年，随着智能手机的普及，基于地理位置的移动应用也大量涌现，如热门的签到、约会和道路交通预测应用（例如 Yelp、Tinder、Waze 和 Yik Yak）。显然，令人兴奋的新型因特网应用的推出并未减速。也许本书的一些读者未来将创建下一代杀手级因特网应用！

本章将研究网络应用的概念及其实现方式。我们将从定义应用层中的关键概念开始，包括应用所需的网络服务、客户端与服务器、进程、传输层接口等。我们将详细探讨多个网络应用，包括 Web、电子邮件、DNS、对等（P2P）文件分发和视频流媒体。（ :ref:`第 9 章 <c9>` 将进一步研究多媒体应用，包括流媒体视频与 IP 语音。）接下来，我们将介绍网络应用的开发，包括基于 TCP 与 UDP 的开发内容。特别地，我们将学习 socket 接口，并通过一些用 Python 编写的简单客户端-服务器应用程序进行讲解。本章结尾还提供了一些有趣的 socket 编程练习。

应用层是学习协议的绝佳起点。它是我们熟悉的领域。我们对许多依赖这些协议的应用程序已经相当了解。这一层可以帮助我们直观地理解“协议”的含义，并引出许多将在学习传输层、网络层和链路层协议时再次遇到的重要问题。

.. toggle::

   Network applications are the raisons d’être of a computer network—if we couldn’t conceive of any useful
   applications, there wouldn’t be any need for networking infrastructure and protocols to support them.
   Since the Internet’s inception, numerous useful and entertaining applications have indeed been created.
   These applications have been the driving force behind the Internet’s success, motivating people in
   homes, schools, governments, and businesses to make the Internet an integral part of their daily
   activities.

   Internet applications include the classic text-based applications that became popular in the 1970s and
   1980s: text e-mail, remote access to computers, file transfers, and newsgroups. They include the killer
   application of the mid-1990s, the World Wide Web, encompassing Web surfing, search, and electronic
   commerce. They include instant messaging and P2P file sharing, the two killer applications introduced
   at the end of the millennium. In the new millennium, new and highly compelling applications continue to
   emerge, including voice over IP and video conferencing such as Skype, Facetime, and Google
   Hangouts; user generated video such as YouTube and movies on demand such as Netflix; multiplayer
   online games such as Second Life and World of Warcraft. During this same period, we have seen the
   emergence of a new generation of social networking applications—such as Facebook, Instagram,
   Twitter, and WeChat—which have created engaging human networks on top of the Internet’s network or
   routers and communication links. And most recently, along with the arrival of the smartphone, there has
   been a profusion of location based mobile apps, including popular check-in, dating, and road-traffic
   forecasting apps (such as Yelp, Tinder, Waz, and Yik Yak). Clearly, there has been no slowing down of
   new and exciting Internet applications. Perhaps some of the readers of this text will create the next
   generation of killer Internet applications!

   In this chapter we study the conceptual and implementation aspects of network applications. We begin
   by defining key application-layer concepts, including network services required by applications, clients
   and servers, processes, and transport-layer interfaces. We examine several network applications in
   detail, including the Web, e-mail, DNS, peer-to-peer (P2P) file distribution, and video streaming.
   ( :ref:`Chapter 9 <c9>` will further examine multimedia applications, including streaming video and VoIP.) We then
   cover network application development, over both TCP and UDP. In particular, we study the socket
   interface and walk through some simple client-server applications in Python. We also provide several
   fun and interesting socket programming assignments at the end of the chapter.

   The application layer is a particularly good place to start our study of protocols. It’s familiar ground.
   We’re acquainted with many of the applications that rely on the protocols we’ll study. It will give us a
   good feel for what protocols are all about and will introduce us to many of the same issues that we’ll see
   again when we study transport, network, and link layer protocols.


.. toctree::
   :maxdepth: 2
   :caption: 内容

   ./s1.rst
   ./s2.rst
   ./s3.rst
   ./s4.rst
   ./s5.rst
   ./s6.rst
   ./s7.rst
   ./summary.rst
   ./homework.rst
   ./socketpro.rst
   ./wiresharklab.rst
   ./interview.rst