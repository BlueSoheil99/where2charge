"""

"""

__all__=[]

from openai import OpenAI
import pandas as pd


class TextAnalyzer:
    def __init__(self, api_key):
        print('textanalyzer is connected to openai')
        # self.client = OpenAI(api_key=api_key)
#
#     def s(self):
#         self.chat_completion = self.chat.completions.create(
#             model="gpt-4o-mini",
#             messages=[
#                 {"role": "system", "content": [{"type": "text", "text": prompt}]},
#                 {"role": "user", "content": [{"type": "text", "text": sentence}]}
#             ],
#             temperature=0.05,
#             max_tokens=256,
#             top_p=1,
#             frequency_penalty=0,
#             presence_penalty=0
#         )
#
#         # Parse response into a dictionary
#         lines = response.choices[0].message.content.strip().split('\n')
#         classification = {category: None for category in classes.keys()}
#         for line in lines:
#             for category in classes.keys():
#                 if line.startswith(category):
#                     value = line.split(': ')[1]
#                     classification[category] = value if value != 'None' else None
#
#         return classification
#
#
#
#
#
# classes = {
#     "Other Parties": ["Car", "Truck", "Motorcycle", "Pedestrian", "Cyclist", "Bus", "Scooter", "Other"],
#     "Injury": ['No Injury', 'Slight', 'Severe', 'Fatality', 'Unknown'],
#     "Damage": ['No Damage', 'Slight', 'Severe', 'Unknown'],
#     "Validity": ['Valid', 'Invalid']
# }
#
# prompt = ("There are multiple sentences describing a collision in which one autonomous vehicle was involved."
#           "Classify the given sentence into the categories below:\n"
#           "Categories:\n")
# for category, options in classes.items():
#     prompt += f"{category}: {','.join(options)}\n"
# prompt += ("the validity category specifies if such an incident is good data for a crash model.\n"
#           "by 'Other Parties' we want to know what option hit the autonomous vehicle (AV) or was hit by it.\n"
#           "Provide the most relevant option for each category. Only use the given options")
# # If none applies or the text is not explicit enough, use 'None'
#
# input_columns = ['Incident description', 'Damage description', 'Injury description', 'Vehicle status']







