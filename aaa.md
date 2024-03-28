# selenium:
- [selenium:](#selenium)
  - [Introduce-The Selenium Browser Automation Project(Selenium 浏览器自动化项目):](#introduce-the-selenium-browser-automation-projectselenium-浏览器自动化项目)
  - [WebDriver:](#webdriver)
    - [Write your first Selenium script:](#write-your-first-selenium-script)
      - [Eight Basic Components(八个基本组件):](#eight-basic-components八个基本组件)
        - [1. Start the session(开始会话)](#1-start-the-session开始会话)
        - [2. Take action on browser(在浏览器上执行操作)](#2-take-action-on-browser在浏览器上执行操作)
        - [3. Request browser information(请求浏览器信息)](#3-request-browser-information请求浏览器信息)
        - [4. Establish Waiting Strategy(建立等待策略)](#4-establish-waiting-strategy建立等待策略)
        - [5. Find an element(查找元素):](#5-find-an-element查找元素)
        - [6. Take action on element(对元素执行操作):](#6-take-action-on-element对元素执行操作)
        - [7. Request element information(请求元素信息):](#7-request-element-information请求元素信息)
        - [8. End the session(结束会话):](#8-end-the-session结束会话)
      - [Whole Code(完整代码):](#whole-code完整代码)
  - [Common use cases of Selenium(Selenium的常见用途):](#common-use-cases-of-seleniumselenium的常见用途)
    - [Web Repetitive Tasks(网页重复任务):](#web-repetitive-tasks网页重复任务)
    - [Web Scraping(网页抓取):](#web-scraping网页抓取)

## Introduce-The Selenium Browser Automation Project(Selenium 浏览器自动化项目):

Selenium is an umbrella project for a range of tools and libraries that enable and support the automation of web browsers.<br>

> 在 "an umbrella project" 中，"umbrella" 的意思是“伞”，在这里是比喻性地指代一个项目或组织，它下面涵盖了多个相关的子项目或组成部分。因此，"an umbrella project" 指的是一个项目或组织，它作为一个整体，覆盖了多个相关的子项目或组成部分。

Selenium 是一个涵盖一系列工具和库的项目，旨在支持和实现对 Web 浏览器的自动化。<br>

It provides extensions(扩展;延伸) to emulate(模仿;模拟) user interaction(交互) with browsers, a distribution server for scaling(扩展性;可伸缩性) browser allocation, and the infrastructure for implementations of the W3C WebDriver specification that lets you write interchangeable code for all major web browsers.<br>

> "distribution": “分发”或“分配”。它指的是 Selenium 提供的服务器，用于分发或分配浏览器资源。

它提供了扩展功能，以模拟用户与浏览器的交互，一个用于扩展浏览器分配的分发服务器，以及实现 W3C WebDriver 规范的基础设施，让您可以为所有主要的 Web 浏览器编写可互换的代码。<br>

🔥🔥🔥This project is made possible by volunteer contributors who have put in thousands of hours of their own time, and made the source code freely available for anyone to use, enjoy, and improve.<br>

🔥🔥🔥这个项目得以实现，要感谢那些自愿贡献者，他们投入了数千小时的个人时间，并免费提供了源代码，供任何人使用、享受和改进。<br>

Selenium brings together browser vendors, engineers, and enthusiasts to further an open discussion around automation of the web platform. The project organises an annual conference to teach and nurture the community.<br>

Selenium 聚集了浏览器供应商、工程师和爱好者，促进了对 Web 平台自动化的开放讨论。该项目每年组织一次会议，旨在教育和培育社区。<br>

At the core of Selenium is [**WebDriver**](https://www.selenium.dev/documentation/webdriver/), an interface to write instruction sets that can be run interchangeably in many browsers. <br>

在 Selenium 的核心是 **WebDriver**，它是一个接口，用于编写可在许多浏览器中可互换运行的指令集。<br>

Once you’ve installed everything, only a few lines of code get you inside a browser. You can find a more comprehensive example in [**Writing your first Selenium script**](https://www.selenium.dev/documentation/webdriver/getting_started/first_script/).<br>

一旦您安装了所有内容，只需几行代码就可以进入一个浏览器。您可以在“编写您的第一个 Selenium 脚本”中找到一个更全面的例子。<br>

不同语言安装方式的链接如下:<br>

```txt
https://www.selenium.dev/downloads/
```

Python语言的安装方式如下:<br>

```bash
pip install selenium
```

```python
from selenium import webdriver


driver = webdriver.Chrome()

driver.get("http://selenium.dev")

driver.quit()
```

See the **Overview** to check the different project components and decide if Selenium is the right tool for you.<br>

请查看概述，检查不同的项目组件，并决定是否 Selenium 是适合您的正确工具。<br>

You should continue on to [**Getting Started**](https://www.selenium.dev/documentation/webdriver/getting_started/) to understand how you can install Selenium and successfully use it as a test automation tool, and scaling simple tests like this to run in large, distributed environments on multiple browsers, on several different operating systems.<br>

您应该继续查看入门指南，了解如何安装 Selenium 并成功将其用作测试自动化工具，以及如何将简单的测试扩展到在多个浏览器、多个不同操作系统的大型分布式环境中运行。<br>


## WebDriver:

If you are beginning with desktop website or mobile website test automation, then you are going to be using WebDriver APIs. <br>

如果你刚开始进行桌面网站或移动网站的测试自动化，那么你将会使用WebDriver API。<br>

WebDriver uses browser automation APIs provided by browser vendors(供应商) to control the browser and run tests. This is as if a real user is operating the browser. <br>

WebDriver利用浏览器供应商提供的浏览器自动化API来控制浏览器并运行测试。这就像一个真实的用户在操作浏览器一样。<br>

Since WebDriver does not require its API to be compiled with application code, it is not intrusive(侵入性的;打扰的). Hence, you are testing the same application which you push live.<br>

由于WebDriver不需要将其API与应用程序代码编译在一起，因此它不会对应用程序造成影响。因此，你正在测试的是发布的同一应用程序。<br>

If you are new to Selenium, we have a few resources that can help you get up to speed right away.<br>

如果你是Selenium的新手，我们有一些资源可以帮助你立即上手。<br>

Selenium supports automation of all the major browsers in the market through the use of WebDriver.<br>

Selenium通过WebDriver支持市场上所有主要的浏览器的自动化。<br>

WebDriver is an API and protocol(协议) that defines a language-neutral interface for controlling the behaviour of web browsers.<br>

WebDriver是一个API和协议，定义了一个语言中立的接口，用于控制浏览器的行为。<br>

Each browser is backed(支持) by a specific WebDriver implementation(实现), called a driver.<br>

每个浏览器都由一个特定的WebDriver实现支持，称为驱动程序。<br>

The driver is the component(组件) responsible for delegating(委派) down to the browser, and handles communication to and from Selenium and the browser.<br>

驱动程序是负责向浏览器委派任务，并处理Selenium与浏览器之间的通信的组件。<br>

This separation(分离) is part of a conscious(有意识的;意识到的) effort to have browser vendors take responsibility for the implementation for their browsers.<br>

这种分离是有意识的努力的一部分，旨在让浏览器供应商为其浏览器的实现负责。<br>

Selenium makes use of these third party drivers where possible, but also provides its own drivers maintained(维护;保持) by the project for the cases when this is not a reality(现实或实际情况).<br>

Selenium尽可能地利用这些第三方驱动程序，但也为那些无法实现的情况提供了由项目维护的自己的驱动程序。<br>

The Selenium framework ties(系;绑;连接) all of these pieces together through a user-facing interface that enables the different browser backends(后端) to be used transparently("透明地"或"清晰地"), enabling cross-browser and cross-platform automation.<br>

> 在文中，"transparently" 指的是以透明的方式或清晰的方式进行操作或执行某项任务，没有隐藏或复杂的过程。这表示 Selenium 框架使得不同浏览器后端可以被透明地使用，即用户无需关注底层细节，就可以实现跨浏览器和跨平台的自动化。

Selenium框架通过用户界面将所有这些部分联系在一起，使不同的浏览器后端可以清晰地使用，实现跨浏览器和跨平台的自动化。<br>

Selenium setup is quite different from the setup of other commercial(商业相关的) tools.<br>

Selenium的设置与其他商业工具的设置非常不同。<br>

🚀🚀🚀Before you can start writing Selenium code, you have to:<br>

🚀🚀🚀在你可以开始编写Selenium代码之前，你必须:<br>

- install the language bindings libraries for your language of choice(安装你选择的语言的语言绑定库)

- the browser you want to use(你想要使用的浏览器)

- the driver for that browser(该浏览器的驱动程序)

### Write your first Selenium script:

Step-by-step instructions(指示、说明或指导) for constructing(建造;构建) a Selenium script.<br>

逐步指南，构建 Selenium 脚本<br>

Once you have Selenium installed, you’re ready to write Selenium code.<br>

一旦你安装了 Selenium，你就可以开始编写 Selenium 代码了。<br>

#### Eight Basic Components(八个基本组件):

Everything Selenium does is send the browser commands to do something or send requests for information.<br>

Selenium 所做的一切都是发送浏览器命令来执行某些操作或发送请求获取信息。<br>

Most of what you’ll do with Selenium is a combination(组合) of these basic commands.<br>

你将使用 Selenium 大部分时间都是在组合这些基本命令。<br>

##### 1. Start the session(开始会话)

For more details on starting a session read our documentation on driver sessions.<br>

有关如何开始会话的更多详细信息，请阅读我们关于驱动程序会话的文档。<br>

```python
driver = webdriver.Chrome()
```

##### 2. Take action on browser(在浏览器上执行操作)

In this example we are navigating to a web page.<br>

在此示例中，我们正在导航到一个网页。<br>

```python
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
```

##### 3. Request browser information(请求浏览器信息)

There are a bunch of types of information about the browser you can request, including window handles, browser size / position, cookies, alerts, etc.<br>

您可以请求关于浏览器的各种类型的信息，包括窗口句柄、浏览器大小/位置、cookie、警报等。<br>

💦💦💦"窗口句柄"是操作系统为了管理窗口而分配给每个窗口的唯一标识符。在 Selenium 中，"window handles" 通常用于引用浏览器窗口的标识符，以便在多个窗口之间进行切换和操作。<br>

💦💦💦游客在使用网页浏览器时不会直接看到窗口句柄。窗口句柄是操作系统为了管理窗口而分配给每个窗口的唯一标识符，它通常在后台被使用。<br>

```python
title = driver.title
```

##### 4. Establish Waiting Strategy(建立等待策略)

Synchronizing(同步) the code with the current state of the browser is one of the biggest challenges with Selenium, and doing it well is an advanced topic.<br>

与当前浏览器状态同步代码是Selenium的最大挑战之一，良好地完成这项任务是一个高级主题。<br>

Essentially(基本上) you want to make sure that the element is on the page before you attempt to locate it and the element is in an interactable state before you attempt to interact with it.<br>

基本上，首先要确保元素出现在页面上后才尝试定位它，并且在尝试与其交互之前，元素处于可交互状态。<br>

An implicit wait is rarely the best solution, but it’s the easiest to demonstrate here, so we’ll use it as a placeholder.<br>

隐式等待很少是最佳解决方案，但它在这里是最容易演示的，因此我们将其用作占位符。<br>

[Read more about Waiting strategies](https://www.selenium.dev/documentation/webdriver/waits/).<br>

```python
driver.implicitly_wait(0.5)
```

🚨🚨🚨implicit wait 是一种等待策略，指定了在查找元素时等待的最长时间，如果在规定的时间内找不到元素，就会抛出异常。<br>

##### 5. Find an element(查找元素):

The majority of commands in most Selenium sessions are element related, and you can’t interact with one without first finding an element.<br>

大多数Selenium会话中的命令都与元素相关，而没有先找到元素，您无法与之交互。<br>

```python
text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
```

##### 6. Take action on element(对元素执行操作):

There are only a handful of actions to take on an element, but you will use them frequently.<br>

对元素执行的操作很少，但您会经常使用它们。<br>

> "Handful" 是一个名词，指的是一把手所能容纳的量，也可以用来形容一小部分、一些或一小批量的东西。在描述数量时，它通常意味着有限的、不多的数量，正好或几乎正好可以用一只手来握住或掌握。

```python
text_box.send_keys("Selenium")
submit_button.click()
```

##### 7. Request element information(请求元素信息):

Elements store a lot of information that can be requested.<br>

元素存储了很多可以请求的信息。<br>

```python
text = message.text
```

##### 8. End the session(结束会话):

This ends the driver process, which by default closes the browser as well. No more commands can be sent to this driver instance. See Quitting Sessions.<br>

这会结束驱动程序进程，默认情况下也会关闭浏览器。无法再向此驱动程序实例发送更多命令。请参阅退出会话。<br>

```python
driver.quit()
```

#### Whole Code(完整代码):

我的代码如下：

```python
# python selenium_test_code.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv

# 加载环境变量
dotenv_path = '.env.local'
load_dotenv(dotenv_path=dotenv_path)

# 设置网络代理环境变量
os.environ['http_proxy'] = os.getenv("HTTP_PROXY")
os.environ['https_proxy'] = os.getenv("HTTPS_PROXY")


driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

title = driver.title

driver.implicitly_wait(0.5)

text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

text_box.send_keys("Selenium")
submit_button.click()

message = driver.find_element(by=By.ID, value="message")
text = message.text

driver.quit()
```

终端信息：

```log
(langchain) root@iZ2zea5v77oawjy2qz7c20Z:/data/chat_system# python selenium_test_code.py 
Traceback (most recent call last):
  File "/data/chat_system/selenium_test_code.py", line 15, in <module>
    driver = webdriver.Chrome()
  File "/root/anaconda3/envs/langchain/lib/python3.10/site-packages/selenium/webdriver/chrome/webdriver.py", line 45, in __init__
    super().__init__(
  File "/root/anaconda3/envs/langchain/lib/python3.10/site-packages/selenium/webdriver/chromium/webdriver.py", line 61, in __init__
    super().__init__(command_executor=executor, options=options)
  File "/root/anaconda3/envs/langchain/lib/python3.10/site-packages/selenium/webdriver/remote/webdriver.py", line 208, in __init__
    self.start_session(capabilities)
  File "/root/anaconda3/envs/langchain/lib/python3.10/site-packages/selenium/webdriver/remote/webdriver.py", line 292, in start_session
    response = self.execute(Command.NEW_SESSION, caps)["value"]
  File "/root/anaconda3/envs/langchain/lib/python3.10/site-packages/selenium/webdriver/remote/webdriver.py", line 347, in execute
    self.error_handler.check_response(response)
  File "/root/anaconda3/envs/langchain/lib/python3.10/site-packages/selenium/webdriver/remote/errorhandler.py", line 229, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.SessionNotCreatedException: Message: session not created: Chrome failed to start: exited normally.
  (session not created: DevToolsActivePort file doesn't exist)
  (The process started from chrome location /usr/bin/google-chrome is no longer running, so ChromeDriver is assuming that Chrome has crashed.)
Stacktrace:
#0 0x557bb674e303 <unknown>
#1 0x557bb64332b7 <unknown>
#2 0x557bb6467b40 <unknown>
#3 0x557bb64636e5 <unknown>
#4 0x557bb64adabc <unknown>
#5 0x557bb64a1123 <unknown>
#6 0x557bb6471095 <unknown>
#7 0x557bb647209e <unknown>
#8 0x557bb67126ab <unknown>
#9 0x557bb67164ba <unknown>
#10 0x557bb66fef85 <unknown>
#11 0x557bb671712f <unknown>
#12 0x557bb66e2e6f <unknown>
#13 0x557bb673b5f8 <unknown>
#14 0x557bb673b7c2 <unknown>
#15 0x557bb674d4a4 <unknown>
#16 0x7fd2f12a16db start_thread

(langchain) root@iZ2zea5v77oawjy2qz7c20Z:/data/chat_system# 
```

## Common use cases of Selenium(Selenium的常见用途):

Most people use Selenium to execute(执行) automated(自动) tests for web applications, but Selenium supports any use case of browser automation.<br>

大多数人使用 Selenium 执行网页应用程序的自动化测试，但 Selenium 支持任何浏览器自动化的用例。<br>

### Web Repetitive Tasks(网页重复任务):

Perhaps you need to log into a website and download something, or submit a form. You can create a Selenium script to run with a service at preset(预设的、预先设定的) times.<br>

也许您需要登录到一个网站并下载一些内容，或者提交一个表单。您可以创建一个 Selenium 脚本，在预设时间与服务一起运行。<br>

### Web Scraping(网页抓取):

Are you looking to collect data from a site that doesn’t have an API?<br>

您是否想从没有 API 的网站收集数据？<br>

Selenium will let you do this, but please make sure you are familiar with the website’s terms of service as some websites do not permit it and others will even block(阻止;阻塞) Selenium.<br>

Selenium 将让您做到这一点，但请确保您熟悉网站的服务条款，因为一些网站不允许这样做，其他网站甚至会阻止 Selenium。<br>


请将下列内容翻译为地道的中文：