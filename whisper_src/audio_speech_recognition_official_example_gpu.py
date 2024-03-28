"""
Auth:peilongchencc@163.com
Description:语音识别(wav文件)-gpu版本
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
model.cuda()

# load audios > 30 seconds
ds = load_dataset("distil-whisper/meanwhile", "default")["test"]
# resample to 16kHz
ds = ds.cast_column("audio", Audio(sampling_rate=16000))
# take first 8 audios and retrieve array
audio = ds[:8]["audio"]
audio = [x["array"] for x in audio]

# make sure to NOT truncate the input audio, to return the `attention_mask` and to pad to the longest audio
inputs = processor(audio, return_tensors="pt", truncation=False, padding="longest", return_attention_mask=True, sampling_rate=16_000)
inputs = inputs.to("cuda", torch.float32)

# transcribe audio to ids
generated_ids = model.generate(**inputs)

transcription = processor.batch_decode(generated_ids, skip_special_tokens=True)
print(transcription[0])