#def generate_pairs_remains_round(self):
#    sorted_list = sorted(self.current_tournament.players, key=lambda x: (int(-x.score), int(x.rank)))
#    paired_list = []
#    already_selected = []
#
#    for i in range(len(sorted_list)):
#        if sorted_list[i].id in already_selected:
#            continue
#        else:
#            player_1 = sorted_list[i]
#            already_selected.append(player_1.id)
#            j = i + 1
#            for j in range(len(sorted_list)):
#                if sorted_list[j].id in already_selected or (player_1.id, sorted_list[j].id) in self.current_tournament.previous_match or (sorted_list[j].id, player_1.id) in self.current_tournament.previous_match:
#                    continue
#                else:
#                    player_2 = sorted_list[j]
#                    already_selected.append(player_2.id)
#                pair = (player_1, player_2)
#                paired_list.append(pair)
#                break
#            
#    return paired_list
#    
#    
#    
#def start_round(self):
#        match = ()
#        already_match = ()
#        match_score = 0.0
#        
#        
#        if len(self.current_tournament.rounds) == 0:
#            # First round 
#            self.current_round = Round("Round 1", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
#            print("-----------------------------")
#            print(self.current_round)
#            print("-----------------------------")
#            self.current_tournament.paired_list = self.generate_pairs_round_1()
#             
#        elif len(self.current_tournament.rounds) <= self.current_tournament.number_round:
#            # Remains rounds
#            self.current_round = Round(f"Round {len(self.current_tournament.rounds) + 1}", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
#            print("-----------------------------")
#            print(self.current_round)
#            print("-----------------------------")
#            self.current_tournament.paired_list = self.generate_pairs_remains_round()
#            print(self.current_tournament.paired_list)
#            
#        for pair in self.current_tournament.paired_list:
#            match = ([pair[0], match_score], [pair[1], match_score])
#            print(f"\nJoueur: {pair[0].last_name}\nVS\nJoueur: {pair[1].last_name}")
#            self.add_score(match)
#            already_match = (pair[0].id, pair[1].id)
#            self.current_tournament.previous_match.append(already_match)
#            self.current_round.matchs.append(match)
#            
#        self.current_tournament.rounds.append(self.current_round)