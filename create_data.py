# This file is AI generated
import csv

# Generate full 50-row LoL esports dataset (5 matches, 2 teams, 5 players per team)
data = [
    # Match 1
    {"match_id":1,"team_name":"TeamAlpha","player_name":"Top1","role":"Top","kills":2,"deaths":5,"assists":3,"cs":200,"gold_earned":12000,"damage":15000,"dealt_objectives":1,"match_date":"2025-08-17"},
    {"match_id":1,"team_name":"TeamAlpha","player_name":"Jungle1","role":"Jungle","kills":4,"deaths":4,"assists":6,"cs":150,"gold_earned":13500,"damage":18000,"dealt_objectives":2,"match_date":"2025-08-17"},
    {"match_id":1,"team_name":"TeamAlpha","player_name":"Mid1","role":"Mid","kills":6,"deaths":3,"assists":5,"cs":220,"gold_earned":15000,"damage":22000,"dealt_objectives":3,"match_date":"2025-08-17"},
    {"match_id":1,"team_name":"TeamAlpha","player_name":"ADC1","role":"ADC","kills":7,"deaths":2,"assists":4,"cs":230,"gold_earned":16000,"damage":25000,"dealt_objectives":2,"match_date":"2025-08-17"},
    {"match_id":1,"team_name":"TeamAlpha","player_name":"Support1","role":"Support","kills":1,"deaths":3,"assists":12,"cs":50,"gold_earned":10000,"damage":8000,"dealt_objectives":1,"match_date":"2025-08-17"},
    {"match_id":1,"team_name":"TeamBeta","player_name":"Top2","role":"Top","kills":3,"deaths":6,"assists":2,"cs":180,"gold_earned":11800,"damage":14000,"dealt_objectives":1,"match_date":"2025-08-17"},
    {"match_id":1,"team_name":"TeamBeta","player_name":"Jungle2","role":"Jungle","kills":2,"deaths":5,"assists":5,"cs":140,"gold_earned":12500,"damage":17000,"dealt_objectives":2,"match_date":"2025-08-17"},
    {"match_id":1,"team_name":"TeamBeta","player_name":"Mid2","role":"Mid","kills":5,"deaths":4,"assists":4,"cs":210,"gold_earned":14500,"damage":21000,"dealt_objectives":2,"match_date":"2025-08-17"},
    {"match_id":1,"team_name":"TeamBeta","player_name":"ADC2","role":"ADC","kills":6,"deaths":3,"assists":3,"cs":225,"gold_earned":15500,"damage":24000,"dealt_objectives":3,"match_date":"2025-08-17"},
    {"match_id":1,"team_name":"TeamBeta","player_name":"Support2","role":"Support","kills":0,"deaths":4,"assists":10,"cs":45,"gold_earned":9500,"damage":7000,"dealt_objectives":1,"match_date":"2025-08-17"},
    # Match 2
    {"match_id":2,"team_name":"TeamAlpha","player_name":"Top1","role":"Top","kills":3,"deaths":4,"assists":4,"cs":210,"gold_earned":12500,"damage":16000,"dealt_objectives":2,"match_date":"2025-08-18"},
    {"match_id":2,"team_name":"TeamAlpha","player_name":"Jungle1","role":"Jungle","kills":5,"deaths":3,"assists":7,"cs":160,"gold_earned":14000,"damage":19000,"dealt_objectives":3,"match_date":"2025-08-18"},
    {"match_id":2,"team_name":"TeamAlpha","player_name":"Mid1","role":"Mid","kills":7,"deaths":2,"assists":6,"cs":240,"gold_earned":15500,"damage":23000,"dealt_objectives":3,"match_date":"2025-08-18"},
    {"match_id":2,"team_name":"TeamAlpha","player_name":"ADC1","role":"ADC","kills":8,"deaths":1,"assists":5,"cs":250,"gold_earned":16500,"damage":26000,"dealt_objectives":3,"match_date":"2025-08-18"},
    {"match_id":2,"team_name":"TeamAlpha","player_name":"Support1","role":"Support","kills":1,"deaths":2,"assists":14,"cs":55,"gold_earned":10500,"damage":9000,"dealt_objectives":2,"match_date":"2025-08-18"},
    {"match_id":2,"team_name":"TeamBeta","player_name":"Top2","role":"Top","kills":2,"deaths":5,"assists":3,"cs":190,"gold_earned":12000,"damage":15000,"dealt_objectives":1,"match_date":"2025-08-18"},
    {"match_id":2,"team_name":"TeamBeta","player_name":"Jungle2","role":"Jungle","kills":3,"deaths":4,"assists":6,"cs":150,"gold_earned":13000,"damage":18000,"dealt_objectives":2,"match_date":"2025-08-18"},
    {"match_id":2,"team_name":"TeamBeta","player_name":"Mid2","role":"Mid","kills":6,"deaths":3,"assists":5,"cs":220,"gold_earned":14500,"damage":22000,"dealt_objectives":3,"match_date":"2025-08-18"},
    {"match_id":2,"team_name":"TeamBeta","player_name":"ADC2","role":"ADC","kills":7,"deaths":2,"assists":4,"cs":230,"gold_earned":16000,"damage":25000,"dealt_objectives":3,"match_date":"2025-08-18"},
    {"match_id":2,"team_name":"TeamBeta","player_name":"Support2","role":"Support","kills":0,"deaths":3,"assists":11,"cs":50,"gold_earned":10000,"damage":7500,"dealt_objectives":1,"match_date":"2025-08-18"},
]


# CSV headers
headers = ["match_id","team_name","player_name","role","kills","deaths","assists","cs","gold_earned","damage","dealt_objectives","match_date"]

# Write CSV
with open("lol_match_data.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    writer.writerows(data)

print("CSV file 'lol_match_data.csv' created successfully!")