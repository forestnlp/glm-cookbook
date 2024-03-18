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
		self.character_meta = {
		"user_info": user_info,
		"bot_info": bot_info,
		"user_name": user_name,
		"bot_name": bot_name
		}

	def chat(self, message):
     
		if(len(self.messages)>=5):
			self.messages.pop()
				
		self.messages.append({"role": "user", "content": message})
		response = ''.join(get_characterglm_response(self.messages, meta=self.character_meta))
		self.messages.append({"role": "assistant", "content": response})
		return response


def generate_dialogue(character_meta_1, character_meta_2):
	# 生成角色1的人设信息
	role_1 = json.loads("".join(generate_role_NameandInfo(character_meta_1)))
	# 生成角色2的人设信息
	role_2 = json.loads("".join(generate_role_NameandInfo(character_meta_2)))

	role_1_name = role_1['name']
	role_1_info = role_1['info']
	role_2_name = role_2['name']
	role_2_info = role_2['info']

	character_1 = CharacterAgent([],bot_name=role_1_name,bot_info=role_1_info,user_name=role_2_name,user_info=role_2_info)
	character_2 = CharacterAgent([],bot_name=role_2_name,bot_info=role_2_info,user_name=role_1_name,user_info=role_1_info)


	chat_history = []

	content = "你好"

	for i in range(20):
		# Character 1 speaks
		content = character_1.chat(content)
		# Character 2 responds
		print(f"{role_1_name}: {content}")
		chat_history.append(f"{role_1_name}: {content}")

		content = character_2.chat(content)
		# Check if the dialogue should end
		print(f"{role_2_name}: {content}")
		chat_history.append(f"{role_2_name}: {content}")

		# 将对话内容输出显示在屏幕上
		dialogue_output = "\n".join(chat_history)

		# 将对话内容导出为文本文件
		with open("dialogue.txt", "w") as file:
			file.write("\n".join(chat_history))
		
	return dialogue_output

# 创建 Gradio 接口
character_meta_1 = gr.Textbox(lines=5, label="角色1信息")
character_meta_2 = gr.Textbox(lines=5, label="角色2信息")


iface = gr.Interface(generate_dialogue, 
	[character_meta_1, character_meta_2],
	"text", 
	title="角色扮演对话生成工具")

iface.launch(share=True)


