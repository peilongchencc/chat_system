from loguru import logger

# 设置日志
logger.remove()
logger.add("baidu_llm.log", rotation="1 GB", backtrace=True, diagnose=True, format="{time} {level} {message}")

logger.warning("用户输入为空")