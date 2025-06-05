.. _c1.8:


1.8 总结
=================

1.8 Summary

.. tab:: 中文

.. tab:: 英文

    
In this chapter we’ve covered a tremendous amount of material! We’ve looked at the various pieces of
hardware and software that make up the Internet in particular and computer networks in general. We
started at the edge of the network, looking at end systems and applications, and at the transport service
provided to the applications running on the end systems. We also looked at the link-layer technologies
and physical media typically found in the access network. We then dove deeper inside the network, into
the network core, identifying packet switching and circuit switching as the two basic approaches for
transporting data through a telecommunication network, and we examined the strengths and
weaknesses of each approach. We also examined the structure of the global Internet, learning that the
Internet is a network of networks. We saw that the Internet’s hierarchical structure, consisting of higher-
and lower-tier ISPs, has allowed it to scale to include thousands of networks.

In the second part of this introductory chapter, we examined several topics central to the field of
computer networking. We first examined the causes of delay, throughput and packet loss in a packet-
switched network. We developed simple quantitative models for transmission, propagation, and queuing
delays as well as for throughput; we’ll make extensive use of these delay models in the homework
problems throughout this book. Next we examined protocol layering and service models, key
architectural principles in networking that we will also refer back to throughout this book. We also
surveyed some of the more prevalent security attacks in the Internet day. We finished our introduction to
networking with a brief history of computer networking. The first chapter in itself constitutes a mini-
course in computer networking.

So, we have indeed covered a tremendous amount of ground in this first chapter! If you’re a bit
overwhelmed, don’t worry. In the following chapters we’ll revisit all of these ideas, covering them in
much more detail (that’s a promise, not a threat!). At this point, we hope you leave this chapter with a
still-developing intuition for the pieces that make up a network, a still-developing command of the
vocabulary of networking (don’t be shy about referring back to this chapter), and an ever-growing desire
to learn more about networking. That’s the task ahead of us for the rest of this book.

Road-Mapping This Book
-----------------------------

Before starting any trip, you should always glance at a road map in order to become familiar with the
major roads and junctures that lie ahead. For the trip we are about to embark on, the ultimate
destination is a deep understanding of the how, what, and why of computer networks. Our road map is
the sequence of chapters of this book:

1. Computer Networks and the Internet
2. Application Layer
3. Transport Layer
4. Network Layer: Data Plane
5. Network Layer: Control Plane
6. The Link Layer and LANs
7. Wireless and Mobile Networks
8. Security in Computer Networks
9. Multimedia Networking

:ref:`Chapters 2 <c2>` through :ref:`6 <c6>` are the five core chapters of this book. You should notice that these chapters are
organized around the top four layers of the five-layer Internet protocol. Further note that our journey will
begin at the top of the Internet protocol stack, namely, the application layer, and will work its way
downward. The rationale behind this top-down journey is that once we understand the applications, we
can understand the network services needed to support these applications. We can then, in turn,
examine the various ways in which such services might be implemented by a network architecture.
Covering applications early thus provides motivation for the remainder of the text.

The second half of the book— :ref:`Chapters 7 <c7>` through :ref:`9 <c9>` —zooms in on three enormously important (and
somewhat independent) topics in modern computer networking. In :ref:`Chapters 7 <c7>`, we examine wireless and
mobile networks, including wireless LANs (including WiFi and Bluetooth), Cellular telephony networks
(including GSM, 3G, and 4G), and mobility (in both IP and GSM networks). :ref:`Chapters 8 <c8>`, which addresses
security in computer networks, first looks at the underpinnings of encryption and network security, and
then we examine how the basic theory is being applied in a broad range of Internet contexts. The last
chapter, which addresses multimedia networking, examines audio and video applications such as
Internet phone, video conferencing, and streaming of stored media. We also look at how a packet-
switched network can be designed to provide consistent quality of service to audio and video
applications.