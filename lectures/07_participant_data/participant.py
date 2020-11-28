# Get Participant Information

def gatherParticipantData(numberOfParticipants):
    participantData = []
    registeredParticipants = 0

    while(registeredParticipants < numberOfParticipants):
        print(registeredParticipants, "left")
        print("- Next Participant -")

        participant = []
        name = input("Name: ")
        participant.append(name)
        country = input("Country: ")
        participant.append(country)
        age = input("Age: ")
        participant.append(age)

        participantData.append(participant)
        registeredParticipants += 1

    return participantData

# Write File


def saveParticipants(participants, filename):
    outputFile = open(filename, "w")

    for participant in participants:
        for data in participant:
            outputFile.write(str(data) + " ")
        outputFile.write("\n")

    outputFile.close()


# Read File


def readParticipants(filename):
    inputFile = open(filename, "r")

    participants = []

    for line in inputFile:
        participant = line.strip("\n").split()
        participants.append(participant)

    inputFile.close()

    return participants


saveParticipants(gatherParticipantData(3), "ParticipantData.txt")
participants = readParticipants("ParticipantData.txt")

# Statistics

Age = {}
for participant in participants:
    if participant[-1] in Age:
        Age[participant[-1]] += 1
    else:
        Age[participant[-1]] = 1

oldest = 0
youngest = 200
mostOccuringAge = 0
counter = 0

for age in Age:
    if age > oldest:
        oldest = age
    if age < youngest:
        youngest = age
    if Age[age] >= counter:
        counter = Age[age]
        mostOccuringAge = age
