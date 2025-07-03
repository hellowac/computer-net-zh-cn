


8.10 总结
=================

8.10 Summary

.. tab:: 中文

.. tab:: 英文

In this chapter, we’ve examined the various mechanisms that our secret lovers, Bob and Alice, can use to communicate securely. We’ve seen that Bob and Alice are interested in confidentiality (so they alone are able to understand the contents of a transmitted message), end-point authentication (so they are sure that they are talking with each other), and message integrity (so they are sure that their messages are not altered in transit). Of course, the need for secure communication is not confined to secret lovers. Indeed, we saw in :ref:`Sections 8.5 <c8.5>` through :ref:`8.8 <c8.8>` that security can be used in various layers in a network architecture to protect against bad guys who have a large arsenal of possible attacks at hand.

The first part of this chapter presented various principles underlying secure communication. In :ref:`Section 8.2 <c8.2>`, we covered cryptographic techniques for encrypting and decrypting data, including symmetric key cryptography and public key cryptography. DES and RSA were examined as specific case studies of these two major classes of cryptographic techniques in use in today’s networks.

In :ref:`Section 8.3 <c8.3>`, we examined two approaches for providing message integrity: message authentication codes (MACs) and digital signatures. The two approaches have a number of parallels. Both use cryptographic hash functions and both techniques enable us to verify the source of the message as well as the integrity of the message itself. One important difference is that MACs do not rely on encryption whereas digital signatures require a public key infrastructure. Both techniques are extensively used in practice, as we saw in :ref:`Sections 8.5 <c8.5>` through :ref:`8.8 <c8.8>`. Furthermore, digital signatures are used to create digital certificates, which are important for verifying the validity of public keys. In :ref:`Section 8.4 <c8.4>`, we examined endpoint authentication and introduced nonces to defend against the replay attack.

In :ref:`Sections 8.5 <c8.5>` through :ref:`8.8 <c8.8>` we examined several security networking protocols that enjoy extensive use in practice. We saw that symmetric key cryptography is at the core of PGP, SSL, IPsec, and wireless security. We saw that public key cryptography is crucial for both PGP and SSL. We saw that PGP uses digital signatures for message integrity, whereas SSL and IPsec use MACs. Having now an understanding of the basic principles of cryptography, and having studied how these principles are actually used, you are now in position to design your own secure network protocols!

Armed with the techniques covered in :ref:`Sections 8.2 <c8.2>` through :ref:`8.8 <c8.8>`, Bob and Alice can communicate securely. (One can only hope that they are networking students who have learned this material and can thus avoid having their tryst uncovered by Trudy!) But confidentiality is only a small part of the network security picture. As we learned in :ref:`Section 8.9 <c8.9>`, increasingly, the focus in network security has been on securing the network infrastructure against a potential onslaught by the bad guys. In the latter part of this chapter, we thus covered firewalls and IDS systems which inspect packets entering and leaving an
organization’s network.

This chapter has covered a lot of ground, while focusing on the most important topics in modern network security. Readers who desire to dig deeper are encouraged to investigate the references cited in this chapter. In particular, we recommend :ref:`[Skoudis 2006] <Skoudis 2006>` for attacks and operational security, :ref:`[Kaufman 1995] <Kaufman 1995>` for cryptography and how it applies to network security, :ref:`[Rescorla 2001] <Rescorla 2001>` for an in-depth but readable treatment of SSL, and :ref:`[Edney 2003] <Edney 2003>` for a thorough discussion of 802.11 security, including an insightful investigation into WEP and its flaws.