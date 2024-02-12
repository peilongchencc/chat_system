请将下列内容翻译为地道的中文：

A unit of work that can be invoked, batched, streamed, transformed and composed.

Key Methods
===========

* invoke/ainvoke: Transforms a single input into an output.
* batch/abatch: Efficiently transforms multiple inputs into outputs.
* stream/astream: Streams output from a single input as it's produced.
* astream_log: Streams output and selected intermediate results from an input.

Built-in optimizations:

* Batch: By default, batch runs invoke() in parallel using a thread pool executor.
            Override to optimize batching.

* Async: Methods with "a" suffix are asynchronous. By default, they execute
            the sync counterpart using asyncio's thread pool.
            Override for native async.

All methods accept an optional config argument, which can be used to configure
execution, add tags and metadata for tracing and debugging etc.

Runnables expose schematic information about their input, output and config via
the input_schema property, the output_schema property and config_schema method.

LCEL and Composition
====================

The LangChain Expression Language (LCEL) is a declarative way to compose Runnables
into chains. Any chain constructed this way will automatically have sync, async,
batch, and streaming support.

The main composition primitives are RunnableSequence and RunnableParallel.

RunnableSequence invokes a series of runnables sequentially, with one runnable's
output serving as the next's input. Construct using the `|` operator or by
passing a list of runnables to RunnableSequence.

RunnableParallel invokes runnables concurrently, providing the same input
to each. Construct it using a dict literal within a sequence or by passing a
dict to RunnableParallel.


For example,

.. code-block:: python

    from langchain_core.runnables import RunnableLambda

    # A RunnableSequence constructed using the `|` operator
    sequence = RunnableLambda(lambda x: x + 1) | RunnableLambda(lambda x: x * 2)
    sequence.invoke(1) # 4
    sequence.batch([1, 2, 3]) # [4, 6, 8]


    # A sequence that contains a RunnableParallel constructed using a dict literal
    sequence = RunnableLambda(lambda x: x + 1) | {
        'mul_2': RunnableLambda(lambda x: x * 2),
        'mul_5': RunnableLambda(lambda x: x * 5)
    }
    sequence.invoke(1) # {'mul_2': 4, 'mul_5': 10}

Standard Methods
================

All Runnables expose additional methods that can be used to modify their behavior
(e.g., add a retry policy, add lifecycle listeners, make them configurable, etc.).

These methods will work on any Runnable, including Runnable chains constructed
by composing other Runnables. See the individual methods for details.

For example,

.. code-block:: python

    from langchain_core.runnables import RunnableLambda

    import random

    def add_one(x: int) -> int:
        return x + 1


    def buggy_double(y: int) -> int:
        '''Buggy code that will fail 70% of the time'''
        if random.random() > 0.3:
            print('This code failed, and will probably be retried!')
            raise ValueError('Triggered buggy code')
        return y * 2

    sequence = (
        RunnableLambda(add_one) |
        RunnableLambda(buggy_double).with_retry( # Retry on failure
            stop_after_attempt=10,
            wait_exponential_jitter=False
        )
    )

    print(sequence.input_schema.schema()) # Show inferred input schema
    print(sequence.output_schema.schema()) # Show inferred output schema
    print(sequence.invoke(2)) # invoke the sequence (note the retry above!!)

Debugging and tracing
=====================

As the chains get longer, it can be useful to be able to see intermediate results
to debug and trace the chain.

You can set the global debug flag to True to enable debug output for all chains:

    .. code-block:: python

        from langchain_core.globals import set_debug
        set_debug(True)

Alternatively, you can pass existing or custom callbacks to any given chain:

    .. code-block:: python

        from langchain_core.tracers import ConsoleCallbackHandler

        chain.invoke(
            ...,
            config={'callbacks': [ConsoleCallbackHandler()]}
        )

For a UI (and much more) checkout LangSmith: https://docs.smith.langchain.com/



langchain中 `chain = prompt | llm | output_parser` 的"|"操作是什么意思？如何实现类似于LangChain中的"|"操作符功能，请给出示例代码，并解释代码的执行逻辑。