import random as rd
e = ""

#fake data
names = [
    "Andy", "Jake", "Richard", "Kate", "Andrew", "Tyler", "Christina", "Tommy",
    "William", "Davis", "David", "Isha", "Jenny", "Kris", "Katty", "Sam",
    "Jonathan", "Marian", "Mary", "Kenny", "Sophia", "Lucas", "Oliver", "Mason",
    "Charlotte", "Ethan", "Amelia", "Jack", "Lily", "James", "Chloe", "Benjamin",
    "Emma", "Elijah", "Ava", "Matthew", "Zoe", "Cameron", "Grace", "Henry",
    "Megan", "Daniel", "Leah", "Michael", "Samantha", "Joshua", "Ella", "Ryan",
    "Abigail", "Isaac", "Victoria", "John", "Mila", "Leo", "Emily", "Aidan",
    "Natalie", "Madison", "Nolan", "Eva", "Matthew", "Scarlett", "Harper",
    "Sebastian", "Luna", "Nathaniel", "Ruby", "Caleb", "Victoria", "Logan",
    "Hannah", "Liam", "Avery", "Maya", "Sophie", "Oliver", "Isaiah", "Lydia",
    "Maggie", "Oliver", "Emma", "George", "Amos", "Nina", "Samantha", "Walter",
    "Samuel", "Sophia", "Ryan", "Lori", "Zachary", "Derek", "Harold", "Brian",
    "Aiden", "Isla", "Riley", "Eli", "Madeline", "Vera", "Michaela", "Myles",
    "Kai", "Dylan", "Ellie", "Tobias", "Avery", "Tessa", "Bella", "Xander",
    "Carter", "Maddox", "Olivia", "Miles", "Henry", "Rachel", "Mason", "Ivy",
    "Abby", "Charlie", "Liam", "Brody", "Jade", "Gavin", "Gage", "Eliza"
]

# fake data
birth_date = [
    "3/14/1987", "7/22/1993", "11/5/2001", "4/2/1979", "8/17/2000", "1/16/1985",
    "9/24/1998", "6/18/1967", "2/25/1995", "3/19/1991", "12/31/1982", "10/4/1999",
    "5/30/2003", "7/10/2000", "4/22/1994", "6/6/1990", "8/1/1980", "2/14/2005",
    "11/22/2000", "3/1/1985", "12/15/1998", "4/17/1990", "7/9/1992", "5/8/1991",
    "1/7/1988", "9/30/1996", "2/18/1993", "8/25/1985", "4/13/1987", "6/4/1997",
    "11/11/1999", "10/10/1995", "9/2/2002", "12/22/1980", "5/5/1994", "7/20/1986",
    "8/23/1999", "3/12/1997", "1/24/2000", "2/3/1989", "9/15/1990", "4/11/1995",
    "3/8/1986", "5/13/1998", "10/21/2004", "11/9/1991", "2/17/1996", "9/3/1984",
    "6/16/2003", "7/15/1993", "1/30/2000", "5/25/1997", "4/20/1991", "8/9/1998",
    "7/29/1988", "3/25/2002", "5/1/1994", "10/5/1992", "6/9/1991", "8/14/1989",
    "12/10/1996", "10/17/2001", "11/14/2000", "5/21/1995", "2/9/1984", "3/7/1990",
    "4/27/1997", "8/30/1992", "6/13/1985", "12/5/1999", "9/27/1994", "2/11/1993",
    "11/18/1987", "7/5/1991", "1/15/1999", "10/23/1990", "4/3/1983", "3/27/1992",
    "6/12/2000", "8/20/1997", "5/17/1988", "10/19/2003", "1/10/1998", "2/1/1995",
    "7/1/1992", "4/24/1996", "3/9/1988", "9/21/1999", "10/8/2001", "12/12/1985"
]

# fake data
adres = [
    "Maplewood", "Redstone", "Aspen", "Hollow", "Evergreen", "Sunrise", "Silside",
    "Tunsil", "Pytime", "Yorndale", "Kedhide", "Cardle", "Maryland", "Yankle",
    "Boslan", "Serchal", "Briarwood", "Oakridge", "Cedarbrook", "Greenfield",
    "Highland", "Lakeview", "Westbrook", "Willow Creek", "Pine Hill", "Shadow Ridge",
    "Lakeside", "Sunnyvale", "Foxwood", "Hillcrest", "Stonebridge", "Golden Valley",
    "Silverpine", "Blue Ridge", "Riverside", "Springfield", "Sunset Park", "Cottonwood",
    "Cypress", "Bayshore", "Windmill", "Birchwood", "Redwing", "Cloverfield",
    "Pinehurst", "Ashwood", "Northview", "Woodlawn", "Clearwater", "Canyon Lake",
    "Parkview", "Hilltop", "Meadowbrook", "Morningstar", "Frostwood", "Silverleaf",
    "Stonegate", "Eastwood", "Mountainview", "Silverstream", "Newport", "Chestnut",
    "Bayview", "Eastbrook", "Country Lane", "Riverbend", "Green Meadows", "Violet Hill",
    "Marblewood", "Waterstone", "Eastgate", "Brighton", "Redwood", "Woodland",
    "Ridgefield", "Sunrise Heights", "Blackwood", "Timberlake", "Northgate", "Silverhill",
    "Magnolia", "Cinnamon Park", "Brookstone", "Sandstone", "Woodspring", "Bluebell",
    "Golden Oaks", "Rolling Hills", "Westfield", "Oakhurst", "Autumnwood", "Shady Acres",
    "Linden", "Sunnyside", "Maple Grove", "Riverstone", "Crystal Creek", "Pine Ridge",
    "Sunset Ridge", "Woodbine", "Morningwood", "Crystal Hill", "Bear Creek", "Windswept",
    "Clearbrook", "Foxrun", "Silver Oak", "Ironwood", "Riverwalk", "Pinefield",
    "Autumn Ridge", "Whispering Pines", "Valley Forge", "Oakdale", "Meadowview", "Cottonhill"
]

#fake data
credit = [
    "729 444 862", "411 222 829", "453 666 937", "536 555 817", "378 444 622",
    "411 333 759", "491 777 803", "539 444 892", "453 555 728", "438 111 930",
    "489 666 851", "456 222 923", "502 444 837", "427 555 915", "533 333 874",
    "458 444 722", "491 666 918", "493 555 732", "401 777 892", "523 444 823",
    "456 222 821", "492 111 938", "501 666 859", "536 444 732", "478 555 830",
    "411 222 821", "531 666 913", "429 444 926", "503 555 821", "494 111 938",
    "520 444 819", "453 555 722", "426 333 862", "450 444 926", "502 666 813",
    "419 555 726", "432 333 838", "536 444 729", "472 555 930", "491 222 913",
    "427 111 811", "493 444 815", "519 555 824", "409 666 836", "451 444 920",
    "438 555 837", "472 333 827", "427 444 928", "499 555 917", "469 111 828",
    "421 444 938", "492 555 924", "530 333 927", "437 444 912", "428 555 835",
    "429 666 913", "453 444 825", "521 555 930", "431 333 825", "456 444 913",
    "492 555 728", "477 111 931", "435 444 817", "432 555 812", "473 333 919",
    "432 444 919", "520 555 826", "497 666 911", "531 444 930", "458 555 813",
    "495 111 832", "422 444 831", "459 555 917", "452 333 824", "541 444 912",
    "429 555 913", "418 666 917", "456 444 930", "427 555 821", "431 333 920",
    "510 444 818", "473 555 926", "519 333 921", "491 444 929", "437 555 926",
    "492 333 817", "521 444 836", "453 555 819", "520 666 924", "431 444 922",
    "435 555 823", "427 333 931", "415 444 929", "431 555 836", "449 333 827",
    "419 444 823", "452 555 926", "437 666 912", "520 444 830", "495 555 923",
    "431 333 826", "470 444 918", "432 555 824", "521 333 921", "438 444 927",
    "514 555 920", "429 333 831", "457 444 923", "491 555 816", "532 333 917",
    "451 444 830", "435 555 923", "459 666 923", "441 444 918", "423 555 820",
    "497 333 929", "462 444 921", "411 555 929", "536 333 930", "491 444 913",
    "452 555 827", "439 333 912", "442 444 920", "432 555 819", "511 333 920",
    "444 444 922", "493 555 921", "491 333 920", "519 444 920", "451 555 813",
    "490 333 926", "533 444 923", "440 555 819", "432 333 921", "512 444 827",
    "529 555 917", "453 333 826", "438 444 920", "434 555 822", "491 333 926",
    "522 444 831", "472 555 923", "438 333 930", "492 444 917"
]

#fake data
phone = [
    "(555) 123-4567", "(555) 234-5678", "(555) 345-6789", "(555) 456-7890",
    "(555) 567-8901", "(555) 678-9012", "(555) 789-0123", "(555) 890-1234",
    "(555) 901-2345", "(555) 012-3456", "(555) 123-0987", "(555) 234-1098",
    "(555) 345-2109", "(555) 456-3210", "(555) 567-4321", "(555) 678-5432",
    "(555) 789-6543", "(555) 890-7654", "(555) 901-8765", "(555) 012-9876",
    "(555) 123-7654", "(555) 234-8765", "(555) 345-9876", "(555) 456-1098",
    "(555) 567-2109", "(555) 678-3210", "(555) 789-4321", "(555) 890-5432",
    "(555) 901-6543", "(555) 012-7654", "(555) 123-8765", "(555) 234-9876",
    "(555) 345-1098", "(555) 456-2109", "(555) 567-3210", "(555) 678-4321",
    "(555) 789-5432", "(555) 890-6543", "(555) 901-7654", "(555) 012-8765",
    "(555) 123-9876", "(555) 234-1098", "(555) 345-2109", "(555) 456-3210",
    "(555) 567-4321", "(555) 678-5432", "(555) 789-6543", "(555) 890-7654",
    "(555) 901-8765", "(555) 012-9876", "(555) 123-7654", "(555) 234-8765",
    "(555) 345-9876", "(555) 456-1098", "(555) 567-2109", "(555) 678-3210",
    "(555) 789-4321", "(555) 890-5432", "(555) 901-6543", "(555) 012-7654",
    "(555) 123-8765", "(555) 234-9876", "(555) 345-1098", "(555) 456-2109",
    "(555) 567-3210", "(555) 678-4321", "(555) 789-5432", "(555) 890-6543",
    "(555) 901-7654", "(555) 012-8765", "(555) 123-9876", "(555) 234-1098",
    "(555) 345-2109", "(555) 456-3210", "(555) 567-4321", "(555) 678-5432",
    "(555) 789-6543", "(555) 890-7654", "(555) 901-8765", "(555) 012-9876",
    "(555) 123-7654", "(555) 234-8765", "(555) 345-9876", "(555) 456-1098",
    "(555) 567-2109", "(555) 678-3210", "(555) 789-4321", "(555) 890-5432"
]

#fake data
ssn = [
    "ASD-102-8291", "ADA-381-7539", "GFQ-213-7194", "XRY-459-2837",
    "JKP-832-1456", "VBN-756-4381", "WER-564-9217", "TYU-641-2380",
    "PKO-972-5610", "KLM-463-8975", "ZXF-823-4671", "BCH-395-6342",
    "JPL-176-8954", "SDV-694-8357", "FVQ-250-9571", "DKS-572-1639",
    "LJQ-937-8462", "NSL-861-4725", "RTN-124-9083", "MVO-632-5098",
    "PIJ-783-2456", "ZKT-572-8319", "LWE-645-1782", "BVN-824-5307",
    "OTG-694-2910", "XGK-539-4726", "JYF-827-6530", "MFW-394-5217",
    "QFR-968-1753", "IUT-382-7645", "YHN-643-8925", "DZW-716-5402",
    "LQA-859-3217", "YFU-594-3271", "ZSP-563-0892", "MVP-451-0739",
    "QMI-745-2531", "BPL-636-4917", "KCM-384-6712", "TQE-975-8412",
    "XSV-302-9846", "PYH-658-5372", "RKP-492-7685", "WOI-745-6310",
    "NSL-563-9782", "WRP-926-4051", "CYO-548-7391", "AVC-672-4893",
    "FXZ-852-3790", "PRW-436-6179", "BJK-783-2145", "MNO-215-9380",
    "KRB-637-5064", "WXL-318-9052", "VWD-827-4316", "SNF-961-2847",
    "DHR-742-8593", "PRL-604-8735", "BJC-185-7429", "GQX-367-5204",
    "LEU-968-7451", "YFA-473-2069", "KFI-953-6420", "HNG-745-3281",
    "LDF-273-8495", "YVX-486-1532", "RHE-561-8234", "AIO-273-9451",
    "MOH-153-2089", "GPA-462-1750", "UWB-917-4632", "QWE-546-8371",
    "FWX-253-6748", "OIQ-935-2075", "JMZ-648-5207", "VOW-397-4621",
    "KNG-623-0589", "XAP-174-2395", "LTF-735-2498", "YIM-572-6813",
    "LGS-430-8271", "PZW-960-5832", "RDA-248-4637", "GJE-601-1937",
    "BPT-318-4705", "NFU-394-8650", "SKD-759-3128", "HFC-821-6942",
    "NPI-516-7483", "YBC-983-4521", "AKD-257-4931", "JRX-643-0579",
    "PKA-572-9306", "DTN-938-4812", "ZQA-195-5627", "WDB-452-6891",
    "FMN-813-2704", "SPL-950-6372", "YKX-295-8613", "LNR-362-1950",
    "GWU-238-5034", "BPI-429-6175", "ACW-751-9842", "VUL-380-5296",
    "YQP-196-7543", "PLH-824-3706", "MRQ-632-1458", "LJP-406-5703",
    "XTK-954-2837", "CVU-573-1049", "KPV-736-5892", "HNY-341-6280",
    "AWS-587-4920", "DOX-912-6357", "VTN-670-4185", "LMF-267-5398",
    "PWJ-801-9426", "FRL-345-2087", "BKM-874-6301", "RPE-543-2967",
    "FSV-932-8145", "KJW-471-6583", "IVH-650-9710", "PNQ-758-3642",
    "CMJ-185-6403", "JTN-304-1526", "TXF-759-2834", "ZPU-691-5742",
    "BSW-824-5137", "RJG-268-3519", "VBF-502-7368", "EOS-913-7854",
    "BPO-415-2679", "DWX-381-9647", "YCQ-692-7418", "KPF-170-2593",
    "VZE-538-6029", "TWE-917-6543", "YXA-456-2839", "GCI-385-9204",
    "LKT-760-8593", "WPN-261-4786", "NCZ-758-6240", "MRU-523-9815"
]

#fake data
jos = ['Web Developer', 'Database Administrator', 'Cybersecurity Specialist',
       'Cloud Engineer', 'Full Stack Developer', 'Network Engineer',
       'IT Project Manager', 'Game Developer', 'QA Tester', 'DevOps Engineer',
       'IT Consultant', 'Blockchain Developer', 'Technical Writer',
       'SEO Specialist', 'Product Manager', 'Cloud Solutions Architect',
       'Technical Support Engineer', 'Registered Nurse', 'Surgeon', 'Pharmacist',
       'Dentist', 'Occupational Therapist', 'Psychologist', 'Nurse Practitioner',
       'Laboratory Technician', 'Pediatrician', 'Medical Coder', 'Health Coach',
       'Chiropractor', 'Emergency Room Doctor', 'Medical Researcher', 'Endocrinologist',
       'Anesthesiologist', 'Financial Analyst', 'Investment Banker',
       'Financial Planner', 'Tax Consultant', 'Chief Financial Officer',
       'Credit Analyst', 'Auditor', 'Risk Manager', 'Business Consultant',
       'Portfolio Manager', 'Insurance Underwriter', 'Operations Manager',
       'Marketing Manager', 'Real Estate Agent', 'Commercial Banker', 'Actuary',
       'Corporate Strategy Manager', 'Procurement Specialist', 'Controller',
       'Tax Advisor', 'Forensic Accountant', 'Equity Analyst',
       'Mergers and Acquisitions Specialist', 'School Principal',
       'Educational Consultant', 'School Counselor', 'Special Education Teacher',
       'College Professor', 'Tutor', 'Instructional Designer', 'Education Administrator',
       'Teaching Assistant', 'ESL Teacher', 'Test Proctor', 'Literacy Specialist',
       'Art Teacher', 'Online Course Instructor', 'Physical Education Teacher',
       'Foreign Language Teacher', 'Educational Content Writer',
       'Learning and Development Specialist', 'Graphic Designer', 'Illustrator',
       'Animator', 'Video Editor', 'Photographer', 'Industrial Designer',
       'Interior Designer', 'Web Designer', 'Creative Director',
       'Product Designer', 'Brand Manager', '3D Modeler', 'User Interface Designer',
       'Set Designer', 'Game Designer', 'Print Designer', 'Content Creator',
       'Social Media Manager', 'Print Production Specialist', 'Sales Representative',
       'Digital Marketing Manager', 'SEO Manager', 'Affiliate Marketing Manager',
       'Customer Success Manager', 'Sales Engineer', 'Product Marketing Manager',
       'Marketing Coordinator', 'Social Media Specialist', 'Market Research Analyst',
       'E-commerce Manager', 'Inside Sales Representative', 'Real Estate Broker',
       'PR Specialist', 'Media Buyer', 'Marketing Director', 'Sales Trainer',
       'Campaign Manager', 'Legal Assistant', 'Judge', 'Legal Counsel',
       'Compliance Officer', 'Corporate Lawyer', 'Contract Manager',
       'Criminal Defense Attorney', 'Tax Attorney', 'Immigration Lawyer',
       'Litigation Support Specialist', 'Human Rights Lawyer',
       'Corporate Compliance Manager', 'Notary Public', 'Public Defender',
       'Court Reporter', 'Legal Consultant', 'Prosecutor', 'Environmental Lawyer',
       'Electrician', 'Carpenter', 'HVAC Technician', 'Welder', 'Landscaper',
       'Sheet Metal Worker', 'Mason', 'Flooring Installer', 'Home Inspector',
       'Demolition Worker', 'Welding Inspector', 'Crane Operator', 'Plumbing Technician',
       'Tile Setter', 'Bartender', 'Hotel Manager', 'Sous Chef', 'Food Stylist',
       'Catering Manager', 'Front Desk Agent', 'Barista', 'Dish Washer', 'Food Safety Manager',
       'Travel Agent', 'Catering Assistant', 'Hotel Concierge', 'Buffet Attendant',
       'Inventory Control Specialist', 'Assembly Line Worker', 'Freight Coordinator',
       'Manufacturing Technician', 'Process Engineer', 'Plant Manager',
       'Distribution Center Associate', 'Fabricator', 'Cost Analyst']

# fake data
emails = [
    "abrahamlincoln245@historymail.com", "paris328@travellog.net", "elonmusk4567@techmail.org",
    "einstein98@geniusmail.com", "thedarkknight307@heroesmail.com", "bigben876@landmark.net",
    "michaeljackson559@musicmail.com", "starwars333@galaxymail.com", "vatican220@catholicmail.org",
    "johndoe502@unknownmail.com", "hollywood845@fakemail.com", "tuscany611@landmark.net",
    "mounteverest345@travellog.net", "titanic4537@fakemail.com", "shakespeare72@geniusmail.com",
    "newyork212@fakemail.com", "tesla256@techmail.org", "amazon4789@techmail.org",
    "cocacola982@foodmail.com", "google834@techmail.org", "louvre92@artmail.com",
    "marilynmonroe701@fakemail.com", "markzuckerberg543@techmail.org", "hollywood129@fakemail.com",
    "harrypotter208@fictionalmail.com", "london112@landmark.net", "facebook338@techmail.org",
    "beijing555@landmark.net", "theda vinci913@geniusmail.com", "starwars708@galaxymail.com",
    "louvre318@artmail.com", "amazon491@techmail.org", "monalisa897@artmail.com",
    "mumbai385@landmark.net", "tuscany271@landmark.net", "mounteverest303@travellog.net",
    "markzuckerberg543@techmail.org", "cocacola219@foodmail.com", "spacex784@techmail.org",
    "newyork223@fakemail.com", "einstein499@geniusmail.com", "abrahamlincoln243@historymail.com",
    "michaeljackson645@musicmail.com", "elvis702@musicmail.com", "harrypotter365@fictionalmail.com",
    "hollywood559@fakemail.com", "tesla456@techmail.org", "vatican520@catholicmail.org",
    "mounteverest875@travellog.net", "paris477@travellog.net", "starwars933@galaxymail.com",
    "beijing274@landmark.net", "london342@landmark.net", "shakespeare902@geniusmail.com",
    "apple743@techmail.org", "titanic112@fakemail.com", "vatican753@catholicmail.org",
    "spacex345@techmail.org", "johndoe803@unknownmail.com", "elvis451@musicmail.com",
    "bigben399@landmark.net", "thedarkknight591@heroesmail.com", "johndoe409@unknownmail.com",
    "louvre540@artmail.com", "amazon222@techmail.org", "newyork204@fakemail.com",
    "mumbai771@landmark.net", "michaeljackson618@musicmail.com", "beijing635@landmark.net",
    "hollywood467@fakemail.com", "markzuckerberg392@techmail.org", "spacex510@techmail.org",
    "elvis238@musicmail.com", "london576@landmark.net", "titanic318@fakemail.com",
    "abrahamlincoln853@historymail.com", "eltonjohn202@musicmail.com", "bigben428@landmark.net",
    "thedarkknight615@heroesmail.com", "mounteverest561@travellog.net", "paris109@travellog.net",
    "newyork604@fakemail.com", "einstein381@geniusmail.com", "mumbai924@landmark.net",
    "hollywood383@fakemail.com", "apple568@techmail.org", "johndoe456@unknownmail.com",
    "vatican722@catholicmail.org", "abrahamlincoln275@historymail.com", "cocacola104@foodmail.com",
    "eltonjohn563@musicmail.com", "titanic856@fakemail.com", "starwars209@galaxymail.com",
    "elvis394@musicmail.com", "google931@techmail.org", "michaeljackson128@musicmail.com",
    "paris875@travellog.net", "spacex257@techmail.org", "tuscany842@landmark.net",
    "johndoe372@unknownmail.com", "markzuckerberg495@techmail.org", "thedarkknight921@heroesmail.com",
    "hollywood728@fakemail.com", "titanic305@fakemail.com", "shakespeare306@geniusmail.com",
    "thedavinici609@geniusmail.com", "tuscany948@landmark.net", "starwars762@galaxymail.com",
    "eltonjohn583@musicmail.com", "newyork102@fakemail.com"
]

#fake data
crim = ["No", "Yes", "No"]

#fake data
sec = [
    "First pet's name?", "Street you grew up on?", "Mother's maiden name?", "Birth city?",
    "First school name?", "First childhood friend?", "First car make?", "Favorite teacher's name?",
    "Favorite color?", "Favorite food?", "First employer's name?", "Father's middle name?",
    "First boss's name?", "Favorite restaurant?", "City at 18?", "Favorite book?", "Favorite movie?",
    "First school attended?", "First crush's name?", "First boyfriend/girlfriend?", "First holiday destination?",
    "First concert attended?", "Birth hospital name?", "Favorite sport?", "Where did you meet your spouse?",
    "Favorite hobby?", "First job?", "Best friend's name?", "Grandmother's name?", "Street in high school?",
    "Oldest child's first name?", "Childhood nickname?", "Favorite TV show?", "First job company name?",
    "Favorite season?", "First roommate's name?", "Childhood dream job?", "Favorite actor?", "First book read?",
    "Favorite school subject?", "Wedding city?", "Childhood hero?", "Favorite childhood toy?", "Father's first name?",
    "Favorite ice cream flavor?", "Pet's name?", "First phone number?", "First teacher's name?", "College city?",
    "First international trip?", "Mother's first name?", "Honeymoon destination?", "First movie in theaters?",
    "Favorite childhood game?", "Favorite music type?", "First school crush?", "Favorite holiday?", "Childhood best friend?",
    "High school location?", "Favorite store?", "Favorite animal?", "First car you drove?", "Favorite pizza topping?",
    "Best friend meet location?", "Mother's favorite hobby?", "9/11 memory location?", "First email address?",
    "First street lived on?", "Childhood phone number?", "Favorite vacation spot?", "Favorite childhood book?",
    "Spouse meeting place?", "High school best friend's first name?", "First best friend's name?", "High school city?",
    "Favorite place to visit?", "First school principal’s name?", "Where did you go to high school?", "First video game you played?",
    "First job company?", "Favorite childhood cartoon?", "Favorite holiday tradition?", "First toy you remember?",
    "First time on an airplane?", "Favorite place to relax?", "First celebrity crush?", "First car model?",
    "Best vacation destination?", "Favorite childhood snack?", "First concert band?", "First major purchase?",
    "Favorite childhood activity?", "First time overseas?", "Favorite childhood friend?", "First best friend’s nickname?",
    "First phone model?", "Favorite park to visit?", "First time you drove?", "Best holiday memory?", "Most memorable family trip?"
]

questions = [
    "What is the applicant's name? ",
    "What is the applicant's date of birth? ",
    "What is the applicant's address? ",
    "What is the applicant's phone number? ",
    "What is the applicant's SSN ",
    "What is the applicant's credit card number? ",
    "What is the applicant's job tittle? ",
    "What is the applicant's email? ",
    "Does the applicant have a criminal record? ",
    "What is the applicant's security question? "
]


done = 0
asked = ""
asked2 = ""

print('''You are a Data Verification Specialist.
Your job is to find the correct info and type it.
Make sure to put it the exact way it is written.
Type "quit" to leave your work.

** WARNING: All the data used is fake and for demonstration purposes only. **
''')
while done < 5:
  Bio = {
      "name": rd.choice(names),
      "date": rd.choice(birth_date),
      "address": rd.choice(adres),
      "phone": rd.choice(phone),
      "ssn": rd.choice(ssn),
      "credit": rd.choice(credit),
      "job": rd.choice(jos),
      "email": rd.choice(emails),
      "criminal": rd.choice(crim),
      "secure": rd.choice(sec)
        }
  print(f'''********************************************************************

                         Applicant Information

  Name: {Bio["name"]}            Date of birth: {Bio["date"]}

  Address: {Bio["address"]}      Phone number: {Bio["phone"]}

  SSN: {Bio["ssn"]}              Credit Card: {Bio["credit"]}

  Job: {Bio["job"]}             Email: {Bio["email"]}

  Criminal history: {Bio["criminal"]}         Security question: {Bio["secure"]}
  ''')

  asking = questions.copy()
  asked = rd.choice(asking)
  asking.remove(asked)
  asked2 = rd.choice(asking)
  asking.remove(asked2)
  answered = input(asked)
  if answered.lower() == "quit":
    print("------------------------------------")
    print("You have submitted your PTO request")
    print("------------------------------------")
    break
  answered2 = input(asked2)
  if answered2.lower() == "quit":
    print("------------------------------------")
    print("You have submitted your PTO request")
    print("------------------------------------")
    break
  def co(one, two):
    if two == questions[0]:
       if one == Bio["name"]:
         return True
    if two == questions[1]:
       if one == Bio["date"]:
         return True
    if two == questions[2]:
       if one == Bio["address"]:
         return True
    if two == questions[3]:
       if one == Bio["phone"]:
         return True
    if two == questions[4]:
       if one == Bio["ssn"]:
         return True
    if two == questions[5]:
       if one == Bio["credit"]:
         return True
    if two == questions[6]:
       if one == Bio["job"]:
         return True
    if two == questions[7]:
       if one == Bio["email"]:
         return True
    if two == questions[8]:
       if one == Bio["criminal"]:
         return True
    if two == questions[9]:
       if one == Bio["secure"]:
         return True

  a = co(answered, asked)
  b = co(answered2, asked2)
  if a == True and b == True:
    print(e)
    done += 1
    left = 5 - done
    print(f"Correct, next form. You have {left} forms left")
    print(e)
  else:
    print(e)
    left = 5 - done
    print(f"Incorrect, next form. You have {left} forms left")
    print(e)
if answered.lower() == "quit" or answered2.lower() == "quit":
  print(e)
else:
 print("-------------------------------")
 print("You have done a good day's work")
 print("-------------------------------")
