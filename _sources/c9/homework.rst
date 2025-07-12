


家庭作业问题和疑问
========================================
Homework Problems and Questions

第9.1节
-------------

R1. 当Victor Video正在观看一个4 Mbps的视频、Facebook Frank每20秒查看一张新的100 Kbyte图片、Martha Music正在收听一个200 kbps的音频流时，重新构建 :ref:`表9.1 <Table 9.1>`。

R2. 视频中有两种冗余类型。描述它们，并讨论如何利用它们进行高效压缩。

R3. 假设一个模拟音频信号每秒采样16,000次，每个采样被量化为1024个级别之一。那么由PCM编码得到的数字音频信号的比特率是多少？

R4. 多媒体应用可分为三类。请列出并描述每一类。

.. toggle::

   R1. Reconstruct :ref:`Table 9.1 <Table 9.1>` for when Victor Video is watching a 4 Mbps video, Facebook Frank is looking at a new 100 Kbyte image every 20 seconds, and Martha Music is listening to 200 kbps audio stream.

   R2. There are two types of redundancy in video. Describe them, and discuss how they can be exploited for efficient compression.

   R3. Suppose an analog audio signal is sampled 16,000 times per second, and each sample is quantized into one of 1024 levels. What would be the resulting bit rate of the PCM digital audio signal?

   R4. Multimedia applications can be classified into three categories. Name and describe each category.

第9.2节
-------------

R5. 流式视频系统可分为三类。请列出并简要描述每一类。

R6. 列举UDP流的三个缺点。

R7. 在HTTP流中，TCP接收缓冲区和客户端的应用缓冲区是同一个东西吗？如果不是，它们之间如何交互？

R8. 考虑一个HTTP流的简单模型。假设服务器以恒定的2 Mbps速率发送比特，并在接收到800万比特后开始播放。初始缓冲延迟tp是多少？

.. toggle::
   
   R5. Streaming video systems can be classified into three categories. Name and briefly describe each of these categories.

   R6. List three disadvantages of UDP streaming.

   R7. With HTTP streaming, are the TCP receive buffer and the client’s application buffer the same thing? If not, how do they interact?

   R8. Consider the simple model for HTTP streaming. Suppose the server sends bits at a constant rate of 2 Mbps and playback begins when 8 million bits have been received. What is the initial buffering delay tp? 

第9.3节
-------------

R9. 端到端延迟和分组抖动之间有什么区别？造成分组抖动的原因是什么？

R10. 为什么一个在其计划播放时间之后接收的分组被视为丢失？

R11. :ref:`第9.3节 <c9.3>` 描述了两种FEC方案。请简要总结它们。这两种方案都通过添加开销来提高流的传输速率。交织（interleaving）是否也会增加传输速率？

.. toggle::
   
   R9. What is the difference between end-to-end delay and packet jitter? What are the causes of packet jitter?

   R10. Why is a packet that is received after its scheduled playout time considered lost?

   R11. :ref:`Section 9.3 <c9.3>` describes two FEC schemes. Briefly summarize them. Both schemes increase the transmission rate of the stream by adding overhead. Does interleaving also increase the transmission rate?

第9.4节
-------------

R12. 接收方如何识别不同会话中的不同RTP流？如何识别同一会话中不同的流？

R13. SIP注册服务器的作用是什么？SIP注册服务器的作用与移动IP中的归属代理有何不同？

.. toggle::
   
   R12. How are different RTP streams in different sessions identified by a receiver? How are different streams from within the same session identified?

   R13. What is the role of a SIP registrar? How is the role of an SIP registrar different from that of a home agent in Mobile IP?

问题
~~~~~~~~~~~~~
Problems

P1. 请看下图。类似于我们在 :ref:`图9.1 <Figure 9.1>` 中的讨论，假设视频以固定比特率编码，因此每个视频块包含在相同固定时间Δ内播放的视频帧。服务器在t0时刻发送第一个视频块，在t0+Δ时发送第二个块，在t0+2Δ时发送第三个块，依此类推。一旦客户端开始播放，每个块应在前一个块之后的Δ时间单位播放。

.. figure:: ../img/804-0.png 
   :align: center

a. 假设客户端在第一个块到达的t1时立即开始播放。在下图中，有多少个视频块（包括第一个块）会及时到达客户端以供播放？请说明你是如何得出答案的。
b. 假设客户端现在在t1+Δ时开始播放。有多少个视频块（包括第一个块）会及时到达客户端以供播放？请说明你是如何得出答案的。
c. 在上面(b)的相同场景中，在等待播放的情况下，客户端缓冲区中最多会存储多少个块？请说明你是如何得出答案的。
d. 客户端最小的播放延迟是多少，以确保每个视频块都能及时到达并播放？请说明你是如何得出答案的。

P2. 回顾在 :ref:`图9.3 <Figure 9.3>` 中所示的HTTP流的简单模型。记B为客户端应用缓冲区大小，Q为客户端应用在开始播放前必须缓冲的比特数，r为视频消费速率。假设服务器在客户端缓冲区未满时以恒定速率x发送比特。

a. 假设x<r。如正文所述，在这种情况下播放将交替进行：连续播放和冻结。请根据Q、r和x求出每段连续播放和冻结期的长度。
b. 现在假设x>r。客户端应用缓冲区在什么时刻t=tf变满？

P3. 回顾在 :ref:`图9.3 <Figure 9.3>` 中所示的HTTP流的简单模型。假设缓冲区大小无限，但服务器以变化速率x(t)发送比特。具体来说，假设x(t)具有如下锯齿形状：在t=0时速率为0，并在线性增长至t=T时达到H，然后重复此模式，如下图所示。

.. figure:: ../img/805-0.png 
   :align: center

a. 服务器的平均发送速率是多少？
b. 假设Q=0，即客户端一接收到视频帧就开始播放，会发生什么？
c. 现在假设Q>0且HT/2≥Q。请根据Q、H和T求出首次播放开始的时间。
d. 假设H>2r且Q=HT/2。请证明在初始播放延迟之后将不会发生冻结。
e. 假设H>2r。请找出不会发生冻结所需的最小Q值。
f. 现在假设缓冲区大小B是有限的，且H>2r。请根据Q、B、T和H求出客户端应用缓冲区第一次变满的时间t=tf。

P4. 回顾在 :ref:`图9.3 <Figure 9.3>` 中所示的HTTP流的简单模型。假设客户端应用缓冲区是无限的，服务器以恒定速率x发送，视频消费速率为r且r<x。并假设播放立即开始。假设用户在t=E时提早终止视频播放。在终止时，如果服务器尚未发送完视频的所有比特，则停止发送。

a. 假设视频长度为无限长。浪费了多少比特（即已发送但未观看的）？
b. 假设视频长度为T秒，且T>E。浪费了多少比特（即已发送但未观看的）？

P5. 考虑一个DASH系统（如 :ref:`第2.6节 <c2.6>` 所述），其中有N个不同码率和质量的视频版本，以及N个不同码率和质量的音频版本。假设我们希望播放器可以随时选择任意的视频和音频组合。

a. 如果我们将音频与视频混合创建文件，使得服务器在任一时刻只发送一个媒体流，那么服务器需要存储多少个文件（每个有不同的URL）？
b. 如果服务器分别发送音频和视频流，并由客户端进行同步，那么服务器需要存储多少个文件？

P6. 在 :ref:`第9.3节 <c9.3>` 的VoIP示例中，设h为添加到每个块的头部字节总数，包括UDP和IP头部。

a. 假设每20毫秒发出一个IP数据报，求出由该应用一方产生的数据报的传输速率（比特/秒）。
b. 当使用RTP时，h的典型值是多少？

P7. 考虑 :ref:`第9.3节 <c9.3>` 中估算平均时延di的过程。假设u=0.1。设r1−t1为最近的一个采样时延，r2−t2为前一个，以此类推。

a. 假设某音频应用接收到四个包，对应采样时延分别为r4−t4、r3−t3、r2−t2、r1−t1。请用这四个采样表达估算的延迟d。
b. 将你的公式推广到n个采样时延。
c. 对于(b)中的公式，让n趋于无穷，并给出结果公式。

   请评论为什么这种平均方式被称为指数移动平均。

P8. 重复P7中(a)和(b)的问题，但针对平均时延偏差的估算。

P9. 在 :ref:`第9.3节 <c9.3>` 的VoIP示例中，我们提出了在线估算时延（指数移动平均）的方法。本题中我们将探讨另一种方法。

设ti为接收到的第i个分组的时间戳，ri为第i个分组的实际接收时间。dn为接收第n个分组后对平均时延的估算。第一个分组到达后，我们设定d1=r1−t1。

a. 若我们希望dn=(r1−t1+r2−t2+⋯+rn−tn)/n，给出以dn−1、rn和tn为变量的递归公式。
b. 请解释为何对于网络电话而言，:ref:`第9.3节 <c9.3>` 中所述的时延估算方法比(a)中的更合适。

P10. 比较 :ref:`第9.3节 <c9.3>` 中用于估算平均时延的方法与 :ref:`第3.5节 <c3.5>` 中用于估算往返时间的方法。这两种方法有何共同点？有何不同？

P11. 请看下图（与 :ref:`图9.3 <Figure 9.3>` 类似）。发送方从t=1开始周期性地发送音频分组。第一个分组在t=8时到达接收方。

.. figure:: ../img/807-0.png 
   :align: center

a. 不考虑播放延迟，分组2到分组8的传输时延是多少？图中的每条垂直和水平线段长度为1、2或3时间单位。
b. 若在第一个分组到达t=8时立即开始播放，前八个分组中哪些未能及时到达以供播放？
c. 若在t=9时开始播放，前八个分组中哪些未能及时到达以供播放？
d. 接收方最小播放延迟是多少，才能确保前八个分组都能及时到达并播放？

P12. 再次参考P11中的图，显示分组音频的传输和接收时间。

a. 使用 :ref:`第9.3.2节 <c9.3.2>` 中di的公式，计算分组2到8的估算时延，设u=0.1。
b. 使用 :ref:`第9.3.2节 <c9.3.2>` 中vi的公式，计算分组2到8的时延偏差估计值，设u=0.1。

P13. 回顾 :ref:`第9.3节 <c9.3>` 中VoIP的两种FEC方案。假设第一种方案每四个原始块生成一个冗余块。第二种方案使用传输速率为主流25%的低比特率编码。

a. 每种方案需要多少额外带宽？每种方案增加了多少播放延迟？
b. 若每五个分组中第一个丢失，两种方案表现如何？哪种音质更好？
c. 若每两个分组中第一个丢失，两种方案表现如何？哪种音质更好？

P14.

a. 假设Skype中有N>2人参与音频会议。每位参与者生成一个恒定速率为r bps的数据流。发起者需要发送多少bps？其余N−1名参与者各需发送多少bps？所有参与者的总发送速率是多少？
b. 对使用中心服务器的Skype视频会议重复(a)问题。
c. 对每个参与者向其余N−1人发送视频流副本的情况，重复(b)问题。

P15.

a. 假设我们向互联网发送两个IP数据报，每个携带一个不同的UDP段。第一个数据报的源IP为A1，目的IP为B，源端口为P1，目的端口为T；第二个数据报的源IP为A2，目的IP为B，源端口为P2，目的端口为T。若A1≠A2且P1≠P2，且两者均成功送达，它们会被送到同一个socket吗？请解释。
b. 假设Alice、Bob和Claire想用SIP和RTP进行音频会议。为了发送和接收来自Bob和Claire的RTP包，Alice只需要一个UDP socket（除SIP消息用socket外）吗？如果是，Alice的SIP客户端如何区分来自Bob和Claire的RTP包？

P16. 判断正误：

a. 如果存储视频从Web服务器直接流向媒体播放器，那么应用使用的传输协议是TCP。
b. 使用RTP时，发送方可以在会话中途更改编码格式。
c. 所有使用RTP的应用都必须使用端口87。
d. 若一个RTP会话中每个发送者有独立的音频和视频流，那么这些流使用相同的SSRC。
e. 在区分服务中，尽管每跳行为定义了不同类别的性能差异，但不要求使用特定机制来实现这些性能。

   .. figure:: ../img/809-0.png 
      :align: center

f. 假设Alice想与Bob建立SIP会话。她的INVITE消息中包含：m=audio 48753 RTP/AVP 3（AVP 3表示GSM音频）。因此，Alice表示她希望发送GSM音频。
g. 以上述为基础，Alice在其INVITE消息中表明她将把音频发送到端口48753。
h. SIP消息通常通过默认SIP端口在SIP实体之间发送。
i. 为了维持注册状态，SIP客户端必须周期性发送REGISTER消息。
j. SIP规定所有SIP客户端必须支持G.711音频编码。

P17. 请看下图，显示一个漏桶监管器接收一个分组流。令令牌缓冲区最多容纳两个令牌，且t=0时满。新令牌以每个时隙一个的速率生成。输出链路速度允许在一个时隙开始时两个分组获得令牌并同时通过输出链路。系统定时细节如下：

A. 分组（若有）在每个时隙开始时到达。如图所示，分组1、2、3在时隙0到达。如果队列中已有分组，新的加入队尾。按FIFO顺序前移。
B. 到达处理完后，如果队列中有分组，根据可用令牌数，一个或两个分组会分别消耗一个令牌并在该时隙通过输出链路。因此，在时隙0中，分组1和2各消耗一个令牌并通过输出链路。
C. 若令牌缓冲区未满，则新令牌被加入，因为令牌生成速率为r = 1个/时隙。
D. 时间前进到下一个时隙，重复以上步骤。

请回答下列问题：

a. 对每个时隙，在到达已处理（步骤1）但分组尚未从队列中通过且未消耗令牌之前，指出队列中的分组及桶中的令牌数。例如，在t=0时隙，队列中有分组1、2、3，桶中有两个令牌。
b. 对每个时隙，指出在令牌被消耗后出现在输出链路上的分组。例如，在t=0时隙，分组1和2出现在漏桶的输出链路上。

P18. 重复P17，但假设r=2。仍假设桶最初为满。

P19. 在P18的基础上，假设r=3，桶容量b=2。你对上述问题的答案会改变吗？

P20. 考虑用于监管平均速率和突发大小的漏桶机制。现在我们也希望监管峰值速率p。说明如何将一个漏桶的输出接入第二个漏桶，使这两个串联漏桶监管平均速率、峰值速率和突发大小。请给出第二个漏桶的桶容量和令牌生成速率。

P21. 若一个分组流符合漏桶规范(r, b)，即在任意时间间隔t内，进入漏桶的分组数小于rt+b，则该分组流是否可能在配置为r和b的漏桶处等待？请解释理由。

P22. 证明只要r1<Rw1/(∑ wj)，那么dmax确实是流1中任何分组在WFQ队列中可能经历的最大延迟。

.. toggle::

   P1. Consider the figure below. Similar to our discussion of :ref:`Figure 9.1 <Figure 9.1>` , suppose that video is encoded at a fixed bit rate, and thus each video block contains video frames that are to be played out over the same fixed amount of time, Δ. The server transmits the first video block at t0, the second block at t0+Δ, the third block at t0+2Δ, and so on. Once the client begins playout, each block should be played out Δ time units after the previous block.

   .. figure:: ../img/804-0.png 
      :align: center

   a. Suppose that the client begins playout as soon as the first block arrives at t1. In the figure below, how many blocks of video (including the first block) will have arrived at the client in time for their playout? Explain how you arrived at your answer.
   b. Suppose that the client begins playout now at t1+Δ. How many blocks of video (including the first block) will have arrived at the client in time for their playout? Explain how you arrived at your answer.
   c. In the same scenario at (b) above, what is the largest number of blocks that is ever stored in the client buffer, awaiting playout? Explain how you arrived at your answer.
   d. What is the smallest playout delay at the client, such that every video block has arrived in time for its playout? Explain how you arrived at your answer.

   P2. Recall the simple model for HTTP streaming shown in :ref:`Figure 9.3 <Figure 9.3>` . Recall that B denotes the size of the client’s application buffer, and Q denotes the number of bits that must be buffered before the client application begins playout. Also r denotes the video consumption rate. Assume that the server sends bits at a constant rate x whenever the client buffer is not full.

   a. Suppose that x<r. As discussed in the text, in this case playout will alternate between periods of continuous playout and periods of freezing. Determine the length of each continuous playout and freezing period as a function of Q, r, and x.
   b. Now suppose that x>r. At what time t=tf does the client application buffer become full?

   P3. Recall the simple model for HTTP streaming shown in :ref:`Figure 9.3 <Figure 9.3>` . Suppose the buffer size is infinite but the server sends bits at variable rate x(t). Specifically, suppose x(t) has the following saw-tooth shape. The rate is initially zero at time t=0 and linearly climbs to H at time t=T. It then repeats this pattern again and again, as shown in the figure below.

   .. figure:: ../img/805-0.png 
      :align: center

   a. What is the server’s average send rate?
   b. Suppose that Q=0, so that the client starts playback as soon as it receives a video frame. What will happen?
   c. Now suppose Q>0 and HT/2≥Q. Determine as a function of Q, H, and T the time at which playback first begins.
   d. Suppose H>2r and Q=HT/2. Prove there will be no freezing after the initial playout delay.
   e. Suppose H>2r. Find the smallest value of Q such that there will be no freezing after the initial playback delay.
   f. Now suppose that the buffer size B is finite. Suppose H>2r. As a function of Q, B, T, and H, determine the time t=tf when the client application buffer first becomes full.

   P4. Recall the simple model for HTTP streaming shown in :ref:`Figure 9.3 <Figure 9.3>` . Suppose the client application buffer is infinite, the server sends at the constant rate x, and the video consumption r<x. rate is r with Also suppose playback begins immediately. Suppose that the user terminates the video early at time t=E. At the time of termination, the server stops sending bits (if it hasn’t already sent all the bits in the video).

   a. Suppose the video is infinitely long. How many bits are wasted (that is, sent but not viewed)?
   b. Suppose the video is T seconds long with T>E. How many bits are wasted (that is, sent but not viewed)?

   P5. Consider a DASH system (as discussed in :ref:`Section 2.6 <c2.6>` ) for which there are N video versions (at N different rates and qualities) and N audio versions (at N different rates and qualities). Suppose we want to allow the player to choose at any time any of the N video versions and any of the N audio versions.
   a. If we create files so that the audio is mixed in with the video, so server sends only one media stream at given time, how many files will the server need to store (each a different URL)?
   b. If the server instead sends the audio and video streams separately and has the client synchronize the streams, how many files will the server need to store?

   P6. In the VoIP example in :ref:`Section 9.3 <c9.3>` , let h be the total number of header bytes added to each chunk, including UDP and IP header.

   a. Assuming an IP datagram is emitted every 20 msecs, find the transmission rate in bits per second for the datagrams generated by one side of this application.
   b. What is a typical value of h when RTP is used?

   P7. Consider the procedure described in :ref:`Section 9.3 <c9.3>` for estimating average delay di. Suppose that u=0.1. Let r1−t1 be the most recent sample delay, let r2−t2 be the next most recent sample delay, and so on.

   a. For a given audio application suppose four packets have arrived at the receiver with
   sample delays r4−t4, r3−t3, r2−t2, and r1−t1. Express the estimate of delay d in terms of the four samples.
   b. Generalize your formula for n sample delays.
   c. For the formula in part (b), let n approach infinity and give the resulting formula.

      Comment on why this averaging procedure is called an exponential moving average.

   P8. Repeat parts (a) and (b) in Question P7 for the estimate of average delay deviation.

   P9. For the VoIP example in :ref:`Section 9.3 <c9.3>` , we introduced an online procedure (exponential moving average) for estimating delay. In this problem we will examine an alternative procedure.

   Let ti be the timestamp of the ith packet received; let ri be the time at which the ith packet is
   received. Let dn be our estimate of average delay after receiving the nth packet. After the first packet is received, we set the delay estimate equal to d1=r1−t1.
   
   a. Suppose that we would like dn=(r1−t1+r2−t2+⋯+rn−tn)/n for all n. Give a recursive formula for dn in terms of dn−1, rn, and tn.
   b. Describe why for Internet telephony, the delay estimate described in :ref:`Section 9.3 <c9.3>` is more appropriate than the delay estimate outlined in part (a).

   P10. Compare the procedure described in :ref:`Section 9.3 <c9.3>` for estimating average delay with the procedure in :ref:`Section 3.5 <c3.5>` for estimating round-trip time. What do the procedures have in common? How are they different?

   P11. Consider the figure below (which is similar to :ref:`Figure 9.3 <Figure 9.3>` ). A sender begins sending packetized audio periodically at t=1. The first packet arrives at the receiver at t=8.

   .. figure:: ../img/807-0.png 
      :align: center

   a. What are the delays (from sender to receiver, ignoring any playout delays) of packets 2 through 8? Note that each vertical and horizontal line segment in the figure has a length of 1, 2, or 3 time units.
   b. If audio playout begins as soon as the first packet arrives at the receiver at t=8, which of the first eight packets sent will not arrive in time for playout?
   c. If audio playout begins at t=9, which of the first eight packets sent will not arrive in time for playout?
   d. What is the minimum playout delay at the receiver that results in all of the first eight packets arriving in time for their playout?

   P12. Consider again the figure in P11, showing packet audio transmission and reception times. 

   a. Compute the estimated delay for packets 2 through 8, using the formula for di from :ref:`Section 9.3.2 <c9.3.2>` . Use a value of u=0.1.
   b. Compute the estimated deviation of the delay from the estimated average for packets 2 through 8, using the formula for vi from :ref:`Section 9.3.2 <c9.3.2>` . Use a value of u=0.1.

   P13. Recall the two FEC schemes for VoIP described in :ref:`Section 9.3 <c9.3>` . Suppose the first scheme generates a redundant chunk for every four original chunks. Suppose the second scheme uses a low-bit rate encoding whose transmission rate is 25 percent of the transmission rate of the nominal stream.

   a. How much additional bandwidth does each scheme require? How much playback delay does each scheme add?
   b. How do the two schemes perform if the first packet is lost in every group of five packets? Which scheme will have better audio quality?
   c. How do the two schemes perform if the first packet is lost in every group of two packets? Which scheme will have better audio quality?

   P14.

   a. Consider an audio conference call in Skype with N>2 participants. Suppose each participant generates a constant stream of rate r bps. How many bits per second will the call initiator need to send? How many bits per second will each of the other N−1 participants need to send? What is the total send rate, aggregated over all participants?
   b. Repeat part (a) for a Skype video conference call using a central server.
   c. Repeat part (b), but now for when each peer sends a copy of its video stream to each of the N−1 other peers.

   P15.

   a. Suppose we send into the Internet two IP datagrams, each carrying a different UDP segment. The first datagram has source IP address A1, destination IP address B, source port P1, and destination port T. The second datagram has source IP address A2, destination IP address B, source port P2, and destination port T. Suppose that A1 is different from A2 and that P1 is different from P2. Assuming that both datagrams reach their final destination, will the two UDP datagrams be received by the same socket? Why or why not?
   b. Suppose Alice, Bob, and Claire want to have an audio conference call using SIP and RTP. For Alice to send and receive RTP packets to and from Bob and Claire, is only one UDP socket sufficient (in addition to the socket needed for the SIP messages)? If yes, then how does Alice’s SIP client distinguish between the RTP packets received from Bob and Claire?

   P16. True or false:

   a. If stored video is streamed directly from a Web server to a media player, then the application is using TCP as the underlying transport protocol.
   b. When using RTP, it is possible for a sender to change encoding in the middle of a session.
   c. All applications that use RTP must use port 87.
   d. If an RTP session has a separate audio and video stream for each sender, then the audio and video streams use the same SSRC.
   e. In differentiated services, while per-hop behavior defines differences in performance among classes, it does not mandate any particular mechanism for achieving these performances.

      .. figure:: ../img/809-0.png 
         :align: center

   f. Suppose Alice wants to establish an SIP session with Bob. In her INVITE message she includes the line: m=audio 48753 RTP/AVP 3 (AVP 3 denotes GSM audio). Alice has therefore indicated in this message that she wishes to send GSM audio.
   g. Referring to the preceding statement, Alice has indicated in her INVITE message that she will send audio to port 48753.
   h. SIP messages are typically sent between SIP entities using a default SIP port number.
   i. In order to maintain registration, SIP clients must periodically send REGISTER messages.
   j. SIP mandates that all SIP clients support G.711 audio encoding.

   P17. Consider the figure below, which shows a leaky bucket policer being fed by a stream of packets. The token buffer can hold at most two tokens, and is initially full at t=0. New tokens arrive at a rate of one token per slot. The output link speed is such that if two packets obtain tokens at the beginning of a time slot, they can both go to the output link in the same slot. The timing details of the system are as follows:

   A. Packets (if any) arrive at the beginning of the slot. Thus in the figure, packets 1, 2, and 3 arrive in slot 0. If there are already packets in the queue, then the arriving packets join the end of the queue. Packets proceed towards the front of the queue in a FIFO manner.
   B. After the arrivals have been added to the queue, if there are any queued packets, one or two of those packets (depending on the number of available tokens) will each remove a token from the token buffer and go to the output link during that slot. Thus, packets 1 and 2 each remove a token from the buffer (since there are initially two tokens) and go to the output link during slot 0.
   C. A new token is added to the token buffer if it is not full, since the token generation rate is r = 1 token/slot.
   D. Time then advances to the next time slot, and these steps repeat.

   Answer the following questions:

   a. For each time slot, identify the packets that are in the queue and the number of tokens in the bucket, immediately after the arrivals have been processed (step 1 above) but before any of the packets have passed through the queue and removed a token. Thus, for the t=0 time slot in the example above, packets 1, 2, and 3 are in the queue, and there are two tokens in the buffer.
   b. For each time slot indicate which packets appear on the output after the token(s) have been removed from the queue. Thus, for the t=0 time slot in the example above, packets 1 and 2 appear on the output link from the leaky buffer during slot 0.

   P18. Repeat P17 but assume that r=2. Assume again that the bucket is initially full.

   P19. Consider P18 and suppose now that r=3 and that b=2 as before. Will your answer to the question above change?

   P20. Consider the leaky bucket policer that polices the average rate and burst size of a packet flow. We now want to police the peak rate, p, as well. Show how the output of this leaky bucket policer can be fed into a second leaky bucket policer so that the two leaky buckets in series police the average rate, peak rate, and burst size. Be sure to give the bucket size and token generation rate for the second policer.

   P21. A packet flow is said to conform to a leaky bucket specification (r, b) with burst size b and average rate r if the number of packets that arrive to the leaky bucket is less than rt+b packets in every interval of time of length t for all t. Will a packet flow that conforms to a leaky bucket specification (r, b) ever have to wait at a leaky bucket policer with parameters r and b? Justify your answer.

   P22. Show that as long as r1<Rw1/(∑ wj), then dmax is indeed the maximum delay that any packet in flow 1 will ever experience in the WFQ queue.

编程作业
--------------------------
Programming Assignment

在本实验中，你将实现一个流式视频服务器和客户端。客户端将使用实时流协议（RTSP）控制服务器操作。服务器将使用实时协议（RTP）对视频进行分组，以UDP传输。你将获得部分实现RTSP和RTP功能的Python代码，任务是完成客户端和服务器的代码。当你完成后，你将创建一个客户端-服务器应用程序，具有以下功能：

- 客户端发送SETUP、PLAY、PAUSE和TEARDOWN的RTSP命令，服务器响应这些命令。
- 当服务器处于播放状态时，它周期性地抓取存储的JPEG帧，使用RTP打包，并通过UDP socket发送RTP包。
- 客户端接收RTP包，提取JPEG帧，解压后显示在客户端屏幕上。

提供的代码已实现了服务器端的RTSP协议及客户端的RTP解包逻辑。代码还负责显示视频。你需要实现客户端的RTSP和服务器的RTP部分。该编程作业将显著提升你对RTP、RTSP和流式视频的理解。强烈推荐完成。作业还建议一些可选练习，包括在客户端和服务器中实现RTSP的DESCRIBE命令。你可以在网站 www.pearsonhighered.com/cs-resources 上找到完整的作业细节以及RTSP协议概述。


.. toggle::

   In this lab, you will implement a streaming video server and client. The client will use the real-time streaming protocol (RTSP) to control the actions of the server. The server will use the real-time protocol (RTP) to packetize the video for transport over UDP. You will be given Python code that partially implements RTSP and RTP at the client and server. Your job will be to complete both the client and server code. When you are finished, you will have created a client-server application that does the following:

   - The client sends SETUP, PLAY, PAUSE, and TEARDOWN RTSP commands, and the server responds to the commands.
   - When the server is in the playing state, it periodically grabs a stored JPEG frame, packetizes the frame with RTP, and sends the RTP packet into a UDP socket.
   - The client receives the RTP packets, removes the JPEG frames, decompresses the frames, and renders the frames on the client’s monitor.

   The code you will be given implements the RTSP protocol in the server and the RTP depacketization in the client. The code also takes care of displaying the transmitted video. You will need to implement RTSP in the client and RTP server. This programming assignment will significantly enhance the student’s understanding of RTP, RTSP, and streaming video. It is highly recommended. The assignment also suggests a number of optional exercises, including implementing the RTSP DESCRIBE command at both client and server. You can find full details of the assignment, as well as an overview of the RTSP protocol, at the Web site www.pearsonhighered.com/cs-resources.