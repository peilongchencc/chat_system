

## RunnableLambda

请将下列内容翻译为地道的中文，要求一行英文一行中文：

Run custom functions.

运行自定义函数。

You can use arbitrary(任意的) functions in the pipeline.

您可以在管道中使用任意的函数。

Note that all inputs to these functions need to be a SINGLE argument.

请注意，这些函数的所有输入都需要是一个单一的参数。

If you have a function that accepts multiple arguments, you should write a wrapper that accepts a single input and unpacks it into multiple argument.

如果您有一个接受多个参数的函数，您应该编写一个包装器，它接受一个单一的输入并将其解包成多个参数。

```bash
%pip install –upgrade –quiet langchain langchain-openai
```

具体代码:<br>

```python
from operator import itemgetter

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_openai import ChatOpenAI


def length_function(text):
    return len(text)


def _multiple_length_function(text1, text2):
    return len(text1) * len(text2)


def multiple_length_function(_dict):
    return _multiple_length_function(_dict["text1"], _dict["text2"])


prompt = ChatPromptTemplate.from_template("what is {a} + {b}")
model = ChatOpenAI()

chain1 = prompt | model

chain = (
    {
        "a": itemgetter("foo") | RunnableLambda(length_function),
        "b": {"text1": itemgetter("foo"), "text2": itemgetter("bar")}
        | RunnableLambda(multiple_length_function),
    }
    | prompt
    | model
)

print(chain.invoke({"foo": "bar", "bar": "gah"}))
# AIMessage(content='3 + 9 equals 12.')
```