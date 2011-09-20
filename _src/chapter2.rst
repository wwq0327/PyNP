第二章 网络客户端
---------------------------------

学习如何在客户端实现一个应用程序协议，或是修改，扩展一个已经存在的Python模块。

理解 socket
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

socket 是操作系统中 I/O 系统的延伸部分，它可以使进程序和机器之间的通信成为可能。

以前经常使用的 socket ，最早起源于 BSD UNIX 类的操作系统。在Unix系统上，比如BSD，有一些现有的，和文件描述符一起工作的系统调用，其中包括 ``open()`` / ``read()`` / ``write()`` 和 ``close()`` 。

把对网络的支持加入操作系统，是以一种扩展现有文件描述符结构的方法来实现。新的系统周用被加入并和 socket 一起工作，而很多的系统调用同样能和 socket 一起工作。因此，一个 socket 允许你使用标准的操作系统和其它计算机，以及你自己机器上的不同进程来通信。

在某些方面，socket 可以被看成一个标准的文件描述符。然后，socket 的确存在一些不同的工作方式。最明显的是建立 socket 的方法。文件调用使用 ``open()`` 来打开，而 socket 是通过 ``socket()`` 函数来建立的，并且还需要另外的调用来连接和激活他们。``recv()`` 和 ``send()`` 这两个系统调用和 ``read()`` 和 ``write()`` 极为相似。``send()`` 和 ``recv()`` 调用提供了 socket 额外特有的功能。

Python 通过 socket 模块提供访问操作系统 socket 库的接口。建立socket 的时候，只需要调用这个模块的函数和常量。

建立 socket
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
对于一个客户端来说，建立一个socket 需要两个步骤：

- 建立一个实际的socket对象

  - 通信协议 ： 指明用什么协议来传输数据

    - IPv4 ( AF_INET )
    - IPv6
    - IPX/SPX(NetWare)
    - AFP(Apple文件共享)

  - 协议家族 ： 定义数据如何被传输

    - TCP ( SOCK_STREAM )
    - UDP ( SOCK_DGRAM )

- 需要把它连接到远程服务器上

对于TCP通信，建立一个 socket 连接，一般用类似这样的代码：

::

   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

连接 socket ，一般需要提供一个 tuple，它包含远程主机名或IP地址和远程端口，连接一个socket 一般用类似这样的代码：
::
 
   s.connect(("www.example.com", 80))

下面的程序建立一个连接并马上终止。

.. literalinclude:: ../codes/ch2/connect.py
   :linenos:

连接到 ``www.google.com`` 上的Web服务器，接着打印状态信息，最后终止。

.. attention::
   C语言的 ``connect()`` 函数需要远程机器的IP地址，在Python中，socket对象的 ``connect()`` 函数会根据需要得用DNS把域名自动转换为IP地址，但是对端口号则不是这样。

寻找端口
^^^^^^^^^^^^^^^^^
Python 的 socket 库包含一个 ``getservbyname()`` 的函数，它可以自动查询服务器端口号。在UNIX系统中，可以 ``/etc/services`` 目录下找到这个列表。

为了查询这个列表，需要两个参数：协议名和端口名。端口名是一个字符串，对应相应的端口，如 ``http`` 端口名对应 ``80`` 这个端口号。

程序： 

.. literalinclude:: ../codes/ch2/connect2.py
   :linenos:

.. attention::
   此程序在Windows下会报错。列表文件，只有*nux下才会存在。

从socket获取信息
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
一旦建立了连接，就可以从那里得到一些有用的信息。下面这个例子演示了这些功能 [#]_ 。

.. literalinclude:: ../codes/ch2/connect3.py
   :linenos:

.. note::
   客户端的IP端口会自动分配，每次运行本程序，端口都会发生变化。

利用 socket 通信
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Python提供两种通信方法：

- socket对象 -- ``send()`` / ``sendto()`` / ``recv()`` / ``recvfrom()`` 调用的接口。
- 文件对象 -- ``read()`` / ``write()`` / ``readline()`` 

处理错误
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

socket 异常
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: ../codes/ch2/socketerrors.py
   :linenos:

Python socket模块定义了四种可能出现的异常：

- 与一般 I/O 和通信问题有关的 ``socket.error``
- 与查询地址信息有关的 ``socket.gaierror``
- 与其它地址错误有关的 ``socket.herror`` (和 C 语言中的 ``h_errno`` 相关)
- 与在一个 socket 上调用 ``settimeout()`` 后，处理超时有关的 ``socket.timeout`` ( 需要 python 2.3+ 版本 )

上例中可产生两个错误：

- 如果主机名不对则产生 ``socket.gaierror`` 
- 如果连接远程主机有问题则产生 ``socket.error``

遗漏的错误
^^^^^^^^^^^^^^^^^^^^^^^

文件对象引起的错误
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

使用 UDP
~~~~~~~~~~~~~~~~~~~

UDP 通信几乎不使用文件类对象。下面是一个 UDP 客户端：

.. literalinclude:: ../codes/ch2/udp.py
   :linenos:

提供两个参数，一个主机名，一个服务器端口。因为不知服务何时回应，所以会进出一个无限循环。

与TCP客户端的区别：

- 调用 ``SOCK_DGRAM``
- 使用 ``UDP`` 通信
- 寻找端口号用的是 ``udp``
- 程序没办法探测到服务器什么时候发送完整数据。

有时， 使用UDP可根本不用调用 ``connect()`` ，这个例子：

.. literalinclude:: ../codes/ch2/udptime.py
   :linenos:

这个程序是一个 ``RFC868`` 上定义的简单时间协议的示范。

总结
~~~~~~~~~~~~~~~

- 网络通信基本接口是 socket， 它扩展了操作系统基本 I/O 到网络通信。
- socket 可通过 ``socket()`` 函数来建立， 通过 ``connect()`` 来连接。
- 得到socket，可以确定本地和远程端点的IP地址和端口号。
- socket 对不同的协议来说都是一种通用的接口，它可以处理 TCP 和 UDP 通信。
- 使用 ``shutdown()`` 可以确保当有写错误发生时，能获得提醒。
- Python提供两种和 socket 工作的接口： 用于 UDP 和高级的 TCP 目的的标准 socket 接口，以及用于简单 TCP 通信的文件类接口。

.. rubric:: Footnotes

.. [#] Windows下执行本程序会报错。

