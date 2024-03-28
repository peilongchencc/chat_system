"""
Auth:peilongchencc@163.com
Description:语音识别(wav文件)-cpu版本
Prerequisite:
```bash
pip install librosa soundfile
```
这两个库通常用于音频处理和分析任务,其中librosa用于音频和音乐分析,而soundfile用于读取和写入音频文件。
Reference link:
Note:
"""
import torch
from transformers import AutoProcessor, WhisperForConditionalGeneration
from datasets import load_dataset, Audio
import os
from dotenv import load_dotenv

# 加载环境变量
dotenv_path = '.env.local'
load_dotenv(dotenv_path=dotenv_path)

# 设置网络代理环境变量
os.environ['http_proxy'] = os.getenv("HTTP_PROXY")
os.environ['https_proxy'] = os.getenv("HTTPS_PROXY")

processor = AutoProcessor.from_pretrained("openai/whisper-tiny.en")
model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-tiny.en")

# 注意这里我们不再调用 model.cuda()，因为我们要在CPU上运行模型
# model.cuda()  # 已删除此行

# 加载音频数据，时间超过30秒
ds = load_dataset("distil-whisper/meanwhile", "default")["test"]
# 重采样到16kHz
ds = ds.cast_column("audio", Audio(sampling_rate=16000))
# 取前8个音频并提取数组
audio = ds[:8]["audio"]
audio = [x["array"] for x in audio]

# 确保不截断输入音频，返回`attention_mask`，并填充到最长音频
inputs = processor(audio, return_tensors="pt", truncation=False, padding="longest", return_attention_mask=True, sampling_rate=16_000)

# 将数据移动到CPU（如果您的电脑没有GPU），注意这里的变化
inputs = inputs.to("cpu", torch.float32)  # 之前是 .to("cuda", torch.float32)

# 转录音频到ids
generated_ids = model.generate(**inputs)

# 解码生成的ids以得到转录文本
transcription = processor.batch_decode(generated_ids, skip_special_tokens=True)
print(transcription[0])

print(f"测试")
print(transcription)
print(len(transcription))
"""
Terminal output:
Folks, if you watch the show, you know, I spent a lot of time right over there. Patiently and astutely scrutinizing the boxwood and mahogany chest set of the day's biggest stories developing the central headline pawns, definitely maneuvering an oso topical night to F6, fainting a classic Sicilian, nade door variation on the news, all the while seeing eight moves deep and patiently marshalling the latest press releases into a fisher's shows in Lip Nitsky attack that culminates in the elegant lethal slow-played, all-passant checkmate that is my nightly monologue. But sometimes, sometimes, folks, I. CHEERING AND APPLAUSE Sometimes I startle away, cubside down in the monkey bars of a condemned playground on a super fun site. Get all hept up on goofballs. Rummage that were discarded tag bag of defective toys. Yank out a fist bowl of disembodied doll limbs, toss them on a stained kid's place mat from a defunct dennies. set up a table inside a rusty cargo container down by the Wharf and challenged toothless drifters to the godless bughouse blitz of tournament that is my segment. Meanwhile.
"""