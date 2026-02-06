responses = [5, 7, 3, 8]
respondent_ids = (1012, 1035, 1021, 1053)

survey_dict = dict(zip(respondent_ids, responses))
print("Survey responses with respondent IDs:", survey_dict)

print(f"Respondent {respondent_ids[2]} gave a response of {survey_dict[respondent_ids[2]]}")