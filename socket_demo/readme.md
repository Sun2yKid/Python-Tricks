# 关于Python Socket 编程

Socket，又称套接字，是一种IPC(Inter-Process Communication进程间通信)方法，
它允许位于同一主机或者使用网络连接的不同主机的应用程序之间交换数据。

socket()系统调用
> fd = socket(domain, type, protocol)

## TCP/IP 跟socket的关系

TCP/IP只是一个协议栈，就像操作系统的运行机制一样，必须要具体实现，同时还要提供对外的操作接口。就像操作系统会提供标准的编程接口，比如Win32编程接口一样，TCP/IP也必须对外提供编程接口，这就是Socket。

## 参考
[Socket Programming in Python (Guide)](https://realpython.com/python-sockets/)
[翻译参考](https://keelii.com/2018/09/24/socket-programming-in-python/)
[Python 标准库](https://docs.python.org/zh-cn/3/library/socket.html?)
[Python 套接字编程指南](https://docs.python.org/zh-cn/3/howto/sockets.html)