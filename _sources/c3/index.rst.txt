.. _c3:

第 3 章 传输层
============================================

Chapter 3 Transport Layer

.. tab:: 中文



.. tab:: 英文

    Residing between the application and network layers, the transport layer is a central piece of the layered
    network architecture. It has the critical role of providing communication services directly to the
    application processes running on different hosts. The pedagogic approach we take in this chapter is to
    alternate between discussions of transport-layer principles and discussions of how these principles are
    implemented in existing protocols; as usual, particular emphasis will be given to Internet protocols, in
    particular the TCP and UDP transport-layer protocols.

    We’ll begin by discussing the relationship between the transport and network layers. This sets the stage
    for examining the first critical function of the transport layer—extending the network layer’s delivery
    service between two end systems to a delivery service between two application-layer processes running
    on the end systems. We’ll illustrate this function in our coverage of the Internet’s connectionless
    transport protocol, UDP.

    We’ll then return to principles and confront one of the most fundamental problems in computer
    networking—how two entities can communicate reliably over a medium that may lose and corrupt data.
    Through a series of increasingly complicated (and realistic!) scenarios, we’ll build up an array of
    techniques that transport protocols use to solve this problem. We’ll then show how these principles are
    embodied in TCP, the Internet’s connection-oriented transport protocol.

    We’ll next move on to a second fundamentally important problem in networking—controlling the
    transmission rate of transport-layer entities in order to avoid, or recover from, congestion within the
    network. We’ll consider the causes and consequences of congestion, as well as commonly used
    congestion-control techniques. After obtaining a solid understanding of the issues behind congestion
    control, we’ll study TCP’s approach to congestion control.


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