.. _c1:

第 1 章 计算机网络与因特网
==================================

Chapter 1 Computer Networks and the Internet 

Today’s Internet is arguably the largest engineered system ever created by ­mankind, with hundreds of
millions of connected computers, communication links, and switches; with billions of users who connect
via laptops, tablets, and smartphones; and with an array of new Internet-connected “things” including
game consoles, surveillance systems, watches, eye glasses, thermostats, body scales, and cars. Given
that the Internet is so large and has so many diverse components and uses, is there any hope of
understanding how it works? Are there guiding principles and structure that can provide a foundation for
understanding such an amazingly large and complex system? And if so, is it possible that it actually
could be both interesting and fun to learn about computer networks? Fortunately, the answer to all of
these questions is a resounding YES! Indeed, it’s our aim in this book to provide you with a modern
introduction to the dynamic field of computer networking, giving you the principles and practical insights
you’ll need to understand not only today’s networks, but tomorrow’s as well.

This first chapter presents a broad overview of computer networking and the Internet. Our goal here is to
paint a broad picture and set the context for the rest of this book, to see the forest through the trees.
We’ll cover a lot of ground in this introductory chapter and discuss a lot of the pieces of a computer
network, without losing sight of the big picture.

We’ll structure our overview of computer networks in this chapter as follows. After introducing some
basic terminology and concepts, we’ll first examine the basic hardware and software components that
make up a network. We’ll begin at the network’s edge and look at the end systems and network
applications running in the network. We’ll then explore the core of a computer network, examining the
links and the switches that transport data, as well as the access networks and physical media that
connect end systems to the network core. We’ll learn that the Internet is a network of networks, and we’ll
learn how these networks connect with each other.

After having completed this overview of the edge and core of a computer network, we’ll take the broader
and more abstract view in the second half of this chapter. We’ll examine delay, loss, and throughput of
data in a computer network and provide simple quantitative models for end-to-end throughput and delay:
models that take into account transmission, propagation, and queuing delays. We’ll then introduce some
of the key architectural principles in computer networking, namely, protocol layering and service models.
We’ll also learn that computer networks are vulnerable to many different types of attacks; we’ll survey
some of these attacks and consider how computer networks can be made more secure. Finally, we’ll
close this chapter with a brief history of computer networking.

.. toggle::

    如今的因特网无疑是人类有史以来构建的最大工程系统，拥有数亿台互联的计算机、通信链路和交换设备，数十亿用户通过笔记本电脑、平板设备和智能手机接入，此外还连接着各种新兴的“物联网”设备，包括游戏主机、监控系统、手表、眼镜、恒温器、体重秤乃至汽车。考虑到因特网规模之庞大、组成之多样、用途之广泛，人们不禁要问：我们有可能理解它的运行原理吗？是否存在某种指导原则与结构，能作为理解这样一个庞大复杂系统的基础？如果有，学习计算机网络是否还有趣甚至充满乐趣？幸运的是，对这些问题的回答都是响亮的“是”！本书的目标正是为你提供一个关于计算机网络这一动态领域的现代化入门，帮助你掌握理解当前网络乃至未来网络所需的基本原理与实用见解。

    本章将对计算机网络及因特网进行宏观概述。我们的目标是从整体上勾勒出全貌，为全书后续内容奠定背景基础，做到“见树又见林”。在这一章中，我们将介绍大量内容，并讨论计算机网络中的诸多组成部分，同时不忘从大局着眼。

    本章对计算机网络的综述结构如下：在介绍一些基础术语与概念之后，我们将首先考察构成网络的基本硬件与软件组件。我们将从网络的边缘开始，研究终端系统与运行在网络中的网络应用；接着转向计算机网络的核心部分，考察传输数据所依赖的链路与交换设备，以及将终端系统接入网络核心的接入网络与物理介质。我们将了解到因特网其实是一个由多个网络互联而成的“网络的网络”，并将学习这些网络之间是如何互联的。

    在完成对计算机网络边缘与核心的综述之后，本章后半部分将转向更高层次的抽象视角。我们将研究计算机网络中的时延、丢包与吞吐量，并给出一些用于分析端到端吞吐量与时延的简单定量模型，这些模型将考虑传输时延、传播时延和排队时延。随后，我们将介绍计算机网络体系结构中的几个关键原则，即协议分层与服务模型。我们还将了解到，计算机网络面临多种攻击威胁；我们将简要概述这些攻击类型，并探讨如何提升网络安全性。最后，本章将以计算机网络的简要历史作为收尾。


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
   ./s8.rst
   ./summary.rst
   ./homework.rst
   ./wiresharklab.rst
   ./interview.rst
