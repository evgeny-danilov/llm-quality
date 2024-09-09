class LlmModels:
    class GPT:
        gpt_4_turbo = 'gpt-4-turbo'
        gpt_4_0125 = 'gpt-4-0125-preview'
        gpt_4o = 'gpt-4o'
        gpt_35_8K = 'gpt-3.5-turbo'
        gpt_35_16k = 'gpt-35-turbo-16k'
        gpt_35_0125 = 'gpt-35-turbo-0125'
        text_embedding_3_large = 'text-embedding-3-large'
        text_embedding_3_small = 'text-embedding-3-small'

    class Amazon:
        Titan_Text_G1_Express = "amazon.titan-text-express-v1"
        Titan_Text_G1_Lite = "amazon.titan-text-lite-v1"
        Titan_Embeddings_G1_Text = "amazon.titan-embed-text-v1"
        Titan_Multimodal_Embeddings_G1 = "amazon.titan-embed-image-v1"
        Titan_Image_Generator_G1 = "amazon.titan-image-generator-v1"

    class Anthropic:
        Claude_2 = "anthropic.claude-v2"
        Claude_2_1 = "anthropic.claude-v2:1"
        Claude_3_Sonnet = "anthropic.claude-3-sonnet-20240229-v1:0"
        Claude_35_Sonnet = "anthropic.claude-3-5-sonnet-20240620-v1:0"
        Claude_3_Haiku = "anthropic.claude-3-haiku-20240307-v1:0"
        Claude_Instant = "anthropic.claude-instant-v1"

    class AI21_Labs:
        Jurassic_2_Mid = "ai21.j2-mid-v1"
        Jurassic_2_Ultra = "ai21.j2-ultra-v1"

    class Cohere:
        Command = "cohere.command-text-v14"
        Command_Light = "cohere.command-light-text-v14"
        Embed_English = "cohere.embed-english-v3"
        Embed_Multilingual = "cohere.embed-multilingual-v3"

    class Meta:
        Llama_2_Chat_13B = "meta.llama2-13b-chat-v1"
        Llama_2_Chat_70B = "meta.llama2-70b-chat-v1"
        Llama_3_Instruct_70B = "meta.llama3-70b-instruct-v1:0 "

    class Mistral_AI:
        Mistral_7B_Instruct = "mistral.mistral-7b-instruct-v0:2"
        Mixtral_8X7B_Instruct = "mistral.mixtral-8x7b-instruct-v0:1"

    class Stability_AI:
        Stable_Diffusion_XL = "stability.stable-diffusion-xl-v0"
        Stable_Diffusion_XL_1 = "stability.stable-diffusion-xl-v1"
