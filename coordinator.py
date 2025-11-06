import requests
import json

# 主机地址
hosts = {
    'channel1_task': 'http://channel1-task:8000',
    'channel1_vote': 'http://channel1-vote:8000',
    'channel2_task': 'http://channel2-task:8000',
    'channel2_vote': 'http://channel2-vote:8000'
}

# 用户输入四个输入值
print("Please enter input values (integers) for each host:")
inputs = {}
for name in hosts.keys():
    inputs[name] = int(input(f"Enter input for {name.replace('_', '-')} (1-100 recommended): "))

def get_result(url, input_value):
    try:
        response = requests.post(url, json={'input': input_value})
        return response.json()
    except Exception:
        return {'input': 'Error', 'output': 'Error'}

# 收集所有结果（发送POST）
results = {name: get_result(url, inputs[name]) for name, url in hosts.items()}

# 通道内表决：检查输入输出一致
def channel_vote(task_res, vote_res):
    if task_res['input'] != vote_res['input']:
        return False, "Input mismatch"
    if task_res['output'] != vote_res['output']:
        return False, "Output mismatch"
    return True, "Pass"

channel1_pass, channel1_msg = channel_vote(results['channel1_task'], results['channel1_vote'])
channel2_pass, channel2_msg = channel_vote(results['channel2_task'], results['channel2_vote'])

# 整体表决
overall_pass = channel1_pass and channel2_pass

print("Inputs you provided:", inputs)
print("Results:", results)
print("Channel 1:", channel1_msg if not channel1_pass else "Pass")
print("Channel 2:", channel2_msg if not channel2_pass else "Pass")
print("Overall Decision:", 'Output' if overall_pass else 'Fault Reported')
if overall_pass:
    print("Final Output:", results['channel1_task']['output'])  # 用Channel1任务输出为例
