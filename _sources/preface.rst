前言
===========

Preface

欢迎阅读第七版《计算机网络：自上而下的方法》。自 16 年前第一版出版以来，我们的书已被数百所学院和大学采用，被翻译成 14 种语言，并被全球超过 10 万名学生和从业者使用。我们听到了其中许多读者的来信，并被积极的回应所震撼。

.. toggle::

   Welcome to the seventh edition of Computer Networking: A Top-Down Approach. Since the publication of the first edition 16 years ago, our book has been adopted for use at many hundreds of colleges and universities, translated into 14 languages, and used by over one hundred thousand students and practitioners worldwide. We’ve heard from many of these readers and have been overwhelmed by the ­positive ­response.

第七版有什么新内容？
---------------------------

What’s New in the Seventh Edition?

我们认为本书之所以取得成功，其中一个重要原因在于它持续提供了一种新颖而及时的计算机网络教学方法。在第七版中我们做出了一些改动，但我们也保留了本书最重要的一些方面——我们相信这些方面是最关键的，使用本书的教师和学生也证实了这一点：即采用自顶向下的方法、聚焦于互联网与现代计算机网络的处理方式、同时关注原理与实践，以及本书在学习计算机网络时所采用的通俗易懂的风格与方法。尽管如此，第七版依然进行了大幅修订与更新。

长期阅读本书的读者会注意到，自本书出版以来，我们首次调整了章节的组织结构。网络层原本只在一章中讲解，现在被拆分为 :ref:`第 4 章 <c4>` （专注于网络层中的“数据平面”组件）和 :ref:`第 5 章 <c5>` （专注于网络层的“控制平面”）。这一网络层内容的扩展反映了软件定义网络（SDN）这一数十年来网络领域最重要、最令人兴奋的进展的重要性迅速上升。虽然 SDN 是一种相对较新的创新，但它已迅速被实践界采用——以至于现在很难想象一本关于现代计算机网络的教材不涵盖 SDN。此前在 :ref:`第 9 章 <c9>` 中讲解的网络管理内容现在被合并到了新的 :ref:`第 5 章 <c5>` 中。和以往一样，我们还更新了本书许多其他章节，以反映自第六版以来网络领域的最新变化。和以往一样，从纸质书中移除的内容可以在本书的配套网站（Companion Website）中找到。最重要的更新包括：

.. toggle::

    We think one important reason for this success has been that our book continues to offer a fresh and timely
    approach to computer networking instruction. We’ve made changes in this seventh edition, but we’ve also kept
    unchanged what we believe (and the instructors and students who have used our book have confirmed) to be
    the most important aspects of this book: its top-down approach, its focus on the Internet and a modern
    treatment of computer networking, its attention to both principles and practice, and its accessible style and
    approach toward learning about computer networking. Nevertheless, the seventh edition has been revised and
    updated substantially.

    Long-time readers of our book will notice that for the first time since this text was published, we’ve changed the
    organization of the chapters themselves. The network layer, which had been previously covered in a single
    chapter, is now covered in :ref:`Chapter 4 <c4>` (which focuses on the so-called “data plane” component of the network
    layer) and :ref:`Chapter 5 <c5>` (which focuses on the network layer’s “control plane”). This expanded coverage of the
    network layer reflects the swift rise in importance of software-defined networking (SDN), arguably the most
    important and exciting advance in networking in decades. Although a relatively recent innovation, SDN has
    been rapidly adopted in practice—so much so that it’s already hard to imagine an introduction to modern
    computer networking that doesn’t cover SDN. The topic of network management, previously covered in
    :ref:`Chapter 9 <c9>`, has now been folded into the new :ref:`Chapter 5 <c5>`. As always, we’ve also updated many other sections
    of the text to reflect recent changes in the dynamic field of networking since the sixth edition. As always,
    material that has been retired from the printed text can always be found on this book’s Companion Website.
    The most important updates are the following:

- :ref:`第 1 章 <c1>` 更新了对互联网不断扩展的覆盖范围和使用情况的描述。
- :ref:`第 2 章 <c2>` （应用层）进行了重大更新。我们移除了有关 FTP 协议和分布式哈希表的内容，为新增的应用层视频流与内容分发网络（包括 Netflix 和 YouTube 的案例研究）部分让路。套接字编程内容也从 Python 2 更新为 Python 3。
- :ref:`第 3 章 <c3>` （传输层）进行了适度更新。关于异步传输模式（ATM）网络的内容已被关于互联网显式拥塞通知（ECN）的更现代材料所取代，两者都用于讲授相同的原理。
- :ref:`第 4 章 <c4>` 讲解了网络层的“数据平面”组件——即每个路由器中决定数据包从输入链路转发到哪个输出链路的转发功能。我们更新了以往版本中传统互联网转发的内容，并新增了关于数据包调度的内容。我们还新增了一个关于 SDN 实践中使用的通用转发（generalized forwarding）部分。本章还在多处进行了更新。组播和广播通信的内容被移除，为新内容腾出空间。
- 在 :ref:`第 5 章 <c5>` 中，我们介绍了网络层的控制平面功能——即控制数据报从源主机到目标主机通过一系列路由器路径的全网逻辑。与前几版一样，我们介绍了路由算法以及当今互联网中使用的路由协议（并更新了 BGP 的讲解）。我们新增了一个重要部分，讲述 SDN 控制平面，在该平面中路由及其他功能由所谓的 SDN 控制器来实现。
- :ref:`第 6 章 <c6>` （现为链路层）更新了以太网和数据中心网络的内容。
- :ref:`第 7 章 <c7>` （无线与移动网络）更新了对 802.11（即“WiFi”）网络和蜂窝网络（包括 4G 和 LTE）的内容。
- :ref:`第 8 章 <c8>` （网络安全）在第六版中已进行了全面更新，在第七版中只进行了适度更新。
- :ref:`第 9 章 <c9>` （多媒体网络）相比第六版略微“变薄”，因为关于视频流和内容分发网络的内容已移至 :ref:`第 2 章 <c2>`，而关于数据包调度的内容已并入 :ref:`第 4 章 <c4>`。
- 我们新增了大量章节末尾的习题内容。与所有以往版本一样，习题也进行了修订、添加和删除。

.. toggle::

   - :ref:`Chapter 1 <c1>` has been updated to reflect the ever-growing reach and use of the ­Internet.
   - :ref:`Chapter 2 <c2>`, which covers the application layer, has been significantly updated. We’ve removed the material on the FTP protocol and distributed hash tables to make room for a new section on application-level video streaming and ­content distribution networks, together with Netflix and YouTube case studies. The socket programming sections have been updated from Python 2 to Python 3.
   - :ref:`Chapter 3 <c3>`, which covers the transport layer, has been modestly updated. The ­material on asynchronous transport mode (ATM) networks has been replaced by more modern material on the Internet’s explicit congestion notification (ECN), which teaches the same principles.
   - :ref:`Chapter 4 <c4>` covers the “data plane” component of the network layer—the per-router forwarding function that determine how a packet arriving on one of a router’s input links is forwarded to one of that router’s output links. We updated the material on traditional Internet forwarding found in all previous editions, and added material on packet scheduling. We’ve also added a new section on generalized forwarding, as practiced in SDN. There are also numerous updates throughout the chapter. Material on multicast and broadcast communication has been removed to make way for the new material.
   - In :ref:`Chapter 5 <c5>`, we cover the control plane functions of the network layer—the ­network-wide logic that controls how a datagram is routed along an end-to-end path of routers from the source host to the destination host. As in previous ­editions, we cover routing algorithms, as well as routing protocols (with an updated treatment of BGP) used in today’s Internet. We’ve added a significant new section on the SDN control plane, where routing and other functions are implemented in so-called SDN controllers.
   - :ref:`Chapter 6 <c6>`, which now covers the link layer, has an updated treatment of Ethernet, and of data center networking.
   - :ref:`Chapter 7 <c7>`, which covers wireless and mobile networking, contains updated ­material on 802.11 (so-called “WiFi) networks and cellular networks, including 4G and LTE.
   - :ref:`Chapter 8 <c8>`, which covers network security and was extensively updated in the sixth edition, has only modest updates in this seventh edition.
   - :ref:`Chapter 9 <c9>`, on multimedia networking, is now slightly “thinner” than in the sixth edition, as material on video streaming and content distribution networks has been moved to :ref:`Chapter 2 <c2>`, and material on packet scheduling has been incorporated into :ref:`Chapter 4 <c4>`.
   - Significant new material involving end-of-chapter problems has been added. As with all previous editions, homework problems have been revised, added, and removed.

一如既往，我们编写本书新版的目标，是继续提供一个聚焦而现代的计算机网络教材，强调原理与实践并重。

.. toggle::

    As always, our aim in creating this new edition of our book is to continue to provide a focused and modern treatment of computer networking, emphasizing both principles and practice.


受众
----------------

Audience

本教材面向计算机网络的初级课程。可供计算机科学系和电子工程系使用。在编程语言方面，本书仅假设学生具备 C、C++、Java 或 Python 的编程经验（即便如此，仅在少数几个地方需要）。虽然本书在精确性和分析性方面优于许多其他计算机网络入门教材，但几乎不使用高中未教授的数学概念。我们有意避免使用高等微积分、概率或随机过程等高级数学概念（尽管我们为具备此类背景的学生提供了一些相关习题）。因此，本书适用于本科课程和一年级研究生课程，同时也适合电信行业的从业者参考使用。

.. toggle::

    This textbook is for a first course on computer networking. It can be used in both computer science and
    electrical engineering departments. In terms of programming languages, the book assumes only that the
    student has experience with C, C++, Java, or Python (and even then only in a few places). Although this book
    is more precise and analytical than many other introductory computer networking texts, it rarely uses any
    mathematical concepts that are not taught in high school. We have made a deliberate effort to avoid using any
    advanced calculus, probability, or stochastic process concepts (although we’ve included some homework
    problems for students with this advanced background). The book is therefore appropriate for undergraduate
    courses and for first-year graduate courses. It should also be useful to practitioners in the telecommunications
    industry.

本教材有何独特之处？
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

What Is Unique About This Textbook?

计算机网络是一个极其复杂的领域，涉及大量彼此交织的概念、协议和技术。为了应对如此广泛而复杂的内容，许多计算机网络教材通常采用“分层”网络体系结构的组织方式。通过这种分层结构，学生可以透过复杂的计算机网络，理解体系结构中每一部分的具体概念与协议，同时把握整体架构的运行方式。从教学法的角度来看，我们的亲身经验表明这种分层方法确实有效。然而，我们发现传统自底向上的教学方法——即从物理层讲起，一步步讲到应用层——并非现代计算机网络课程的最佳选择。

.. toggle::

    The subject of computer networking is enormously complex, involving many concepts, protocols, and
    technologies that are woven together in an intricate manner. To cope with this scope and complexity, many
    computer networking texts are often organized around the “layers” of a network architecture. With a layered
    organization, students can see through the complexity of computer networking—they learn about the distinct
    concepts and protocols in one part of the architecture while seeing the big picture of how all parts fit together.
    From a pedagogical perspective, our personal experience has been that such a layered approach indeed
    works well. Nevertheless, we have found that the traditional approach of teaching—bottom up; that is, from the
    physical layer towards the application layer—is not the best approach for a modern course on computer
    networking.

    

自顶向下的方法
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A Top-Down Approach

我们的教材在 16 年前首次提出了“自顶向下”的网络教学方法——也就是从应用层讲起，然后逐步深入到底层的物理层。从教师和学生那里获得的反馈证明，这种自顶向下的方法具有诸多优势，在教学上也确实行之有效。首先，它强调了应用层（网络中的“高增长区”）。事实上，许多近年来计算机网络的重大变革——包括 Web、点对点文件共享和媒体流服务——都发生在应用层。课程早期强调应用层问题，与其他教材形成鲜明对比，后者通常只对网络应用、其需求、应用层范式（如客户端-服务器和点对点）以及应用编程接口做简单介绍。

其次，我们和许多使用本教材的教师都有这样的经验：在课程开始时教授网络应用是一种极具激励作用的教学策略。学生对学习电子邮件和 Web 等日常使用的网络应用工作原理感到非常兴奋。一旦学生理解了这些应用，就能进一步理解支持这些应用所需的网络服务，从而再进一步理解这些服务在底层如何实现。因此，早期介绍应用为后续学习提供了强有力的动机。

第三，自顶向下的方法使教师可以在课程早期引入网络应用开发。学生不仅可以了解流行应用与协议的工作方式，还能学习如何轻松创建自己的网络应用和应用层协议。通过自顶向下的方式，学生能较早接触套接字编程、服务模型和协议这些在后续各层都会再次出现的重要概念。我们采用 Python 提供套接字编程示例，突出核心思想，避免复杂代码带来的困扰。电子工程和计算机科学的本科生应能轻松理解这些 Python 示例。

.. toggle::

    Our book broke new ground 16 years ago by treating networking in a top-down ­manner—that is, by
    beginning at the application layer and working its way down toward the physical layer. The feedback we
    received from teachers and students alike have confirmed that this top-down approach has many advantages
    and does indeed work well pedagogically. First, it places emphasis on the application layer (a “high growth
    area” in networking). Indeed, many of the recent revolutions in ­computer networking—including the Web,
    peer-to-peer file sharing, and media streaming—have taken place at the application layer. An early emphasis
    on application-layer issues differs from the approaches taken in most other texts, which have only a small
    amount of material on network applications, their requirements, application-layer paradigms (e.g., client-server
    and peer-to-peer), and application programming ­interfaces. ­Second, our experience as instructors (and that
    of many instructors who have used this text) has been that teaching networking applications near the
    beginning of the course is a powerful motivational tool. Students are thrilled to learn about how networking
    applications work—applications such as e-mail and the Web, which most students use on a daily basis. Once
    a student understands the applications, the student can then understand the network services needed to
    support these applications. The student can then, in turn, examine the various ways in which such services
    might be provided and implemented in the lower layers. Covering applications early thus provides motivation
    for the remainder of the text.

    Third, a top-down approach enables instructors to introduce network application development at an early
    stage. Students not only see how popular applications and protocols work, but also learn how easy it is to
    create their own network ­applications and application-level protocols. With the top-down approach, students
    get early ­exposure to the notions of socket programming, service models, and ­protocols—important
    concepts that resurface in all subsequent layers. By providing socket programming examples in Python, we
    highlight the central ideas without confusing students with complex code. Undergraduates in electrical
    engineering and computer science should not have difficulty following the Python code.

聚焦互联网
------------------------

An Internet Focus

尽管从第四版开始我们在书名中去掉了 “Featuring the Internet” 的字样，但这并不意味着我们不再聚焦互联网。事实上，情况恰恰相反！正因为互联网已变得如此普遍，我们认为任何网络教材都必须以互联网为重要内容，因此这一短语已显得多余。我们仍然以互联网的体系结构和协议为研究计算机网络基本概念的主要载体。当然，我们也涵盖了其他网络体系结构中的概念和协议。但书中的重点显然放在互联网上，这一点体现在我们以互联网的五层体系结构组织全书：应用层、传输层、网络层、链路层和物理层。

聚焦互联网的另一个好处是，大多数计算机科学和电子工程专业的学生都渴望了解互联网及其协议。他们知道互联网是一项革命性和颠覆性的技术，也看到了它对世界的深远影响。鉴于互联网的重要性，学生自然会对其内部运作机制产生浓厚兴趣。因此，教师借助互联网作为核心引导学生学习基本原理时，往往能轻松激发学生的学习热情。

.. toggle::

    Although we dropped the phrase “Featuring the Internet” from the title of this book with the fourth edition, this
    doesn’t mean that we dropped our focus on the Internet. Indeed, nothing could be further from the case!
    Instead, since the Internet has become so pervasive, we felt that any networking textbook must have a
    significant focus on the Internet, and thus this phrase was somewhat unnecessary. We continue to use the
    Internet’s architecture and protocols as primary vehicles for studying fundamental computer networking
    concepts. Of course, we also include concepts and protocols from other network architectures. But the
    spotlight is clearly on the Internet, a fact reflected in our organizing the book around the Internet’s five-layer
    architecture: the application, transport, network, link, and physical layers.

    Another benefit of spotlighting the Internet is that most computer science and electrical engineering students
    are eager to learn about the Internet and its protocols. They know that the Internet has been a revolutionary
    and disruptive technology and can see that it is profoundly changing our world. Given the enormous relevance
    of the Internet, students are naturally curious about what is “under the hood.” Thus, it is easy for an instructor
    to get students excited about basic principles when using the Internet as the guiding focus.

教授网络原理
--------------------------------

Teaching Networking Principles

本书的两个独特特征——自顶向下的方法与聚焦互联网——都已体现在我们的书名中。如果我们能在副标题中再加上一个词，那将是“原理”（principles）。网络领域如今已经足够成熟，能够识别出一系列基本重要的问题。例如，在传输层，基本问题包括：如何在不可靠的网络层上实现可靠通信，如何建立与终止连接以及握手过程，拥塞与流量控制，以及多路复用。网络层的三个基本问题是：如何确定两台路由器之间的“优良”路径，如何互连大量异构网络，以及如何管理现代网络的复杂性。在链路层，基本问题是如何共享多路接入信道。而在网络安全中，保障机密性、认证与消息完整性的技术均基于密码学原理。

本书识别了这些基本网络问题，并研究了解决这些问题的方法。学习这些原理的学生，将获得“长保质期”的知识——即使今天的网络标准与协议在未来被淘汰，这些原理仍将保持其重要性和相关性。我们相信，以互联网为切入点，再辅以对基本问题及其解决方法的深入讲解，能够使学生快速理解几乎所有网络技术。

.. toggle::

    Two of the unique features of the book—its top-down approach and its focus on the Internet—have appeared
    in the titles of our book. If we could have squeezed a third phrase into the subtitle, it would have contained the
    word principles. The field of networking is now mature enough that a number of fundamentally important issues
    can be identified. For example, in the transport layer, the fundamental issues include reliable communication
    over an unreliable network layer, connection establishment/ teardown and handshaking, congestion and flow
    control, and multiplexing. Three fundamentally important network-layer issues are determining “good” paths
    between two routers, interconnecting a large number of heterogeneous networks, and managing the
    complexity of a modern network. In the link layer, a fundamental problem is sharing a multiple access channel.
    In network security, techniques for providing confidentiality, authentication, and message integrity are all based
    on cryptographic fundamentals. This text identifies fundamental networking issues and studies approaches
    towards addressing these issues. The student learning these principles will gain knowledge with a long “shelf
    life”—long after today’s network standards and protocols have become obsolete, the principles they embody
    will remain important and relevant. We believe that the combination of using the Internet to get the student’s
    foot in the door and then emphasizing fundamental issues and solution approaches will allow the student to 
    quickly understand just about any networking technology.




网站资源
------------------

The Website

每本新书均附带十二个月的配套网站访问权限，网址为 http://www.pearsonhighered.com/cs-resources/，该网站为所有读者提供以下内容：

.. admonition:: 译注

   第七版的资源，请访问: https://media.pearsoncmg.com/aw/ecs_kurose_compnetwork_7/cw/

   在线动画例子: https://media.pearsoncmg.com/aw/ecs_kurose_compnetwork_7/cw/#interactiveanimations

- **交互式学习资料。** 本书的配套网站包含 VideoNotes ——由作者讲解的全书重点主题的视频演示，以及章节末类似问题的解题演示。我们已在网站上预置了第 1 至第 5 章的 VideoNotes 和在线习题，并将持续增加和更新这些内容。如同前几版，网站中也包含多个用 Java 小程序展示的关键网络概念动画。此外，网站提供交互式测验，帮助学生检验基本理解程度。教师可将这些交互内容融入课堂讲解，或作为小型实验使用。
- **补充技术资料。** 由于每版都会新增内容，我们不得不移除部分旧内容以控制篇幅。例如，为了给本版新增内容让位，我们删除了关于 FTP、分布式哈希表和组播的部分。这些出现在早期版本的内容依然有价值，因此可在本书网站上找到。
- **编程作业。** 网站提供多项详细的编程作业，包括构建多线程 Web 服务器、带图形界面的电子邮件客户端、可靠数据传输协议的发送端与接收端编程、分布式路由算法实现等。
- **Wireshark 实验。** 实际观察协议运行过程能极大加深对网络协议的理解。网站提供大量 Wireshark 作业，学生可通过这些作业观察两个协议实体之间的消息交互过程。网站涵盖了 HTTP、DNS、TCP、UDP、IP、ICMP、以太网、ARP、WiFi、SSL 及获取网页请求中涉及的所有协议的独立实验。我们会持续新增实验内容。

除了配套网站外，作者还维护一个公开网站 http://gaia.cs.umass.edu/kurose_ross/interactive，提供交互式习题，涵盖与章节末问题类似的问题并提供解答。学生可生成无限多的类似问题及其答案，帮助他们真正掌握相关内容。

.. toggle::

    Each new copy of this textbook includes twelve months of access to a Companion ­Website for all book
    readers at http://www.pearsonhighered.com/cs-resources/, which includes:

    - **Interactive learning material.** The book’s Companion Website contains ­VideoNotes—video presentations of important topics throughout the book done by the authors, as well as walkthroughs of solutions to problems similar to those at the end of the chapter. We’ve seeded the Web site with VideoNotes and ­online problems for Chapters 1 through 5 and will continue to actively add and update this material over time. As in earlier editions, the Web site contains the interactive Java applets that animate many key networking concepts. The site also has interactive quizzes that permit students to check their basic understanding of the subject matter. Professors can integrate these interactive features into their lectures or use them as mini labs.
    - **Additional technical material.** As we have added new material in each edition of our book, we’ve had to remove coverage of some existing topics to keep the book at manageable length. For example, to make room for the new ­material in this ­edition, we’ve removed material on FTP, distributed hash tables, and multicasting, Material that appeared in earlier editions of the text is still of ­interest, and thus can be found on the book’s Web site.
    - **Programming assignments.** The Web site also provides a number of detailed programming assignments, which include building a multithreaded Web ­server, building an e-mail client with a GUI interface, programming the sender and ­receiver sides of a reliable data transport protocol, programming a distributed routing algorithm, and more.
    - **Wireshark labs.** One’s understanding of network protocols can be greatly ­deepened by seeing them in action. The Web site provides numerous Wireshark assignments that enable students to actually observe the sequence of messages exchanged between two protocol entities. The Web site includes separate Wireshark labs on HTTP, DNS, TCP, UDP, IP, ICMP, Ethernet, ARP, WiFi, SSL, and on tracing all protocols involved in satisfying a request to fetch a Web page. We’ll continue to add new labs over time.

    In addition to the Companion Website, the authors maintain a public Web site,
    http://gaia.cs.umass.edu/kurose_ross/interactive, containing interactive exercises that create (and present
    solutions for) problems similar to selected end-of-chapter problems. Since students can generate (and view
    solutions for) an unlimited number of similar problem instances, they can work until the material is truly
    mastered.

教学特色
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pedagogical Features

我们每人都有超过 30 年的计算机网络教学经验，合计超过 60 年，在此期间我们教授了成千上万名学生。同时我们也一直从事计算机网络研究。（事实上，Jim 和 Keith 最早在 1979 年于哥伦比亚大学 Mischa Schwartz 的网络课程上相识，当时两人都是硕士生。）我们相信这些经历赋予了我们良好的视角来看待网络领域的历史与未来发展方向。

尽管如此，我们仍努力避免将本书内容偏向我们自己的研究兴趣。若您对我们的研究感兴趣，可访问我们的个人网站。本书内容聚焦于现代计算机网络，讲述当代协议与技术，以及支撑它们的原理。我们也认为学习（和教授）网络是件有趣的事。本书通过幽默表达、类比及现实案例，使学习过程更轻松有趣。

.. toggle::

    We have each been teaching computer networking for more than 30 years. Together, we bring more than 60
    years of teaching experience to this text, during which time we have taught many thousands of students. We
    have also been active researchers in computer networking during this time. (In fact, Jim and Keith first met
    each other as master’s students in a computer networking course taught by Mischa Schwartz in 1979 at
    Columbia University.) We think all this gives us a good perspective on where networking has been and where
    it is likely to go in the future. Nevertheless, we have resisted temptations to bias the material in this book
    towards our own pet research projects. We figure you can visit our personal Web sites if you are interested in
    our research. Thus, this book is about modern computer networking—it is about contemporary protocols and
    technologies as well as the underlying principles behind these protocols and technologies. We also believe
    that learning (and teaching!) about networking can be fun. A sense of humor, use of analogies, and real-world
    examples in this book will hopefully make this material more fun.

教师资源包
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Supplements for Instructors

我们为教师提供完整的教学资源包，可从 Pearson 的教师资源中心获取（http://www.pearsonhighered.com/irc）。请访问该中心了解如何访问以下教师资源：

- **PowerPoint® 幻灯片。** 我们为全部九章提供幻灯片，并已针对第七版进行了全面更新。幻灯片详尽覆盖每章内容，采用图形和动画（而非冗长的文本项目符号）以增强视觉吸引力。我们提供可编辑的原始幻灯片，教师可根据需求自行修改。有些幻灯片由使用本书的其他教师贡献。

- **习题解答。** 我们提供课后习题、编程作业和 Wireshark 实验的解答手册。如前所述，本书前六章新增了大量习题。

.. toggle::

    We provide a complete supplements package to aid instructors in teaching this course. This material can be
    accessed from Pearson’s Instructor Resource Center (http://www.pearsonhighered.com/irc). Visit the
    Instructor Resource Center for ­information about accessing these instructor’s supplements.

    - **PowerPoint® slides.** We provide PowerPoint slides for all nine chapters. The slides have been completely
    updated with this seventh edition. The slides cover each chapter in detail. They use graphics and
    animations (rather than relying only on monotonous text bullets) to make the slides interesting and visually
    appealing. We provide the original PowerPoint slides so you can customize them to best suit your own
    teaching needs. Some of these slides have been contributed by other instructors who have taught from our
    book.
    - **Homework solutions.** We provide a solutions manual for the homework problems in the text, programming
    assignments, and Wireshark labs. As noted ­earlier, we’ve introduced many new homework problems in
    the first six chapters of the book.

章节依赖关系
~~~~~~~~~~~~~~~~~~~~~~~~~

Chapter Dependencies

第一章为本书打下独立的网络基础，介绍了众多关键概念与术语，为全书奠定基础。其余所有章节都直接依赖第一章。在学习完 :ref:`第 1 章 <c1>` 后，我们建议教师按顺序教授 :ref:`第 2 章 <c2>` 至 :ref:`第 6 章 <c5>`，以贯彻自顶向下的教学理念。这五章的内容均建立在前面章节的基础之上。

完成前六章后，教师可以更灵活地选择后续章节。最后三章之间无直接依赖，可按任意顺序授课。但它们均依赖于前六章的内容。许多教师倾向于先讲完前六章，再挑选其中一章作为“甜点”补充讲解。

.. toggle::

    The first chapter of this text presents a self-contained overview of computer networking. Introducing many key
    concepts and terminology, this chapter sets the stage for the rest of the book. All of the other chapters directly
    depend on this first chapter. After completing :ref:`Chapter 1 <c1>`, we recommend instructors cover :ref:`Chapters 2 <c2>` through
    :ref:`6 <c5>` in sequence, following our top-down philosophy. Each of these five chapters leverages material from the
    preceding chapters. After completing the first six chapters, the instructor has quite a bit of flexibility. There are
    no interdependencies among the last three chapters, so they can be taught in any order. However, each of the
    last three chapters depends on the material in the first six chapters. Many instructors first teach the first six
    chapters and then teach one of the last three chapters for “dessert.”

最后一点：我们愿意听取您的反馈
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

One Final Note: We’d Love to Hear from You

我们欢迎学生与教师通过电子邮件向我们反馈对本书的任何意见。我们非常高兴能听到世界各地教师与学生对前五版的反馈，并已将许多建议融入新版中。我们同样欢迎教师投稿新的课后习题（及解答），作为现有题目的补充，我们将其发布在网站的教师专属区域。

我们也鼓励师生开发新的 Java 小程序，用以展示本书所讲的概念与协议。如果您制作了适合本书的小程序，请提交给我们。如果其内容（包括符号与术语）符合要求，我们将很乐意将其添加至网站，并注明作者信息。

因此，正如那句老话所说：“请继续写信给我们！”我们非常欢迎您继续发送有趣的网址、指出书中的错字、提出不同观点、告诉我们哪些内容有效、哪些无效，以及您认为下一版应添加或删减哪些内容。请将邮件发送至 kurose@cs.umass.edu 和 keithwross@nyu.edu。

.. toggle::

    We encourage students and instructors to e-mail us with any comments they might have about our book. It’s
    been wonderful for us to hear from so many instructors and students from around the world about our first five
    editions. We’ve incorporated many of these suggestions into later editions of the book. We also encourage
    instructors to send us new homework problems (and solutions) that would complement the current homework
    problems. We’ll post these on the instructor-only portion of the Web site. We also encourage instructors and
    students to create new Java applets that illustrate the concepts and protocols in this book. If you have an
    applet that you think would be appropriate for this text, please submit it to us. If the applet (including notation
    and terminology) is appropriate, we’ll be happy to include it on the text’s Web site, with an appropriate
    reference to the applet’s authors.

    So, as the saying goes, “Keep those cards and letters coming!” Seriously, please do continue to send us
    interesting URLs, point out typos, disagree with any of our claims, and tell us what works and what doesn’t
    work. Tell us what you think should or shouldn’t be included in the next edition. Send your e-mail to
    kurose@cs.umass.edu and keithwross@nyu.edu.

致谢
-------------------

Acknowledgments

自 1996 年我们开始撰写本书以来，许多人给予我们宝贵帮助，并对我们如何组织和教授网络课程的思考产生了深远影响。我们要向从本书最初草稿至第七版过程中帮助过我们的人致以诚挚感谢。

我们也非常感谢来自全球各地的数百位读者——学生、教师、从业者——他们为本书的前几版提供了建议与反馈。特别感谢以下人士：

.. toggle::

    Since we began writing this book in 1996, many people have given us invaluable help and have been
    influential in shaping our thoughts on how to best organize and teach a networking course. We want to say A
    BIG THANKS to everyone who has helped us from the earliest first drafts of this book, up to this seventh
    edition. We are also very thankful to the many hundreds of readers from around the world—students, faculty,
    practitioners—who have sent us thoughts and comments on earlier editions of the book and suggestions for
    future editions of the book. Special thanks go out to:

- Al Aho (Columbia University)
- Hisham Al-Mubaid (University of Houston-Clear Lake)
- Pratima Akkunoor (Arizona State University)
- Paul Amer (University of Delaware)
- Shamiul Azom (Arizona State University)
- Lichun Bao (University of California at Irvine)
- Paul Barford (University of Wisconsin)
- Bobby Bhattacharjee (University of Maryland)
- Steven Bellovin (Columbia University)
- Pravin Bhagwat (Wibhu)
- Supratik Bhattacharyya (previously at Sprint)
- Ernst Biersack (Eurécom Institute)
- Shahid Bokhari (University of Engineering & Technology, Lahore)
- Jean Bolot (Technicolor Research)
- Daniel Brushteyn (former University of Pennsylvania student)
- Ken Calvert (University of Kentucky)
- Evandro Cantu (Federal University of Santa Catarina)
- Jeff Case (SNMP Research International)
- Jeff Chaltas (Sprint)
- Vinton Cerf (Google)
- Byung Kyu Choi (Michigan Technological University)
- Bram Cohen (BitTorrent, Inc.)
- Constantine Coutras (Pace University)
- John Daigle (University of Mississippi)
- Edmundo A. de Souza e Silva (Federal University of Rio de Janeiro)
- Philippe Decuetos (Eurécom Institute)
- Christophe Diot (Technicolor Research)
- Prithula Dhunghel (Akamai)
- Deborah Estrin (University of California, Los Angeles)
- Michalis Faloutsos (University of California at Riverside)
- Wu-chi Feng (Oregon Graduate Institute)
- Sally Floyd (ICIR, University of California at Berkeley)
- Paul Francis (Max Planck Institute)
- David Fullager (Netflix)
- Lixin Gao (University of Massachusetts)
- JJ Garcia-Luna-Aceves (University of California at Santa Cruz)
- Mario Gerla (University of California at Los Angeles)
- David Goodman (NYU-Poly)
- Yang Guo (Alcatel/Lucent Bell Labs)
- Tim Griffin (Cambridge University)
- Max Hailperin (Gustavus Adolphus College)
- Bruce Harvey (Florida A&M University, Florida State University)
- Carl Hauser (Washington State University)
- Rachelle Heller (George Washington University)
- Phillipp Hoschka (INRIA/W3C)
- Wen Hsin (Park University)
- Albert Huang (former University of Pennsylvania student)
- Cheng Huang (Microsoft Research)
- Esther A. Hughes (Virginia Commonwealth University)
- Van Jacobson (Xerox PARC)
- Pinak Jain (former NYU-Poly student)
- Jobin James (University of California at Riverside)
- Sugih Jamin (University of Michigan)
- Shivkumar Kalyanaraman (IBM Research, India)
- Jussi Kangasharju (University of Helsinki)
- Sneha Kasera (University of Utah)
- Parviz Kermani (formerly of IBM Research)
- Hyojin Kim (former University of Pennsylvania student)
- Leonard Kleinrock (University of California at Los Angeles)
- David Kotz (Dartmouth College)
- Beshan Kulapala (Arizona State University)
- Rakesh Kumar (Bloomberg)
- Miguel A. Labrador (University of South Florida)
- Simon Lam (University of Texas)
- Steve Lai (Ohio State University)
- Tom LaPorta (Penn State University)
- Tim-Berners Lee (World Wide Web Consortium)
- Arnaud Legout (INRIA)
- Lee Leitner (Drexel University)
- Brian Levine (University of Massachusetts)
- Chunchun Li (former NYU-Poly student)
- Yong Liu (NYU-Poly)
- William Liang (former University of Pennsylvania student)
- Willis Marti (Texas A&M University)
- Nick McKeown (Stanford University)
- Josh McKinzie (Park University)
- Deep Medhi (University of Missouri, Kansas City)
- Bob Metcalfe (International Data Group)
- Sue Moon (KAIST)
- Jenni Moyer (Comcast)
- Erich Nahum (IBM Research)
- Christos Papadopoulos (Colorado Sate University)
- Craig Partridge (BBN Technologies)
- Radia Perlman (Intel)
- Jitendra Padhye (Microsoft Research)
- Vern Paxson (University of California at Berkeley)
- Kevin Phillips (Sprint)
- George Polyzos (Athens University of Economics and Business)
- Sriram Rajagopalan (Arizona State University)
- Ramachandran Ramjee (Microsoft Research)
- Ken Reek (Rochester Institute of Technology)
- Martin Reisslein (Arizona State University)
- Jennifer Rexford (Princeton University)
- Leon Reznik (Rochester Institute of Technology)
- Pablo Rodrigez (Telefonica)
- Sumit Roy (University of Washington)
- Dan Rubenstein (Columbia University)
- Avi Rubin (Johns Hopkins University)
- Douglas Salane (John Jay College)
- Despina Saparilla (Cisco Systems)
- John Schanz (Comcast)
- Henning Schulzrinne (Columbia University)
- Mischa Schwartz (Columbia University)
- Ardash Sethi (University of Delaware)
- Harish Sethu (Drexel University)
- K. Sam Shanmugan (University of Kansas)
- Prashant Shenoy (University of Massachusetts)
- Clay Shields (Georgetown University)
- Subin Shrestra (University of Pennsylvania)
- Bojie Shu (former NYU-Poly student)
- Mihail L. Sichitiu (NC State University)
- Peter Steenkiste (Carnegie Mellon University)
- Tatsuya Suda (University of California at Irvine)
- Kin Sun Tam (State University of New York at Albany)
- Don Towsley (University of Massachusetts)
- David Turner (California State University, San Bernardino)
- Nitin Vaidya (University of Illinois)
- Michele Weigle (Clemson University)
- David Wetherall (University of Washington)
- Ira Winston (University of Pennsylvania)
- Di Wu (Sun Yat-sen University)
- Shirley Wynn (NYU-Poly)
- Raj Yavatkar (Intel)
- Yechiam Yemini (Columbia University)
- Dian Yu (NYU Shanghai)
- Ming Yu (State University of New York at Binghamton)
- Ellen Zegura (Georgia Institute of Technology)
- Honggang Zhang (Suffolk University)
- Hui Zhang (Carnegie Mellon University)
- Lixia Zhang (University of California at Los Angeles)
- Meng Zhang (former NYU-Poly student)
- Shuchun Zhang (former University of Pennsylvania student)
- Xiaodong Zhang (Ohio State University)
- ZhiLi Zhang (University of Minnesota)
- Phil Zimmermann (independent consultant)
- Mike Zink (University of Massachusetts)
- Cliff C. Zou (University of Central Florida)

我们还要感谢 Pearson 的整个团队，尤其是 Matt Goldstein 和 Joanne Manning，他们在第七版的出版过程中做出了杰出贡献，并耐心包容了两位非常挑剔、几乎天生无法按时交稿的作者！我们也感谢插图设计师 Janet Theurer 和 Patrice Rossi Calkin，她们负责了本版及过往版本中精彩的图示设计，还要感谢 Katie Ostler 和她在 Cenveo 的团队，出色地完成了本版的制作工作。最后，特别感谢我们在 Addison-Wesley 的前两任编辑 Michael Hirsch 和 Susan Hartman。没有他们的出色管理、不懈鼓励、几近无限的耐心、幽默感与坚持，本书可能不会成形，也不会成为今天的模样。

.. toggle::

    We also want to thank the entire Pearson team—in particular, Matt Goldstein and Joanne Manning—who have
    done an absolutely outstanding job on this seventh ­edition (and who have put up with two very finicky authors
    who seem congenitally ­unable to meet deadlines!). Thanks also to our artists, Janet Theurer and Patrice
    Rossi Calkin, for their work on the beautiful figures in this and earlier editions of our book, and to Katie Ostler
    and her team at Cenveo for their wonderful production work on this edition. Finally, a most special thanks go to
    our previous two editors at ­Addison-Wesley—Michael Hirsch and Susan Hartman. This book would not be
    what it is (and may well not have been at all) without their graceful management, constant encouragement,
    nearly infinite patience, good humor, and perseverance.

    
