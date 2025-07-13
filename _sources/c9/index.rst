.. _c9:


第 9 章 多媒体网络
============================================

Chapter 9 Multimedia Networking

无论是在床上休息，还是乘坐公交和地铁，世界各地的人们目前都在使用互联网按需观看电影和电视节目。像 Netflix 和亚马逊这样的北美互联网电影和电视发行公司，以及中国的优酷和看看，几乎已成为家喻户晓的名字。但人们不仅仅是在观看互联网视频，他们还通过 YouTube 等网站上传和分发自己生成的内容，成为互联网视频的生产者和消费者。此外，Skype、Google Talk 和微信（在中国极为流行）等网络应用不仅允许人们通过互联网拨打“电话”，还支持视频和多人会议功能。事实上，我们预测到本十年末，大多数视频消费和语音通话都将端到端地通过互联网进行，通常连接的是通过蜂窝和 WiFi 访问网络接入互联网的无线设备。传统的电话和广播电视正在迅速变得过时。

我们从 :ref:`第 9.1 节 <c9.1>` 开始，对多媒体应用进行分类。我们将看到多媒体应用可以分为流式存储音视频、对话式 *语音/视频传输* 和 *流式直播音视频* 三类。每一类应用都有其独特的服务需求，显著不同于电子邮件、网页浏览和远程登录等传统弹性应用。在 :ref:`第 9.2 节 <c9.2>` 中，我们将详细探讨视频流。我们将探索视频流背后的许多基本原理，包括客户端缓存、预取和根据可用带宽调整视频质量。在 :ref:`第 9.3 节 <c9.3>` 中，我们研究对话式语音和视频，这类应用对端到端延迟非常敏感，但可以容忍偶尔的数据丢失。这里我们将探讨自适应播放、前向纠错和误差隐藏等技术如何减轻网络引起的数据包丢失和延迟问题。我们还将以 Skype 作为案例研究。在 :ref:`第 9.4 节 <c9.4>` 中，我们将学习 RTP 和 SIP 两种流行的实时对话式语音和视频应用协议。在 :ref:`第 9.5 节 <c9.5>` 中，我们将探讨网络内部用以区分不同类型流量（例如，对延迟敏感的对话语音应用与弹性应用如网页浏览）的机制，并实现对多类流量的差异化服务。

.. toggle::

   While lounging in bed or riding buses and subways, people in all corners of the world are currently using
   the Internet to watch movies and television shows on demand. Internet movie and television distribution
   companies such as Netflix and Amazon in North America and Youku and Kankan in China have
   practically become household names. But people are not only watching Internet videos, they are using
   sites like YouTube to upload and distribute their own user-generated content, becoming Internet video
   producers as well as consumers. Moreover, network applications such as Skype, Google Talk, and
   WeChat (enormously popular in China) allow people to not only make “telephone calls” over the
   Internet, but to also enhance those calls with video and multi-person conferencing. In fact, we predict
   that by the end of the current decade most of the video consumption and voice conversations will take
   place end-to-end over the Internet, more typically to wireless devices connected to the Internet via
   cellular and WiFi access networks. Traditional telephony and broadcast television are quickly becoming
   obsolete.

   We begin this chapter with a taxonomy of multimedia applications in :ref:`Section 9.1 <c9.1>`. We’ll see that a
   multimedia application can be classified as either streaming stored audio/video, conversational
   *voice/video-over-IP*, or *streaming live audio/video*. We’ll see that each of these classes of applications
   has its own unique service requirements that differ significantly from those of traditional elastic
   applications such as e-mail, Web browsing, and remote login. In :ref:`Section 9.2 <c9.2>`, we’ll examine video
   streaming in some detail. We’ll explore many of the underlying principles behind video streaming,
   including client buffering, prefetching, and adapting video quality to available bandwidth. In :ref:`Section 9.3 <c9.3>`,
   we investigate conversational voice and video, which, unlike elastic applications, are highly sensitive to
   end-to-end delay but can tolerate occasional loss of data. Here we’ll examine how techniques such as
   adaptive playout, forward error correction, and error concealment can mitigate against network-induced
   packet loss and delay. We’ll also examine Skype as a case study. In :ref:`Section 9.4 <c9.4>`, we’ll study RTP and
   SIP, two popular protocols for real-time conversational voice and video applications. In :ref:`Section 9.5 <c9.5>`,
   we’ll investigate mechanisms within the network that can be used to distinguish one class of traffic (e.g.,
   delay-sensitive applications such as conversational voice) from another (e.g., elastic applications such
   as browsing Web pages), and provide differentiated service among multiple classes of traffic.

.. toctree::
   :maxdepth: 2
   :caption: 内容

   ./s1.rst
   ./s2.rst
   ./s3.rst
   ./s4.rst
   ./s5.rst
   ./summary.rst
   ./homework.rst
   ./interview.rst
