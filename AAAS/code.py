# # Priority Dictionary :
# priorety = {"IT Fundamentals": 1, "Mathematics I": 2, "Physics I": 4, "Electronics": 3, "English Language I": 3,
#             "Hand Drawing": 4,
#             "History of Computing": 4, "Social Context of Computing": 4, "Programming Fundamentals": 1,
#             "Mathematics II": 2,
#             "Physics II": 4, "Digital Circuits": 4, " Interpersonal Communication": 4, "Human Rights": 4,
#             "English Language II": 3,
#             "Computer Law": 4, "Discrete Structures": 2, "Object-Oriented Programming": 1, "Project Management": 1,
#             "Data Communications": 2,
#             "Technical Writing": 4, "Foundations of Information Systems": 2, "Business Administration": 4,
#             "Data Structures and Algorithms": 1,
#             "Databases": 3, "Computer Architecture": 2, "Probability and Statistics": 4, "Computers and Ethics": 4,
#             "Systems Analysis and Design": 4, "File Organization": 4, "Computer Networks": 2, "Image Processing": 3,
#             "Software Engineering": 1, "Visual Programming": 3, "Computer Graphics": 3,
#             "Algorithm Design and Analysis": 3,
#             "Operating Systems": 3, "Automata and Language Theory": 4, "Advanced Computer Graphics": 4,
#             "Artificial Intelligence": 3,
#             "Software Development and Professional Practice": 1, "Field Training": 4, "Compiler Construction": 4,
#             "Capstone Project I": 1,
#             "Introduction to Computer Security": 4, "Web Programming": 4, "Computer Vision": 4,
#             "Network Programming": 4, "Capstone Project II": 1,
#             "Machine Learning": 4, "Cryptography": 4, "Parallel Computation": 4, "Computer Animation": 4,
#             "Advanced Database": 4}
#
# # Prerequisite Dictionary for every Course
# prerequisite = {"IT Fundamentals": None, "Mathematics I": None, "Physics I": None, "Electronics": None,
#                 "English Language I": None, "Hand Drawing": None,
#                 "History of Computing": None, "Social Context of Computing": None,
#                 "Programming Fundamentals": "IT Fundamentals", "Mathematics II": "Mathematics I",
#                 "Physics II": None, "Digital Circuits": "Electronics", " Interpersonal Communication": None,
#                 "Human Rights": None, "English Language II": "English Language I",
#                 "Computer Law": None, "Discrete Structures": "Mathematics II",
#                 "Object-Oriented Programming": "Programming Fundamentals",
#                 "Project Management": "IT Fundamentals", "Data Communications": "IT Fundamentals",
#                 "Technical Writing": "English Language I", "Foundations of Information Systems": "IT Fundamentals",
#                 "Business Administration": None, "Data Structures and Algorithms": "Object-Oriented Programming",
#                 "Databases": "Foundations of Information Systems",
#                 "Computer Architecture": ["Programming Fundamentals", "Discrete Structures"],
#                 "Probability and Statistics": "Mathematics II", "Computers and Ethics": None,
#                 "Systems Analysis and Design": "IT Fundamentals", "File Organization": "Object-Oriented Programming",
#                 "Computer Networks": ["Computer Architecture", "Data Communications"],
#                 "Image Processing": "Data Structures and Algorithms",
#                 "Software Engineering": "Data Structures and Algorithms",
#                 "Visual Programming": "Data Structures and Algorithms",
#                 "Computer Graphics": ["Discrete Structures", "IT Fundamentals"],
#                 "Algorithm Design and Analysis": "Data Structures and Algorithms",
#                 "Operating Systems": "Computer Architecture",
#                 "Automata and Language Theory": ["Discrete Structures", "Programming Fundamentals"],
#                 "Advanced Computer Graphics": "Computer Graphics",
#                 "Artificial Intelligence": ["Discrete Structures", "IT Fundamentals"],
#                 "Software Development and Professional Practice": "Software Engineering",
#                 "Field Training": "Project Management",
#                 "Compiler Construction": ["Visual Programming", "Computer Architecture",
#                                           "Data Structures and Algorithms"],
#                 "Capstone Project I": ["Project Management", "Software Development and Professional Practice"],
#                 "Introduction to Computer Security": ["Computer Networks", "Data Structures and Algorithms"],
#                 "Web Programming": ["Data Communications", "Programming Fundamentals"],
#                 "Computer Vision": ["Physics II", "Object-Oriented Programming"],
#                 "Network Programming": "Computer Networks",
#                 "Capstone Project II": ["Project Management", "Software Development and Professional Practice"],
#                 "Machine Learning": "Artificial Intelligence",
#                 "Cryptography": ["Computer Networks", "Data Structures and Algorithms"],
#                 "Parallel Computation": ["Operating Systems", "Algorithm Design and Analysis"],
#                 "Computer Animation": "Image Processing", "Advanced Database": None}
#
# # studied = ['IT Fundamentals', 'Mathematics I', 'Electronics', 'English Language I', 'English Language II',
# #            'Physics I', 'Hand Drawing', 'History of Computing', 'Social Context of Computing',
# #            'Programming Fundamentals', 'Mathematics II', 'Physics II',
# #            'Digital Circuits', ' Interpersonal Communication', 'Human Rights', 'Computer Law',
# #            'Discrete Structures', 'Data Communications', 'Foundations of Information Systems',
# #            'Object-Oriented Programming', 'Project Management', 'Technical Writing', 'Business Administration',
# #             'Databases', 'Computer Architecture','Data Structures and Algorithms',
# #            'Probability and Statistics', 'Computers and Ethics',
# #            # 'Systems Analysis and Design', 'File Organization',
# #            #  'Computer Networks','Image Processing', 'Visual Programming', 'Computer Graphics',
# #            # 'Algorithm Design and Analysis', 'Software Engineering',
# #            # 'Operating Systems', 'Artificial Intelligence', 'Software Development and Professional Practice',
# #            # 'Automata and Language Theory', 'Advanced Computer Graphics', 'Field Training',
# #            'Compiler Construction', 'Introduction to Computer Security', 'Web Programming', 'Computer Vision',
# #            'Network Programming', 'Capstone Project I','Machine Learning', 'Cryptography', 'Parallel Computation',
# #            'Computer Animation', 'Advanced Database','Capstone Project II'
# #            ]
#
# # def print_info(request):
# #     try:
# #         idtoken = request.session['uid']
# #         url = request.POST.get('url')
# #         a = authe.get_account_info(idtoken)
# #         a = a['users']
# #         a = a[0]
# #         a = a['localId']
# #         print("info" + str(a))
# #         print(url)
# #
# #         list_sub = database.child('users').child(a).child('studied_courses').get().val()
# #         list_sub2 = database.child('users').child(a).child('studied_courses').child("sub1").get().val()
# #         values = list_sub.values()
# #         allcrs = courses_Check(values)
# #         dataJSON1 = dumps(allcrs)
# #         print("your values: ")
# #         for i in values:
# #             print(i)
# #
# #         print(list_sub2)
# #         so = {"sub52": 'Computer Animation', "sub53": 'Advanced Database', "sub54": 'Capstone Project II', }
# #         # print(database.child('aaas-a442a').child('subjects').get(idtoken).val())
# #
# #         name = database.child('users').child(a).child('details').child('name').get(idtoken).val()
# #         return render(request, 'index.html', {'e': name})
# #     except KeyError:
# #         message = "oops user logged out, please sign in again"
# #         return render(request, "index.html", {"msg": message, "data": dataJSON1})
#
# failed = []
# studied = []
# can_registered = []
#
# # Not Studied Courses
# for i in studied:
#     del prerequisite[i]
# not_studied = list(prerequisite.keys())
#
# # Courses that can be Registered
# for i in prerequisite:
#     if prerequisite[i] in studied or prerequisite[i] is None or prerequisite[i] in failed:
#         if i not in can_registered:
#             can_registered.append(i)
#     elif type(prerequisite[i]) == list:
#         subprerequisite = prerequisite[i]
#         flag = 1
#         for s in subprerequisite:
#             if s not in studied:
#                 flag = 0
#                 break
#
#         if flag:
#             if i not in can_registered:
#                 can_registered.append(i)
#
# # Priority Check
# fp_courses = []
# sp_courses = []
# thp_courses = []
# fop_courses = []
# for i in can_registered:
#     #    i + " : %s" % priorety.get(i)
#     if priorety.get(i) == 1:
#         fp_courses.append(i)
#     elif priorety.get(i) == 2:
#         sp_courses.append(i)
#     elif priorety.get(i) == 3:
#         thp_courses.append(i)
#     else:
#         fop_courses.append(i)
#
# allcources = [fp_courses, sp_courses, thp_courses, fop_courses]
#
# print(allcources)


# Priority Dictionary :
priorety = {"IT Fundamentals": 1, "Mathematics I": 2, "Physics I": 4, "Electronics": 3, "English Language I": 3,
            "Hand Drawing": 4,
            "History of Computing": 4, "Social Context of Computing": 4, "Programming Fundamentals": 1,
            "Mathematics II": 2,
            "Physics II": 4, "Digital Circuits": 4, " Interpersonal Communication": 4, "Human Rights": 4,
            "English Language II": 3,
            "Computer Law": 4, "Discrete Structures": 2, "Object-Oriented Programming": 1, "Project Management": 1,
            "Data Communications": 2,
            "Technical Writing": 4, "Foundations of Information Systems": 2, "Business Administration": 4,
            "Data Structures and Algorithms": 1,
            "Databases": 3, "Computer Architecture": 2, "Probability and Statistics": 4, "Computers and Ethics": 4,
            "Systems Analysis and Design": 4, "File Organization": 4, "Computer Networks": 2, "Image Processing": 3,
            "Software Engineering": 1, "Visual Programming": 3, "Computer Graphics": 3,
            "Algorithm Design and Analysis": 3,
            "Operating Systems": 3, "Automata and Language Theory": 4, "Advanced Computer Graphics": 4,
            "Artificial Intelligence": 3,
            "Software Development and Professional Practice": 1, "Field Training": 4, "Compiler Construction": 4,
            "Capstone Project I": 1,
            "Introduction to Computer Security": 4, "Web Programming": 4, "Computer Vision": 4,
            "Network Programming": 4, "Capstone Project II": 1,
            "Machine Learning": 4, "Cryptography": 4, "Parallel Computation": 4, "Computer Animation": 4,
            "Advanced Database": 4}

# Prerequisite Dictionary for every Course
prerequisite = {"IT Fundamentals": None, "Mathematics I": None, "Physics I": None, "Electronics": None,
                "English Language I": None, "Hand Drawing": None,
                "History of Computing": None, "Social Context of Computing": None,
                "Programming Fundamentals": "IT Fundamentals", "Mathematics II": "Mathematics I",
                "Physics II": None, "Digital Circuits": "Electronics", " Interpersonal Communication": None,
                "Human Rights": None, "English Language II": "English Language I",
                "Computer Law": None, "Discrete Structures": "Mathematics II",
                "Object-Oriented Programming": "Programming Fundamentals",
                "Project Management": "IT Fundamentals", "Data Communications": "IT Fundamentals",
                "Technical Writing": "English Language I", "Foundations of Information Systems": "IT Fundamentals",
                "Business Administration": None, "Data Structures and Algorithms": "Object-Oriented Programming",
                "Databases": "Foundations of Information Systems",
                "Computer Architecture": ["Programming Fundamentals", "Discrete Structures"],
                "Probability and Statistics": "Mathematics II", "Computers and Ethics": None,
                "Systems Analysis and Design": "IT Fundamentals", "File Organization": "Object-Oriented Programming",
                "Computer Networks": ["Computer Architecture", "Data Communications"],
                "Image Processing": "Data Structures and Algorithms",
                "Software Engineering": "Data Structures and Algorithms",
                "Visual Programming": "Data Structures and Algorithms",
                "Computer Graphics": ["Discrete Structures", "IT Fundamentals"],
                "Algorithm Design and Analysis": "Data Structures and Algorithms",
                "Operating Systems": "Computer Architecture",
                "Automata and Language Theory": ["Discrete Structures", "Programming Fundamentals"],
                "Advanced Computer Graphics": "Computer Graphics",
                "Artificial Intelligence": ["Discrete Structures", "IT Fundamentals"],
                "Software Development and Professional Practice": "Software Engineering",
                "Field Training": "Project Management",
                "Compiler Construction": ["Visual Programming", "Computer Architecture",
                                          "Data Structures and Algorithms"],
                "Capstone Project I": ["Project Management", "Software Development and Professional Practice"],
                "Introduction to Computer Security": ["Computer Networks", "Data Structures and Algorithms"],
                "Web Programming": ["Data Communications", "Programming Fundamentals"],
                "Computer Vision": ["Physics II", "Object-Oriented Programming"],
                "Network Programming": "Computer Networks",
                "Capstone Project II": ["Project Management", "Software Development and Professional Practice"],
                "Machine Learning": "Artificial Intelligence",
                "Cryptography": ["Computer Networks", "Data Structures and Algorithms"],
                "Parallel Computation": ["Operating Systems", "Algorithm Design and Analysis"],
                "Computer Animation": "Image Processing", "Advanced Database": None}


# studied = ['IT Fundamentals', 'Mathematics I', 'Electronics', 'English Language I', 'English Language II',
#            'Physics I', 'Hand Drawing', 'History of Computing', 'Social Context of Computing',
#            'Programming Fundamentals', 'Mathematics II', 'Physics II',
#            'Digital Circuits', ' Interpersonal Communication', 'Human Rights', 'Computer Law',
#            'Discrete Structures', 'Data Communications', 'Foundations of Information Systems',
#            'Object-Oriented Programming', 'Project Management', 'Technical Writing', 'Business Administration',
#             'Databases', 'Computer Architecture','Data Structures and Algorithms',
#            'Probability and Statistics', 'Computers and Ethics',
#            # 'Systems Analysis and Design', 'File Organization',
#            #  'Computer Networks','Image Processing', 'Visual Programming', 'Computer Graphics',
#            # 'Algorithm Design and Analysis', 'Software Engineering',
#            # 'Operating Systems', 'Artificial Intelligence', 'Software Development and Professional Practice',
#            # 'Automata and Language Theory', 'Advanced Computer Graphics', 'Field Training',
#            'Compiler Construction', 'Introduction to Computer Security', 'Web Programming', 'Computer Vision',
#            'Network Programming', 'Capstone Project I','Machine Learning', 'Cryptography', 'Parallel Computation',
#            'Computer Animation', 'Advanced Database','Capstone Project II'
#            ]

# def print_info(request):
#     try:
#         idtoken = request.session['uid']
#         url = request.POST.get('url')
#         a = authe.get_account_info(idtoken)
#         a = a['users']
#         a = a[0]
#         a = a['localId']
#         print("info" + str(a))
#         print(url)
#
#         list_sub = database.child('users').child(a).child('studied_courses').get().val()
#         list_sub2 = database.child('users').child(a).child('studied_courses').child("sub1").get().val()
#         values = list_sub.values()
#         allcrs = courses_Check(values)
#         dataJSON1 = dumps(allcrs)
#         print("your values: ")
#         for i in values:
#             print(i)
#
#         print(list_sub2)
#         so = {"sub52": 'Computer Animation', "sub53": 'Advanced Database', "sub54": 'Capstone Project II', }
#         # print(database.child('aaas-a442a').child('subjects').get(idtoken).val())
#
#         name = database.child('users').child(a).child('details').child('name').get(idtoken).val()
#         return render(request, 'index.html', {'e': name})
#     except KeyError:
#         message = "oops user logged out, please sign in again"
#         return render(request, "index.html", {"msg": message, "data": dataJSON1})
def courses_check(studied, failed):
    can_registered = []
    # Not Studied Courses
    for i in studied:
        del prerequisite[i]
    not_studied = list(prerequisite.keys())

    # Courses that can be Registered
    for i in prerequisite:
        if prerequisite[i] in studied or prerequisite[i] is None or prerequisite[i] in failed:
            if i not in can_registered:
                can_registered.append(i)
        elif type(prerequisite[i]) == list:
            subprerequisite = prerequisite[i]
            flag = 1
            for s in subprerequisite:
                if s not in studied:
                    flag = 0
                    break

            if flag:
                if i not in can_registered:
                    can_registered.append(i)

    # Priority Check
    fp_courses = []
    sp_courses = []
    thp_courses = []
    fop_courses = []
    for i in can_registered:
        #    i + " : %s" % priorety.get(i)
        if priorety.get(i) == 1:
            fp_courses.append(i)
        elif priorety.get(i) == 2:
            sp_courses.append(i)
        elif priorety.get(i) == 3:
            thp_courses.append(i)
        else:
            fop_courses.append(i)

    allcources = [fp_courses, sp_courses, thp_courses, fop_courses]
    return (allcources)

