前言
===========

Preface

.. tab:: 中文

    

.. tab:: 英文

    Welcome to the seventh edition of Computer Networking: A Top-Down Approach. Since the publication of the
    first edition 16 years ago, our book has been adopted for use at many hundreds of colleges and universities,
    translated into 14 languages, and used by over one hundred thousand students and practitioners worldwide.
    We’ve heard from many of these readers and have been overwhelmed by the ­positive ­response.

What’s New in the Seventh Edition?
---------------------------

What’s New in the Seventh Edition?

.. tab:: 中文



.. tab:: 英文


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

    As always, our aim in creating this new edition of our book is to continue to provide a focused and modern
    treatment of computer networking, emphasizing both principles and practice.

Audience
----------------

Audience

.. tab:: 中文



.. tab:: 英文

    This textbook is for a first course on computer networking. It can be used in both computer science and
    electrical engineering departments. In terms of programming languages, the book assumes only that the
    student has experience with C, C++, Java, or Python (and even then only in a few places). Although this book
    is more precise and analytical than many other introductory computer networking texts, it rarely uses any
    mathematical concepts that are not taught in high school. We have made a deliberate effort to avoid using any
    advanced calculus, probability, or stochastic process concepts (although we’ve included some homework
    problems for students with this advanced background). The book is therefore appropriate for undergraduate
    courses and for first-year graduate courses. It should also be useful to practitioners in the telecommunications
    industry.

What Is Unique About This Textbook?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

What Is Unique About This Textbook?

.. tab:: 中文



.. tab:: 英文

    The subject of computer networking is enormously complex, involving many concepts, protocols, and
    technologies that are woven together in an intricate manner. To cope with this scope and complexity, many
    computer networking texts are often organized around the “layers” of a network architecture. With a layered
    organization, students can see through the complexity of computer networking—they learn about the distinct
    concepts and protocols in one part of the architecture while seeing the big picture of how all parts fit together.
    From a pedagogical perspective, our personal experience has been that such a layered approach indeed
    works well. Nevertheless, we have found that the traditional approach of teaching—bottom up; that is, from the
    physical layer towards the application layer—is not the best approach for a modern course on computer
    networking.

A Top-Down Approach
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A Top-Down Approach

.. tab:: 中文



.. tab:: 英文

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

An Internet Focus
------------------------

An Internet Focus

.. tab:: 中文



.. tab:: 英文

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

Teaching Networking Principles
--------------------------------

Teaching Networking Principles

.. tab:: 中文



.. tab:: 英文

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


The Website
------------------

The Website

.. tab:: 中文



.. tab:: 英文

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

Pedagogical Features
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pedagogical Features

.. tab:: 中文



.. tab:: 英文

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

Supplements for Instructors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Supplements for Instructors

.. tab:: 中文



.. tab:: 英文

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

Chapter Dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~

Chapter Dependencies

.. tab:: 中文



.. tab:: 英文

    The first chapter of this text presents a self-contained overview of computer networking. Introducing many key
    concepts and terminology, this chapter sets the stage for the rest of the book. All of the other chapters directly
    depend on this first chapter. After completing :ref:`Chapter 1 <c1>`, we recommend instructors cover :ref:`Chapters 2 <c2>` through
    :ref:`6 <c5>` in sequence, following our top-down philosophy. Each of these five chapters leverages material from the
    preceding chapters. After completing the first six chapters, the instructor has quite a bit of flexibility. There are
    no interdependencies among the last three chapters, so they can be taught in any order. However, each of the
    last three chapters depends on the material in the first six chapters. Many instructors first teach the first six
    chapters and then teach one of the last three chapters for “dessert.”

One Final Note: We’d Love to Hear from You
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

One Final Note: We’d Love to Hear from You

.. tab:: 中文



.. tab:: 英文


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

Acknowledgments
-------------------

Acknowledgments

.. tab:: 中文



.. tab:: 英文

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

    We also want to thank the entire Pearson team—in particular, Matt Goldstein and Joanne Manning—who have
    done an absolutely outstanding job on this seventh ­edition (and who have put up with two very finicky authors
    who seem congenitally ­unable to meet deadlines!). Thanks also to our artists, Janet Theurer and Patrice
    Rossi Calkin, for their work on the beautiful figures in this and earlier editions of our book, and to Katie Ostler
    and her team at Cenveo for their wonderful production work on this edition. Finally, a most special thanks go to
    our previous two editors at ­Addison-Wesley—Michael Hirsch and Susan Hartman. This book would not be
    what it is (and may well not have been at all) without their graceful management, constant encouragement,
    nearly infinite patience, good humor, and perseverance.