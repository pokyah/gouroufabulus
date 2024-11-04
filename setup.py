import os
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv('HF_TOKEN')
print(HF_TOKEN)

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
print(OPENAI_API_KEY)
# from https://huggingface.co/blog/tgi-messages-api#create-an-inference-endpoint
# and from https://huggingface.co/learn/cookbook/en/tgi_messages_api_demo

# endpoint = create_inference_endpoint(
#     "nous-hermes-2-mixtral-8x7b-demo",
#     repository="NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO",
#     framework="pytorch",
#     task="text-generation",
#     accelerator="gpu",
#     vendor="aws",
#     region="us-east-1",
#     type="protected",
#     instance_type="nvidia-a100",
#     instance_size="x2",
#     custom_image={
#         "health_route": "/health",
#         "env": {
#             "MAX_INPUT_LENGTH": "4096",
#             "MAX_BATCH_PREFILL_TOKENS": "4096",
#             "MAX_TOTAL_TOKENS": "32000",
#             "MAX_BATCH_TOTAL_TOKENS": "1024000",
#             "MODEL_ID": "/repository",
#         },
#         "url": "ghcr.io/huggingface/text-generation-inference:sha-1734540", # use this build or newer
#     },
# )

# endpoint.wait()
# print(endpoint.status)


