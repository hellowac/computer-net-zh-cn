


家庭作业问题和疑问
========================================

Homework Problems and Questions

SECTION 2.1
-------------

R1. 列出五种非专有的互联网应用及其使用的应用层协议。

R2. 网络架构和应用架构之间有什么区别？

R3. 在一对进程之间的通信会话中，哪个进程是客户端，哪个是服务器？

R4. 对于一个 P2P 文件共享应用，你是否同意“通信会话中没有客户端和服务器端的概念”这一说法？为什么或为什么不？

R5. 一个主机上运行的进程用什么信息来标识另一个主机上运行的进程？

R6. 假设你想尽可能快地从远程客户端向服务器执行一个事务。你会使用 UDP 还是 TCP？为什么？

R7. 参考 :ref:`图 2.4 <Figure 2.4>`，我们看到 :ref:`图 2.4 <Figure 2.4>` 中列出的所有应用都不同时要求无数据丢失和时效性。你能否设想一个既要求无数据丢失又高度敏感于时间的应用？

R8. 列出传输协议可以提供的四大类服务。对于每一类服务，指出是 UDP、TCP 还是两者都提供此服务。

R9. 请回忆 TCP 可以通过 SSL 增强以提供进程到进程的安全服务（包括加密）。SSL 是在传输层还是应用层运行？如果应用程序开发者想让 TCP 通过 SSL 增强，他/她需要做什么？

.. toggle::

    R1. List five nonproprietary Internet applications and the application-layer protocols that they use.

    R2. What is the difference between network architecture and application architecture?

    R3. For a communication session between a pair of processes, which process is the client and which is the server?

    R4. For a P2P file-sharing application, do you agree with the statement, “There is no notion of client and server sides of a communication session”? Why or why not?

    R5. What information is used by a process running on one host to identify a process running on another host?

    R6. Suppose you wanted to do a transaction from a remote client to a server as fast as possible. Would you use UDP or TCP? Why?

    R7. Referring to :ref:`Figure 2.4 <Figure 2.4>` , we see that none of the applications listed in :ref:`Figure 2.4 <Figure 2.4>` requires both no data loss and timing. Can you conceive of an application that requires no data loss and that is also highly time-sensitive?

    R8. List the four broad classes of services that a transport protocol can provide. For each of the service classes, indicate if either UDP or TCP (or both) provides such a service.

    R9. Recall that TCP can be enhanced with SSL to provide process-to-process security services, including encryption. Does SSL operate at the transport layer or the application layer? If the application developer wants TCP to be enhanced with SSL, what does the developer have to do?

SECTION 2.2–2.5
~~~~~~~~~~~~~~~~

R10. 什么是握手协议？

R11. 为什么 HTTP、SMTP 和 POP3 是运行在 TCP 上而不是 UDP 上？

R12. 考虑一个电子商务网站希望为每个顾客保留购买记录。请描述如何通过 cookie 实现这一点。

R13. 请描述 Web 缓存如何减少获取所请求对象的延迟。Web 缓存是否会减少用户请求的所有对象的延迟，还是仅减少部分对象的延迟？为什么？

R14. Telnet 到一个 Web 服务器并发送一个多行请求消息。在请求消息中包含 **If-modified-since:** 首部行以强制响应消息返回 **304 Not Modified** 状态码。

R15. 列出几个流行的即时通讯应用。它们是否使用与 SMS 相同的协议？

R16. 假设 Alice 使用基于 Web 的电子邮件账户（如 Hotmail 或 Gmail）发送一条消息给 Bob，Bob 使用 POP3 从其邮件服务器中访问邮件。请讨论该消息如何从 Alice 的主机传输到 Bob 的主机。务必列出用于在两台主机之间移动消息的应用层协议序列。

R17. 打印出你最近收到的一封电子邮件的首部。**Received:** 首部行有多少条？请分析该消息中的每一条首部行。

R18. 从用户的角度来看，POP3 中的“下载并删除”模式与“下载并保留”模式有什么区别？

R19. 一个组织的 Web 服务器和邮件服务器是否可能具有完全相同的主机名别名（例如 **foo.com**）？包含邮件服务器主机名的资源记录（RR）应属于哪种类型？

R20. 查看你收到的电子邮件，检查一封来自 .edu 邮件地址用户的邮件首部。是否可以从首部中确定该邮件是从哪台主机发送的（IP 地址）？对一封来自 Gmail 账户的邮件也做同样的分析。

.. toggle::

    R10. What is meant by a handshaking protocol?

    R11. Why do HTTP, SMTP, and POP3 run on top of TCP rather than on UDP?

    R12. Consider an e-commerce site that wants to keep a purchase record for each of its customers. Describe how this can be done with cookies.

    R13. Describe how Web caching can reduce the delay in receiving a requested object. Will Web caching reduce the delay for all objects requested by a user or for only some of the objects? Why?

    R14. Telnet into a Web server and send a multiline request message. Include in the request message the **If-modified-since:** header line to force a response message with the **304 Not Modified** status code.

    R15. List several popular messaging apps. Do they use the same protocols as SMS?

    R16. Suppose Alice, with a Web-based e-mail account (such as Hotmail or Gmail), sends a message to Bob, who accesses his mail from his mail server using POP3. Discuss how the message gets from Alice’s host to Bob’s host. Be sure to list the series of application-layer protocols that are used to move the message between the two hosts.

    R17. Print out the header of an e-mail message you have recently received. How many **Received:** header lines are there? Analyze each of the header lines in the message.

    R18. From a user’s perspective, what is the difference between the download-and-delete mode and the download-and-keep mode in POP3?

    R19. Is it possible for an organization’s Web server and mail server to have exactly the same alias for a hostname (for example, **foo.com**)? What would be the type for the RR that contains the hostname of the mail server?

    R20. Look over your received e-mails, and examine the header of a message sent from a user with a .edu e-mail address. Is it possible to determine from the header the IP address of the host from which the message was sent? Do the same for a message sent from a Gmail account.

SECTION 2.5
~~~~~~~~~~~~~

R21. 在 BitTorrent 中，假设 Alice 在一个 30 秒的时间段内向 Bob 提供了若干数据块。Bob 是否一定会回报 Alice，在同一时间段内向她提供数据块？为什么或为什么不？

R22. 考虑一个新加入 BitTorrent 的对等方 Alice，她初始时没有任何数据块。由于没有块，她无法成为任何其他对等方的前四上传者，因为她没有可上传的内容。那么 Alice 如何获得第一个数据块？

R23. 什么是覆盖网络（overlay network）？它是否包括路由器？覆盖网络中的边指的是什么？

.. toggle::

    R21. In BitTorrent, suppose Alice provides chunks to Bob throughout a 30-second interval. Will Bob necessarily return the favor and provide chunks to Alice in this same interval? Why or why not?

    R22. Consider a new peer Alice that joins BitTorrent without possessing any chunks. Without any chunks, she cannot become a top-four uploader for any of the other peers, since she has nothing to upload. How then will Alice get her first chunk?

    R23. What is an overlay network? Does it include routers? What are the edges in the overlay network?

SECTION 2.6
~~~~~~~~~~~~~

R24. CDN 通常采用两种不同的服务器部署策略之一。请列出并简要描述这两种策略。

R25. 除了延迟、丢包和带宽性能等网络相关的考虑因素外，在设计 CDN 服务器选择策略时还有哪些重要因素？

.. toggle::

    R24. CDNs typically adopt one of two different server placement philosophies. Name and briefly describe them.

    R25. Besides network-related considerations such as delay, loss, and bandwidth performance, there are other important factors that go into designing a CDN server selection strategy. What are they?

SECTION 2.7
~~~~~~~~~~~~~~

R26. 在 :ref:`第 2.7 节 <c2.7>` 中，描述的 UDP 服务器只需要一个套接字，而 TCP 服务器则需要两个套接字。为什么？如果 TCP 服务器要支持 n 个来自不同客户端主机的并发连接，它需要多少个套接字？

R27. 对于 :ref:`第 2.7 节 <c2.7>` 中描述的基于 TCP 的客户端-服务器应用程序，为什么必须先执行服务器程序再执行客户端程序？对于基于 UDP 的客户端-服务器应用程序，为什么客户端程序可以在服务器程序之前执行？

.. toggle::

    R26. In :ref:`Section 2.7 <c2.7>`, the UDP server described needed only one socket, whereas the TCP server
    needed two sockets. Why? If the TCP server were to support n simultaneous connections, each from a different client host, how many sockets would the TCP server need?

    R27. For the client-server application over TCP described in :ref:`Section 2.7 <c2.7>` , why must the server program be executed before the client program? For the client-server application over UDP, why may the client program be executed before the server program?

Problems
~~~~~~~~~~~

P1. 判断正误？

a. 用户请求一个包含一些文本和三张图片的网页。对于这个页面，客户端将发送一个请求消息并接收四个响应消息。
b. 两个不同的网页（例如，www.mit.edu/research.html 和 www.mit.edu/students.html）可以通过同一个持久连接发送。
c. 在浏览器与源服务器之间使用非持久连接时，单个 TCP 段可能携带两个不同的 HTTP 请求消息。
d. HTTP 响应消息中的 **Date:** 头指示响应中对象最后被修改的时间。
e. HTTP 响应消息的消息体永远不会为空。

.. toggle::

    P1. True or false?

    a. A user requests a Web page that consists of some text and three images. For this page, the client will send one request message and receive four response messages.
    b. Two distinct Web pages (for example, www.mit.edu/research.html and www.mit.edu/students.html) can be sent over the same persistent connection.
    c. With nonpersistent connections between browser and origin server, it is possible for a single TCP segment to carry two distinct HTTP request messages.
    d. The **Date:** header in the HTTP response message indicates when the object in the response was last modified.
    e. HTTP response messages never have an empty message body.

P2. SMS、iMessage 和 WhatsApp 都是智能手机实时消息系统。通过在网上做一些调研，为每个系统写一段关于它们使用的协议的介绍。然后写一段说明它们之间的差异。

.. toggle::

    P2. SMS, iMessage, and WhatsApp are all smartphone real-time messaging systems. After doing some research on the Internet, for each of these systems write one paragraph about the protocols they use. Then write a paragraph explaining how they differ.

P3. 考虑一个 HTTP 客户端想要获取给定 URL 的网页。HTTP 服务器的 IP 地址最初未知。在这种情况下，除了 HTTP，还需要哪些传输层和应用层协议？

.. toggle::

    P3. Consider an HTTP client that wants to retrieve a Web document at a given URL. The IP address of the HTTP server is initially unknown. What transport and application-layer protocols besides HTTP are needed in this scenario?

P4. 考虑下面这串 ASCII 字符，是浏览器发送 HTTP GET 消息时被 Wireshark 捕获的（即这是 HTTP GET 消息的实际内容）。字符 <cr><lf> 分别是回车和换行符（下面文本中斜体的 <cr> 表示 HTTP 头中该处包含的单个回车字符）。回答以下问题，并指出你在 HTTP GET 消息中的位置。

.. code:: http

    GET /cs453/index.html HTTP/1.1<cr><lf>Host: gai
    a.cs.umass.edu<cr><lf>User-Agent: Mozilla/5.0 (
    Windows;U; Windows NT 5.1; en-US; rv:1.7.2) Gec
    ko/20040804 Netscape/7.2 (ax) <cr><lf>Accept:ex
    t/xml, application/xml, application/xhtml+xml, text
    /html;q=0.9, text/plain;q=0.8, image/png,*/*;q=0.5
    <cr><lf>Accept-Language: en-us, en;q=0.5<cr><lf>Accept-
    Encoding: zip, deflate<cr><lf>Accept-Charset: ISO
    -8859-1, utf-8;q=0.7,*;q=0.7<cr><lf>Keep-Alive: 300<cr>
    <lf>Connection:keep-alive<cr><lf><cr><lf>

a. 浏览器请求的文档 URL 是什么？
b. 浏览器使用的 HTTP 版本是多少？
c. 浏览器请求的是非持久连接还是持久连接？
d. 浏览器所在主机的 IP 地址是多少？
e. 是哪种类型的浏览器发起了该请求？为什么 HTTP 请求消息中需要浏览器类型？

.. toggle::

    P4. Consider the following string of ASCII characters that were captured by Wireshark when the browser sent an HTTP GET message (i.e., this is the actual content of an HTTP GET message). The characters <cr><lf> are carriage return and line-feed characters (that is, the italized character string <cr> in the text below represents the single carriage-return character that was contained at that point in the HTTP header). Answer the following questions, indicating where in the HTTP GET message below you find the answer.

    .. code:: http

        GET /cs453/index.html HTTP/1.1<cr><lf>Host: gai
        a.cs.umass.edu<cr><lf>User-Agent: Mozilla/5.0 (
        Windows;U; Windows NT 5.1; en-US; rv:1.7.2) Gec
        ko/20040804 Netscape/7.2 (ax) <cr><lf>Accept:ex
        t/xml, application/xml, application/xhtml+xml, text
        /html;q=0.9, text/plain;q=0.8, image/png,*/*;q=0.5
        <cr><lf>Accept-Language: en-us, en;q=0.5<cr><lf>Accept-
        Encoding: zip, deflate<cr><lf>Accept-Charset: ISO
        -8859-1, utf-8;q=0.7,*;q=0.7<cr><lf>Keep-Alive: 300<cr>
        <lf>Connection:keep-alive<cr><lf><cr><lf>

    a. What is the URL of the document requested by the browser?
    b. What version of HTTP is the browser running?
    c. Does the browser request a non-persistent or a persistent connection?
    d. What is the IP address of the host on which the browser is running?
    e. What type of browser initiates this message? Why is the browser type needed in an HTTP request message?

P5. 以下文本是服务器对上述 HTTP GET 消息的响应。回答以下问题，并指出答案在消息中的位置。

.. code:: http

    HTTP/1.1 200 OK<cr><lf>Date: Tue, 07 Mar 2008
    12:39:45GMT<cr><lf>Server: Apache/2.0.52 (Fedora)
    <cr><lf>Last-Modified: Sat, 10 Dec2005 18:27:46
    GMT<cr><lf>ETag: ”526c3-f22-a88a4c80”<cr><lf>Accept-
    Ranges: bytes<cr><lf>Content-Length: 3874<cr><lf>
    Keep-Alive: timeout=max=100<cr><lf>Connection:
    Keep-Alive<cr><lf>Content-Type: text/html; charset=
    ISO-8859-1<cr><lf><cr><lf><!doctype html public ”-
    //w3c//dtd html 4.0 transitional//en”><lf><html><lf>
    <head><lf> <meta http-equiv=”Content-Type”
    content=”text/html; charset=iso-8859-1”><lf> <meta
    name=”GENERATOR” content=”Mozilla/4.79 [en] (Windows NT
    5.0; U) Netscape]”><lf> <title>CMPSCI 453 / 591 /
    NTU-ST550ASpring 2005 homepage</title><lf></head><lf>
    <much more document text following here (not shown)>

a. 服务器是否成功找到该文档？文档回复的时间是什么时候？
b. 文档最后一次修改时间是什么时候？
c. 返回的文档有多少字节？
d. 返回的文档前 5 个字节是什么？服务器是否同意保持持久连接？

.. toggle::

    P5. The text below shows the reply sent from the server in response to the HTTP GET message in the question above. Answer the following questions, indicating where in the message below you find the answer.

    .. code:: http

        HTTP/1.1 200 OK<cr><lf>Date: Tue, 07 Mar 2008
        12:39:45GMT<cr><lf>Server: Apache/2.0.52 (Fedora)
        <cr><lf>Last-Modified: Sat, 10 Dec2005 18:27:46
        GMT<cr><lf>ETag: ”526c3-f22-a88a4c80”<cr><lf>Accept-
        Ranges: bytes<cr><lf>Content-Length: 3874<cr><lf>
        Keep-Alive: timeout=max=100<cr><lf>Connection:
        Keep-Alive<cr><lf>Content-Type: text/html; charset=
        ISO-8859-1<cr><lf><cr><lf><!doctype html public ”-
        //w3c//dtd html 4.0 transitional//en”><lf><html><lf>
        <head><lf> <meta http-equiv=”Content-Type”
        content=”text/html; charset=iso-8859-1”><lf> <meta
        name=”GENERATOR” content=”Mozilla/4.79 [en] (Windows NT
        5.0; U) Netscape]”><lf> <title>CMPSCI 453 / 591 /
        NTU-ST550ASpring 2005 homepage</title><lf></head><lf>
        <much more document text following here (not shown)>

    a. Was the server able to successfully find the document or not? What time was the document reply provided?
    b. When was the document last modified?
    c. How many bytes are there in the document being returned?
    d. What are the first 5 bytes of the document being returned? Did the server agree to a persistent connection?

P6. 获取 HTTP/1.1 规范 (:ref:`RFC 2616 <RFC 2616>`)。回答以下问题：

a. 说明客户端和服务器之间用来表示持久连接关闭的信号机制。关闭连接的信号可以由客户端、服务器还是两者之一发送？
b. HTTP 提供了哪些加密服务？
c. 客户端能否与同一个服务器打开三个或更多同时连接？
d. 如果服务器或客户端检测到连接空闲了一段时间，可能会关闭该连接。是否可能一方开始关闭连接时，另一方仍在通过该连接发送数据？请解释。

.. toggle::

    P6. Obtain the HTTP/1.1 specification (:ref:`RFC 2616 <RFC 2616>`). Answer the following questions:

    a. Explain the mechanism used for signaling between the client and server to indicate that a persistent connection is being closed. Can the client, the server, or both signal the close of a connection?
    b. What encryption services are provided by HTTP?
    c. Can a client open three or more simultaneous connections with a given server?
    d. Either a server or a client may close a transport connection between them if either one detects the connection has been idle for some time. Is it possible that one side starts closing a connection while the other side is transmitting data via this connection? Explain.

P7. 假设你在浏览器中点击链接获取网页。该 URL 的 IP 地址未缓存在本地主机，因此需要 DNS 查询。假设查询过程中访问了 n 个 DNS 服务器，往返时间分别为 RTT1, ..., RTTn。假设网页只包含一个小的 HTML 对象，RTT0 表示本地主机与包含该对象的服务器间的往返时间。假设对象传输时间为零，从点击链接到接收对象共需多少时间？

.. toggle::

    P7. Suppose within your Web browser you click on a link to obtain a Web page. The IP address for the associated URL is not cached in your local host, so a DNS lookup is necessary to obtain the IP address. Suppose that n DNS servers are visited before your host receives the IP address from DNS; the successive visits incur an RTT of RTT1,. . .,RTTn. Further suppose that the Web page associated with the link contains exactly one object, consisting of a small amount of HTML text. Let RTT0 denote the RTT between the local host and the server containing the object. Assuming zero transmission time of the object, how much time elapses from when the client clicks on the link until the client receives the object?

P8. 参考问题 P7，假设 HTML 文件引用了同一服务器上的八个非常小的对象。在忽略传输时间的情况下，分别计算以下情况下的耗时：

a. 非持久 HTTP 且无并行 TCP 连接？
b. 非持久 HTTP 且浏览器配置为 5 个并行连接？
c. 持久 HTTP？

.. toggle::

    P8. Referring to Problem P7, suppose the HTML file references eight very small objects on the same server. Neglecting transmission times, how much time elapses with

    a. Non-persistent HTTP with no parallel TCP connections?
    b. Non-persistent HTTP with the browser configured for 5 parallel connections? 
    c. Persistent HTTP?

P9. 参考 :ref:`图 2.12 <Figure 2.12>`，假设某机构网络连接到互联网。平均对象大小为 850,000 比特，机构浏览器向源服务器的平均请求率为每秒 16 个。假设从访问链路互联网侧路由器转发 HTTP 请求到接收响应的平均时间为 3 秒（见 :ref:`第 2.2.5 节 <c2.2.5>`）。将总平均响应时间建模为平均访问延迟（即互联网路由器到机构路由器的延迟）与平均互联网延迟之和。访问延迟用 Δ/(1-Δβ) 表示，其中 Δ 是访问链路传输一个对象所需的平均时间，β 是对象到达访问链路的速率。

a. 求总平均响应时间。
b. 现在假设机构 LAN 中安装了缓存，缓存未命中率为 0.4。求总响应时间。

.. toggle::

    P9. Consider :ref:`Figure 2.12 <Figure 2.12>` , for which there is an institutional network connected to the Internet. Suppose that the average object size is 850,000 bits and that the average request rate from the institution’s browsers to the origin servers is 16 requests per second. Also suppose that the amount of time it takes from when the router on the Internet side of the access link forwards an HTTP request until it receives the response is three seconds on average (see :ref:`Section 2.2.5 <c2.2.5>`). Model the total average response time as the sum of the average access delay (that is, the delay from Internet router to institution router) and the average Internet delay. For the average access delay, use Δ/(1-Δβ), where Δ is the average time required to send an object over the access link and b is the arrival rate of objects to the access link.

    a. Find the total average response time.
    b. Now suppose a cache is installed in the institutional LAN. Suppose the miss rate is 0.4. Find the total response time.

P10. 考虑一条短链路长 10 米，发送端和接收端双向传输速率均为 150 比特/秒。假设数据包长 100,000 比特，控制包（如 ACK 或握手包）长 200 比特。假设有 N 个并行连接，每个连接占带宽的 1/N。考虑 HTTP 协议，假设每个下载对象长 100 Kbits，且初始下载对象引用了同一发送者的 10 个对象。在这种情况下，通过非持久 HTTP 的多个并行实例进行并行下载是否合理？再考虑持久 HTTP，是否期望相比非持久情况有显著提升？请论证解释。

.. toggle::

    P10. Consider a short, 10-meter link, over which a sender can transmit at a rate of 150 bits/sec in both directions. Suppose that packets containing data are 100,000 bits long, and packets containing only control (e.g., ACK or handshaking) are 200 bits long. Assume that N parallel connections each get 1/N of the link bandwidth. Now consider the HTTP protocol, and suppose that each downloaded object is 100 Kbits long, and that the initial downloaded object contains 10 referenced objects from the same sender. Would parallel downloads via parallel instances of non-persistent HTTP make sense in this case? Now consider persistent HTTP. Do you expect significant gains over the non-persistent case? Justify and explain your answer.

P11. 考虑上题场景，假设该链路由 Bob 与另外四个用户共享。Bob 使用非持久 HTTP 的并行实例，其他四个用户不使用并行下载。

a. Bob 的并行连接能帮助他更快获取网页吗？为什么？
b. 如果五个用户都打开五个非持久 HTTP 并行实例，Bob 的并行连接还会有优势吗？为什么？

.. toggle::

    P11. Consider the scenario introduced in the previous problem. Now suppose that the link is shared by Bob with four other users. Bob uses parallel instances of non-persistent HTTP, and the other four users use non-persistent HTTP without parallel downloads.

    a. Do Bob’s parallel connections help him get Web pages more quickly? Why or why not?
    b. If all five users open five parallel instances of non-persistent HTTP, then would Bob’s parallel connections still be beneficial? Why or why not?

P12. 编写一个简单的 TCP 服务器程序，接受客户端输入的多行内容，并将这些内容打印到服务器的标准输出。（你可以通过修改文本中的 TCPServer.py 程序来实现。）编译并运行你的程序。在另一台有网页浏览器的机器上，将浏览器中的代理服务器设置为运行你服务器程序的主机，并适当配置端口号。此时，浏览器应将 GET 请求消息发送到你的服务器，你的服务器应在标准输出上显示这些消息。利用此平台判断浏览器是否会针对本地缓存的对象生成条件 GET 消息。

.. toggle::

    P12. Write a simple TCP program for a server that accepts lines of input from a client and prints the lines onto the server’s standard output. (You can do this by modifying the TCPServer.py program in the text.) Compile and execute your program. On any other machine that contains a Web browser, set the proxy server in the browser to the host that is running your server program; also configure the port number appropriately. Your browser should now send its GET request messages to your server, and your server should display the messages on its standard output. Use this platform to determine whether your browser generates conditional GET messages for objects that are locally cached.

P13. SMTP 中的 **MAIL FROM:** 与邮件消息本身中的 **From:** 有何区别？

.. toggle::

    P13. What is the difference between **MAIL FROM:** in SMTP and **From:** in the mail message itself?

P14. SMTP 如何标记消息体的结束？HTTP 呢？HTTP 能否使用与 SMTP 相同的方法标记消息体结束？请解释。

.. toggle::

    P14. How does SMTP mark the end of a message body? How about HTTP? Can HTTP use the same method as SMTP to mark the end of a message body? Explain.

P15. 阅读 SMTP 的 RFC 5321。MTA 是什么的缩写？考虑下面收到的一封垃圾邮件（修改自真实垃圾邮件）。假设只有这封垃圾邮件的发起者是恶意的，其他主机均为正常，请找出生成该垃圾邮件的恶意主机。

.. code:: smtp

    From - Fri Nov 07 13:41:30 2008
    Return-Path: <tennis5@pp33head.com>
    Received: from barmail.cs.umass.edu (barmail.cs.umass.edu
    [128.119.240.3]) by cs.umass.edu (8.13.1/8.12.6) for
    <hg@cs.umass.edu>; Fri, 7 Nov 2008 13:27:10 -0500
    Received: from asusus-4b96 (localhost [127.0.0.1]) by
    barmail.cs.umass.edu (Spam Firewall) for <hg@cs.umass.edu>; Fri, 7
    Nov 2008 13:27:07 -0500 (EST)
    Received: from asusus-4b96 ([58.88.21.177]) by barmail.cs.umass.edu
    for <hg@cs.umass.edu>; Fri, 07 Nov 2008 13:27:07 -0500 (EST)
    Received: from [58.88.21.177] by inbnd55.exchangeddd.com; Sat, 8
    Nov 2008 01:27:07 +0700
    From: ”Jonny” <tennis5@pp33head.com>
    To: <hg@cs.umass.edu>

    Subject: How to secure your savings

.. toggle::

    P15. Read RFC 5321 for SMTP. What does MTA stand for? Consider the following received spam e-mail (modified from a real spam e-mail). Assuming only the originator of this spam e-mail is malicious and all other hosts are honest, identify the malacious host that has generated this spam e-mail.

    .. code:: smtp

        From - Fri Nov 07 13:41:30 2008
        Return-Path: <tennis5@pp33head.com>
        Received: from barmail.cs.umass.edu (barmail.cs.umass.edu
        [128.119.240.3]) by cs.umass.edu (8.13.1/8.12.6) for
        <hg@cs.umass.edu>; Fri, 7 Nov 2008 13:27:10 -0500
        Received: from asusus-4b96 (localhost [127.0.0.1]) by
        barmail.cs.umass.edu (Spam Firewall) for <hg@cs.umass.edu>; Fri, 7
        Nov 2008 13:27:07 -0500 (EST)
        Received: from asusus-4b96 ([58.88.21.177]) by barmail.cs.umass.edu
        for <hg@cs.umass.edu>; Fri, 07 Nov 2008 13:27:07 -0500 (EST)
        Received: from [58.88.21.177] by inbnd55.exchangeddd.com; Sat, 8
        Nov 2008 01:27:07 +0700
        From: ”Jonny” <tennis5@pp33head.com>
        To: <hg@cs.umass.edu>

        Subject: How to secure your savings

P16. 阅读 POP3 的 RFC :rfc:`1939`。UIDL POP3 命令的作用是什么？

.. toggle::

    P16. Read the POP3 RFC, :rfc:`1939`. What is the purpose of the UIDL POP3 command? 

P17. 考虑使用 POP3 访问你的电子邮件。

a. 假设你配置了 POP 邮件客户端为下载后删除模式。完成以下交互过程：
   
   .. code:: text 

        C: list 
        S: 1 498 
        S: 2 912
        S: .
        C: retr 1
        S: blah blah ... 
        S: ..........blah
        S: . ?
        ?

b. 假设你配置了 POP 邮件客户端为下载后保留模式。完成以下交互过程：
   
   .. code:: text 

        C: list 
        S: 1 498 
        S: 2 912
        S: .
        C: retr 1
        S: blah blah ... 
        S: ..........blah
        S: . ?
        ?

c. 假设你配置了 POP 邮件客户端为下载后保留模式。基于 (b) 部分的对话，假设你检索了邮件 1 和 2，退出 POP，五分钟后再次访问 POP 以获取新邮件。假设这五分钟内没有新邮件到达。请给出第二次 POP 会话的交互记录。

.. toggle::

    P17. Consider accessing your e-mail with POP3.

    a. Suppose you have configured your POP mail client to operate in the download-and- delete mode. Complete the following transaction:
    
    .. code:: text 

        C: list 
        S: 1 498 
        S: 2 912
        S: .
        C: retr 1
        S: blah blah ... 
        S: ..........blah
        S: . ?
        ?

    b. Suppose you have configured your POP mail client to operate in the download-and-keep mode. Complete the following transaction:
    
    .. code:: text 

        C: list 
        S: 1 498 
        S: 2 912
        S: .
        C: retr 1
        S: blah blah ... 
        S: ..........blah
        S: . ?
        ?

    c. Suppose you have configured your POP mail client to operate in the download-and-keep mode. Using your transcript in part (b), suppose you retrieve messages 1 and 2, exit POP, and then five minutes later you again access POP to retrieve new e-mail. Suppose that in the five-minute interval no new messages have been sent to you. Provide a transcript of this second POP session.

P18.

a. 什么是 whois 数据库？
b. 使用互联网上的多个 whois 数据库，查找两个 DNS 服务器的名称。请注明使用了哪些 whois 数据库。
c. 使用本地主机的 nslookup 工具向三个 DNS 服务器发送查询：本地 DNS 服务器和在 (b) 部分找到的两个 DNS 服务器。尝试查询 Type A、NS 和 MX 记录。总结你的发现。
d. 使用 nslookup 查找一个拥有多个 IP 地址的 Web 服务器。你所在机构（学校或公司）的 Web 服务器是否有多个 IP 地址？
e. 使用 ARIN whois 数据库，确定你所在大学使用的 IP 地址范围。
f. 描述攻击者如何利用 whois 数据库和 nslookup 工具在发动攻击前对机构进行侦察。
g. 讨论为什么 whois 数据库应当公开可用。

.. toggle::

    P18.

    a. What is a whois database?
    b. Use various whois databases on the Internet to obtain the names of two DNS servers. Indicate which whois databases you used.
    c. Use nslookup on your local host to send DNS queries to three DNS servers: your local DNS server and the two DNS servers you found in part (b). Try querying for Type A, NS, and MX reports. Summarize your findings.
    d. Use nslookup to find a Web server that has multiple IP addresses. Does the Web server of your institution (school or company) have multiple IP addresses?
    e. Use the ARIN whois database to determine the IP address range used by your university.
    f. Describe how an attacker can use whois databases and the nslookup tool to perform reconnaissance on an institution before launching an attack.
    g. Discuss why whois databases should be publicly available.

P19. 本题利用 Unix 和 Linux 主机上的有用工具 dig 来探索 DNS 服务器层级结构。回想 :ref:`图 2.19 <c2.19>` 中，DNS 层级结构中的 DNS 服务器通过返回更低层级 DNS 服务器的名称，将查询委派给该服务器。先阅读 dig 的手册页，然后回答：

a. 从根 DNS 服务器（任一根服务器 [a-m].root-servers.net）开始，使用 *dig* 依次查询你所在系的 Web 服务器 IP 地址。展示回答查询时的 DNS 委派链中服务器名称列表。
b. 对 google.com、yahoo.com 或 amazon.com 等多个流行网站重复 (a) 部分。

.. toggle::

    P19. In this problem, we use the useful dig tool available on Unix and Linux hosts to explore the hierarchy of DNS servers. Recall that in :ref:`Figure 2.19 <c2.19>` , a DNS server in the DNS hierarchy delegates a DNS query to a DNS server lower in the hierarchy, by sending back to the DNS client the name of that lower-level DNS server. First read the man page for dig, and then answer the following questions.

    a. Starting with a root DNS server (from one of the root servers [a-m].root-servers.net), initiate a sequence of queries for the IP address for your department’s Web server by using *dig*. Show the list of the names of DNS servers in the delegation chain in answering your query.
    b. Repeat part (a) for several popular Web sites, such as google.com, yahoo.com, or amazon.com.

P20. 假设你能访问部门本地 DNS 服务器中的缓存。你能提出一种方法，大致判断部门用户中哪些外部 Web 服务器最受欢迎吗？请解释。

.. toggle::

    P20. Suppose you can access the caches in the local DNS servers of your department. Can you propose a way to roughly determine the Web servers (outside your department) that are most popular among the users in your department? Explain.

P21. 假设你部门有一台为所有计算机服务的本地 DNS 服务器。你是普通用户（非网络/系统管理员）。你能判断部门中某台计算机几秒前是否访问了某个外部网站吗？请解释。

.. toggle::

    P21. Suppose that your department has a local DNS server for all computers in the department. You are an ordinary user (i.e., not a network/system administrator). Can you determine if an external Web site was likely accessed from a computer in your department a couple of seconds ago? Explain.

P22. 考虑向 N 个对等点分发大小为 F=15 Gbits 的文件。服务器上传速率 us=30 Mbps，每个对等点下载速率 di=2 Mbps，上传速率 u。对于 N=10、100、1000，u=300 Kbps、700 Kbps、2 Mbps，制作表格，列出客户端-服务器分发和 P2P 分发在不同 N 和 u 组合下的最短分发时间。

.. toggle::

    P22. Consider distributing a file of F=15 Gbits to N peers. The server has an upload rate of us=30 Mbps, and each peer has a download rate of di=2 Mbps and an upload rate of u. For N=10, 100, and 1,000 and u=300 Kbps, 700 Kbps, and 2 Mbps, prepare a chart giving the minimum distribution time for each of the combinations of N and u for both client-server distribution and P2P distribution.

P23. 考虑使用客户端-服务器架构向 N 个对等点分发大小为 F 比特的文件。假设流体模型，服务器可同时向多个对等点发送数据，速率可不同，只要总和不超过 us。

a. 若 us/N≤dmin，指定一种分发方案，分发时间为 NF/us。
b. 若 us/N≥dmin，指定一种分发方案，分发时间为 F/dmin。
c. 结论：最短分发时间一般为 max{NF/us, F/dmin}。

.. toggle::

    P23. Consider distributing a file of F bits to N peers using a client-server architecture. Assume a fluid model where the server can simultaneously transmit to multiple peers, transmitting to each peer at different rates, as long as the combined rate does not exceed us.

    a. Suppose that us/N≤dmin. Specify a distribution scheme that has a distribution time of NF/us.
    b. Suppose that us/N≥dmin. Specify a distribution scheme that has a distribution time of F/dmin.
    c. Conclude that the minimum distribution time is in general given by max{NF/us, F/dmin}.

P24. 考虑使用 P2P 架构向 N 个对等点分发大小为 F 比特的文件。假设流体模型。为简化假设 dmin 非常大，故对等点下载带宽永远不是瓶颈。

a. 若 us≤(us+u1+...+uN)/N，指定一种分发方案，分发时间为 F/us。
b. 若 us≥(us+u1+...+uN)/N，指定一种分发方案，分发时间为 NF/(us+u1+...+uN)。
c. 结论：最短分发时间一般为 max{F/us, NF/(us+u1+...+uN)}。

.. toggle::

    P24. Consider distributing a file of F bits to N peers using a P2P architecture. Assume a fluid model. For simplicity assume that dmin is very large, so that peer download bandwidth is never a bottleneck.

    a. Suppose that us≤(us+u1+...+uN)/N. Specify a distribution scheme that has a distribution time of F/us.
    b. Suppose that us≥(us+u1+...+uN)/N. Specify a distribution scheme that has a distribution time of NF/(us+u1+...+uN).
    c. Conclude that the minimum distribution time is in general given by max{F/us, NF/(us+u1+...+uN)}.

P25. 考虑一个有 N 个活动对等点的覆盖网络，每对等点之间都有活动的 TCP 连接。此外，假设 TCP 连接经过总共 M 个路由器。相应的覆盖网络中有多少个节点和边？

.. toggle::

    P25. Consider an overlay network with N active peers, with each pair of peers having an active TCP connection. Additionally, suppose that the TCP connections pass through a total of M routers. How many nodes and edges are there in the corresponding overlay network?

P26. 假设 Bob 加入了一个 BitTorrent 种子，但他不想向其他对等点上传任何数据（即所谓的“搭便车”）。

a. Bob 声称他能收到整个文件副本。这个说法可能吗？为什么？
b. Bob 进一步声称他可以通过使用实验室中多台计算机（不同 IP 地址）使“搭便车”更高效。他如何做到？

.. toggle::

    P26. Suppose Bob joins a BitTorrent torrent, but he does not want to upload any data to any other peers (so called free-riding).

    a. Bob claims that he can receive a complete copy of the file that is shared by the swarm. Is Bob’s claim possible? Why or why not?
    b. Bob further claims that he can further make his “free-riding” more efficient by using a collection of multiple computers (with distinct IP addresses) in the computer lab in his department. How can he do that?

P27. 考虑一个 DASH 系统，有 N 种视频版本（N 个不同的码率和质量）和 N 种音频版本（N 个不同的码率和质量）。假设播放器能随时选择任意一种视频版本和任意一种音频版本。

a. 如果创建的文件将音频混合到视频中，服务器每次只发送一个媒体流，服务器需存储多少个文件（即多少不同 URL）？
b. 如果服务器分别发送音频和视频流，客户端负责同步，服务器需存储多少个文件？

.. toggle::

    P27. Consider a DASH system for which there are N video versions (at N different rates and qualities) and N audio versions (at N different rates and qualities). Suppose we want to allow the player to choose at any time any of the N video versions and any of the N audio versions.

    a. If we create files so that the audio is mixed in with the video, so server sends only one media stream at given time, how many files will the server need to store (each a different URL)?
    b. If the server instead sends the audio and video streams separately and has the client synchronize the streams, how many files will the server need to store? 

P28. 在一台主机上安装并编译 Python 程序 TCPClient 和 UDPClient，在另一台主机上安装并编译 TCPServer 和 UDPServer。

a. 如果先运行 TCPClient，再运行 TCPServer，会发生什么？为什么？
b. 如果先运行 UDPClient，再运行 UDPServer，会发生什么？为什么？
c. 如果客户端和服务器端使用不同端口号，会发生什么？

.. toggle::

    P28. Install and compile the Python programs TCPClient and UDPClient on one host and TCPServer and UDPServer on another host.

    a. Suppose you run TCPClient before you run TCPServer. What happens? Why? 
    b. Suppose you run UDPClient before you run UDPServer. What happens? Why? 
    c. What happens if you use different port numbers for the client and server sides?

P29. 假设在 UDPClient.py 中，创建套接字后添加一行：

.. code::

    clientSocket.bind(('', 5432))

这会使得 UDPServer.py 需要更改吗？UDPClient 和 UDPServer 的套接字端口号各是多少？修改前端口号是多少？

.. toggle::

    P29. Suppose that in UDPClient.py, after we create the socket, we add the line:

    .. code::

        clientSocket.bind(('', 5432))

    Will it become necessary to change UDPServer.py? What are the port numbers for the sockets in UDPClient and UDPServer? What were they before making this change?

P30. 你能配置浏览器打开与某个网站的多个同时连接吗？大量同时 TCP 连接有什么优点和缺点？

.. toggle::

    P30. Can you configure your browser to open multiple simultaneous connections to a Web site? What are the advantages and disadvantages of having a large number of simultaneous TCP connections?

P31. 我们见过 Internet TCP 套接字把发送的数据视为字节流，而 UDP 套接字识别消息边界。字节流 API 相较于显式识别并保留应用定义的消息边界的 API，有什么优点和缺点？

.. toggle::

    P31. We have seen that Internet TCP sockets treat the data being sent as a byte stream but UDP sockets recognize message boundaries. What are one advantage and one disadvantage of byte-oriented API versus having the API explicitly recognize and preserve application-defined message boundaries?

P32. 什么是 Apache Web 服务器？它的成本是多少？它目前具有什么功能？你可以查阅维基百科回答此问题。

.. toggle::

    P32. What is the Apache Web server? How much does it cost? What functionality does it currently have? You may want to look at Wikipedia to answer this question.