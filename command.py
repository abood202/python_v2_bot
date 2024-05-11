from info import *
from btn import btn_my_groups,btn_private_chat

#!تفعيل الخواص او امكانيات البوت داخل المجموعة او في الخاص؟؟
#التعامل مع اوامر البوت

#?الاوامر
def bot_option(message_text,data,chat_id,message,
               OK_Link,OK_forword,Send_book,
               some_link,warning
               ,user_id,Admin_list,
               all_member,some_forword):
    """
    اوامر البوت داخل الجروب او الخاص
    """    
    #?اذا ادمن للبوت يقدر يفعل الحجات دي
    if user_id in Admin_list:
        if message_text == "فتح الكل":
            stete_option = {
                "OK_Link": "True",
                "forword message": "True",
                "send book": "True",
                "Specific links":"True",
                "Specific forword":"True"
            }

            bot.reply_to(message,"تم تفعيل الكل")
            
        elif message_text == "قفل الكل":
            stete_option = {
                "OK_Link": "False",
                "forword message": "False",
                "send book": "False",
                "Specific links":"False",
                "Specific forword":"False",
                "warning":"False"
            }
            bot.reply_to(message,"تم تعطيل الكل")

        elif message_text == "تفعيل الروابط":
            if OK_Link == "False":
                stete_option = {
                    "OK_Link":"True"
                }
                
                bot.reply_to(message,text="تم التفعيل")
            else:
                bot.reply_to(message,text="مفعلة من قبل")
                return
            
        elif message_text == "تعطيل الروابط":
            if OK_Link == "True":
                stete_option = {
                    "OK_Link":"False",
                    "Specific links":"False"
                }
                
                bot.reply_to(message,text="تم التعطيل")
            else:
                bot.reply_to(message,text="معطلة بالفعل")
                return
            
        elif message_text == "فتح روابط معينة":
            if some_link == "False":
                stete_option = {
                    "Specific links":"True",
                    "OK_Link":"True"
                }
                
                bot.reply_to(message,text="تم التفعيل")
            else:
                bot.reply_to(message,text="مفعلة من قبل")
                return
            
        elif message_text == "قفل روابط معينة":
            if some_link == "True":
                stete_option = {
                    "Specific links":"False"
                }
                
                bot.reply_to(message,text="تم التعطيل")
            else:
                bot.reply_to(message,text="معطلة بالفعل") 
                return
            
            
        elif message_text == "فتح التحويل":
            if OK_forword == "False":
                stete_option = {
                    "forword message":"True"
                }

                bot.reply_to(message,text="تم التفعيل")
            else:
                bot.reply_to(message,text="مفعلة من قبل")
                return

        elif message_text == "منع التحويل":
            if OK_forword == "True":
                stete_option = {
                    "forword message":"False",
                    "Specific forword":"False"
                }

                bot.reply_to(message,text="تم التعطيل")
            else:
                bot.reply_to(message,text="معطلة بالفعل")  
                return

        elif message_text == "فتح تحويل محدد":
            if some_forword == "False":
                stete_option = {
                    "forword message":"True",
                    "Specific forword":"True"
                }

                bot.reply_to(message,text="تم التفعيل")
            else:
                bot.reply_to(message,text="مفعلة من قبل")
                return
            
        elif message_text == "قفل تحويل محدد":
            if some_forword == "True":
                stete_option = {
                    "Specific forword":"False"
                }

                bot.reply_to(message,text="تم التعطيل")
            else:
                bot.reply_to(message,text="معطلة بالفعل")  
                return

        elif message_text == "تفعيل الكتب":
            if Send_book == "False":
                stete_option = {
                    "send book":"True"
                }

                bot.reply_to(message,text="تم التفعيل")
            else:
                bot.reply_to(message,text="مفعلة من قبل")
                return
            
        elif message_text == "تعطيل الكتب":
            if Send_book == "True":
                stete_option = {
                    "send book":"False"
                }
                
                bot.reply_to(message,text="تم التعطيل")
            else:
                bot.reply_to(message,text="معطلة بالفعل") 
                return
            
        elif message_text == "تفعيل التحذير":
            if warning == "False":
                stete_option = {
                    "warning":"True"
                }
                
                bot.reply_to(message,text="تم التفعيل")
            else:
                bot.reply_to(message,text="مفعلة من قبل")
                return
            
        elif message_text == "تعطيل التحذير":
            if warning == "True":
                stete_option = {
                    "warning":"False"
                }
                bot.reply_to(message,text="تم التعطيل")
            else:
                bot.reply_to(message,text="معطلة بالفعل") 
                return
            


        data["Groups"][f"{chat_id}"].update(stete_option)
        with open('backend/Chat_Data.json', 'w') as f:
            json.dump(data, f)


def bot_command(message):
    """
    في الخاص فقط
    """
    chat_id = message.chat.id
    chat_title = message.chat.title
    chat_username = message.chat.username 

    #?######اللي ارسل الرسالة########
    user_id = message.from_user.id
    full_name = message.from_user.full_name
    username = message.from_user.username

    keybord= btn_private_chat()

    if message.text == "/start":
        bot.reply_to(message,f"""
مرحبا بك {full_name} 
معك بايثون الاصدار الثاني😎
لمزيد من المساعدة /help
ولا تنسي الاشتراك في القنوات والمجموعات الخاصة بنا 😏
""",reply_markup=keybord)

    elif message.text == "/help":
        message_id = message.id
        #?حذف الرسائل القديمة 
        # list_ids = list(range(message_id-50, message_id))
        # bot.delete_messages(chat_id,list_ids)

        #? قراءة البيانات الحالية من الملف
        with open("backend/Users_Data.json", 'r') as f:
            data_Admins = json.load(f)
        with open("backend/Chat_Data.json", 'r') as f:
            data_groups = json.load(f)

        Admins = data_Admins["Admins"]
        Groups = data_groups["Groups"]
        new_data = {
            "Groups":{},
            "now_group":"0"
        }
        if str(user_id) in Admins:
            groups = Admins[f"{user_id}"]["groups"]
            for i in Groups:
                if i in groups:
                    admns = Groups[i]["Admins"]
                    if user_id in admns:
                        dat = {
                            i:groups[i]
                        }
                        new_data["Groups"].update(dat)

            if list(groups.keys()) != []:
                with open(f"Admins_bot/{user_id}.json", "w",encoding="utf-8") as f:
                    json.dump(new_data, f, ensure_ascii=False, indent=4)
                btn_my_groups(message,user_id)
            else:
                bot.reply_to(message,"اضفني الي مجموعتك اولا",reply_markup=keybord)
        else:            
            bot.reply_to(message,"اضفني الي مجموعتك اولا",reply_markup=keybord)

