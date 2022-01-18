#first number is top: px, second number is left: px

pixel_locations = {
    "Yonge Street and Gould Street": [440, 452],
    "Yonge Street and Gerrard Street": [258, 452],
    "Yonge Street and Dundas Street": [572, 452],
    "Yonge Street and Elm Street": [394, 452],
    "Yonge Street and College Street": [75, 452],

    "Bond Street and Gould Street": [440, 683],
    "Bond Street and Dundas Street": [624,683],

    "Victoria Street and Gould Street": [440, 580],
    "Victoria Street and Dundas Street": [601, 580],
    "Victoria Street and Gerrard Street": [258, 580],

    "Nelson Mandela Walk": [349, 580],
    "Nelson Mandela Walk and Gould Street": [440, 580],
    "Nelson Mandela Walk and Gerrard Street": [258, 580],

    "Church Street and Gould Street": [440, 777],
    "Church Street and Gerrard Street": [258, 777],
    "Church Street and Dundas Street": [601, 777],
    "Church Street and Carlton Street": [105, 777],

    "O'Keefe Laneway and Gould Street": [440, 513],
    "O'Keefe Laneway and Gerrard Street": [258, 513],

    "Mutual Street and Gould Street": [440, 931],
    "Mutual Street and Dundas Street": [601, 931],
    "Mutual Street and Gerrard Street": [258, 931],

    "Jarvis Street and Dundas Street": [601, 1039],
    "Jarvis Street and Gerrard Street": [258, 1039],

    "Bay Street and Dundas Street": [572, 268],

    "Dalhousie Street and Gould Street": [440, 845],
    "Dalhousie Street and Dundas Street": [601, 845],

    #Buildings or landmarks

    'Yonge - Dundas Square': [608, 495],
    'HOEM': [670, 1005],
    'Jorgenson Hall': [291, 548],
    'Devonian Pond': [462, 607],
    'Pitman Hall': [350, 906],
    'Sally Horsfall Eaton Centre for Studies in Community Health': [305, 906],
    'Dundas Station': [550, 486],
    'Daphne Cockwell Complex': [574, 750],
    'Ram in the Rye Pub': [474, 751],
    'The G. Raymond Chang School of Continuing Education': [496, 609],
    'Victoria Building': [532, 609],
    'Library': [415, 547],
    'Mattamy Athletic Centre': [78, 710],
    'Recreation and Athletics Centre': [377, 683],
    'Rogers Communications Centre': [412, 850],
    'George Vari Engineering and Computing Centre': [540, 813],
    'Student Learning Centre': [417, 485],
    'Ted Rogers School of Management': [612, 332],
    'Podium': [349, 548],
    'Kerr Hall': [335, 683],
    'Kerr Hall West': [347, 619],
    'Kerr Hall South': [412, 683],
    "Balzac's": [451, 665],

    #No location
    'Online': [0, 0],
    'Ryerson campus': [0, 0],
    "Yonge Street and Bay Street": [0, 0],

}

proper_location_names = {

    'Yonge Street and Gould Street': 'Yonge Street and Gould Street',
    'Yonge Street and  Gould Street': 'Yonge Street and Gould Street',
    'Gould Street and Yonge Street': 'Yonge Street and Gould Street',
    'Yonge Street and Gould Street ': 'Yonge Street and Gould Street',

    'Yonge Street and Gerrard Street': 'Yonge Street and Gerrard Street',
    'Yonge Street and Gerrard Street West': 'Yonge Street and Gerrard Street',
    'Gerrard Street East and Yonge Street': 'Yonge Street and Gerrard Street',
    'Gerrard Street and Yonge Street': 'Yonge Street and Gerrard Street',
    'Yonge Street and Gerrard Street East': 'Yonge Street and Gerrard Street',
    'Yonge Street and Gerrard Street West area': 'Yonge Street and Gerrard Street',
    'Yonge Street and Gerrard Street area': 'Yonge Street and Gerrard Street',

    'Yonge Street and Dundas Street': 'Yonge Street and Dundas Street',
    'Yonge Street and Dundas Street West': 'Yonge Street and Dundas Street',
    'Dundas Street and Yonge Street': 'Yonge Street and Dundas Street',
    'Yonge Street and Dundas Street East': 'Yonge Street and Dundas Street',
    'Yonge Street between College Street and Dundas Street': 'Yonge Street and Dundas Street',
    'Dundas Street West and Yonge Street': 'Yonge Street and Dundas Street',

    'Yonge Street and Elm Street': 'Yonge Street and Elm Street',
    '351 Yonge Street': 'Yonge Street and Elm Street',

    'Yonge Street and College Street': 'Yonge Street and College Street',


    'Bond Street and Gould Street': 'Bond Street and Gould Street',
    'Gould Street and Bond Street': 'Bond Street and Gould Street',
    'Gold Street and Bond Street': 'Bond Street and Gould Street',

    'Bond Street and Dundas Street': 'Bond Street and Dundas Street',
    'Bond Street and Dundas Street East': 'Bond Street and Dundas Street',


    'Victoria Street and Gould Street': 'Victoria Street and Gould Street',
    'Gould Street and Victoria Street': 'Victoria Street and Gould Street',
    'Victoria Street and Gould Street ': 'Victoria Street and Gould Street',
    'Victoria Street and Gould Street area': 'Victoria Street and Gould Street',
    'Gould Street and Victoria Street area': 'Victoria Street and Gould Street',

    'Victoria Street and Dundas Street': 'Victoria Street and Dundas Street',
    'Victoria Street and Dundas Street East': 'Victoria Street and Dundas Street',
    'Dundas Street East and Victoria Street': 'Victoria Street and Dundas Street',
    'Victoria Street and Dundas Street area': 'Victoria Street and Dundas Street',

    'Victoria Street and Gerrard Street': 'Victoria Street and Gerrard Street',
    'Victoria Street and Gerrard Street East': 'Victoria Street and Gerrard Street',
    'Gerrard Street and Victoria Street': 'Victoria Street and Gerrard Street',
    'Gerrard Street East and Victoria Street': 'Victoria Street and Gerrard Street',
    'Gerrard Street and Victoria Laneway area': 'Victoria Street and Gerrard Street',

    "Nelson Mandela Walk": "Nelson Mandela Walk",

    'Nelson Mandela Walk and Gould Street': 'Nelson Mandela Walk and Gould Street',

    'Nelson Mandela Walk and Gerrard Street': 'Nelson Mandela Walk and Gerrard Street',
    'Gerrard Street East and Nelson Mandela Walk': 'Nelson Mandela Walk and Gerrard Street',
    'Nelson Mandela Walk and Gerrard Street East': 'Nelson Mandela Walk and Gerrard Street',


    'Church Street and Gould Street': 'Church Street and Gould Street',
    'Gould Street and Church Street': 'Church Street and Gould Street',

    'Church Street and Gerrard Street': 'Church Street and Gerrard Street',
    'Church Street and Gerrard Street East': 'Church Street and Gerrard Street',
    'Gerrard Street East and Church Street': 'Church Street and Gerrard Street',
    'Church Street and Gerrard Street East ': 'Church Street and Gerrard Street',
    'Church Street and Gerrard Street area': 'Church Street and Gerrard Street',

    'Church Street and Dundas Street': 'Church Street and Dundas Street',
    'Church Street and Dundas Street East': 'Church Street and Dundas Street',
    'Dundas Street East and Church Street': 'Church Street and Dundas Street',

    'Church Street and Carlton Street': 'Church Street and Carlton Street',
    'Carlton Street and Church Street': 'Church Street and Carlton Street',


    "O'Keefe Laneway and Gould Street": "O'Keefe Laneway and Gould Street",
    'O’Keefe Laneway and Gould Street': "O'Keefe Laneway and Gould Street",
    'Gould Street and O’Keefe Lane': "O'Keefe Laneway and Gould Street",
    'O’Keefe Lane and Gould Street': "O'Keefe Laneway and Gould Street",
    'Gould Street and O’Keefe Laneway': "O'Keefe Laneway and Gould Street",

    "O'Keefe Laneway and Gerrard Street": "O'Keefe Laneway and Gerrard Street",
    'O’Keefe Laneway and Gerrard Street': "O'Keefe Laneway and Gerrard Street",
    'Gerrard Street East and O’Keefe Laneway': "O'Keefe Laneway and Gerrard Street",


    'Mutual Street and Gould Street': 'Mutual Street and Gould Street',

    'Mutual Street and Dundas Street': 'Mutual Street and Dundas Street',
    'Mutual Street and Dundas Street East': 'Mutual Street and Dundas Street',
    'Dundas Street East and Mutual Street': 'Mutual Street and Dundas Street',

    'Mutual Street and Gerrard Street': 'Mutual Street and Gerrard Street',
    'Mutual Street and Gerrard Street East': 'Mutual Street and Gerrard Street',
    'Gerrard Street East and Mutual Street': 'Mutual Street and Gerrard Street',


    'Jarvis Street and Dundas Street': 'Jarvis Street and Dundas Street',
    'Jarvis Street and Dundas Street East': 'Jarvis Street and Dundas Street',
    'Dundas Street East and Jarvis Street': 'Jarvis Street and Dundas Street',

    'Jarvis Street and Gerrard Street': 'Jarvis Street and Gerrard Street',
    'Gerrard Street East and Jarvis Street': 'Jarvis Street and Gerrard Street',

    'Bay Street and Dundas Street': 'Bay Street and Dundas Street',
    'Dundas Street West and Bay Street': 'Bay Street and Dundas Street',


    'Dalhousie Street and Gould Street': 'Dalhousie Street and Gould Street',
    'Gould Street and Dalhousie Street': 'Dalhousie Street and Gould Street',

    'Dalhousie Street and Dundas Street': 'Dalhousie Street and Dundas Street',
    'Dundas Street East and Dalhousie Street': 'Dalhousie Street and Dundas Street',


    #Buildings / landmarks

    'Yonge - Dundas Square': 'Yonge - Dundas Square',
    'Yonge-Dundas Square': 'Yonge - Dundas Square',
    'Yonge - Dundas Square building': 'Yonge - Dundas Square',
    'Yonge-Dundas Square building': 'Yonge - Dundas Square',

    'HOEM': 'HOEM',

    'Jorgenson Hall': 'Jorgenson Hall',

    'Devonian Pond': 'Devonian Pond',

    'Pitman Hall': 'Pitman Hall',
    'Pitman Hall Quad ': 'Pitman Hall',

    'Victoria Building': 'Victoria Building',
    'Victoria building': 'Victoria Building',
    '285 Victoria Street': 'Victoria Building',
    '285 Victoria Street planters': 'Victoria Building',

    'Sally Horsfall Eaton Centre for Studies in Community Health': 'Sally Horsfall Eaton Centre for Studies in Community Health',
    'Dundas Station': 'Dundas Station',
    'Daphne Cockwell Complex': 'Daphne Cockwell Complex',
    'Ram in the Rye Pub': 'Ram in the Rye Pub',

    'The G. Raymond Chang School of Continuing Education': 'The G. Raymond Chang School of Continuing Education',
    'Heaslip House and the G. Raymond Chang School of Continuing Education': 'The G. Raymond Chang School of Continuing Education',


    'Library': 'Library',
    'Library building': 'Library',

    'Mattamy Athletic Centre': 'Mattamy Athletic Centre',
    'Mattamy Athletic Centre at the Gardens': 'Mattamy Athletic Centre',

    'Recreation and Athletics Centre': 'Recreation and Athletics Centre',
    'Recreational and Athletics Centre': 'Recreation and Athletics Centre',

    'Rogers Communications Centre': 'Rogers Communications Centre',
    'Rogers Communication Centre': 'Rogers Communications Centre',

    'George Vari Engineering and Computing Centre': 'George Vari Engineering and Computing Centre',
    'George Vari Engineering and Computing Centre ': 'George Vari Engineering and Computing Centre',

    'Student Learning Centre': 'Student Learning Centre',
    'Student Learning Centre building': 'Student Learning Centre',
    'Basil Box at the Student Learning Centre': 'Student Learning Centre',
    'Student Learning Center': 'Student Learning Centre',

    'Ted Rogers School of Management': 'Ted Rogers School of Management',
    'Ted Rogers School of Management building': 'Ted Rogers School of Management',

    'Podium': 'Podium',
    'Podium building': 'Podium',

    'Kerr Hall': 'Kerr Hall',
    'Kerr Hall Quad': 'Kerr Hall',

    'Kerr Hall West': 'Kerr Hall West',

    'Kerr Hall South': 'Kerr Hall South',

    "Balzac's": "Balzac's",
    'Balzac’s at the Ryerson Image Centre': "Balzac's",
    'Balzac’s at the Ryerson Image Arts Centre': "Balzac's",

    #No location
    'Online': 'No Location',
    'Ryerson campus': 'No Location',
    'Yonge Street and Bay Street': 'No Location',

}

def assign_names_pixels(location):

    try:
        name = proper_location_names[f'{location}']
    except:
        print("The following location does not exist in the system: " + location)
        
    pixels = pixel_locations[f'{name}']

    result = [name, pixels[0], pixels[1]]

    return result

'''
Raw Data:

('Yonge Street and Gould Street',) 
('Yonge Street and  Gould Street',)
('Gould Street and Yonge Street',)
('Yonge Street and Gould Street ',)

('Yonge Street and Gerrard Street',)
('Yonge Street and Gerrard Street West',)
('Gerrard Street East and Yonge Street',)
('Gerrard Street and Yonge Street',)
('Yonge Street and Gerrard Street East',)
('Yonge Street and Gerrard Street West area',)
('Yonge Street and Gerrard Street area',)

('Yonge Street and Dundas Street',)
('Yonge Street and Dundas Street West',)
('Dundas Street and Yonge Street',)
('Yonge Street and Dundas Street East',)
('Yonge Street between College Street and Dundas Street',)
('Dundas Street West and Yonge Street',)

('Yonge Street and Elm Street',)

('Yonge Street and College Street',)


('Bond Street and Gould Street',)
('Gould Street and Bond Street',) 
('Gold Street and Bond Street',)

('Bond Street and Dundas Street',)
('Bond Street and Dundas Street East',)


('Victoria Street and Gould Street',)
('Gould Street and Victoria Street',)
('Victoria Street and Gould Street ',)
('Victoria Street and Gould Street area',)
('Gould Street and Victoria Street area',)

('Victoria Street and Dundas Street East',)
('Dundas Street East and Victoria Street',)
('Victoria Street and Dundas Street',)
('Victoria Street and Dundas Street area',)

('Victoria Street and Gerrard Street',)
('Victoria Street and Gerrard Street East',)
('Gerrard Street and Victoria Street',)
('Gerrard Street East and Victoria Street',)
('Gerrard Street and Victoria Laneway area',)


('Nelson Mandela Walk and Gould Street',)

('Nelson Mandela Walk and Gerrard Street',)
('Gerrard Street East and Nelson Mandela Walk',)
('Nelson Mandela Walk and Gerrard Street East',)


('Church Street and Gould Street',)
('Gould Street and Church Street',)

('Church Street and Gerrard Street',)
('Church Street and Gerrard Street East',)
('Gerrard Street East and Church Street',)
('Church Street and Gerrard Street East ',)
('Church Street and Gerrard Street area',)

('Church Street and Dundas Street',)
('Church Street and Dundas Street East',)

('Church Street and Carlton Street',)
('Carlton Street and Church Street',)


("O'Keefe Laneway and Gould Street",)
('O’Keefe Laneway and Gould Street',)
('Gould Street and O’Keefe Lane',)
('O’Keefe Lane and Gould Street',)
('Gould Street and O’Keefe Laneway',)

("O'Keefe Laneway and Gerrard Street",)
('O’Keefe Laneway and Gerrard Street',)
('Gerrard Street East and O’Keefe Laneway',)


('Mutual Street and Gould Street',)

('Mutual Street and Dundas Street',)
('Mutual Street and Dundas Street East',)
('Dundas Street East and Mutual Street',)

('Mutual Street and Gerrard Street',)
('Mutual Street and Gerrard Street East',)
('Gerrard Street East and Mutual Street',)


('Jarvis Street and Dundas Street',)
('Jarvis Street and Dundas Street East',)
('Dundas Street East and Jarvis Street',)

('Jarvis Street and Gerrard Street')
('Gerrard Street East and Jarvis Street',)

('Bay Street and Dundas Street')
('Dundas Street West and Bay Street',)


('Dalhousie Street and Gould Street',)
('Gould Street and Dalhousie Street',)

('Dalhousie Street and Dundas Street')
('Dundas Street East and Dalhousie Street',)


#Buildings / landmarks

('Yonge - Dundas Square',)
('Yonge-Dundas Square',)
('Yonge - Dundas Square building',)
('Yonge-Dundas Square building',)

('HOEM',)
('Jorgenson Hall',)
('Devonian Pond',)

('Pitman Hall')
('Pitman Hall Quad ',)

('351 Yonge Street',)

('285 Victoria Street')
('285 Victoria Street planters',)

('Sally Horsfall Eaton Centre for Studies in Community Health',)
('Dundas Station',)
('Daphne Cockwell Complex',)
('Ram in the Rye Pub',)

('The G. Raymond Chang School of Continuing Education',)
('Heaslip House and the G. Raymond Chang School of Continuing Education',)
('Victoria building',)

('Library',)
('Library building',)

('Mattamy Athletic Centre',)
('Mattamy Athletic Centre at the Gardens',)

('Recreation and Athletics Centre',)
('Recreational and Athletics Centre',)

('Rogers Communications Centre',)
('Rogers Communication Centre',)

('George Vari Engineering and Computing Centre',)
('George Vari Engineering and Computing Centre ',)

('Student Learning Centre',)
('Student Learning Centre building',)
('Basil Box at the Student Learning Centre',)
('Student Learning Center',)

('Ted Rogers School of Management',)
('Ted Rogers School of Management building',)

('Podium',)
('Podium building',)

('Kerr Hall',)
('Kerr Hall Quad',)

('Kerr Hall West',)

('Kerr Hall South',)

("Balzac's")
('Balzac’s at the Ryerson Image Centre',)
('Balzac’s at the Ryerson Image Arts Centre',)

#No location
('Online',)
('Ryerson campus',)
('Yonge Street and Bay Street',)


'''