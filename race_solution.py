

class Races:#(s)

    def read_results(self):#(s)
    

        with open('input.txt', 'r') as file:
            lines = file.read().splitlines()
        results_string = []

        for line in lines:
            results_string.append(line)
        return (results_string);

    def race_result(self, boat_type, race_number, results_string):#(s)


        if boat_type == 10:
            boat_type = 0

        j = 0
        for i in range(len(results_string)):
            if boat_type == int(results_string[i][1]):
                j += 1
                if j == race_number:
                    return results_string[i][5:]
        return ""




    def class_table_result(self, boat_type, results_string):#(s)


        if boat_type == 10:
            boat_type = 0

        def process_results(results_string, boat_type):
            boat = {str(i).zfill(2): [[], []] for i in range(1, 11)}

            for result in results_string:
                if int(result[1]) == boat_type:
                    race = result[5:]
                    pairs = race.split("-")
                    des = 0

                    for pair in pairs:
                        first = pair[:2]
                        second = pair[2:]

                        if second == "xx":
                            second = str(11)
                            des += 1
                        else:
                            second = str(int(second) - des)

                        if first in boat:
                            if int(result[3]) == 1:
                                boat[first][0].append(int(second))
                            else:
                                boat[first][1].append(int(second))

            return boat
        
        boat=process_results(results_string, boat_type);

        final_table = [[key, sum(values[0]) + 2 * sum(values[1])] for key, values in boat.items()]
        final_race = None
        for string in results_string:
            if string[:2] == "0" + str(boat_type):
                final_race = string
            elif string[:2] == "1" + str(boat_type):
                final_race = string    
        final_race = final_race[5:]       
        # Split the final_race string by '-' and extract the first two characters of each part.
        race_parts = [part[:2] for part in final_race.split('-')]
        # Create a dictionary that maps each race part to its position in the list.
        part_positions = {part: i for i, part in enumerate(race_parts)}
        # Sort the final_table based on the positions of race parts.
        final_table.sort(key=lambda item: part_positions.get(item[0]))
        sorted_data = [f"{key}-position-{value:02}" for key, value in final_table]
        sorted_data = sorted(sorted_data, key=lambda item: (len(item.split('-', 2)[2]), item.split('-', 2)[2]))
   
        return   ", ".join([item.replace('position', f"{i + 1:02}") for i, item in enumerate(sorted_data)]);
        

    def class_table_discard_result(self, boat_type, results_string):#(s)

        boat = {str(i).zfill(2): [[], []] for i in range(1, 11)}

        if boat_type == 10:
            boat_type = 0
    

        def process_results(results_string, boat_type):
            boat = {str(i).zfill(2): [[], []] for i in range(1, 11)}

            for result in results_string:
                if int(result[1]) == boat_type:
                    race = result[5:]
                    pairs = race.split("-")
                    des = 0

                    for pair in pairs:
                        first = pair[:2]
                        second = pair[2:]

                        if second == "xx":
                            second = str(11)
                            des += 1
                        else:
                            second = str(int(second) - des)

                        if first in boat:
                            if int(result[3]) == 1:
                                boat[first][0].append(int(second))
                            else:
                                boat[first][1].append(int(second))

            return boat
        
        boat=process_results(results_string, boat_type);

        final_table = []
        for key, values in boat.items():
            values[0].sort()
            values[1].sort()

            if len(values[0]) > 2:
                values[0] = values[0][:-1]
            if len(values[1]) > 2:
                values[1] = values[1][:-1]

            total_points = sum(values[0]) + 2 * sum(values[1])
            final_table.append([key, total_points])

        final_race = None

        for string in results_string:
            prefix = string[:2]
            if prefix == f"0{boat_type}" or prefix == f"1{boat_type}":
                final_race = string

        final_race = final_race[5:]

        # Split the final_race string by '-' and extract the first two characters of each part.
        race_parts = [part[:2] for part in final_race.split('-')]

        # Create a dictionary that maps each race part to its position in the list.
        part_positions = {part: i for i, part in enumerate(race_parts)}

        # Sort the final_table based on the positions of race parts.
        final_table.sort(key=lambda item: part_positions.get(item[0]))


        sorted_data = []
        for  i, sublist in enumerate(final_table):
            element_0 = sublist[0]
            element_1 = f"{sublist[1]:02}"
            sorted_data.append(f"{element_0}-position-{element_1}")

        sorted_data.sort(key=lambda item: (len(item.split('-', 2)[2]), item.split('-', 2)[2]))


        for i, item in enumerate(sorted_data):
            relative_position = str(i + 1).zfill(2)
            sorted_data[i] = item.replace('position', relative_position)
  
        return ", ".join(sorted_data);


    def medal_table_result(self, results_string):#(s)

        # Your code here


        def process_results(results_string, medal_table):
            updated_medal_table = medal_table.copy()  # Create a copy to avoid modifying the original

            for boat in range(1, 11):
                R = {str(i).zfill(2): [[], []] for i in range(1, 11)}
                if boat == 10:
                    boat = 0
                for i in range(len(results_string)):
                    if int(results_string[i][1]) == boat:
                        race = results_string[i][5:]
                        pairs = race.split("-")
                        des = 0

                        for pair in pairs:
                            first = pair[:2]
                            second = pair[2:]

                            if second == "xx":
                                second = "11"
                                des += 1
                            else:
                                second = str(int(second) - des)

                            if first in R:
                                index = 0 if int(results_string[i][3]) == 1 else 1
                                R[first][index].append(int(second))

                final_table = []
                for key, value in R.items():
                    if len(value[0]) > 2:
                        value[0].sort()
                        value[0] = value[0][:-1]
                    if len(value[1]) > 2:
                        value[1].sort()
                        value[1] = value[1][:-1]

                    total_points = sum(value[0]) + 2 * sum(value[1])
                    final_table.append([key, total_points])

                for string in results_string:
                    if string[:2] == "0" + str(boat):
                        final_race = string
                    elif string[:2] == "1" + str(boat):
                        final_race = string
                final_race = final_race[5:]

                race_parts = [part[:2] for part in final_race.split('-')]
                part_positions = {part: i for i, part in enumerate(race_parts)}
                final_table.sort(key=lambda item: part_positions.get(item[0]))

                sorted_data = []
                for i, sublist in enumerate(final_table):
                    element_0 = sublist[0]
                    element_1 = f"{sublist[1]:02}"
                    sorted_data.append(f"{element_0}-position-{element_1}")

                sorted_data = sorted(sorted_data, key=lambda item: (len(item.split('-', 2)[2]), item.split('-', 2)[2]))

                for i, item in enumerate(sorted_data):
                    relative_position = f"{i + 1:02}"
                    sorted_data[i] = item.replace('position', relative_position)

                stripped_data = [item[:2] for item in sorted_data[:3]]

                i = 0
                j = 1

                while i < len(stripped_data):
                    for row in updated_medal_table:
                        if stripped_data[i] == row[0]:
                            row[j] += 1
                            del stripped_data[i]
                            j += 1
                            break
                    else:
                        i += 1

            return updated_medal_table
        
        medal_table = [[f"{i + 1:02}", 0, 0, 0, 0] for i in range(10)]

        medal_table2=process_results(results_string, medal_table);
         
        for row in medal_table2:
            row[4] = row[1] * 3 + row[2] * 2 + row[3]

        medal_table.sort(key=lambda x: (-x[4], -x[1], -x[2], -x[3], int(x[0])))

        final_medal_table = [f"{int(row[0]):02d}-{int(row[1]):02d}-{int(row[2]):02d}-{int(row[3]):02d}-{int(row[4]):02d}" for row in medal_table]
        

        return ", ".join(final_medal_table);



if __name__ == '__main__':#(s)

    pass#(s)