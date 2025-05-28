.. _c2:

第 2 章 应用层
============================================

Chapter 2 Application Layer 

.. tab:: 中文



.. tab:: 英文

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