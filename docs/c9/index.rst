.. _c9:

Chapter 9 Multimedia Networking
============================================

Chapter 9 Multimedia Networking

.. tab:: 中文



.. tab:: 英文

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
   ./wiresharklab.rst
   ./interview.rst
