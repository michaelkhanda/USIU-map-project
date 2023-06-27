# Welcome to the USIU map
# Creating the USIU map
import operator


departure = input("Where are you? ")
stops = int(input("How many stops do you have? "))
multiDest = []

for i in range(stops):
    destination = input("Where do you want to go? ")
    multiDest.append(destination)

wheelChair = input("Do you need wheelchair access? (Y/N)")

class Environment():
    myGraph = {'gate_a': set(['admin_block', 'village', 'quality_control', 'admin_parking', 'main_lab']),
               'main_lab': set(['gate_a', 'lillian_beam', 'village']),
               'admin_block': set(['lillian_beam', 'quality_control', 'admin_parking', 'gate_a']),
               'quality_control': set(['admin_block', 'lillian_beam', 'admin_parking', 'cafeteria', 'gate_a', 'transport_office']),
               'lillian_beam': set(['admin_block', 'admin_parking', 'cafeteria', 'quality_control', 'village']),
               'admin_parking': set(['admin_block', 'lillian_beam', 'quality_control', 'cafeteria', 'gate_a', 'transport_office']),
               'cafeteria': set(['lillian_beam', 'quality_control', 'transport_office', 'admin_parking', 'hostels', 'cafellata', 'library', 'csob']),
               'transport_office': set(['quality_control', 'admin_parking', 'bus_parking', 'hostels', 'cafellata', 'cafeteria', 'cafellata_parking']),
               'cafellata': set(['hostels', 'transport_office', 'cafellata_parking', 'bus_parking', 'basketball_court', 'auditorium', 'library', 'csob', 'village', 'cafeteria']),
               'hostels': set(['cafellata', 'transport_office', 'cafellata_parking', 'bus_parking', 'basketball_court', 'auditorium', 'village', 'csob', 'library', 'cafeteria']),
               'cafellata_parking': set(['hostels', 'transport_office', 'cafellata', 'bus_parking', 'basketball_court', 'students_centre_parking']),
               'bus_parking': set(['hostels', 'transport_office', 'cafellata', 'cafellata_parking', 'basketball_court', 'students_centre_parking']),
               'basketball_court': set(['hostels', 'cafellata', 'bus_parking', 'cafellata_parking', 'students_centre_parking']),
               'students_centre_parking': set(['students_centre', 'basketball_court', 'library', 'bus_parking', 'cafellata_parking', 'auditorium_parking', 'auditorium']),
               'students_centre': set(['students_centre_parking', 'auditorium_parking', 'auditorium', 'library', 'pool_parking', 'science_complex', 'science_complex_parking']),
               'auditorium': set(['auditorium_parking', 'students_centre', 'library', 'students_centre_parking', 'science_complex_parking', 'science_complex', 'pool_parking', 'csob', 'hostels', 'cafellata']),
               'auditorium_parking': set(['auditorium', 'students_centre', 'library', 'students_centre_parking', 'science_complex_parking', 'pool_parking']),
               'library': set(['auditorium', 'auditorium_parking', 'students_centre', 'students_centre_parking', 'science_complex', 'science_complex_parking', 'pool_parking', 'library_parking', 'csob', 'village', 'cafeteria', 'hostels', 'cafellata']),
               'library_parking': set(['science_complex_parking', 'science_complex', 'library', 'csob']),
               'science_complex_parking': set(['science_complex', 'library_parking', 'library', 'csob', 'auditorium_parking', 'shss', 'auditorium', 'pool_parking', 'students_centre']),
               'science_complex': set(['science_complex_parking', 'auditorium', 'library_parking', 'library', 'csob', 'pool_parking', 'students_centre', 'shss']),
               'pool_parking': set(['pool', 'science_complex', 'science_complex_parking', 'library', 'auditorium_parking', 'auditorium', 'students_centre', 'shss']),
               'pool': set(['pool_parking']),
               'shss': set(['pool_parking', 'science_complex', 'science_complex_parking', 'shss_parking', 'gate_b']),
               'gate_b': set(['shss_parking', 'shss']),
               'shss_parking': set(['gate_b', 'shss']),
               'csob': set(['hostels', 'library', 'science_complex', 'science_complex_parking', 'library_parking', 'village', 'auditorium', 'cafellata', 'cafeteria']),
               'village': set(['gate_a', 'lillian_beam', 'hostels', 'cafellata', 'library', 'csob'])
               }

    # The distance between the buildings
    cost = {str(['gate_a', 'admin_block']): '116', str(['gate_a', 'main_lab']): '124',  str(['gate_a', 'village']): '280', str(['gate_a', 'quality_control']): '137', str(['gate_a', 'admin_parking']): '128',
            str(['main_lab', 'gate_a']): '124', str(['main_lab', 'lillian_beam']): '54',  str(['main_lab', 'village']): '90',
            str(['admin_block', 'lillian_beam']): '51', str(['admin_block', 'quality_control']): '40', str(['admin_block', 'admin_parking']): '108', str(['admin_block', 'gate_a']): '116',
            str(['quality_control', 'admin_block']): '40', str(['quality_control', 'transport_office']): '85', str(['quality_control', 'lillian_beam']): '105', str(['quality_control', 'admin_parking']): '67', str(['quality_control', 'cafeteria']): '69', str(['quality_control', 'gate_a']): '134',
            str(['lillian_beam', 'main_lab']): '54', str(['lillian_beam', 'cafeteria']): '72', str(['lillian_beam', 'admin_block']): '51', str(['lillian_beam', 'admin_parking']): '158', str(['lillian_beam', 'quality_control']): '105', str(['lillian_beam', 'village']): '144',
            str(['admin_parking', 'admin_block']): '108', str(['admin_parking', 'lillian_beam']): '158', str(['admin_parking', 'cafeteria']): '103', str(['admin_parking', 'quality_control']): '67', str(['admin_parking', 'gate_a']): '128', str(['admin_parking', 'transport_office']): '122',
            str(['cafeteria', 'lillian_beam']): '72', str(['cafeteria', 'csob']): '241', str(['cafeteria', 'quality_control']): '69', str(['cafeteria', 'transport_office']): '81', str(['cafeteria', 'admin_parking']): '103', str(['cafeteria', 'hostels']): '96', str(['cafeteria', 'cafellata']): '135', str(['cafeteria', 'library']): '246',
            str(['transport_office', 'quality_control']): '85', str(['transport_office', 'bus_parking']): '105', str(['transport_office', 'admin_parking']): '122', str(['transport_office', 'hostels']): '32', str(['transport_office', 'cafellata']): '54', str(['transport_office', 'cafeteria']): '81', str(['transport_office', 'cafellata_parking']): '100',
            str(['cafellata', 'hostels']): '51', str(['cafellata', 'transport_office']): '54', str(['cafellata', 'cafeteria']): '135', str(['cafellata', 'cafellata_parking']): '46', str(['cafellata', 'bus_parking']): '56', str(['cafellata', 'basketball_court']): '128', str(['cafellata', 'auditorium']): '204', str(['cafellata', 'library']): '260', str(['cafellata', 'csob']): '258', str(['cafellata', 'village']): '279',
            str(['hostels', 'cafellata']): '51', str(['hostels', 'transport_office']): '32', str(['hostels', 'cafeteria']): '96', str(['hostels', 'cafellata_parking']): '97', str(['hostels', 'bus_parking']): '106', str(['hostels', 'basketball_court']): '119', str(['hostels', 'auditorium']): '166', str(['hostels', 'village']): '240', str(['hostels', 'csob']): '221', str(['hostels', 'library']): '225',
            str(['cafellata_parking', 'hostels']): '97', str(['cafellata_parking', 'transport_office']): '100', str(['cafellata_parking', 'cafellata']): '46', str(['cafellata_parking', 'bus_parking']): '41', str(['cafellata_parking', 'basketball_court']): '175', str(['cafellata_parking', 'students_centre_parking']): '128',
            str(['bus_parking', 'hostels']): '106', str(['bus_parking', 'transport_office']): '105', str(['bus_parking', 'cafellata']): '56', str(['bus_parking', 'cafellata_parking']): '41', str(['bus_parking', 'basketball_court']): '84', str(['bus_parking', 'students_centre_parking']): '107',
            str(['basketball_court', 'hostels']): '119', str(['basketball_court', 'cafellata']): '128', str(['basketball_court', 'bus_parking']): '84', str(['basketball_court', 'cafellata_parking']): '175', str(['basketball_court', 'students_centre_parking']): '87',
            str(['students_centre_parking', 'students_centre']): '122', str(['students_centre_parking', 'library']): '181', str(['students_centre_parking', 'basketball_court']): '86', str(['students_centre_parking', 'bus_parking']): '106', str(['students_centre_parking', 'cafellata_parking']): '131', str(['students_centre_parking', 'auditorium_parking']): '123', str(['students_centre_parking', 'auditorium']): '80',
            str(['students_centre', 'students_centre_parking']): '122', str(['students_centre', 'auditorium_parking']): '196', str(['students_centre', 'auditorium']): '178', str(['students_centre', 'library']): '200', str(['students_centre', 'pool_parking']): '65', str(['students_centre', 'science_complex']): '73', str(['students_centre', 'science_complex_parking']): '150',
            str(['auditorium', 'auditorium_parking']): '117', str(['auditorium', 'cafellata']): '204', str(['auditorium', 'students_centre']): '171', str(['auditorium', 'library']): '97', str(['auditorium', 'students_centre_parking']): '83', str(['auditorium', 'science_complex_parking']): '239', str(['auditorium', 'science_complex']): '318', str(['auditorium', 'pool_parking']): '208', str(['auditorium', 'csob']): '174', str(['auditorium', 'hostels']): '168',
            str(['auditorium_parking', 'auditorium']): '119', str(['auditorium_parking', 'students_centre']): '196',
            str(['auditorium_parking', 'library']): '214',
            str(['auditorium_parking', 'students_centre_parking']): '123',
            str(['auditorium_parking', 'science_complex_parking']): '300',
            str(['auditorium_parking', 'pool_parking']): '215',
            str(['library', 'auditorium']): '96', str(['library', 'auditorium_parking']): '215',
            str(['library', 'students_centre']): '173', str(['library', 'students_centre_parking']): '181',
            str(['library', 'science_complex_parking']): '187', str(['library', 'pool_parking']): '183',
            str(['library', 'library_parking']): '235', str(['library', 'csob']): '114',
            str(['library', 'village']): '263', str(['library', 'cafellata']): '261',
            str(['library', 'cafeteria']): '247', str(['library', 'hostels']): '227', str(['library', 'science_complex']): '234',
            str(['library_parking', 'science_complex_parking']): '244',
            str(['library_parking', 'science_complex']): '279', str(['library_parking', 'library']): '214',
            str(['library_parking', 'csob']): '326',
            str(['science_complex_parking', 'science_complex']): '99', str(['science_complex_parking', 'shss']): '325',
            str(['science_complex_parking', 'library_parking']): '239',
            str(['science_complex_parking', 'library']): '365', str(['science_complex_parking', 'csob']): '363',
            str(['science_complex_parking', 'auditorium_parking']): '300',
            str(['science_complex_parking', 'auditorium']): '215',
            str(['science_complex_parking', 'pool_parking']): '97',
            str(['science_complex_parking', 'students_centre']): '123',
            str(['science_complex', 'science_complex_parking']): '107',
            str(['science_complex', 'library_parking']): '275', str(['science_complex', 'library']): '234', str(['science_complex', 'auditorium']): '318',
            str(['science_complex', 'csob']): '347', str(['science_complex', 'pool_parking']): '65',
            str(['science_complex', 'students_centre']): '96', str(['science_complex', 'shss']): '91',
            str(['pool_parking', 'pool']): '64', str(['pool_parking', 'science_complex']): '65',
            str(['pool_parking', 'science_complex_parking']): '97', str(['pool_parking', 'library']): '183',
            str(['pool_parking', 'auditorium_parking']): '215', str(['pool_parking', 'auditorium']): '208',
            str(['pool_parking', 'students_centre']): '65', str(['pool_parking', 'shss']): '101',
            str(['pool', 'pool_parking']): '64',
            str(['shss', 'pool_parking']): '101', str(['shss', 'science_complex']): '91',
            str(['shss', 'science_complex_parking']): '325', str(['shss', 'shss_parking']): '145',
            str(['shss', 'gate_b']): '154',
            str(['gate_b', 'shss_parking']): '9', str(['gate_b', 'shss']): '154',
            str(['shss_parking', 'gate_b']): '9', str(['shss_parking', 'shss']): '145',
            str(['csob', 'hostels']): '221', str(['csob', 'library']): '114', str(['csob', 'science_complex']): '347',
            str(['csob', 'science_complex_parking']): '363', str(['csob', 'library_parking']): '326',
            str(['csob', 'village']): '56', str(['csob', 'auditorium']): '174', str(['csob', 'cafellata']): '258',
            str(['csob', 'cafeteria']): '241',
            str(['village', 'gate_a']): '280', str(['village', 'lillian_beam']): '144',
            str(['village', 'hostels']): '239', str(['village', 'cafellata']): '279',
            str(['village', 'library']): '263', str(['village', 'csob']): '258', str(['village', 'main_lab']): '90',
            }

    start = departure
    for i in multiDest:
        goal = i

    my_heuristics = {'gate_a': ['8', '20'],
                     'admin_block': ['7', '17'],
                     'quality_control': ['11', '27'],
                     'lillian_beam': ['12', '25'],
                     'admin_parking': ['10', '28'],
                     'cafeteria': ['10', '24'],
                     'transport_office': ['9', '26'],
                     'cafellata': ['7', '21'],
                     'hostels': ['8', '22'],
                     'cafellata_parking': ['4', '21'],
                     'bus_parking': ['5', '19'],
                     'basketball_court': ['6', '18'],
                     'students_centre_parking': ['4', '15'],
                     'students_centre': ['6', '10'],
                     'auditorium': ['9', '17'],
                     'auditorium_parking': ['8', '14'],
                     'library': ['11', '16'],
                     'library_parking': ['14', '14'],
                     'science_complex_parking': ['10','10'],
                     'science_complex': ['11', '8'],
                     'pool_parking': ['7', '8'],
                     'pool': ['6', '7'],
                     'shss': ['10', '5'],
                     'gate_b': ['19', '1'],
                     'shss_parking': ['13', '3'],
                     'csob': ['14', '20'],
                     'village': ['15', '23'],
                     'main_lab': ['14', '25']}


class Agent(Environment):
    def get_cost(path_to_cost):
        path_cost = 0
        i = 0
        while i < len(path_to_cost) - 1:  # -1 so it doesnt go out of bounds, while is to add up all the costs
            l = []
            l.append(path_to_cost[i])  # first node
            l.append(path_to_cost[i + 1])  # second node
            path_cost = path_cost + int(Environment.cost[str(l)])  # read cost between the nodes (1 and 2)
            i += 1
            return path_cost

        # to get the heuristics

    def get_h(vertex, goal):
        v = []  # will contain parameters
        g = []
        for i in Environment.my_heuristics[vertex]:
            v.append(int(i))
        for i in Environment.my_heuristics[goal]:
            g.append(int(i))

        heu = abs(v[0] - g[0]) + abs(v[1] - g[1])  # The Manhattan Distance
        return heu

    def A_star(graph, start, goal):
        if wheelChair == "Y":
            import WheelChairAccess
        p = []  # host the path
        p.append(start)
        while True:
            neighbour = graph[start]
            h = {}
            for i in neighbour.difference(p):  # to go through all neighbours
                l = []
                l.append(str(start))
                l.append(str(i))  # the neighbour
                h[i] = Agent.get_h(i, goal) + Agent.get_cost(l)

            sorted_h = sorted(h.items(), key=operator.itemgetter(1))
            x = next(iter(sorted_h[0]))  # first item in sorted list at this point contains the best heuristics
            p.append(x)
            if x == goal:
                return p
            else:
                start = x

    def BFS(graph, start, goal):
        stack = [(start, [start])]
        p = []
        while stack:
            (vertex, path) = stack.pop(0)
            for next in graph[vertex] - set(path):
                if next == goal:
                    p.append(path + [next])
                    return p
                else:
                    stack.append((next, path + [next]))
        return p

    def __init__(self, Environment):
        print('\nShortest Route-Path:', Agent.BFS(Environment.myGraph, Environment.start, Environment.goal))
        print('Longest Route-Path:', Agent.A_star(Environment.myGraph, Environment.start, Environment.goal))



theEnvironment = Environment()
theAgent = Agent(theEnvironment)
import CheckTime
