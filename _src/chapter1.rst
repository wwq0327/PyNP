第一章 客户/服务器网络介绍
------------------------------------------------------------

理解 TCP 基础
~~~~~~~~~~~~~~~~~~~~~~~~~~

- TCP/IP是一些协议（Protocols）的合集。当前大多数使用中的通信都使用TCP协议。
- Internet是在一些共享的线路上发送数据的。
- 为了实现共享，TCP是通过把你要发送的数据流分解成很多小信息包在Internet上传输的（也许伴有其它程序的信息包），而这些信息包到了接收都的地方会再次重新合成在一起。


寻址
^^^^^^^^^^^^^

- 不同的程序分配不同的端口。
- 每个TCP连接的端点是由一个IP地址和一个端口号来唯一标识的。


可靠性
^^^^^^^^^^^^^^

- 每个信息包都包含一个 **校检码** .
- 收到的每个信息包都会反馈一下。
- 每个信息包都会传送一个序号。

路由
^^^^^^^^^^^^^^

信息包会经过不同的网络。在Internet上负责接收信息包并决定如何把它们传输到目的地的设备叫 **路由** 。

安全
^^^^^^^^^^^^^^

SSL 一般在TCP连接之上，与程序代码混合在一层。它提供服务器的认证/加密/数据完整性。TLS的原理与SSL非常类似。

使用客户/服务器模式
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TCP/IP 对于 **客户/服务器** 类型的通信很有帮助。在客户/服务器结构下， **服务器** 一直在侦听来自 **客户端** 的请求，有请求后，就建立连接来处理它们。

服务器端端口号
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

在 C/S 模式中，服务器通常用是侦听一个大家都知道的端口号。

- 国际因特网地址分配委员会（Internet Assigned Numbers Authorith，IANA）维护的官方已分配的端口列表。在Linux或Unix系统中，在 ``/etc/services`` 下可找到这个列表。

如果我所编写的服务器不在这个列表上，就应该选择一个大于1024的端口。这样可尽量避免和其它服务冲突，端口号最大为 **65535** 。

客户端端口号
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
不很重要。

理解UDP
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

UDP，它被用来从一个系统向其它系统传送非常短的消息，它只提供一个保证：那就是你所收到的数据是完整的。不保证是否真的收到，也不保证只收到一次。还不能保证收到的信息次序是否和发送的时候一致。但只要没有受到攻击，通过 UDP 接收到的数据通常都会是完整的。

它比 TCP 低级， TCP 建立和关闭连接都需要时间，而 UDP 对连接没有什么概念，所以不存在花费时间建立和关闭连接。

UDP用的最广泛的在应用软件的DNS系统。

你应该用　TCP，如果：

- 需要一个可靠的数据传输，以低保数据完整无缺的达到目的地。
- 协议需要不止一个请求和服务器的回答。
- 要发送较多的数据。
- 初始连接出现短暂的延迟是可以容忍的。

你应该用 UDP，如果：

- 不太关心信息包是否到达或者不丰在意信息包到达的顺序是否正确，再或者可以自己察觉这些问题并自己解决。
- 协议只包括基本请求和回答。
- 需要尽快建立网络会话。
- 只传送很少一部分数据。UDP的限制是一个信息包不超过 **64K** ，通常人们只用UDP传送 **1K** 以下的数据。

理解物理传输和以太网
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TCP/IP有一个优点，就是可以在不同的物理网络硬件之间传送数据。比较常见的：

- 以太网
- 端对端(PPP, Peer-Peer Protocol)
- 令牌环网络
- DSL连接
- Cable Modems连接
- 人造卫星连接
- 移动电话以及如T1那样的专线连接

Python 网络编程
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

底层接口
^^^^^^^^^^^^^^^^^^^
Python 提供了访问底层操作系统 Socket 接口的全部方法，需要的时候这些接口可能为你提供灵活而强有力的功能。

基本客户端操作
'''''''''''''''''''''''
一个简单的Python客户端程序：

.. literalinclude:: ../codes/ch1/gopherclient.py
   :linenos:

这是在现实世界中能找到的、可能运行的网络协议实现的最小程序。它实现的是 Gopher 协议，一种Web出现之前在Internet上非常流行的协议。这个程序需要两个命令行参数：主机名和文件名，实现从主机上请求相关文档的功能。

它通过调用 ``socket.socket()`` 来建立一个 Socket 。参数告诉系统需要一个Internet socket来进行TCP通信。接着，程序连接远程主机并提供文件名。最后获得响应后，在屏幕上打印下来。

使用：
::

    python gopherclient.py quux.org /

你将得到Gopher服务器根目录的文件列表。

错误和异常
'''''''''''''''''''''

Python会自动检查错误，并在有错误发生时产生异常，如果给出一个不存在的主机名，如：
::

    wyatt@wyatt-desktop:~/git/PyNP/codes/ch1$ python gopherclient.py quuxxxxxxxxxxx.org /
    Traceback (most recent call last):
      File "gopherclient.py", line 24, in <module>
        s.connect((host, port))
      File "/usr/lib/python2.7/socket.py", line 224, in meth
        return getattr(self._sock,name)(*args)
    socket.gaierror: [Errno -5] No address associated with hostname

Python会检测到错误并产生一个 ``socket.gaierror`` 异常。因为程序没有处理异常，修改之后：

.. literalinclude:: ../codes/ch1/gopherclient2.py
   :language: python
   :linenos:

这样在尝试连接到一个不存在的服务器时会得到比较友好的错误信息。

.. note::

   sendall()函数能一次性发送所有数据，如果有错误，它会产生异常;否则，表明信息发送成功。

文件对象
'''''''''''''''''''''''

Python 程序员会熟悉文件对象的方法： ``readline()`` 、 ``write()`` 、 ``read()`` 等。Socket不提供类似的接口，但提供了一个 ``makefile()`` 函数来生成供你使用的文件类对象。下面功能相同的例子，则是使用文件类接口重写：

.. literalinclude:: ../codes/ch1/gopherclient3.py
   :linenos:

基本服务器操作
'''''''''''''''''''''''''

用Python编写服务器程序同样很简单，例如：

.. literalinclude:: ../codes/ch1/server.py
   :linenos:

使用方法：

- 服务器端： ``python server.py``
- 客户端： ``telnet localhost 51423`` 
- 客户端输入信息后会得到相应的字符数量回馈。

在Ubuntu下，看起来像这样：
::

   wyatt@wyatt-desktop:~/git/PyNP$ telnet localhost 51432
   Trying 127.0.0.1...
   Connected to localhost.
   Escape character is '^]'.
   Please enter a string: hello
   You entered 5 characters.
   Connection closed by foreign host.

高级接口
^^^^^^^^^^^^^^^^^

使用Python已提供的协议来解决编程问题，例如：

.. literalinclude:: ../codes/ch1/download.py
   :linenos:

使用方法：
::

   python download.py http://mirrors.163.com/debian/ls-lR.gz | gunzip |more

这个命令可以解开压缩数据并发送。

总结
~~~~~~~~~~

- TCP/IP 协议可以用于多种不同的传输。每一个终端是靠唯一的IP地址和端口号来区分的。
- 服务器通过一些事先知道的端口来侦听连接。当一个客户端连接时，它的操作系统通常会选择一个事先不知道的端口号。
- 有两种常的数据传输协议： TCP， 可能提供高可靠性和完整的会话;UDP， 用于小且简短但是快速的会话。
- 大多数人用Python编写网络程序，要么自己设计协议， 要么用一些内置的模块来实现一些已经存在的协议。对那些自己设计协议的人来说，Python提供了全面的socket接口，而C语言网络程序员会觉得很熟悉。
