from json import *

from django.shortcuts import render
from django.urls import reverse
from pyrebase import pyrebase
from AAAS.courses import *
from AAAS.code import *
from django import forms

choices_list = []


def get_my_choices():
    # you place some logic here
    return choices_list


# -------------------^^ Confogrations for FireBase ^^------------------- #
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


# -------------------^^ landing page View ^^------------------- #
def get_absolute_url(self):
    return reverse("create")


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
    return render(request, "new_main.html", {"e": email, "n": name, "id": id,
                                             "mail": e_mail, "department": department, "phone": phone,
                                             "address": address})


# -------------------^^ Login page View { LogIn with Firebase Session } ^^------------------- #
def reglogin(request):
    # email = request.POST.get('email')
    # passw = request.POST.get("pass")
    #
    # try:
    #     user = authe.sign_in_with_email_and_password(email, passw)
    #
    # except:
    #     message = "invalid username or Pass+word or check your internet connection"
    #     return render(request, "newlogin.html", {"msg": message})
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
    return render(request, "Registrer_Login.html")  # {"e": email, "n": name}


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
    return render(request, "profile.html")


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
    #     return render(request, "regester.html", {"msg": message})
    return render(request, "login.html")


# -------------------^^ Main Student page View ^^------------------- #
def mainstu(request):
    return render(request, "new_main.html")


# -------------------^^ (Old) Courses Registration page View ^^------------------- #
def course_submit(request):
    try:  # Session Start
        idtoken = request.session['uid']
        url = request.POST.get('url')
        a = authe.get_account_info(idtoken)
        a = a['users']
        a = a[0]
        a = a['localId']
        # data = json.loads(developerJsonString{})
        # list_sub = database.child('users').child(a).child('registered_courses').(data, idtoken)
        return render(request, "about_stu.html")
    # -------------------^^ Getting Data From Site App To Database ^^------------------- #
    except:
        return print("Exception Happened")



# -------------------^^ Course Registration page View ^^------------------- #
def course_registration(request):
    try:  # Session Start
        idtoken = request.session['uid']
        url = request.POST.get('url')
        a = authe.get_account_info(idtoken)
        a = a['users']
        a = a[0]
        a = a['localId']
        # print("info" + str(a))  # Print User Info
        # print(url)  # Print Link Info
        # -------------------^^ Getting Data From Database ^^------------------- #
        list_sub = database.child('users').child(a).child('studied_courses').get().val()
        # data = json.loads(developerJsonString{})
        # list_sub = database.child('users').child(a).child('registered_courses').(data,idtoken)

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

    except:
        return print("Exception Happened")
    print("studied : ", keys)
    print("Failed : ", failed)
    allcourses = courses_check(keys, keys2)

    print("All Courses : ", allcourses)
    dataJSON1 = dumps(allcourses)
    print("Data JSON 1 : ", dataJSON1)
    dicsh = getCredithours()
    # dump data
    dataJSON = dumps(dicsh)
    print("Data JSON : ",dataJSON)
    return render(request, "courseRegister.html", {"data": dataJSON1, "Dict": dataJSON})


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
    # try:  # Session Start
    #     idtoken = request.session['uid']
    #     url = request.POST.get('url')
    #     a = authe.get_account_info(idtoken)
    #     a = a['users']
    #     a = a[0]
    #     a = a['localId']
    #     print("info" + str(a))  # Print User Info
    #     print(url)  # Print Link Info
    # -------------------^^ Getting Data From Database ^^------------------- #
    # list_sub = database.child('users').child(a).child('studied_courses').get().val()
    # values = list_sub.values()  # Assigning data List Of Studied Courses
    # failed = []  # Assigning data List Of Failed Courses
    # if values is None:  # Rendering Empty Data
    # values = []
    # -------------------^^ Checking For Available Courses With AAAS Algorithm ^^------------------- #
    courses_Description = getCoursesDescrition()  # Assign List Of Available Courses
    dataJSON1 = dumps(courses_Description)  # Parsing The List Of Subjects To Script Format ( JSON )
    # print(dataJSON1)
    # print("your values: ")
    # for i in values:
    #     print(i)
    # print(dataJSON1)
    # -------------------^^ Getting User Info From Database ^^------------------- #
    # name = database.child('users').child(a).child('details').child('name').get(idtoken).val()
    return render(request, "about_stu.html", {"Description": dataJSON1})


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
