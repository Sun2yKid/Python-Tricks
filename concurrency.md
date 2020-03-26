
## Gevent
> gevent是一个基于libev的并发库。它为各种并发和网络相关的任务提供了整洁的API。gevent中用到的主要模式就是前面说的 greenlet（以C扩展模块形式接入Python的轻量级协程）。
https://github.com/selfboot/CS_Offer/blob/master/Python/Coroutine.md


## python 协程与go协程的区别

https://www.cnblogs.com/lgjbky/p/10838035.html


## Actor模型
Don’t communicate by sharing memory, share memory by communicating
“不要以共享内存的方式来通信，相反，要通过通信来共享内存。”
通过消息通信的机制来避免竞态条件
https://www.cnblogs.com/zhanlang/p/10585749.html
> 一般来说有两种策略用来在并发线程中进行通信：共享数据和消息传递。使用共享数据方式的并发编程面临的最大的一个问题就是数据条件竞争。处理各种锁的问题是让人十分头痛的一件事。

> 实现消息传递有两种常见的类型：基于channel（golang为典型代表）的消息传递和基于Actor（erlang为代表）的消息传递。
 
 
> Actor模型(Actor model)首先是由Carl Hewitt在1973定义， 由Erlang OTP 推广，其 消息传递更加符合面向对象的原始意图。Actor属于并发组件模型，通过组件方式定义并发编程范式的高级阶段，避免使用者直接接触多线程并发或线程池等基础概念。

> Actor模型(Actor model)首先是由Carl Hewitt在1973定义， 由Erlang OTP 推广，其 消息传递更加符合面向对象的原始意图。Actor属于并发组件模型，通过组件方式定义并发编程范式的高级阶段，避免使用者直接接触多线程并发或线程池等基础概念。


> Actor模型=数据+行为+消息。

> Actor模型是一个通用的并发编程模型，而非某个语言或框架所有，几乎可以用在任何一门编程语言中，其中最典型的是erlang，在语言层面就提供了Actor模型的支持，杀手锏应用RabbitMQ 就是基于erlang开发的

> Actor内部是以单线程的模式来执行的，类似于redis，所以Actor完全可以实现分布式锁类似的应用。

> 每个Actor都有一个专用的MailBox来接收消息，这也是Actor实现异步的基础。

http://jolestar.com/parallel-programming-model-thread-goroutine-actor/
> Actor的概念其实和OO里的对象类似，是一种抽象。面对对象编程对现实的抽象是对象=属性+行为（method），但当使用方调用对象行为（method）的时候，其实占用的是调用方的CPU时间片，是否并发也是由调用方决定的。这个抽象其实和现实世界是有差异的。现实世界更像Actor的抽象，互相都是通过异步消息通信的。


## Go的CSP并发模型
https://www.cnblogs.com/sunsky303/p/9115530.html
> Go实现了两种并发形式。第一种是大家普遍认知的：多线程共享内存。其实就是Java或者C++等语言中的多线程开发。另外一种是Go语言特有的，也是Go语言推荐的：CSP（communicating sequential processes）并发模型。
> Go线程实现模型MPG
M指的是Machine，一个M直接关联了一个内核线程。
P指的是”processor”，代表了M所需的上下文环境，也是处理用户级代码逻辑的处理器。
G指的是Goroutine，其实本质上也是一种轻量级的线程。

全局runqueue是各个P在运行完自己的本地的Goroutine runqueue后用来拉取新goroutine的地方。P也会周期性的检查这个全局runqueue上的goroutine