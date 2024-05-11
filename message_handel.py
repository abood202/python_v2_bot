from info import *
from save_chat_and_member import save_Chat_info, check_me,check_save_member,sing_admins_to_private
from command import bot_option
#بتاع الروابط
from link import About_links
#بتاع التحويل
from forword_message import About_forward_message
#الكتب والازرار
from send_book import get_book,filter_txt

#?للملفات والروابط والرسائل 
#?هنا للمجموعة
def handel_message(message,data,data_private):
    #?########معلومات المجموعة او الشات###########
    # chat_type = message.chat.type #supergroup,private
    chat_id = message.chat.id
    chat_title = message.chat.title
    chat_username = message.chat.username    
    
    #?نوع الرسالة والنص بتاعها
    message_type = message.content_type
    message_text = message.text    
    message_id = message.id
    
    #?######اللي ارسل الرسالة########
    user_id = message.from_user.id
    full_name = message.from_user.full_name
    username = message.from_user.username

    chat_members_count = bot.get_chat_members_count(chat_id=chat_id)
    user = bot.get_chat_member(chat_id,user_id)
    # print(user)
    # group_list = list(data['Groups'].keys())
    chat_stat = bot.get_chat(chat_id)
    link_Chat = chat_stat.invite_link
    
    user_stat,data,data_private = save_Chat_info(data_private,data,message,user,chat_members_count,link_Chat)

    #?تسجيل لمجموعة
    data = check_save_member(data,message,user_id,full_name,username,chat_id)

    data = check_me(data,chat_id,chat_username,message)


    Admin_list = list(data['Groups'][f'{chat_id}']['Admins'])
    Moderators_list = list(data['Groups'][f'{chat_id}']['Moderators'])
    
    list_fowrword = list(data["Groups"][f"{chat_id}"]["forward_message"])
    
    reply_words = data["Groups"][f"{chat_id}"]["rep_words"][0]
    
    OK_Link =    data["Groups"][f"{chat_id}"]["OK_Link"]
    some_link =  data["Groups"][f"{chat_id}"]["Specific links"]

    OK_forword = data["Groups"][f"{chat_id}"]["forword message"]
    some_forword = data["Groups"][f"{chat_id}"]["Specific forword"]
    Send_book =  data["Groups"][f"{chat_id}"]["send book"]    
    warning =    data["Groups"][f"{chat_id}"]["warning"]

    awnar = data['Groups'][f'{chat_id}']['owner'] 
    safeCounter = data['Groups'][f"{chat_id}"]["chat_member"][0][f"{user_id}"]["safeCounter"]
    all_member = data['Groups'][f"{chat_id}"]["chat_member"][0]
    
    #?خيارات البوت
    option_bot_list = [
        "فتح الكل","قفل الكل","تفعيل الروابط",
        "تعطيل الروابط","فتح التحويل","منع التحويل",
        "فتح تحويل محدد","قفل تحويل محدد","تفعيل الكتب",
        "تعطيل الكتب","تفعيل التحذير","تعطيل التحذير",
        "فتح روابط معينة","قفل روابط معينة"
    ]
    
    if message_text in option_bot_list:        
        bot_option(message_text,data,chat_id,message,
               OK_Link,OK_forword,Send_book,
               some_link,warning
               ,user_id,Admin_list,
               all_member,some_forword)

    elif (message_text =="الادمن") and (user_id in Admin_list):
        call_admin = ""
        for i in Admin_list:
            admns = bot.get_chat_member(chat_id,i)
            name_admin = admns.user.full_name
            id_admin = admns.user.id
            usernam_admin = admns.user.username
            ub_user = f"[{name_admin}](tg://user?id={id_admin})"
            if usernam_admin == None:
                call_admin += f"الاسم : {name_admin}\nاسم المستخدم :{ub_user}\n---------------------------------\n"
            else:
                call_admin += f"الاسم : {name_admin}\nاسم المستخدم :{ub_user}\n---------------------------------\n"
        bot.reply_to(message=message,text=call_admin,parse_mode="markdown")    

    elif (message_text == "رفع ادمن") and (str(user_id) == awnar):
        if "reply_to_message" in message.json:
            id_reply_user = message.json["reply_to_message"]["from"]['id']
            if id_reply_user in Admin_list:
                bot.reply_to(message,"هذا المستخدم ادمن من قبل")
            else:
                Admin_list.append(id_reply_user)
                new_admin = {
                    "Admins":Admin_list
                }
                data["Groups"][f"{chat_id}"].update(new_admin)
                with open('backend/Chat_Data.json', 'w') as f:
                    json.dump(data, f)
                bot.reply_to(message,"تم رفع ادمن")
            data,data_private = sing_admins_to_private(data_private,data,id_reply_user,chat_id,chat_username,chat_title,chat_members_count)

    elif (message_text == "تنزيل ادمن") and (str(user_id) == awnar):
        if "reply_to_message" in message.json:
            id_reply_user = message.json["reply_to_message"]["from"]['id']
            if id_reply_user in Admin_list:
                Admin_list.remove(id_reply_user)
                new_admin = {
                    "Admins":Admin_list
                }
                data["Groups"][f"{chat_id}"].update(new_admin)
                with open('backend/Chat_Data.json', 'w') as f:
                    json.dump(data, f)
                bot.reply_to(message,"تم التنزيل")

            else:
                bot.reply_to(message,"هذا ليس ادمن")

            data,data_private = sing_admins_to_private(data_private,data,id_reply_user,chat_id,chat_username,chat_title,chat_members_count)

    elif (message_text) and ( "،" in message_text) and (user_id in Admin_list) and ("reply_to_message" in message.json):
        if "reply_to_message" in message.json:
            id_reply_user = message.json["reply_to_message"]["from"]['id']
            list_manage = [1814696703,5176738408]
            if str(id_reply_user) in all_member:
                member = all_member[f"{id_reply_user}"]
                member_id = id_reply_user
                member_safeCounter = all_member[f"{id_reply_user}"]["safeCounter"]
                member_num_messages = all_member[f"{id_reply_user}"]["Number of messages"]
                member_num_Document = all_member[f"{id_reply_user}"]["Number of Document"]
                member_username = all_member[f"{id_reply_user}"]["username"]
                member_name_user = all_member[f"{id_reply_user}"]["name_user"]
                message_info =f"""
أيدي العضو : `{member_id}`
الاسم : [{member_name_user}](tg://user?id={member_id})
اسم المستخدم :@{member_username}
عدد الرسائل النصية : {member_num_messages}
عدد الملفات : {member_num_Document}
عدد الانذارات : {member_safeCounter}
"""
                
                for i in list_manage:
                    bot.send_message(i,message_info,parse_mode="markdown")
                
                return data,data_private
            else:
                for i in list_manage:
                    bot.send_message(i,"يبدو ان هذا العضو لم يرسل رسالة من قبل او انه غير مسجل تحقق من ذلك",parse_mode="markdown")
            return data,data_private

        return data,data_private
    
    else:
        #?الجزء الخاص بالروابط
        found_message,data = About_links(message,chat_id,Admin_list,
                            user_id,Moderators_list,data,
                            user_stat,list_fowrword)
        #*اذا الرسالة موجودة بعد التحقق من الروابط
        if found_message:
            #?جزء تحويل الرسالة او الملفات
            found_message = About_forward_message(message,chat_id,user_id,
                            message_type,message_id,list_fowrword,awnar,
                            Moderators_list,Admin_list,OK_forword,
                            some_forword,warning,safeCounter,full_name,
                            data,link_Chat,chat_title)

            #?المفترض هنا يتحقق من الكتاب
            #? بعد اما يتأكد من الروابط والتحويل
            if found_message:
                #?هنا يرسل الكتب والردود                
                if message_text:                    
                    message_text = filter_txt(message_text)
                    words = message_text.split()
                    with open("backend/users_history.json", 'r') as f:
                        un_data = json.load(f)
                    unknow = un_data
                    reply_unavailable = unknow["un_know"]
                    reply_books = unknow["books"]
                    count_rep = 0
                    for i in reply_books:
                        books_name = list(i.keys())
                        books_id = list(i.values())
                        for x in books_name:
                            if x in message_text:
                                bot.copy_messages(chat_id,from_chat_id="-1001939329726",message_ids=books_id)
                                count_rep +=1
                                break
                    if count_rep != 0:
                        bot.reply_to(message,".")
                        return data,data_private
                            
                    for i in reply_unavailable:
                        i = filter_txt(i)
                        if i in message_text:
                            bot.reply_to(message,"غير متوفر")
                            return data,data_private

                    if (words[0] == "بحث") and (Send_book == "True"):# and (chat_members_count >= 200):                        
                        x = (" ").join(words[1:])
                        if x != "" :
                            # get_book(x,user_id,chat_id,message,full_name)
                            def filter_book(message, user_id):
                                thread = threading.Thread(target=get_book, args=(x,user_id,chat_id,message,full_name,Send_book))
                                thread.start()
                            filter_book(message, user_id)
                        return data,data_private

                    else:
                        for i in list(reply_words.keys()):
                            x = filter_txt(i)
                            if x in message_text:
                                ssr = filter_txt(reply_words[i])
                                bot.reply_to(message,ssr)
                                break

                        return data,data_private
            
            else:
                # print(found_message)
                # print("The message not Found")
                return data,data_private
            return data,data_private
    return data,data_private

btn_list = ["اضافة عضو للسجل😈","عرض سجل عضو محدد😈",
"اضافة بيانات لعضو مسجل","عرض اعضاء السجل📃",
"⛓اغلاق🔐","عرض الكتب","اضافة كتب","حذف كتب",
"الغير متوفر🕳","الكتب📕","اضافة","عرض","حذف","الغاء❌","تم✅",
"حذف كتب📚","حذف ملفات📄","حذف سطر من السجل","حذف عضو من السجل"
]

#?الكتب اللي هتتمسح اذا داس اوكية
semply_books = []
semply_id = []
#?الغير متوفر
semply_unknow = []

#?فتح مجال للكتب
is_file = False
is_book = False
#?فتح مجال للكتب
is_id = False

is_unknow = False


#?هذا للخاص مع البوت
#?هذا للسجل
def private_message(message):
    chat_id = message.chat.id
    
    #?نوع الرسالة والنص بتاعها
    message_text = message.text    
    
    #?######اللي ارسل الرسالة########
    user_id = message.from_user.id
    Keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    history_admin = [1814696703,5176738408]
    if user_id in history_admin :
        global is_book
        global is_id
        global is_file 
        global is_unknow

        if is_book:
            if message_text not in btn_list:
                message_text = filter_txt(message_text)
                if message_text not in semply_books :
                    semply_books.append(message_text)   
                    bot.reply_to(message,"ادخل الاسم التالي")
                else:
                    bot.reply_to(message,"لقد ادخلت هذا الاسم من قبل")

        elif is_id:
            if message_text not in btn_list:                
                if message_text.isdigit():
                    if message_text in semply_id:
                        bot.reply_to(message,"لقد ادخلت هذا الأيدي من قبل")
                    else:
                        if len(semply_books) > len(semply_id):                            
                            semply_id.append(message_text) 
                            bot.reply_to(message,"ادخل الأيدي التالي")
                        elif len(semply_books) < len(semply_id):
                            bot.reply_to(message,"يبدو ان عدد الكتب اقل من الايدي\nادخل بقية الايدي الناقص")
                        elif len(semply_books) == len(semply_id):
                            bot.reply_to(message,"اكتمل عدد الكتب ارسل تم الان")

        elif is_file:
            if message.document:
                with open("backend/book_name.json",'r',encoding='utf-8') as f:
                    data = json.load(f)                    
                books = data["book"]
                file_name = message.document.file_name
                if file_name in books:
                    bot.reply_to(message,"هذا الكتاب مسجل")
                    semply_books.append(file_name)
                else:
                    bot.reply_to(message,"هذا الكتاب ليس في قائمة الكتب")

        elif is_unknow:
            if message_text not in btn_list:
                message_text = filter_txt(message_text)
                if message_text not in semply_unknow:
                    with open("backend/users_history.json",'r',encoding='utf-8') as f:
                        data = json.load(f)
                    un_know = data["un_know"]
                    if message_text in un_know:
                        bot.reply_to(message,"هذا مجود من قبل")
                    else:
                        semply_unknow.append(message_text)
                        bot.reply_to(message,"ارسل المزيد اذا كنت تريد او اضغط تم للانتهاء")


        if message_text == "التسجيل":
            btn1 = types.KeyboardButton(text="🗄السجل🕵️‍♂️✍")
            btn2 = types.KeyboardButton(text="الكتب📕")
            btn3 = types.KeyboardButton(text="الغير متوفر🕳")
            btn4 = types.KeyboardButton(text="⛓اغلاق🔐")
            Keyboard.add(btn1)
            Keyboard.add(btn2)
            Keyboard.add(btn3)
            Keyboard.add(btn4)
            bot.send_message(chat_id,"تم الفتح",reply_markup=Keyboard)

        elif message_text == "🗄السجل🕵️‍♂️✍":
            btn1 = types.KeyboardButton(text="اضافة عضو للسجل😈")
            btn2 = types.KeyboardButton(text="اضافة بيانات لعضو مسجل")
            btn3 = types.KeyboardButton(text="عرض سجل عضو محدد😈")
            btn4 = types.KeyboardButton(text="عرض اعضاء السجل📃")
            btn5 = types.KeyboardButton(text="حذف سطر من السجل")
            btn6 = types.KeyboardButton(text="حذف عضو من السجل")
            btn7 = types.KeyboardButton(text="⛓اغلاق🔐")
            Keyboard.add(btn4,btn1)
            Keyboard.add(btn3,btn2)
            Keyboard.add(btn5,btn6)
            Keyboard.add(btn7)
            bot.send_message(chat_id,"تم فتح السجل",reply_markup=Keyboard)

        elif message_text == "اضافة عضو للسجل😈":
            bot.send_message(chat_id,text="ارسل أيدي لعضو😀")
            bot.register_next_step_handler(message, lambda m: add_newuser(m,chat_id))

        elif message_text == "عرض سجل عضو محدد😈":
            bot.send_message(chat_id,text="ارسل أيدي لعضو😎")
            bot.register_next_step_handler(message, lambda m: show_history_user(m,chat_id))

        elif message_text == "اضافة بيانات لعضو مسجل":
            bot.send_message(chat_id,"ارسل الان أيدي العضو🥱")
            bot.register_next_step_handler(message, lambda m: add__history_user(m,chat_id))
        
        elif message_text == "عرض اعضاء السجل📃":
            show_all_member(message)

        elif message_text == "حذف سطر من السجل":
            bot.reply_to(message,"ارسل ايدي العضو")
            bot.register_next_step_handler(message, lambda m: del_line(m,chat_id))

        elif message_text == "حذف عضو من السجل":
            bot.reply_to(message,"ارسل ايدي العضو")
            bot.register_next_step_handler(message, lambda m: del_member(m,chat_id))


        elif message_text == "الكتب📕":
            btn1 = types.KeyboardButton(text="عرض الكتب")
            btn2 = types.KeyboardButton(text="اضافة كتب")
            btn3 = types.KeyboardButton(text="حذف كتب")
            btn4 = types.KeyboardButton(text="⛓اغلاق🔐")
            Keyboard.add(btn1)
            Keyboard.add(btn2)
            Keyboard.add(btn3)
            Keyboard.add(btn4)
            bot.send_message(chat_id,"تم فتح الكتب",reply_markup=Keyboard)            

        elif message_text == "عرض الكتب":
            with open("backend/users_history.json",'r',encoding='utf-8') as f:
                data = json.load(f)
            books = data["books"]
            show_books =""
            for i in books:
                books_name = list(i.keys())
                books_id = list(i.values())
                bok_nam = ""
                bok_id = ""

                for i in books_name:
                    bok_nam += f"الاسم : {i}\n"
                    
                for i in books_id:
                    bok_id += f"{i}\n"
                    
                show_books += f"""
الكتب : 
{bok_nam}
الأيدي : 
{bok_id}
########################
"""
            if books !=[]:
                bot.reply_to(message,show_books)

        elif message_text == "اضافة كتب":
            is_book = True
            btn1 = types.KeyboardButton(text="تم✅")
            btn2 = types.KeyboardButton(text="الغاء❌")
            btn3 = types.KeyboardButton(text="⛓اغلاق🔐")
            Keyboard.add(btn1)
            Keyboard.add(btn2)
            Keyboard.add(btn3)            
            bot.reply_to(message,"ارسل اسم الكتاب",reply_markup=Keyboard)

        elif message_text == "حذف كتب":
            is_file = True
            btn1 = types.KeyboardButton(text="حذف كتب📚")
            btn2 = types.KeyboardButton(text="حذف ملفات📄")
            btn3 = types.KeyboardButton(text="⛓اغلاق🔐")
            Keyboard.add(btn1)
            Keyboard.add(btn2)
            Keyboard.add(btn3)            
            bot.reply_to(message,"اختر",reply_markup=Keyboard)

        elif message_text == "حذف كتب📚":
            bot.reply_to(message,"ارسل اسم الكتاب")
            bot.register_next_step_handler(message, lambda m: delbook(m,chat_id))
            
        elif message_text == "حذف ملفات📄":
            is_file = True
            btn1 = types.KeyboardButton(text="تم✅")
            btn2 = types.KeyboardButton(text="الغاء❌")
            btn3 = types.KeyboardButton(text="⛓اغلاق🔐")
            Keyboard.add(btn1)
            Keyboard.add(btn2)
            Keyboard.add(btn3)
            bot.reply_to(message,"ارسل الملفات الان",reply_markup=Keyboard)


        elif message_text == "تم✅":

            if is_book:
                is_book = False
                is_id = True
                bot.reply_to(message,"ارسل أيدي الكتاب")
            
            elif is_id:
                if len(semply_books) > len(semply_id):
                    bot.reply_to(message,"يبدو ان عدد الكتب اكبر من الايدي \nادخل الأيدي التالي")
                elif len(semply_books) < len(semply_id):
                    bot.reply_to(message,"يبدو ان عدد الكتب اقل من الايدي\nادخل بقية الايدي الناقصة")
                elif len(semply_books) == len(semply_id):
                    is_book = False
                    is_id = False
                    all_books = ""
                    if semply_books and semply_id != []:
                        for i,x in zip(semply_books,semply_id):
                            all_books += f"الاسم : {i}\n"
                            all_books += f"الايدي : {x}\n"
                        bot.reply_to(message,all_books)
                        new_list = {}
                        for i,x in zip(semply_books,semply_id):
                            new_={
                                i:x
                            }
                            new_list.update(new_)
                        add_books(new_list)

                    Keyboard_close = types.ReplyKeyboardRemove()
                    bot.send_message(chat_id,"تم اغلاق لوحة المفاتيح",reply_markup=Keyboard_close)
                    semply_books.clear()
                    semply_id.clear()
                    semply_unknow.clear()

            elif is_file:
                is_file = False
                all_file = ""
                for i in semply_books:
                    all_file += f"{i}\n"
                if semply_books != []:
                    bot.reply_to(message,f"يتم حذف هذه الملفات الان : \n{all_file}")
                    del_books(semply_books)
                    Keyboard_close = types.ReplyKeyboardRemove()
                    bot.send_message(chat_id,"تم اغلاق لوحة المفاتيح",reply_markup=Keyboard_close)

                    semply_books.clear()
                    semply_id.clear()
                    semply_unknow.clear()

            elif is_unknow:
                is_unknow = False
                if semply_unknow != []:
                    with open("backend/users_history.json",'r',encoding='utf-8') as f:
                        data = json.load(f)
                    un_know = data["un_know"]
                    for i in semply_unknow:
                        un_know.append(i)
                    new_data = {
                        "un_know":un_know
                    }
                    data.update(new_data)
                    with open("backend/users_history.json",'w',encoding='utf-8') as f:
                        json.dump(data, f)
                    Keyboard_close = types.ReplyKeyboardRemove()
                    bot.send_message(chat_id,"تم اغلاق لوحة المفاتيح",reply_markup=Keyboard_close)

                    semply_books.clear()
                    semply_id.clear()
                    semply_unknow.clear()


        elif message_text == "الغاء❌":
            is_book = False
            is_id = False
            is_file = False
            is_unknow = False
            semply_books.clear()
            semply_id.clear()
            semply_unknow.clear()
            Keyboard_close = types.ReplyKeyboardRemove()
            bot.send_message(chat_id,"تم اغلاق لوحة المفاتيح",reply_markup=Keyboard_close)


        elif message_text == "الغير متوفر🕳":
            btn1 = types.KeyboardButton(text="عرض")
            btn2 = types.KeyboardButton(text="اضافة")
            btn3 = types.KeyboardButton(text="حذف")
            btn4 = types.KeyboardButton(text="⛓اغلاق🔐")
            Keyboard.add(btn1)
            Keyboard.add(btn2)
            Keyboard.add(btn3)
            Keyboard.add(btn4)
            bot.send_message(chat_id,"تم فتح الغير متوفر",reply_markup=Keyboard)   

        elif message_text == "عرض":#?عرض الغير متوفر
            with open("backend/users_history.json",'r',encoding='utf-8') as f:
                data = json.load(f)
            unknow = data["un_know"]
            all_unknow=""
            for i in unknow:
                all_unknow +=f"{i}\n"
            if unknow != []:
                bot.reply_to(message,all_unknow)

        elif message_text == "اضافة":
            is_unknow = True
            btn1 = types.KeyboardButton(text="تم✅")
            btn2 = types.KeyboardButton(text="الغاء❌")
            btn3 = types.KeyboardButton(text="⛓اغلاق🔐")
            Keyboard.add(btn1)
            Keyboard.add(btn2)
            Keyboard.add(btn3)            
            bot.reply_to(message,"ارسل اسم الكتاب",reply_markup=Keyboard)
            
        elif message_text == "حذف":
            bot.reply_to(message,"ارسل ماتريد حذفة")
            bot.register_next_step_handler(message, lambda m: del_unknow(m,chat_id))


        elif message_text == "⛓اغلاق🔐":
            is_book = False
            is_id = False
            is_file = False
            is_unknow = False
            semply_books.clear()
            semply_id.clear()
            semply_unknow.clear()

            Keyboard_close = types.ReplyKeyboardRemove()
            bot.send_message(chat_id,"تم اغلاق لوحة المفاتيح",reply_markup=Keyboard_close)


#?عرض اعضاء السجل
def show_all_member(message):
    with open("backend/users_history.json",'r',encoding='utf-8') as f:
        data = json.load(f)
    users = data["users"]
    all_user = ""
    for i in users:
        id_user = i
        name_user = users[i]["name"]

        all_user +=f"""
أيدي العضو : `{id_user}`
اسم العضو : [{name_user}](tg://user?id={id_user})

"""
    
    if users != {}:
        bot.reply_to(message,all_user,parse_mode="markdown")

#? اضافة عضو للسجل
def add_newuser(message,chat_id):
    text_message = message.text 
    for i in btn_list:
        if i in text_message:
            bot.send_message(chat_id,"تم التحديث")
            return

    with open("backend/users_history.json",'r',encoding='utf-8') as f:
        data = json.load(f)
    list_users = data["users"]
    if text_message in list_users:
        bot.send_message(chat_id,"هذا العضو موجود من قبل😕")
    else:
        new_user = {
            f"{text_message}":{
                "name": "",
                "hestory": []
            }
            
        }
        list_users.update(new_user)
        with open("backend/users_history.json", 'w',encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        bot.send_message(chat_id,"ارسل الان اسم الشخص😃")
        bot.register_next_step_handler(message, lambda m: add_newuser_name(m,chat_id,text_message))

def add_newuser_name(message,chat_id,userid):
    text_message = message.text 
    for i in btn_list:
        if i in text_message:
            bot.send_message(chat_id,"تم التحديث")
            return
    
    with open("backend/users_history.json",'r',encoding='utf-8') as f:
        data = json.load(f)
    name_user = data["users"][userid]["name"]
    name_user = message.text
    new_data = {
        "name":name_user
    }
    data["users"][userid].update(new_data)
    with open("backend/users_history.json", 'w',encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    bot.send_message(chat_id,"تم اضافة هذا العضو الي السجل😏")

#?عرض سجل العضو
def show_history_user(message,chat_id):
    text_message = message.text 
    for i in btn_list:
        if i in text_message:
            bot.send_message(chat_id,"تم التحديث")
            return
    with open("backend/users_history.json",'r',encoding='utf-8') as f:
        data = json.load(f)
    list_users = data["users"]
    if text_message in list_users:
        data_user = list(list_users[text_message]["hestory"])
        if data_user == []:
            txt ="هذا العضو لم يتم تسجيل بيانات له😏😐"
            bot.send_message(chat_id,txt)
        else:
            item_list = ''
            for index, item in enumerate(data_user, start=1):
                item_list +=f"""
{index}- {item}
"""

            bot.send_message(chat_id,"👨‍💻\n\n"+item_list)
    else:
        bot.send_message(chat_id,"هذا العضو غير مجود في السجل😱")

#?اضافة سجل للعضو
def add__history_user(message,chat_id):
    text_message = message.text 
    for i in btn_list:
        if i in text_message:
            bot.send_message(chat_id,"تم التحديث")
            return
    
    with open("backend/users_history.json",'r',encoding='utf-8') as f:
        data = json.load(f)
    list_users = data["users"]
    if text_message in list_users:
        data_user = list(list_users[text_message]["hestory"])
        item_list = ""
        for index, item in enumerate(data_user, start=1):
            item_list +=f"""
{index}- {item}
"""

        bot.send_message(chat_id,f"{item_list}\n\n👨‍💻 هذه يياناته ادخل الان ماتريد اضافتة")
        bot.register_next_step_handler(message, lambda m: add__history_user2(m,chat_id,text_message))
    else:
        bot.send_message(chat_id,"هذا العضو غير مجود في السجل😱")

def add__history_user2(message,chat_id,userid):
    text_message = message.text 
    for i in btn_list:
        if i in text_message:
            bot.send_message(chat_id,"تم التحديث")
            return
        
    with open("backend/users_history.json",'r',encoding='utf-8') as f:
        data = json.load(f)
    list_users = data["users"]
    dataa = list(data["users"][userid]["hestory"])
    dataa.append(text_message)
    data["users"][userid]["hestory"] = dataa

    with open("backend/users_history.json", 'w',encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    bot.reply_to(message,f"تم الاضافة بنجاح 🥳")


#?حذف عضو من السجل
def del_member(message,chat_id):
    txt = message.text
    for i in btn_list:
        if i in txt:
            bot.send_message(chat_id,"تم التحديث")
            return

    with open("backend/users_history.json",'r',encoding='utf-8') as f:
        data = json.load(f)
    list_users = data["users"]
    if txt in list_users:
        data["users"].pop(txt)
        with open("backend/users_history.json", 'w') as f:
            json.dump(data, f, indent=4)
        bot.reply_to(message,"تم حذف العضو")

    else:
        bot.reply_to(message,"هذا العضو غير مسجل")
    
#?حذف سطر من السجل
def del_line(message,chat_id):
    text_message = message.text 
    for i in btn_list:
        if i in text_message:
            bot.send_message(chat_id,"تم التحديث")
            return
        
    with open("backend/users_history.json",'r',encoding='utf-8') as f:
        data = json.load(f)
    list_users = data["users"]
    if text_message in list_users:
        data_user = list(list_users[text_message]["hestory"])
        if data_user == []:
            txt ="هذا العضو لم يتم تسجيل بيانات له😏😐"
            bot.send_message(chat_id,txt)
        else:
            item_list = ''
            for index, item in enumerate(data_user, start=1):
                item_list +=f"""
{index}- {item}
"""

            bot.send_message(chat_id,"👨‍💻 هذه بياناتة ارسل رقم السطر : \n\n"+item_list)
            bot.register_next_step_handler(message, lambda m: del_line2(m,chat_id,text_message))

def del_line2(message,chat_id,userid):
    text_message = message.text 
    for i in btn_list:
        if i in text_message:
            bot.send_message(chat_id,"تم التحديث")
            return
    
    with open("backend/users_history.json",'r',encoding='utf-8') as f:
        data = json.load(f)
    list_users = data["users"]
    data_user = list(list_users[userid]["hestory"])
    if text_message.isdigit():
        num_line =int(text_message)-1
        del data_user[num_line]
        list_users[userid]["hestory"] = data_user

        with open("backend/users_history.json", 'w') as f:
            json.dump(data, f, indent=4)
        bot.reply_to(message,"تم الحذف")
    else:    
        bot.reply_to(message,"عليك ادخال رقم صحيح")



#?اضافة كتاب
def add_books(new_list):
    with open("backend/users_history.json",'r',encoding='utf-8') as f:
        data = json.load(f)
    books = list(data["books"])
    books.append(new_list)
    new_data = {
        "books":books
    }
    data.update(new_data)
    with open("backend/users_history.json",'w',encoding='utf-8') as f:
        json.dump(data, f)

#?حذف الكتب الملفات
def del_books(key_list):
    with open("backend/book_name.json",'r',encoding='utf-8') as f:
        data = json.load(f)
    books = data["book"]
    for i in key_list:
        books.pop(i)

    with open("backend/book_name.json", 'w') as f:
        json.dump(data, f, indent=4)

#?حذف الكتب التحويل
def delbook(message,chat_id):
    text_message = message.text 
    for i in btn_list:
        if i in text_message:
            bot.send_message(chat_id,"تم التحديث")
            return
    
    with open("backend/users_history.json",'r',encoding='utf-8') as f:
        data = json.load(f)
    books = list(data["books"])
    for i in  books:
        for x in i :
            if text_message == x:
                books.remove(i)
                new_data = {
                    "books":books
                }
                data.update(new_data)
                with open("backend/users_history.json",'w',encoding='utf-8') as f:
                    json.dump(data, f)
                bot.reply_to(message,f"تم حذف هذه المجموعة : \n{list(i.keys())}")
                return

#?حذف الغير توفر
def del_unknow(message,chat_id):
    txt = message.text
    for i in btn_list:
        if i in txt:
            bot.send_message(chat_id,"تم التحديث")
            return
    
    with open("backend/users_history.json",'r',encoding='utf-8') as f:
        data = json.load(f)
    un_know = list(data["un_know"])
    if txt in un_know:
        un_know.remove(txt)
        new = {
            "un_know":un_know
        }
        data.update(new)
        with open("backend/users_history.json",'w',encoding='utf-8') as f:
            json.dump(data, f)
        bot.reply_to(message,f"تم حذف {txt}")

    else:
        bot.reply_to(message,"هذا الكتاب غير مسجل من قبل")
    

