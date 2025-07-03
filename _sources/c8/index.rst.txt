.. _c8:


第 8 章 计算机网络中的安全性
============================================

Chapter 8 Security in Computer Networks

.. tab:: 中文



.. tab:: 英文

   Way back in :ref:`Section 1.6 <c1.6>` we described some of the more prevalent and damaging classes of Internet
   attacks, including malware attacks, denial of service, sniffing, source masquerading, and message
   modification and deletion. Although we have since learned a tremendous amount about computer
   networks, we still haven’t examined how to secure networks from those attacks. Equipped with our
   newly acquired expertise in computer networking and Internet protocols, we’ll now study in-depth secure
   communication and, in particular, how computer networks can be defended from those nasty bad guys.

   Let us introduce Alice and Bob, two people who want to communicate and wish to do so “securely.” This
   being a networking text, we should remark that Alice and Bob could be two routers that want to
   exchange routing tables securely, a client and server that want to establish a secure transport
   connection, or two e-mail applications that want to exchange secure e-mail—all case studies that we will
   consider later in this chapter. Alice and Bob are well-known fixtures in the security community, perhaps
   because their names are more fun than a generic entity named “A” that wants to communicate securely
   with a generic entity named “B.” Love affairs, wartime communication, and business transactions are the
   commonly cited human needs for secure communications; preferring the first to the latter two, we’re
   happy to use Alice and Bob as our sender and receiver, and imagine them in this first scenario.

   We said that Alice and Bob want to communicate and wish to do so “securely,” but what precisely does
   this mean? As we will see, security (like love) is a many-splendored thing; that is, there are many facets
   to security. Certainly, Alice and Bob would like for the contents of their communication to remain secret
   from an eavesdropper. They probably would also like to make sure that when they are communicating,
   they are indeed communicating with each other, and that if their communication is tampered with by an
   eavesdropper, that this tampering is detected. In the first part of this chapter, we’ll cover the
   fundamental cryptography techniques that allow for encrypting communication, authenticating the party
   with whom one is communicating, and ensuring message integrity.

   In the second part of this chapter, we’ll examine how the fundamental ­cryptography principles can be
   used to create secure networking protocols. Once again taking a top-down approach, we’ll examine
   secure protocols in each of the (top four) layers, beginning with the application layer. We’ll examine how
   to secure e-mail, how to secure a TCP connection, how to provide blanket security at the network layer,
   and how to secure a wireless LAN. In the third part of this chapter we’ll consider operational security,which is about protecting organizational networks from attacks. In particular, we’ll take a careful look at
   how firewalls and intrusion detection systems can enhance the security of an organizational network.



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
   ./s9.rst
   ./summary.rst
   ./homework.rst
   ./wiresharklab.rst
   ./interview.rst

