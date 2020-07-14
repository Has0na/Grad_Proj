from json import *
from django.shortcuts import render
from django.urls import reverse
from pyrebase import pyrebase
from AAAS.code import *
from AAAS.courses import *
from requests.exceptions import *

# -------------------^^ Confegrations for FireBase ^^------------------- #
config = {
    'apiKey': "AIzaSyBdAGklSfW5-AQmGJTpVsJJSfnzHjuvb00",
    'authDomain': "aaas-a442a.firebaseapp.com",
    'databaseURL': "https://aaas-a442a.firebaseio.com",
    'projectId': "aaas-a442a",
    'storageBucket': "aaas-a442a.appspot.com",
    'messagingSenderId': "163237067783"

}
# -------------------^^ Assigning Confogration to Varibles for FireBase  ^^------------------- #
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()

# # -------------------^^ Registrer Views ^^------------------- #
# def get_absolute_url(self):
#     return reverse("create")
#
#

#
# def logout(request):
#     auth.logout(request)
#     # authe.current_user = None
#     return render(request, "login.html")


# def postsign(request):
#     email = request.POST.get('email')
#     passw = request.POST.get("pass")
#
#     try:
#         user = authe.sign_in_with_email_and_password(email, passw)
#
#     except:
#         message = "invalid credentials"
#         return render(request, "login.html", {"msg": message})
#     print(user['idToken'])
#     session_id = user['idToken']
#     request.session['uid'] = str(session_id)
#     return render(request, "index.html", {"e": email})

# -------------------^^ Login page View { LogIn with Firebase Session } ^^------------------- #
def reglogin(request):
    return render(request, "Registrer_Login.html")  # {"e": email, "n": name}


# -------------------^^ Login page View { LogIn with Firebase Session } ^^------------------- #
def regmain(request):
    # email = request.POST.get('email')
    # passw = request.POST.get("pass")
    # try:
    #     user = authe.sign_in_with_email_and_password(email, passw)
    # except:
    #     message = "invalid username or Pass+word or check your internet connection"
    #     return render(request, "addUser.html", {"msg": message})
    # print(user['idToken'])
    # session_id = user['idToken']
    # request.session['uid'] = str(session_id)
    # idtoken = request.session['uid']
    # url = request.POST.get('url')
    # a = authe.get_account_info(idtoken)
    # a = a['users']
    # a = a[0]
    # a = a['localId']
    # name = database.child('users').child(a).child('details').child('name').get(idtoken).val()
    return render(request, "index.html")  # {"e": email, "n": name}


# -------------------^^ landing page View ^^------------------- #
def registrer_role(request):
    return render(request, "regestrer_updates.html")


# -------------------^^ landing page View ^^------------------- #
def reg_main(request):
    return render(request, "regtst1.html")


# -------------------^^ Git Student Courses List View ^^------------------- #
def add_s(request):
    return render(request, "studied.html")


# -------------------^^ Git Student Courses List View ^^------------------- #
def reset_pass(request):
    authe.send_password_reset_email("email")
    email2 = request.POST.get('email')
    return render(request, "login.html")


# -------------------^^ Git Student Courses List View ^^------------------- #
def post_add(request):
    name = request.POST.get('uname')
    id = request.POST.get('userid')
    print(name)
    email = request.POST.get('uemail')
    print(email)
    passw = request.POST.get('upass')
    phone_number = request.POST.get('phone')
    address = request.POST.get('address')
    department = request.POST.get('depart')

    print(passw)
    # try:
    user = authe.create_user_with_email_and_password(email, passw)
    uid = user['localId']
    data = {"name": name, "user id": id, "Email": email, "status": "1", "password": passw, "phone number": phone_number,
            "address": address, 'department': department, }
    database.child("users").child(uid).child("details").set(data)
    return render(request, "index.html")


# -------------------^^ Git Student Courses List View ^^------------------- #
def fill_info(request):
    try:
        idtoken = request.session['uid']
        url = request.POST.get('url')
        a = authe.get_account_info(idtoken)
        a = a['users']
        a = a[0]
        a = a['localId']
        print("info" + str(a))
        print(url)
        data = {
            # first term
            'IT Fundamentals': "A", 'Mathematics I': "B", 'Physics I': "c", 'Electronics': "B",
            'English Language I': "B-", 'Hand Drawing': "c+", 'History of Computing': "B",
            # # second term
            "Social Context of Computing": "B-", 'Programming Fundamentals': "A-", 'Mathematics II': "B-",
            'Physics II': "B-", 'Digital Circuits': "B-", ' Interpersonal Communication': "B-",
            'Human Rights': "C", 'English Language II': "B", 'Computer Law': "B",
            # # second grade
            'Discrete Structures': "C", 'Object-Oriented Programming': "C",
            'Project Management': "C",
            # 'Data Communications': "C",
            'Technical Writing': "C", 'Foundations of Information Systems': "C",
            'Business Administration': "C",
            # 2s_term
            'Data Structures and Algorithms': "C",
            'Databases': "B", 'Computer Architecture': "B",
            'Probability and Statistics': "C", 'Computers and Ethics': "C",
            'Systems Analysis and Design': "C+", 'File Organization': "C-",

            # # # third grade
            # "30": 'Computer Networks', "31": 'Image Processing', "32": 'Visual Programming',
            # "33": 'Computer Graphics',
            # "34": 'Algorithm Design and Analysis', "35": 'Software Engineering',
            #
            #  'Operating Systems',  'Artificial Intelligence': "C",
            #  'Software Development and Professional Practice',
            #  'Automata and Language Theory', "40": 'Advanced Computer Graphics', "41": 'Field Training',
            # # # fourth grade
            #  'Compiler Construction': "C",  'Introduction to Computer Security': "C",  'Web Programming': "C",
            #  'Computer Vision': "C",  'Network Programming': "C",
            #  'Capstone Project I': "C",
            #  'Machine Learning': "C",  'Cryptography',: "C" 'Parallel Computation': "C",
            #  'Computer Animation': "C",  'Advanced Database': "C",  'Capstone Project II': "C",
        }

        database.child('users').child(a).child('studied_courses').set(data, idtoken)
        name = database.child('users').child(a).child('details').child('name').get(idtoken).val()
        return render(request, 'index.html', {'e': name})
    except KeyError:
        message = "oops user logged out, please sign in again"
        return render(request, "index.html", {"msg": message})


# -------------------^^ Git Student Courses List View ^^------------------- #
def fill_info2(request):
    try:
        idtoken = request.session['uid']
        url = request.POST.get('url')
        a = authe.get_account_info(idtoken)
        a = a['users']
        a = a[0]
        a = a['localId']
        print("info" + str(a))
        print(url)
        data = {'Data Communications': "F", }

        database.child('users').child(a).child('failed_courses').set(data, idtoken)
        name = database.child('users').child(a).child('details').child('name').get(idtoken).val()
        return render(request, 'index.html', {'e': name})
    except KeyError:
        message = "oops user logged out, please sign in again"
        return render(request, "index.html", {"msg": message})


# -------------------^^ Git Student Courses List View ^^------------------- #
# def get_id(request):
#     try:
#        # user_id = request.POST.get('fname')
#         user2=request.POST['fname']
#         print(user2)
#         # print(user_id)
#         # studied = database.child('users').child(user_id).child('studied_courses').get().val()
#         # print(studied)
#         # failed = database.child('users').child(user_id).child('failed_courses').get().val()
#         # registered = database.child('users').child(user_id).child('failed_courses').get().val()
#     except:
#         print("failed")
#
#     return render(request, "regestrer_updates.html")


# -------------------^^ Login page View ^^------------------- #
def signIn(request):
    return render(request, "newlogin.html")


# -------------------^^ LogOut page View ^^------------------- #
def logout(request):
    try:
        authe.current_user = None
    except KeyError:
        pass
    return render(request, "newlogin.html")


# -------------------^^ Get User Details Function ^^------------------- #
def getUser(request):
    user = database.Post.get(id)
    all_users = database.child("users").shallow().get()
    print(all_users.val())

    session_id = user['idToken']
    request.session['uid'] = str(session_id)


# -------------------^^ Login page View { LogIn with Firebase Session } ^^------------------- #
def postsign(request):
    email = request.POST.get('email')
    passw = request.POST.get("pass")
    try:
        user = authe.sign_in_with_email_and_password(email, passw)
    except:
        message = "invalid username or Pass+word or check your internet connection"
        return render(request, "newlogin.html", {"msg": message})
    print(user['idToken'])
    session_id = user['idToken']
    request.session['uid'] = str(session_id)
    idtoken = request.session['uid']
    url = request.POST.get('url')
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    name = database.child('users').child(a).child('details').child('name').get(idtoken).val()
    id = database.child('users').child(a).child('details').child('user id').get(idtoken).val()
    e_mail = database.child('users').child(a).child('details').child('Email').get(idtoken).val()
    department = database.child('users').child(a).child('details').child('department').get(idtoken).val()
    phone = database.child('users').child(a).child('details').child('phone number').get(idtoken).val()
    address = database.child('users').child(a).child('details').child('address').get(idtoken).val()
    return render(request, "new_main.html", {"n": name, "id": id, "mail": e_mail, "department": department,
                                             "phone": phone, "address": address})


# -------------------^^ Users Registration page View ^^------------------- #
def register_Details(request):
    return render(request, "registeration_info.html")


# -------------------^^ Users Registration page View ^^------------------- #
def report(request):
    return render(request, "report.html")


# -------------------^^ Users Registration page View ^^------------------- #
def contact_us(request):
    return render(request, "contact_us.html")


# -------------------^^ Users Registration page View ^^------------------- #
def profile(request):
    name, id2, e_mail, department, phone, address = load_Session(request)
    return render(request, "profile.html", {"n": name, "id": id2,
                                            "mail": e_mail, "department": department, "phone": phone,
                                            "address": address})


# -------------------^^ Users Registration page View ^^------------------- #
def student_report(request):
    name, id2, e_mail, department, phone, address = load_Session(request)
    return render(request, "stReport.html", {"n": name, "id": id2,
                                             "mail": e_mail, "department": department, "phone": phone,
                                             "address": address})


# -------------------^^ Users Registeration page View ^^------------------- #
def postsignup(request):
    # name = request.POST.get('uname')
    # print(name)
    # email = request.POST.get('uemail')
    # print(email)
    # passw = request.POST.get('upass')
    # print(passw)
    # # try:
    # user = authe.create_user_with_email_and_password(email, passw)
    # uid = user['localId']
    # data = {"name": name, "status": "1"}
    # database.child("users").child(uid).child("details").set(data)

    # except:
    #     message = "Unable to create account try again"
    #     return render(request, "addUser.html", {"msg": message})
    return render(request, "login.html")


# ------------------------^^ Load Session Function ^^--------------- #


# ------------------------^^ Load Session Function ^^--------------- #
def load_Session(request):
    idtoken = request.session['uid']
    url = request.POST.get('url')
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    name = database.child('users').child(a).child('details').child('name').get(idtoken).val()
    id2 = database.child('users').child(a).child('details').child('user id').get(idtoken).val()
    e_mail = database.child('users').child(a).child('details').child('Email').get(idtoken).val()
    department = database.child('users').child(a).child('details').child('department').get(idtoken).val()
    phone = database.child('users').child(a).child('details').child('phone number').get(idtoken).val()
    address = database.child('users').child(a).child('details').child('address').get(idtoken).val()
    return name, id2, e_mail, department, phone, address


# -------------------^^ Main Student page View ^^------------------- #
def mainstu(request):
    name, id2, e_mail, department, phone, address = load_Session(request)
    return render(request, "new_main.html", {"n": name, "id": id2,
                                             "mail": e_mail, "department": department, "phone": phone,
                                             "address": address})


# -------------------^^ (Old) Courses Registration page View ^^------------------- #
def course_submit(request):
    try:  # Session Start
        idtoken = request.session['uid']
        url = request.POST.get('url')
        a = authe.get_account_info(idtoken)
        a = a['users']
        a = a[0]
        a = a['localId']
        # -------------------^^ Getting Data From Database ^^------------------- #
        list_sub = database.child('users').child(a).child('studied_courses').get().val()
        failed = database.child('users').child(a).child('failed_courses').get().val()
        print(list_sub.keys())
        print(failed)
        if list_sub is not None:
            keys = list(list_sub.keys())
        else:
            keys = []
        if failed is not None:
            keys2 = list(failed.keys())
        else:
            keys2 = []
        # data = json.loads(developerJsonString{})
        # list_sub = database.child('users').child(a).child('registered_courses').(data, idtoken)
        # print(list_sub)
        allcourses = courses_check(keys, keys2)
        semsGPA = dumps(1.9)
        print(semsGPA)
        dataJSON1 = dumps(allcourses)
        # Get Dictionary data
        dicsh = getCredithours()
        # dumps Dictionary data
        dataJSON = dumps(dicsh)
        name, id2, e_mail, department, phone, address = load_Session(request)
        return render(request, "about_stu.html",
                      {"data": dataJSON1, "Dict": dataJSON, "ps": semsGPA, "n": name, "id": id2,
                       "mail": e_mail, "department": department, "phone": phone,
                       "address": address})
    except:
        return print("Exception Happened")

    # -------------------^^ Getting Data From Site App To Database ^^------------------- #


# -------------------^^ Course Registration page View ^^------------------- #
def course_registration(request):
    try:  # Session Start
        idtoken = request.session['uid']
        url = request.POST.get('url')
        a = authe.get_account_info(idtoken)
        a = a['users']
        a = a[0]
        a = a['localId']
        usrid = a
        # print(usrid)
        # -------------------^^ Getting Data From Database ^^------------------- #
        list_sub = database.child('users').child(a).child('studied_courses').get().val()
        failed = database.child('users').child(a).child('failed_courses').get().val()
        # print(list_sub.keys())
        # print(failed)
        if list_sub is not None:
            keys = list(list_sub.keys())
        else:
            keys = []
        if failed is not None:
            keys2 = list(failed.keys())
        else:
            keys2 = []
    except:
        return print("Exception Happened")
    allcourses = courses_check(keys, keys2)
    semsGPA = dumps(1.9)
    # print(semsGPA)
    dataJSON1 = dumps(allcourses)
    # Get Dictionary data
    dicsh = getCredithours()
    # dumps Dictionary data
    dataJSON = dumps(dicsh)
    name, id2, e_mail, department, phone, address = load_Session(request)
    return render(request, "courseRegister.html",
                  {"data": dataJSON1, "Dict": dataJSON, "ps": semsGPA, "n": name, "id": id2,
                   "mail": e_mail, "department": department, "phone": phone,
                   "address": address, "userid": usrid})


# def course_Description(request):
#     # try:  # Session Start
#     #     idtoken = request.session['uid']
#     #     url = request.POST.get('url')
#     #     a = authe.get_account_info(idtoken)
#     #     a = a['users']
#     #     a = a[0]
#     #     a = a['localId']
#     #     print("info" + str(a))  # Print User Info
#     #     print(url)  # Print Link Info
#     # -------------------^^ Getting Data From Database ^^------------------- #
#     # list_sub = database.child('users').child(a).child('studied_courses').get().val()
#     # values = list_sub.values()  # Assigning data List Of Studied Courses
#     failed = []  # Assigning data List Of Failed Courses
#     # if values is None:  # Rendering Empty Data
#     values = []
#     # -------------------^^ Checking For Available Courses With AAAS Algorithm ^^------------------- #
#     coursesDescription = getCoursesDescrition()  # Assign List Of Available Courses
#     dataJSON1 = dumps(coursesDescription)  # Parsing The List Of Subjects To Script Format ( JSON )
#     print(dataJSON1)
#     print("your values: ")
#     for i in values:
#         print(i)
#
#     print(coursesDescription)
#     # -------------------^^ Getting User Info From Database ^^------------------- #
#     # name = database.child('users').child(a).child('details').child('name').get(idtoken).val()
#     return render(request, "about_stu.html", {"Description": dataJSON1})


# except KeyError:  # Exception for Finished Students & Bugs
#     name = database.child('users').child(a).child('details').child('name').get(idtoken).val()
#     message = "There are no available courses, You will be forwarded to home page"
#     return render(request, 'new_main.html', {"msg": message, 'n': name})


# -------------------^^ Contact US page View ^^------------------- #
def aboutst(request):
    try:  # Session Start
        name, id2, e_mail, department, phone, address = load_Session(request)
        # -------------------^^ Checking For Available Courses With AAAS Algorithm ^^------------------- #
        courses_Description = getCoursesDescrition()  # Assign List Of Available Courses
        dataJSON1 = dumps(courses_Description)
    except:
        print("hhhhh")
    # Parsing The List Of Subjects To Script Format ( JSON )
    # print(dataJSON1)
    return render(request, "about_stu.html", {"n": name, "id": id2,
                                              "mail": e_mail, "department": department, "phone": phone,
                                              "address": address, "Description": dataJSON1})


# -------------------^^ Contact US page View ^^------------------- #
def aboutus(request):
    return render(request, "aboutus.html")


# -------------------^^ Contact US page View ^^------------------- #
# def registrer_Updates(request):

# return render(request, "regestrer_updates.html", {'choice': MY_CHOICES})


# -------------------^^ Code Testin page View for features ^^------------------- #
def code_test(request):
    # create data dictionary
    dataDictionary = {
        'hello': 'World',
        'geeks': 'forgeeks',
        'ABC': 123,
        456: 'abc',
        14000605: 1,
        'list': ['geeks', 4, 'geeks'],
        'dictionary': {'you': 'can', 'send': 'anything', 3: 1}
    }
    dicsh = getCredithours()
    # dump data
    dataJSON = dumps(dicsh)
    return render(request, 'anyGrade.html', {'data': dataJSON})
