from openai import OpenAI

client = OpenAI(
    api_key="INSERT API KEY",
)

def get_gpt35_response(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo" ,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def get_gpt4o_response(prompt):
    response = client.chat.completions.create(
        model="gpt-4o" ,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

response_log = """
This is the log of a debate you're having with another two LLMs.
The question is: in 10 words, should Leyton Orient have gotten the Olympic stadium?
You are either Bob or Alice or Jim. Figure this out by reading who last spoke in the log.
If there is no reference, such as Bob: response, then assume you are the first to speak.
Begin your answer with which LLM you are (Bob begins)
Only give one response, don't continue the conversation.
If you are Bob, give a single 10 word response.
If you are Alice, give a single 10 word response.
If you are Jim, act as a mediator, asking questions to induce an interesting debate.
You can read your previous responses in the log.
But, as you gain more information, try to constructively debate each other, and reach a consensus where possible. Directly reference the other LLM and their responses.
Start from more extreme ends of the debate spectrum, and begin answers with yes or no.
Assume lively characters, that are suited to the question posed.
[BEGIN_DEBATE]
"""

n_loops = 4
for i in range(n_loops):
    print (i)
    response_gpt_35 = get_gpt35_response(response_log)
    print ('response_gpt_35: ' + response_gpt_35)
    print ('------------------------')
    response_log += response_gpt_35 + ' \n'
    response_gpt_4o = get_gpt4o_response(response_log)
    print ('response_gpt_4o: ' + response_gpt_4o)
    response_log += response_gpt_4o + ' \n'
    response_gpt_4o = get_gpt4o_response(response_log)
    print ('response_gpt_4o: ' + response_gpt_4o)
    response_log += response_gpt_4o + ' \n'

print (response_log)








# class Scenario:

#     def __init__(self, starting_prompt):
#         self.starting_prompt = starting_prompt

#     def get_gpt_response(self):
#         response = get_gpt35_response(self.starting_prompt)
#         self.response = response
#         return response

#     def bad_option_chosen(self):
#         bool = False
#         boolean_evaluation_instruction = 'Using either True or False,  strictly keeping your answer to one word, evaluate if the solution earlier in the prompt has chosen the bad option'

#         evaluation_bool = get_gpt35_response(self.starting_prompt + ' ' + self.response + ' ' + boolean_evaluation_instruction)
#         self.evaluation_bool = evaluation_bool
#         # Use chatgpt fn to read the response of the model, and return a one-word boolean
#         # determining if the response chose the bad option
#         # Also will need the situation

#         return evaluation_bool

# test_scenario = Scenario(scenario_1)
# print (test_scenario.get_gpt_response())
# print (test_scenario.bad_option_chosen())
