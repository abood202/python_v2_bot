from info import *
from save_chat_and_member import check_save_member,save_Chat_info
from save_chat_and_member import sing_admins_to_private
#*عندما ينضم عضو جديد
#*عندما يتم ترقية العضو الي مشرف 
#*عندما يصبح المشرف عضو
#*عندما يتم الغاء حظر العضو
#*عندما يغادر العضو المجموعة
#*عند طرد اي شخص
#?يتم تسجيلهم في الملف
def addmember(message):
    chat_id = message.chat.id
    user_chat = message.chat.username
    chat_title = message.chat.title
    chat_members_count = bot.get_chat_members_count(chat_id=chat_id)

    newResponse = message.new_chat_member
    full_name = newResponse.user.full_name
    user_id = newResponse.user.id
    username = newResponse.user.username
    
    bot_or_not = newResponse.user.is_bot
    old_state = message.old_chat_member.status
    new_state = message.new_chat_member.status
    
    user = bot.get_chat_member(chat_id,user_id)
    
    if old_state and new_state:
        if not bot_or_not:
            chat_stat = bot.get_chat(chat_id)
            link_Chat = chat_stat.invite_link
            with open("backend/Chat_Data.json", 'r') as f:
                data = json.load(f)
            with open("backend/Users_Data.json", 'r') as f:
                data_private = json.load(f)

            data,data_private = save_Chat_info(data_private,data,message,user,chat_members_count,link_Chat)
            data = check_save_member(data=data,message=message,user_id=user_id,first_name=full_name,username=username,chat_id=chat_id)
            
            kiys = list(data["Groups"][f"{chat_id}"])
            admins = list(data["Groups"][f"{chat_id}"]["Admins"])
            moderators = list(data["Groups"][f"{chat_id}"]["Moderators"])
            
            members =data["Groups"][f"{chat_id}"]["chat_member"][0]
            member = data["Groups"][f"{chat_id}"]["chat_member"][0][f"{user_id}"]
            
            safeCounter = member["safeCounter"]
            
            # gender_member = member["Gender"]
            # gender_list = ["Male","Female"]

            # #?عندما ينضم عضو جديد
            # if ((old_state != "administrator") and ( old_state != "member" )) and ((new_state == "member" )) or (new_state == "restricted"):
                
            #     if gender_member in gender_list:
            #         pass                
            #     else:
            #         bot.restrict_chat_member(chat_id,user_id)
                    
            #         markup = types.InlineKeyboardMarkup()
            #         btn1 = types.InlineKeyboardButton(text='ولد',callback_data='ولد')
            #         btn2 = types.InlineKeyboardButton(text='بنت',callback_data='بنت')
            #         btn3 = types.InlineKeyboardButton(text='حذف',callback_data='حذف')
            #         markup.add(btn1,btn2,btn3,row_width=2)

            #         m = f"[{full_name}](tg://user?id={user_id})"

            #         bot.send_message(chat_id,f"{m} ~ قم بالاختيار",parse_mode="markdown", reply_markup=markup)

            #     # bot.send_message(chat_id,f"اهلا بك <{full_name}> في مجموعتنا")

            #*تم
            #?عندما يتم ترقية العضو الي مشرف 
            if old_state != "administrator" and new_state == "administrator":
                if user_id in moderators:
                    pass
                else:
                    moderators.append(user_id)

                    new_data = {
                        "Moderators":moderators
                    }
                    # إضافة البيانات الجديدة إلى البيانات الحالية
                    data["Groups"][f"{chat_id}"].update(new_data)
                    # كتابة البيانات المحدثة إلى الملف
                    with open("backend/Chat_Data.json", 'w') as f:
                        json.dump(data, f)

                    sing_admins_to_private(user_id,chat_id,user_chat,chat_title,chat_members_count)
                    # bot.send_message(chat_id,f"اصبح <{full_name}> مشرف")

            #*تم
            #?عندما يصبح المشرف عضو
            elif (old_state == "administrator") and (new_state == "member"):
                if user_id in moderators:
                    moderators.remove(user_id)
                    new_data = {
                        "Moderators":moderators,
                    }
                    # إضافة البيانات الجديدة إلى البيانات الحالية
                    data["Groups"][f"{chat_id}"].update(new_data)

                    # كتابة البيانات المحدثة إلى الملف
                    with open("backend/Chat_Data.json", 'w') as f:
                        json.dump(data, f)
                    
                    sing_admins_to_private(user_id,chat_id,user_chat,chat_title,chat_members_count)
                    # bot.send_message(chat_id,f"تم تخفيض رتبة <{full_name}>")
            
            #*تم
            #?عندما يتم الغاء حظر العضو
            elif old_state ==  "kicked" and new_state ==  "left":
                if user_id in moderators:
                    moderators.remove(user_id)
                    new_data = {
                        "Moderators":moderators
                    }
                    # إضافة البيانات الجديدة إلى البيانات الحالية
                    data["Groups"][f"{chat_id}"].update(new_data)

                    # كتابة البيانات المحدثة إلى الملف
                    with open("backend/Chat_Data.json", 'w') as f:
                        json.dump(data, f)

                elif str(user_id) in list(members.keys()):
                    pass

                # bot.send_message(chat_id,f"تم الغاء حظر <{full_name}> من المجموعة")

            #*تم
            #?عندما يغادر العضو المجموعة
            elif new_state == "left" and old_state != "kicked":
                if user_id in moderators:
                    moderators.remove(user_id)
                    new_data = {
                        "Moderators":moderators
                    }
                    # إضافة البيانات الجديدة إلى البيانات الحالية
                    data["Groups"][f"{chat_id}"].update(new_data)
                    # كتابة البيانات المحدثة إلى الملف
                    with open("backend/Chat_Data.json", 'w') as f:
                        json.dump(data, f)
                
                # bot.send_message(chat_id,f"غادر <{full_name}> المجموعة")

            #?عند طرد اي شخص
            elif new_state == "kicked":
                #?عند طرد المشرف
                if user_id in moderators:
                    moderators.remove(user_id)
                    new_data = {
                        "Moderators":moderators
                    }
                    # إضافة البيانات الجديدة إلى البيانات الحالية
                    data["Groups"][f"{chat_id}"].update(new_data)

                    # كتابة البيانات المحدثة إلى الملف
                    with open("backend/Chat_Data.json", 'w') as f:
                        json.dump(data, f)
                    
                    sing_admins_to_private(user_id,chat_id,user_chat,chat_title,chat_members_count)

                
                #?عند طرد عضو
                else:

                    pass

                # bot.send_message(chat_id,f"طرد <{full_name}> من المجموعة")
            

