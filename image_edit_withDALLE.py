import os
import openai


key= "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"
#openai.api_key = os.environ["OPENAI_API_KEY"]
"""openai.api_key = key
res=openai.Image.create(
  prompt="A cute baby sea otter",
  n=2,
  size="1024x1024"
)
print(res)
"""
openai.api_key = key
openai.Image.create_edit(
  image=open("C:\\Users\HP\\Downloads\\IMG_20220614_071933.jpg", "rb"),
  mask=open("mask.jpg", "rb"),
  prompt="a face with beards",
  n=2,
  size="1024x1024"
)
