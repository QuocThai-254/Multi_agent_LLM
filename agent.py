import autogen
from autogen import AssistantAgent , UserProxyAgent
from autogen . code_utils import extract_code
TIMEOUT = 60

config_list = autogen . config_list_from_json ("./OAI_CONFIG_LIST.json")