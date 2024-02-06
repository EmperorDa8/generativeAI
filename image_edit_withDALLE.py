import os
import openai

key= OPENAI_API_KEY
#openai.api_key = os.environ["OPENAI_API_KEY"]
"""openai.api_key = key
res=openai.Image.create(
  prompt="A male lion in the arctic snow",
  n=2,
  size="1024x1024"
)
print(res)
"""
openai.api_key = key
products=openai.Image.create_edit(
  image=open("C:\\Users\HP\\Downloads\\IMG_20220614_071933.jpg", "rb"),
  mask=open("mask.jpg", "rb"),
  prompt="a face with beards",
  n=2,
  size="1024x1024"
)
print(products)
