import json

with open("data/forecast_5days_a.json") as data:
    for quiz, details in data.items():
        print(details)
        print()
        # for quesNum, content in details.items():
        #     print(quesNum)
        #     print(content)
            # print(f”Question {quesNum} : {content[“question”]}“)
            # for option in content[“options”]:
            #     print(f”      {option}“)
        # print()