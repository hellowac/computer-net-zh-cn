


8.10 小结
=================
8.10 Summary

在本章中，我们考察了秘密恋人 Bob 和 Alice 用于安全通信的各种机制。我们看到 Bob 和 Alice 关注保密性（使得只有他们能理解所传输消息的内容）、端点认证（确保他们确实在与对方通信）以及消息完整性（确保消息在传输过程中未被篡改）。当然，对安全通信的需求并不局限于秘密恋人。实际上，我们在 :ref:`第 8.5 节 <c8.5>` 到 :ref:`第 8.8 节 <c8.8>` 中看到，安全可以在网络体系结构的各个层中使用，以抵御拥有大量攻击手段的恶意攻击者。

本章的第一部分介绍了安全通信所依据的各种原理。在 :ref:`第 8.2 节 <c8.2>` 中，我们讲解了用于数据加密与解密的加密技术，包括对称密钥加密和公钥加密。我们以 DES 和 RSA 为例，研究了这两类主要加密技术在当今网络中的具体应用。

在 :ref:`第 8.3 节 <c8.3>` 中，我们探讨了两种提供消息完整性的方法：消息认证码（MAC）和数字签名。这两种方法有许多相似之处。它们都使用加密哈希函数，并都能验证消息的来源以及消息本身的完整性。其中一个重要的区别是，MAC 不依赖于加密，而数字签名需要一个公钥基础设施。正如我们在 :ref:`第 8.5 节 <c8.5>` 到 :ref:`第 8.8 节 <c8.8>` 中看到的，这两种技术在实际中都被广泛应用。此外，数字签名还用于创建数字证书，这是验证公钥有效性的关键。在 :ref:`第 8.4 节 <c8.4>` 中，我们研究了端点认证并引入了随机数（nonce）来防御重放攻击。

在 :ref:`第 8.5 节 <c8.5>` 到 :ref:`第 8.8 节 <c8.8>` 中，我们研究了多个在实践中被广泛使用的安全网络协议。我们看到，对称密钥加密是 PGP、SSL、IPsec 和无线安全的核心。我们看到，公钥加密对于 PGP 和 SSL 都至关重要。我们看到 PGP 使用数字签名来实现消息完整性，而 SSL 和 IPsec 使用的是 MAC。现在你已经理解了密码学的基本原理，并了解了这些原理如何实际应用，你已经具备了设计自己安全网络协议的能力！

借助于 :ref:`第 8.2 节 <c8.2>` 到 :ref:`第 8.8 节 <c8.8>` 中讲授的技术，Bob 和 Alice 可以安全地通信。（我们只能希望他们是学过这些内容的网络课程学生，因此能避免被 Trudy 揭露他们的幽会！）但保密性只是网络安全图景的一小部分。正如我们在 :ref:`第 8.9 节 <c8.9>` 中了解到的，网络安全越来越关注保护网络基础设施免受潜在攻击者的入侵。因此，在本章后半部分，我们介绍了防火墙和 IDS 系统，这些系统可检查进入和离开组织网络的数据包。

本章内容丰富，涵盖了现代网络安全中最重要的主题。希望深入了解的读者可以查阅本章引用的文献。特别推荐：:ref:`[Skoudis 2006] <Skoudis 2006>`，讲述攻击和运营安全；:ref:`[Kaufman 1995] <Kaufman 1995>`，讲述密码学及其在网络安全中的应用；:ref:`[Rescorla 2001] <Rescorla 2001>`，深入而易读地解析 SSL；以及 :ref:`[Edney 2003] <Edney 2003>`，全面讨论 802.11 安全问题，包括对 WEP 及其缺陷的深刻分析。

.. toggle::

    In this chapter, we’ve examined the various mechanisms that our secret lovers, Bob and Alice, can use to communicate securely. We’ve seen that Bob and Alice are interested in confidentiality (so they alone are able to understand the contents of a transmitted message), end-point authentication (so they are sure that they are talking with each other), and message integrity (so they are sure that their messages are not altered in transit). Of course, the need for secure communication is not confined to secret lovers. Indeed, we saw in :ref:`Sections 8.5 <c8.5>` through :ref:`8.8 <c8.8>` that security can be used in various layers in a network architecture to protect against bad guys who have a large arsenal of possible attacks at hand.

    The first part of this chapter presented various principles underlying secure communication. In :ref:`Section 8.2 <c8.2>`, we covered cryptographic techniques for encrypting and decrypting data, including symmetric key cryptography and public key cryptography. DES and RSA were examined as specific case studies of these two major classes of cryptographic techniques in use in today’s networks.

    In :ref:`Section 8.3 <c8.3>`, we examined two approaches for providing message integrity: message authentication codes (MACs) and digital signatures. The two approaches have a number of parallels. Both use cryptographic hash functions and both techniques enable us to verify the source of the message as well as the integrity of the message itself. One important difference is that MACs do not rely on encryption whereas digital signatures require a public key infrastructure. Both techniques are extensively used in practice, as we saw in :ref:`Sections 8.5 <c8.5>` through :ref:`8.8 <c8.8>`. Furthermore, digital signatures are used to create digital certificates, which are important for verifying the validity of public keys. In :ref:`Section 8.4 <c8.4>`, we examined endpoint authentication and introduced nonces to defend against the replay attack.

    In :ref:`Sections 8.5 <c8.5>` through :ref:`8.8 <c8.8>` we examined several security networking protocols that enjoy extensive use in practice. We saw that symmetric key cryptography is at the core of PGP, SSL, IPsec, and wireless security. We saw that public key cryptography is crucial for both PGP and SSL. We saw that PGP uses digital signatures for message integrity, whereas SSL and IPsec use MACs. Having now an understanding of the basic principles of cryptography, and having studied how these principles are actually used, you are now in position to design your own secure network protocols!

    Armed with the techniques covered in :ref:`Sections 8.2 <c8.2>` through :ref:`8.8 <c8.8>`, Bob and Alice can communicate securely. (One can only hope that they are networking students who have learned this material and can thus avoid having their tryst uncovered by Trudy!) But confidentiality is only a small part of the network security picture. As we learned in :ref:`Section 8.9 <c8.9>`, increasingly, the focus in network security has been on securing the network infrastructure against a potential onslaught by the bad guys. In the latter part of this chapter, we thus covered firewalls and IDS systems which inspect packets entering and leaving an
    organization’s network.

    This chapter has covered a lot of ground, while focusing on the most important topics in modern network security. Readers who desire to dig deeper are encouraged to investigate the references cited in this chapter. In particular, we recommend :ref:`[Skoudis 2006] <Skoudis 2006>` for attacks and operational security, :ref:`[Kaufman 1995] <Kaufman 1995>` for cryptography and how it applies to network security, :ref:`[Rescorla 2001] <Rescorla 2001>` for an in-depth but readable treatment of SSL, and :ref:`[Edney 2003] <Edney 2003>` for a thorough discussion of 802.11 security, including an insightful investigation into WEP and its flaws.