import gradio as gr
from api import generate_role_NameandInfo,get_characterglm_response
import json

class CharacterAgent:
    def __init__(self, messages, user_name, user_info, bot_name, bot_info):
        self.messages = messages
        self.user_name = user_name
        self.user_info = user_info
        self.bot_name = bot_name
        self.bot_info = bot_info

    def chat(self, message):
        self.messages.append(message)
        return message


def generate_dialogue(character_meta_1, character_meta_2):
	# 生成角色1的人设信息
	role_1 = json.loads("".join(generate_role_NameandInfo(character_meta_1)))
	# 生成角色2的人设信息
	role_2 = json.loads("".join(generate_role_NameandInfo(character_meta_2)))

	role_1_name = role_1['name']
	role_1_info = role_1['info']
	role_2_name = role_2['name']
	role_2_info = role_2['info']

	character_1 = CharacterAgent([],role_1_name,role_1_info,role_2_name,role_2_info)
	character_2 = CharacterAgent([],role_2_name,role_2_info,role_1_name,role_1_info)
		
	

# 创建 Gradio 接口
character_meta_1 = gr.Textbox(lines=5, label="角色1信息")

character_meta_2 = gr.Textbox(lines=5, label="角色2信息")


iface = gr.Interface(generate_dialogue, 
                     [character_meta_1, character_meta_2],
                     "text", 
                     title="角色扮演对话生成工具")
iface.launch(share=True)
