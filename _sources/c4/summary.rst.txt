.. _c4.5:


4.5 总结
=================

4.5 Summary

.. tab:: 中文

.. tab:: 英文

In this chapter we’ve covered the **data plane** functions of the network layer—the per-router functions that determine how packets arriving on one of a router’s input links are forwarded to one of that router’s output links. We began by taking a detailed look at the internal operations of a router, studying input and output port functionality and destination-based forwarding, a router’s internal switching mechanism, packet queue management and more. We covered both traditional IP forwarding (where forwarding is based on a datagram’s destination address) and generalized forwarding (where forwarding and other functions may be performed using values in several different fields in the datagram’s header) and seen the versatility of the latter approach. We also studied the IPv4 and IPv6 protocols in detail, and Internet addressing, which we found to be much deeper, subtler, and more interesting than we might have expected.

With our newfound understanding of the network-layer’s data plane, we’re now ready to dive into the network layer’s control plane in :ref:`Chapter 5 <c5>`!