# IOC vs DI

##Overview:

## What's IOC?

Refernce: https://dzone.com/articles/ioc-vs-di


“IoC is when you have someone else create objects for you.” So instead of writing “new MyObject” in your code, the object is created by someone else. This ‘someone else’ is normally referred to as an IoC container.


IoC is much more than object creation: a Spring Context or a Servlet Container not only create objects, but manage their entire lifecycle

That includes creating objects, destroying them, and invoking certain methods of the object at different stages of its lifecycle. These methods are often described as callbacks


## What's Bean?

Spring-managed objects, as you likely know, are called Beans
 
## What's DI?

Dependency Injection has become one of the cornerstones of modern software engineering, as it is fundamental to allow proper testing.

To put it simply, having DI is the opposite to having hardcoded dependencies.


In simple words, its injection of dependencies.