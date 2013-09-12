import os, shutil, glob

USstates = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}


src = 'E:\\datafiles\\aasggeothermal'

gdbaList = glob.glob(src+'\\*\\*\\*.gdb')
gdbbList = glob.glob(src+'\\*\\*\\*\\*.gdb')
gdbcList = glob.glob(src+'\\*\\*\\*\\*\\*.gdb')
gdbdList = glob.glob(src+'\\*\\*\\*\\*\\*\\*.gdb')
gdbeList = glob.glob(src+'\\*\\*.gdb')
gdbfList = glob.glob(src+'\\*.gdb')

gdbList = gdbaList + gdbbList + gdbcList + gdbdList + gdbeList + gdbfList

for gdb in gdbList:
    filename = gdb.rsplit('\\',1)
    filename = filename[1]
    state = USstates.get(filename[0:2])
    path = 'E:\\datafiles\\newTree\\'+state+'\\service_gdb'
    if not os.path.exists(path):
        os.makedirs(path)
    try:
        shutil.move(gdb,path)
    except: print "Could not move " + str(gdb) +'.  A file of the same name already exists.'
