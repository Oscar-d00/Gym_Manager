
class Athletes:
    def __init__(self, name, weight, session, stage):
        self.name = str(name)
        self.weight = int(weight)
        self.session = int(session)
        self.stage = str(stage)

athletes_list = []

f = open("athletes.txt", "r")

for line in f:
    parts = line.strip().split(",")
    athletes_list.append(parts)


def heaviest_athlete(athletes_list):
    heaviest = 0
    for athlete in athletes_list:
        if int(athlete[1]) > heaviest:
            heaviest = int(athlete[1])
            name = athlete[0]
    return name, heaviest
    print(f"The heaviest athlete is {name} with a weight of {heaviest} kg.")

def find_athlete_by_name(athletes_list, name):
    for athlete in athletes_list:
        if athlete[0].lower() == name.lower():
            return athlete
    return None
    print(f"Athlete {name} not found.")

# find_athlete = input("Enter the name of the athlete you want to find: ")

# athlete = find_athlete_by_name(athletes_list, find_athlete)
# if athlete:
#     print(f"Athlete {athlete[0]} found with weight {athlete[1]} kg and session {athlete[2]}.")
# else:
#     print(f"Athlete {find_athlete} not found.")

def filter_athletes(trainingplan, stage):
    #filter the athletes based on the training plan and stage

def count_athletes_by_stage(athletes_list, stage):
    #return a list of athletes in the given stage

def export_athletes_to_txt(athletes_list, filename):
    #export the athletes list to a text file who attended more than a number of sessions

def io_audit(athletes_list):
    #create a table with every athlete's name, weight, session, and stage and their monthly payment and their total payment and at the end calculate the total the gym should expect

def draw_stack_of_triangles(n):
    #draw a stack of triangles with the given number of triangles, idk why this is in the task.