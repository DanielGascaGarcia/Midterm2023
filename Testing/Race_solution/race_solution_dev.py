#**************************************************************
#                             1
#**************************************************************

def read_results():#(s)
    with open('C:/Midterm2023/Testing/Testing/input.txt', 'r') as file:
        lines = file.read().splitlines()
    results_string = []

    for line in lines:
       results_string.append(line)
    return (results_string)#(s)


#**************************************************************
#                             2
#**************************************************************

def race_result(boat, race, results_string):
    for race_result_string in results_string:
        segments = race_result_string.split('-');
        boat_race_type = segments[0];
        current_boat_type = int(boat_race_type[:2]);
        current_race_type = int(boat_race_type[2:]);
        
        if current_boat_type == boat and current_race_type == race:
            return race_result_string;


#**************************************************************
#                             3
#**************************************************************

def class_table_result(boat_type, race_results):
    def calculate_total_points(race_results):
        total_points = {}
    
        for results_string in race_results:
            segments = results_string.split('-')
            boat_race_type = segments[0]
            country_positions = segments[1:]
    
            for i, position in enumerate(country_positions):
                country = position[:2]
                points = int(position[2:]) if position[2:].isdigit() else 11
    
                if country in total_points:
                    total_points[country] += points
                else:
                    total_points[country] = points
    
        return total_points

    def get_last_race_position(country, boat_type, race_results):
        for results_string in reversed(race_results):
            segments = results_string.split('-')
            current_boat_type = int(segments[0][:2])
            country_positions = segments[1:]
    
            if current_boat_type == boat_type:
                for i, position in enumerate(country_positions):
                    if position.startswith(country):
                        return i + 1
    
        return float('inf')

    class_results = []
    total_points = calculate_total_points(race_results)
    
    for country, points in total_points.items():
        class_results.append((country, points))
    
    class_results.sort(key=lambda x: (x[1], get_last_race_position(x[0], boat_type, race_results)))

    result_string = ", ".join([f"{country}-{position:02d}-{points}" for position, (country, points) in enumerate(class_results, 1)])

    return result_string

#**************************************************************
#                             4
#**************************************************************
def class_table_discard_result(boat_type, race_results):
    def calculate_total_points(race_results):
        total_points = {}
    
        for results_string in race_results:
            segments = results_string.split('-')
            boat_race_type = segments[0]
            country_positions = segments[1:]
    
            for i, position in enumerate(country_positions):
                country = position[:2]
                points = int(position[2:]) if position[2:].isdigit() else 11
    
                if country in total_points:
                    total_points[country].append(points)
                else:
                    total_points[country] = [points]
    
        return total_points

    def get_last_race_position(country, boat_type, race_results):
        for results_string in reversed(race_results):
            segments = results_string.split('-')
            current_boat_type = int(segments[0][:2])
            country_positions = segments[1:]
    
            if current_boat_type == boat_type:
                for i, position in enumerate(country_positions):
                    if position.startswith(country):
                        return i + 1
    
        return float('inf')

    class_results = []
    total_points = calculate_total_points(race_results)
    
    for country, points_list in total_points.items():
        if len(points_list) <= 2:
            total_points[country] = sum(points_list)
        else:
            total_points[country] = sum(sorted(points_list)[:-2])
    
    for country, points in total_points.items():
        class_results.append((country, points))
    
    class_results.sort(key=lambda x: (x[1], get_last_race_position(x[0], boat_type, race_results)))

    m_table_string = []

    for position, (country, points) in enumerate(class_results, start=1):
        m_table_string.append(f"{country}-{position:02d}-{points}")

        medal_table_string = ', '.join(m_table_string)
    return medal_table_string

#**************************************************************
#                             5
#**************************************************************

def medal_table_result(boat_type, race_results):
    def calculate_medals(race_results):
        medal_scores = {}

        for results_string in race_results:
            segments = results_string.split('-')
            country_positions = segments[1:]

            for i, position in enumerate(country_positions):
                country = position[:2]

                if i < 3:
                    if country in medal_scores:
                        medal_scores[country][i] += 1
                    else:
                        medal_scores[country] = [0, 0, 0]
                        medal_scores[country][i] += 1

        return medal_scores

    class_table_string = class_table_discard_result(boat_type, race_results)
    medal_scores = calculate_medals(race_results)

    medal_table = []

    for country, medals in medal_scores.items():
        golds, silvers, bronzes = medals
        total_score = golds * 3 + silvers * 2 + bronzes

        medal_table.append((country, golds, silvers, bronzes, total_score))

    medal_table.sort(key=lambda x: (x[4], x[1], x[2], x[3], x[0]))

    disqualifications_string = ""

    for country, golds, silvers, bronzes, total_score in medal_table:
        disqualifications_string += f"{country}-{golds}-{silvers}-{bronzes}-{total_score}, "

    return disqualifications_string.rstrip(', ')


def discualifications_race_result(race_results):
    disqualifications = {}

    for results_string in race_results:
        segments = results_string.split('-')
        country_positions = segments[1:]

        for position in country_positions:
            country = position[:2]
            disqualification_count = position[2:].count('x')

            if country in disqualifications:
                disqualifications[country] += disqualification_count
            else:
                disqualifications[country] = disqualification_count
    
    max_country = max(disqualifications, key=disqualifications.get)
    max_country_disqualifications = disqualifications[max_country]

    boat_disqualifications = {}
    
    for results_string in race_results:
        segments = results_string.split('-')
        boat_type = int(segments[0][2:])
        disqualification_count = segments[1:].count('xx')

        if boat_type in boat_disqualifications:
            boat_disqualifications[boat_type] += disqualification_count
        else:
            boat_disqualifications[boat_type] = disqualification_count
    
    max_boat_type = max(boat_disqualifications, key=boat_disqualifications.get)
    max_boat_disqualifications = boat_disqualifications[max_boat_type]

    disqualifications_string = "{:02d}{:02d}-{:02d}{:02d}".format(
        int(max_country), max_country_disqualifications,
        max_boat_type, max_boat_disqualifications
    )

    return disqualifications_string



if __name__ == '__main__':
# 1       
    a=read_results();
    print("Input:");
    print("\n");
    print(a);
    print("\n");
# 2
    boat=1;
    race=1;
    b=race_result(boat, race, a);
    print("Result for Boat kind "+str(boat)+" and race "+str(race)+"\n");
    print(b);
    print("\n");
# 3
    Class=5;
    c=class_table_result(Class,a);
    print("Result for Class "+str(Class)+": \n");
    print(c);
    print("\n");

# 4
    Class=5;
    d=class_table_discard_result(Class,a);
    print("Result for Discards is "+str(Class)+": \n");
    print(d);
    print("\n");
 
# 5 
    Class = 5 
    e = medal_table_result(Class, a);
    print("Country medal table  is "+str(Class)+": \n");
    print(e);
    print("\n");

# 6 
    e = discualifications_race_result(a);
    print("naughtiest Country and Boats are: "+str(e)+"\n");
    print(e);
    print("\n");
