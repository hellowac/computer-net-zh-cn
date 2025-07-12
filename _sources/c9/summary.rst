.. _c9.6:


9.6 小结
=================
9.6 Summary

多媒体网络是当今互联网中最令人兴奋的发展之一。全球人们在电视机前的时间越来越少，而是使用智能手机和设备接收直播和点播的音频和视频传输。此外，借助YouTube等网站，用户不仅是多媒体互联网内容的消费者，也是生产者。除了视频分发，互联网还被用于传输电话通话。事实上，在未来十年内，互联网及无线互联网接入可能使传统的电路交换电话系统成为过去。VoIP不仅以低成本提供电话服务，还提供许多增值服务，如视频会议、在线目录服务、语音留言以及与Facebook、微信等社交网络的集成。

在 :ref:`第9.1节 <c9.1>` 中，我们描述了视频和语音的内在特性，然后将多媒体应用分为三类：（i）流式存储音视频，（ii）基于IP的会话语音/视频，以及（iii）流式直播音视频。

在 :ref:`第9.2节 <c9.2>` 中，我们深入研究了流式存储视频。对于流式视频应用，预先录制的视频存放在服务器上，用户向服务器发送请求按需观看视频。我们看到流式视频系统可分为两类：UDP流和HTTP流。我们观察到流式视频最重要的性能指标是平均吞吐量。

在 :ref:`第9.3节 <c9.3>` 中，我们考察了如何设计会话多媒体应用（如VoIP）在尽力而为网络上运行。对于会话多媒体，时序因素非常重要，因为此类应用对延迟极为敏感。另一方面，会话多媒体应用对丢包有一定容忍度——偶尔丢包只会导致音视频播放时偶尔出现卡顿，且这些丢包常能部分或完全被掩盖。我们了解了客户端缓冲、包序列号和时间戳的组合如何大大减轻网络抖动的影响。我们还介绍了Skype这一领先的语音和视频IP公司背后的技术。在 :ref:`第9.4节 <c9.4>` 中，我们研究了VoIP的两个重要标准协议，即RTP和SIP。

在 :ref:`第9.5节 <c9.5>` 中，我们介绍了如何利用若干网络机制（链路级调度机制和流量管控）为多个流量类别提供区分服务。

.. toggle::

    Multimedia networking is one of the most exciting developments in the Internet today. People throughout the world less and less time in front of their televisions, and are instead use their smartphones and devices to receive audio and video transmissions, both live and prerecorded. Moreover, with sites like YouTube, users have become producers as well as consumers of multimedia Internet content. In addition to video distribution, the Internet is also being used to transport phone calls. In fact, over the next 10 years, the Internet, along with wireless Internet access, may make the traditional circuit- switched telephone system a thing of the past. VoIP not only provides phone service inexpensively, but also provides numerous value-added services, such as video conferencing, online directory services, voice messaging, and integration into social networks such as Facebook and WeChat.

    In :ref:`Section 9.1 <c9.1>`, we described the intrinsic characteristics of video and voice, and then classified multimedia applications into three categories: (i) streaming stored audio/video, (ii) conversational voice/video-over-IP, and (iii) streaming live audio/video.

    In :ref:`Section 9.2 <c9.2>`, we studied streaming stored video in some depth. For streaming video applications, prerecorded videos are placed on servers, and users send requests to these servers to view the videos on demand. We saw that streaming video systems can be classified into two categories: UDP streaming and HTTP. We observed that the most important performance measure for streaming video is average throughput.

    In :ref:`Section 9.3 <c9.3>`, we examined how conversational multimedia applications, such as VoIP, can be designed to run over a best-effort network. For conversational multimedia, timing considerations are important because conversational applications are highly delay-sensitive. On the other hand, conversational multimedia applications are loss—tolerant—occasional loss only causes occasional glitches in audio/video playback, and these losses can often be partially or fully concealed. We saw how a combination of client buffers, packet sequence numbers, and timestamps can greatly alleviate the effects of network-induced jitter. We also surveyed the technology behind Skype, one of the leading voice- and video-over-IP companies. In :ref:`Section 9.4 <c9.4>`, we examined two of the most important standardized protocols for VoIP, namely, RTP and SIP.

    In :ref:`Section 9.5 <c9.5>`, we introduced how several network mechanisms (link-level scheduling disciplines and traffic policing) can be used to provide differentiated service among several classes of traffic.