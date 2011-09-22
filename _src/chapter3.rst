第三章 网络服务器
----------------------------------
学完本章，你将能够编写一个具有完整功能的服务器程序

准备连接
~~~~~~~~~~~~~~~~~

对于建立一个服务器，需要四步：

- 建立 socket 对象
- 设置 socket 选项 （可选的）
- 绑定到个端口 （同样，也可以是一个指定的网卡）
- 侦听连接

这里的代码片断可以实现这样的功能：
::
   
   host = ''
   port = 51423

   # Step 1 ( Create the socket object)
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   
   # Step 2 ( Set the socket options) 
   s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

   # Step 3 ( Bind to a port and interface)
   s.bind((host, port))
   
   # Step 4 ( Listen for connections)
   s.listen(5)

建立 socket 对象
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
和客户端的方法一样： 
::

   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

设置和得到socket选项
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``setsockopt`` 和 ``getsockopt`` 如下:
::

   setsockopt(level, optname, value)
   getsockopt(level, optname, value)

表 setsockopt() 和 getsockopt() 的选项名称

=============== ========================================= ===========================
选项                  意义                                   期望值
=============== ========================================= ===========================
SO_BINDTODEVICE  可以全使socket只在某                          一个字符串给出设备
                 个网络接口（网卡）有效。                         的名称，或者一个空
                 也许不能是移动便携设备                           字符串反回值
--------------- ----------------------------------------- ---------------------------
A                    B                                          C
=============== ========================================= ===========================    
                                                      
下面这段代码将打印出Python所支持的 socket 选项：

.. literalinclude:: ../codes/ch3/sockopts.py
   :linenos:

绑定 socket
^^^^^^^^^^^^^^^^^^^^^^^^
绑定一个端口号，需要执行下面的命令：
::

   s.bind(('', 80))

``bind()`` 函数的第一个参数是要绑定的IP地址，通常为空，表示可以绑定到所有的接口和地址。

侦听连接
^^^^^^^^^^^^^^^^^^^
``listen()`` 允许有多少个未决（等待）的连接在队列中等待。作为一个绽，很多人设置为5。

接受连接
~~~~~~~~~~~~~~~~~~~~~~~~
服务器连续运行的办法是小心的设计一个无限循环。这里有一个基本服务器的例子：

.. literalinclude:: ../codes/ch3/basicserver.py
   :linenos:

为了测试这个服务器程序，你可以使用 ``telnet localhost 51423`` 进行测试。

使用 UDP
~~~~~~~~~~~~~~~~~~~~~~~~
这个代码用来测试UDP客户端

.. literalinclude:: ../codes/ch3/udpechoserver.py
   :linenos:

.. note::
   此代码可以第二章的 ``udp.py`` 结合起来使用。

使用 inetd 或 xinetd
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ubuntu中需要安装 xinetd :
::

   sudo apt-get install xinetd

配置文件在 ``/etc/xinetd.d`` 和 ``/etc/xinetd.conf`` 中。

通过 syslog 来记录日志
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Unix 和类 Unix系统提供了一个称为 syslog 的工具，Python提供了一个很方便的接口。

.. attention::
  syslog工具是不能在Windows上工作的。如果要在Windows工作，可考虑logging模块和NTEventLogHandler()函数。

在 Python 中使用 syslog
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Python 提供了一个可以作为系统syslog程序接口的syslog模块。在开始记录信息之前，必须用openlog()函数来初始化syslog接口，Python如此定义它：

::

   openlog(ident[, logopt[, facility]])

- 第一个参数， ident， 是一个标识字符串，它会被载入到每一条日志信息中，通常是程序的名称，有时候还包含进程ID。

日志系统初始化后，如想实际记录一条信息，可以调用 ``syslog()`` 函数。Python定义如下：
::
 
   syslog([priority,] message)

其中 ``message`` 是一个你想记录的简单字符串。 ``priority`` 表明了这条信息的重要性。下面一个是演示 ``syslog`` 用法的例子：

.. literalinclude:: ../codes/ch3/syslogsample.py
   :linenos:

可以 ``/var/log/syslog`` 查看到错误日志。

避免死锁
~~~~~~~~~~~~~~~~~

