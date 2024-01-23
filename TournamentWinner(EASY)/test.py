# "competitions": [["HTML", "C#"], ["C#", "Python"],["Python", "HTML"]], "results": [0, 0, 1] == "Python"
# "competitions": [["HTML", "Java"], ["Java", "Python"], ["Python", "HTML"]], "results": [0, 1, 1] == "Java"
# "competitions": [["HTML", "Java"], ["Java", "Python"], ["Python", "HTML"], ["C#", "Python"], ["Java", "C#"], ["C#", "HTML"]] "results": [0, 1, 1, 1, 0, 1] == C#
# "competitions": [["HTML", "Java"], ["Java", "Python"], ["Python", "HTML"], ["C#", "Python"], ["Java", "C#"], ["C#", "HTML"], ["SQL", "C#"], ["HTML", "SQL"],  ["SQL", "Python"], ["SQL", "Java"]], "results": [0, 1, 1, 1, 0, 1, 0, 1, 1, 0] == C#
# "competitions": [["Bulls", "Eagles"]], "results": [1] == Bulls
# "competitions": [["Bulls", "Eagles"], ["Bulls", "Bears"], ["Bears", "Eagles"]], "results": [0, 0, 0] == Eagles
# "competitions": [["Bulls", "Eagles"], ["Bulls", "Bears"], ["Bulls", "Monkeys"], ["Eagles", "Bears"], ["Eagles", "Monkeys"], ["Bears", "Monkeys"]],  "results": [1, 1, 1, 1, 1, 1] == Bulls
# {
#   "competitions": [
#     ["AlgoMasters", "FrontPage Freebirds"],
#     ["Runtime Terror", "Static Startup"],
#     ["WeC#", "Hypertext Assassins"],
#     ["AlgoMasters", "WeC#"],
#     ["Static Startup", "Hypertext Assassins"],
#     ["Runtime Terror", "FrontPage Freebirds"],
#     ["AlgoMasters", "Runtime Terror"],
#     ["Hypertext Assassins", "FrontPage Freebirds"],
#     ["Static Startup", "WeC#"],
#     ["AlgoMasters", "Static Startup"],
#     ["FrontPage Freebirds", "WeC#"],
#     ["Hypertext Assassins", "Runtime Terror"],
#     ["AlgoMasters", "Hypertext Assassins"],
#     ["WeC#", "Runtime Terror"],
#     ["FrontPage Freebirds", "Static Startup"]
#   ],
#   "results": [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]
# } == AlgoMasters
#
# {
#   "competitions": [
#     ["HTML", "Java"],
#     ["Java", "Python"],
#     ["Python", "HTML"],
#     ["C#", "Python"],
#     ["Java", "C#"],
#     ["C#", "HTML"],
#     ["SQL", "C#"],
#     ["HTML", "SQL"],
#     ["SQL", "Python"],
#     ["SQL", "Java"]
#   ],
#   "results": [0, 0, 0, 0, 0, 0, 1, 0, 1, 1]
# } == SQL
#
#
# {
#   "competitions": [
#     ["A", "B"]
#   ],
#   "results": [0]
# } == B
#