import gradio as gr

if __name__ == "__main__":
    block = gr.Blocks()
    with block as demo:
        gr.Markdown("""<h1><center>LangChain-ChatLLM-Webui</center></h1>
        <center><font size=3>
        本项目基于LangChain和大型语言模型系列模型, 提供基于本地知识的自动问答应用. <br>
        目前项目提供基于<a href='https://github.com/THUDM/ChatGLM-6B' target="_blank">ChatGLM-6B </a>的LLM和包括GanymedeNil/text2vec-large-chinese、nghuyong/ernie-3.0-base-zh、nghuyong/ernie-3.0-nano-zh在内的多个Embedding模型, 支持上传 txt、docx、md、pdf等文本格式文件. <br>
        后续将提供更加多样化的LLM、Embedding和参数选项供用户尝试, 欢迎关注<a href='https://github.com/thomas-yanxin/LangChain-ChatGLM-Webui' target="_blank">Github地址</a>.
        </center></font>
        """)
        with gr.Row():
            with gr.Column(scale=1):
                model_choose = gr.Accordion("模型选择")
                with model_choose:
                    large_language_model = gr.Dropdown(
                        ["llm1","llm2"],
                        label="large language model",
                        value="llm1")

                    embedding_model = gr.Dropdown(
                        ["emb1","emb2"],
                        label="Embedding model",
                        value="emb1")
                    load_model_button = gr.Button("重新加载模型")
                model_argument = gr.Accordion("模型参数配置")
                with model_argument:
                    top_k = gr.Slider(1,
                                      10,
                                      value=6,
                                      step=1,
                                      label="vector search top k",
                                      interactive=True)
                    history_len = gr.Slider(0,
                                            5,
                                            value=3,
                                            step=1,
                                            label="history len",
                                            interactive=True)
                    temperature = gr.Slider(0,
                                            1,
                                            value=0.01,
                                            step=0.01,
                                            label="temperature",
                                            interactive=True)
                    top_p = gr.Slider(0,
                                      1,
                                      value=0.9,
                                      step=0.1,
                                      label="top_p",
                                      interactive=True)

                file = gr.File(label='请上传知识库文件',
                               file_types=['.txt', '.md', '.docx', '.pdf'])

            with gr.Column(scale=4):
                chatbot = gr.Chatbot([[None, None]],
                                     label='ChatLLM').style(height=750)
                message = gr.Textbox(label='请输入问题')
                state = gr.State()

                with gr.Row():
                    clear_history = gr.Button("🧹 清除历史对话")
                    send = gr.Button("🚀 发送")
        gr.Markdown("""提醒：<br>
        1. 使用时请先上传自己的知识文件，并且文件中不含某些特殊字符，否则将返回error. <br>
        2. 有任何使用问题，请通过[Github Issue区](https://github.com/thomas-yanxin/LangChain-ChatGLM-Webui/issues)进行反馈. <br>
        """)
    # threads to consume the request
    demo.queue(concurrency_count=3) \
        .launch(server_name='0.0.0.0', # ip for listening, 0.0.0.0 for every inbound traffic, 127.0.0.1 for local inbound
                server_port=7860, # the port for listening
                show_api=False, # if display the api document
                share=True, # if register a public url
                inbrowser=True) # if browser would be open automatically
