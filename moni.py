class Pipe:
    def __init__(self, function):
        self.function = function

    def __or__(self, other):
        def combined_function(input):
            return other.function(self.function(input))
        return Pipe(combined_function)

    def __call__(self, input):
        return self.function(input)

# 示例函数
def prompt(input):
    return f"处理的输入: {input}"

def llm(input):
    return f"LLM处理后: {input}"

def output_parser(input):
    return f"解析输出: {input}"

# 包装函数
prompt_pipe = Pipe(prompt)
llm_pipe = Pipe(llm)
output_parser_pipe = Pipe(output_parser)

# 使用"|"操作符链接
pipeline = prompt_pipe | llm_pipe | output_parser_pipe

# 执行
result = pipeline("hello")
print(result)
