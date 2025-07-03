.. _c2.9:


2.9 总结
=================

1.8 Summary

.. tab:: 中文

.. tab:: 英文

In this chapter, we’ve studied the conceptual and the implementation aspects of network applications. We’ve learned about the ubiquitous client-server architecture adopted by many Internet applications and seen its use in the HTTP, SMTP, POP3, and DNS protocols. We’ve studied these important application- level protocols, and their corresponding associated applications (the Web, file transfer, e-mail, and DNS) in some detail. We’ve learned about the P2P architecture and how it is used in many applications. We’ve also learned about streaming video, and how modern video distribution systems leverage CDNs. We’ve examined how the socket API can be used to build network applications. We’ve walked through the use of sockets for connection-oriented (TCP) and connectionless (UDP) end-to-end transport services. The first step in our journey down the layered network architecture is now complete!

At the very beginning of this book, in :ref:`Section 1.1 <c1.1>`, we gave a rather vague, bare-bones definition of a protocol: “the format and the order of messages exchanged between two or more communicating entities, as well as the actions taken on the transmission and/or receipt of a message or other event.” The material in this chapter, and in particular our detailed study of the HTTP, SMTP, POP3, and DNS protocols, has now added considerable substance to this definition. Protocols are a key concept in networking; our study of application protocols has now given us the opportunity to develop a more intuitive feel for what protocols are all about.

In :ref:`Section 2.1 <c2.1>`, we described the service models that TCP and UDP offer to applications that invoke them. We took an even closer look at these service models when we developed simple applications that run over TCP and UDP in :ref:`Section 2.7 <c2.7>`. However, we have said little about how TCP and UDP provide these service models. For example, we know that TCP provides a reliable data service, but we haven’t said yet how it does so. In the next chapter we’ll take a careful look at not only the what, but also the how and why of transport protocols.

Equipped with knowledge about Internet application structure and application-level protocols, we’re now ready to head further down the protocol stack and examine the transport layer in :ref:`Chapter 3 <c3>`.