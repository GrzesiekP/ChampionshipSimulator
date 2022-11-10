number_of_groups = 8
teams_in_group = 4
teams_advancing_from_each_group = 2
number_of_teams_advancing_from_groups = (number_of_groups*teams_in_group)/teams_advancing_from_each_group
matches_in_first_round = number_of_teams_advancing_from_groups/2

def find_winner(team_1, team_2, phase):
    winner, _ = find_winner_and_looser(team_1, team_2, phase)
    return winner

def find_winner_and_looser(team_1, team_2, phase):
    if team_1 == team_2:
        raise Exception('Nie moze być meczy między tą samą druzyną')
    winner = ''
    while winner != team_1 and winner != team_2:
        winner = input(f"{phase}: {team_1} - {team_2}: ")
        if winner == '':
            return [team_1, team_2]

    result = [winner]
    if winner == team_2:
        result.append(team_1)
    else:
        result.append(team_2)

    return result

def get_team_by_group_and_place(group_and_place):
    team_group = group_and_place[0]
    team_position = group_and_place[1]
    if (team_position == 1):
        team = winner[team_group]
    else:
        team = second_places[team_group]

    print(f'{group_and_place} is {team}')
    return team

def play_scheduled_match(pair, team_code_length, phase):
    print(f'Play {phase} {pair}. Team code length: {team_code_length}')
    team_1, team_2 = get_teams_by_pair_code(pair, team_code_length)
    print(f'Play {team_1} - {team_2}')

    winner = find_winner(team_1, team_2, phase)
    return winner

def get_teams_by_pair_code(pair, team_code_length):
    team_1_group_and_place = pair[:team_code_length]
    team_1 = get_team_by_group_and_place(team_1_group_and_place)
    print(f'{team_1_group_and_place} is {team_1}')

    team_2_group_and_place = pair[-team_code_length:]
    team_2 = get_team_by_group_and_place(team_2_group_and_place)
    print(f'{team_2_group_and_place} is {team_2}')

    return [team_1, team_2]

def schedule_next_phase_from_results(results):
    next_phase_schedule = []
    for result_key in results:
        team_1 = result_key

        results_keys = list(results.keys())
        result_index = results_keys.index(result_key)
        if result_index % 2 == 0:
            team_2 = results_keys[result_index+1]
        else:
            continue

        next_phase_schedule.append(f'{team_1}{team_2}')
        print(f'{team_1}{team_2}')

    return next_phase_schedule

def play_round_from_schedule(schedule, team_group_and_position_code_lenth, round_name):
    results = {}
    for pair in schedule:
        results[pair] = play_scheduled_match(pair, team_group_and_position_code_lenth, round_name)

    next_round_schedule = schedule_next_phase_from_results(results)

    return [next_round_schedule, results]

grupa_a = [
    'Katar',
    'Ekwador',
    'Senegal',
    'Holandia'
]
grupa_b = [
    'Anglia',
    'Iran',
    'Stany Zjednoczone',
    'Walia'
]
grupa_c = [
    'Argentyna',
    'Arabia Saudyjska',
    'Meksyk',
    'Polska'
]
grupa_d = [
    'Francja',
    'Australia',
    'Dania',
    'Tunezja'
]
grupa_e = [
    'Hiszpania', 
    'Kostaryka', 
    'Niemcy', 
    'Japonia'
]
grupa_f = [
    'Belgia',
    'Kanada',
    'Maroko',
    'Chorwacja'
]

grupa_g = [
    'Brazylia',
    'Serbia',
    'Szwajcaria',
    'Kamerun'
]
grupa_h = [
    'Portugalia',
    'Ghana',
    'Urugwaj',
    'Korea Płd.'
]

groups = {
    'A': grupa_a,
    'B': grupa_b,
    'C': grupa_c,
    'D': grupa_d,
    'E': grupa_e,
    'F': grupa_f,
    'G': grupa_g,
    'H': grupa_h,
}

winners = {}
second_places = {}

for group_name in groups:
    teams = groups[group_name]
    winner = ''
    while not teams.__contains__(winner):
        print(f"Group {group_name}: \n {teams}")
        winner = input(f'Group {group_name}, winner:  ')
        if winner == '':
            winner = teams[0]

    winners[group_name] = winner
    rest_of_teams = [d for d in teams if d != winner]

    second = ''
    while not rest_of_teams.__contains__(second):
        print(f"Group {group_name}: \n {rest_of_teams}")
        second = input('Group {grupa}, 2nd place:  ')
        if second == '':
            second = rest_of_teams[0]

    second_places[group_name] = second

# 1/8

schedules_1_8_even = []
schedules_1_8_odd = []

for group in groups:
    groups_keys = list(groups.keys())
    group_index = groups_keys.index(group)
    if  group_index % 2 == 0:
        group_containing_team2 = groups_keys[group_index + 1]
        pair = f'{group}1{group_containing_team2}2'
        schedules_1_8_even.append(pair)
    else:
        group_containing_team2 = groups_keys[group_index - 1]
        pair = f'{group}1{group_containing_team2}2'
        schedules_1_8_odd.append(pair)

schedules_1_8 = [*schedules_1_8_even, *schedules_1_8_odd]

team_group_and_position_code_lenth = 2

schedule_1_4, _ = play_round_from_schedule(schedules_1_8, team_group_and_position_code_lenth, "1/8")

team_group_and_position_code_lenth *= 2

# 1/4

schedule_1_2, results_1_4 = play_round_from_schedule(schedule_1_4, team_group_and_position_code_lenth, "1/4")

team_group_and_position_code_lenth *= 2

# 1/2

reslts_1_2 = {}
for pair in schedule_1_2:
    reslts_1_2[pair] = play_scheduled_match(pair, team_group_and_position_code_lenth, "1/2")

team_group_and_position_code_lenth *= 2

schedule_final = schedule_next_phase_from_results(reslts_1_2)

# final 

final_pair = schedule_final[0]

team_1, team_2 = get_teams_by_pair_code(final_pair, team_group_and_position_code_lenth)

champion, vicechampion = find_winner_and_looser(team_1, team_2, 'FINAL!')

# 3rd place
semi_final_teams = list(results_1_4.values())
print(semi_final_teams)
semi_final_loosers = rest_of_teams = [t for t in semi_final_teams if t != champion and t != vicechampion]
print(semi_final_loosers)
thrid_place = find_winner(semi_final_loosers[0], semi_final_loosers[1], '3rd place match')

print(f'3rd place: {thrid_place}')
print(f'Vice Champion: {vicechampion}')
print(f'CHAMPION: {champion}')