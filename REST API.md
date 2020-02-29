## REST API 

Representational State Transfer 表现层状态转移

Roy Fielding 在其博士论文“Architectural Styles and the Design of Network-based Software Architectures”的第 5 章中描述了 Web 服务的 REST 架构方式


* REST将数据作为资源来访问，表现形式反映在URI中，由此定位资源；

* C/S架构，客户端和服务端的信息交流是通过无状态的HTTP协议，传递资源的表现层；

* 对资源的操作，主要就是一些增删改查，体现在http的集中请求方式上，通过HTTP动词来描述操作；

* 请求体资源的表现形式，使用请求头的content-type为json或xml编码方式，以及通用的响应状态码；

* 使用版本嵌入url的方式方便版本更新和向下兼容；