Socket 编程作业
=================================
Socket Programming Assignments

配套网站包含六个套接字编程作业。前四个作业在下面进行了总结。第五个作业使用 ICMP 协议，摘要见 :ref:`第 5 章 <c5>` 结尾。第六个作业涉及多媒体协议，摘要见 :ref:`第 9 章 <c9>` 结尾。强烈建议学生完成其中的几个作业，甚至全部完成。学生可以在网站 `www.pearsonhighered.com/cs-resources <http://www.pearsonhighered.com/cs-resources>`_ 上找到这些作业的完整细节，以及一些关键的 Python 代码片段。

.. toggle::

    The Companion Website includes six socket programming assignments. The first four assignments are summarized below. The fifth assignment makes use of the ICMP protocol and is summarized at the end of :ref:`Chapter 5 <c5>`. The sixth assignment employs multimedia protocols and is summarized at the end of :ref:`Chapter 9 <c9>` . It is highly recommended that students complete several, if not all, of these assignments. Students can find full details of these assignments, as well as important snippets of the Python code, at the Web site `www.pearsonhighered.com/cs-resources <http://www.pearsonhighered.com/cs-resources>`_.

Assignment 1: Web Server
-------------------------

在这个作业中，你将用 Python 开发一个简单的 Web 服务器，它只能处理一个请求。具体而言，你的 Web 服务器将：（i）当客户端（浏览器）联系它时，创建一个连接套接字；（ii）通过该连接接收 HTTP 请求；（iii）解析该请求以确定被请求的具体文件；（iv）从服务器文件系统中获取所请求的文件；（v）创建一个包含所请求文件和头部行的 HTTP 响应消息；（vi）通过 TCP 连接将响应发送给请求的浏览器。如果浏览器请求了一个在服务器中不存在的文件，你的服务器应该返回一个“404 Not Found”错误消息。

在配套网站中，我们提供了服务器的框架代码。你的任务是完成代码，运行你的服务器，然后通过运行在不同主机上的浏览器发送请求来测试你的服务器。如果你在一台已运行 Web 服务器的主机上运行你的服务器，那么你应该为你的 Web 服务器使用一个不同于端口 80 的端口。

.. toggle::

    In this assignment, you will develop a simple Web server in Python that is capable of processing only one request. Specifically, your Web server will (i) create a connection socket when contacted by a client (browser); (ii) receive the HTTP request from this connection; (iii) parse the request to determine the specific file being requested; (iv) get the requested file from the server’s file system; (v) create an HTTP response message consisting of the requested file preceded by header lines; and (vi) send the response over the TCP connection to the requesting browser. If a browser requests a file that is not present in your server, your server should return a “404 Not Found” error message.

    In the Companion Website, we provide the skeleton code for your server. Your job is to complete the code, run your server, and then test your server by sending requests from browsers running on different hosts. If you run your server on a host that already has a Web server running on it, then you should use a different port than port 80 for your Web server.


Assignment 2: UDP Pinger
---------------------------

在这个编程作业中，你将用 Python 编写一个客户端 ping 程序。你的客户端将向服务器发送一个简单的 ping 消息，从服务器接收一个对应的 pong 消息，并确定客户端发送 ping 消息与接收到 pong 消息之间的延迟。这个延迟称为往返时间（Round Trip Time, RTT）。客户端和服务器所提供的功能类似于现代操作系统中标准的 ping 程序。然而，标准的 ping 程序使用的是互联网控制消息协议（ICMP）（我们将在 :ref:`第 5 章 <c5>` 中学习）。这里我们将创建一个非标准（但简单！）的基于 UDP 的 ping 程序。

你的 ping 程序将向目标服务器发送 10 个 ping 消息，每个消息都通过 UDP 发送。对于每个消息，当返回相应的 pong 消息时，客户端应确定并打印 RTT。由于 UDP 是不可靠的协议，客户端或服务器发送的分组可能会丢失。因此，客户端不能无限期地等待 ping 消息的回复。你应让客户端最多等待一秒钟来接收服务器的回复；如果没有收到回复，客户端应假设该分组丢失，并打印相应消息。

在这个作业中，你将获得服务器的完整代码（在配套网站上提供）。你的任务是编写客户端代码，该代码与服务器代码非常相似。建议你首先仔细研究服务器代码，然后编写客户端代码，在其中自由剪切粘贴服务器代码中的行。

.. toggle::

    In this programming assignment, you will write a client ping program in Python. Your client will send a simple ping message to a server, receive a corresponding pong message back from the server, and determine the delay between when the client sent the ping message and received the pong message. This delay is called the Round Trip Time (RTT). The functionality provided by the client and server is similar to the functionality provided by standard ping program available in modern operating systems. However, standard ping programs use the Internet Control Message Protocol (ICMP) (which we will
    study in :ref:`Chapter 5 <c5>`). Here we will create a nonstandard (but simple!) UDP-based ping program.

    Your ping program is to send 10 ping messages to the target server over UDP. For each message, your client is to determine and print the RTT when the corresponding pong message is returned. Because UDP is an unreliable protocol, a packet sent by the client or server may be lost. For this reason, the client cannot wait indefinitely for a reply to a ping message. You should have the client wait up to one second for a reply from the server; if no reply is received, the client should assume that the packet was lost and print a message accordingly.

    In this assignment, you will be given the complete code for the server (available in the Companion Website). Your job is to write the client code, which will be very similar to the server code. It is recommended that you first study carefully the server code. You can then write your client code, liberally cutting and pasting lines from the server code.

Assignment 3: Mail Client
---------------------------

本编程作业的目标是创建一个简单的邮件客户端，它能够向任何收件人发送电子邮件。你的客户端需要与一个邮件服务器（例如 Google 的邮件服务器）建立一个 TCP 连接，使用 SMTP 协议与邮件服务器进行对话，通过邮件服务器向收件人（例如你的朋友）发送电子邮件，最后关闭与邮件服务器的 TCP 连接。

对于这个作业，配套网站提供了客户端的框架代码。你的任务是完成该代码，并通过向不同的用户账户发送邮件来测试你的客户端。你还可以尝试通过不同的服务器（例如，通过 Google 的邮件服务器或你所在大学的邮件服务器）发送邮件。

.. toggle::

    The goal of this programming assignment is to create a simple mail client that sends e-mail to any recipient. Your client will need to establish a TCP connection with a mail server (e.g., a Google mail server), dialogue with the mail server using the SMTP protocol, send an e-mail message to a recipient (e.g., your friend) via the mail server, and finally close the TCP connection with the mail server.

    For this assignment, the Companion Website provides the skeleton code for your client. Your job is to complete the code and test your client by sending e-mail to different user accounts. You may also try sending through different servers (for example, through a Google mail server and through your university mail server).

Assignment 4: Multi-Threaded Web Proxy
----------------------------------------

在这个作业中，你将开发一个 Web 代理。当你的代理从浏览器接收到一个对象的 HTTP 请求时，它会生成一个对该对象的新 HTTP 请求并将其发送到源服务器。当代理从源服务器接收到包含该对象的 HTTP 响应时，它会创建一个新的 HTTP 响应（包括该对象），并将其发送给客户端。该代理将是多线程的，因此它能够同时处理多个请求。

对于这个作业，配套网站提供了代理服务器的框架代码。你的任务是完成该代码，然后通过让不同的浏览器通过你的代理请求 Web 对象来测试它。

.. toggle::

    In this assignment, you will develop a Web proxy. When your proxy receives an HTTP request for an object from a browser, it generates a new HTTP request for the same object and sends it to the origin server. When the proxy receives the corresponding HTTP response with the object from the origin server, it creates a new HTTP response, including the object, and sends it to the client. This proxy will be multi-threaded, so that it will be able to handle multiple requests at the same time.

    For this assignment, the Companion Website provides the skeleton code for the proxy server. Your job is to complete the code, and then test it by having different browsers request Web objects via your proxy.
