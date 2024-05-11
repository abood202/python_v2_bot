from info import *

#!التحقق مما اذا كان مشترك ام لا


#*تسجيل الاعضاء كل رسالة يبعتوها
#*اذا كان العضو مالك الجروب 
#*اذا كان العضو مشرف
#*اذا كان عضو 
#*اذا كان مخفي
#*التحقق من البوت لتسجيلو في الادمن او المشرفين

#?بيسجل الادمن بالجروب عشان يتعامل في الخاص
def sing_admins_to_private(data_private,data_groups,user_id,chat_id,user_chat,chat_title,chat_members_count):
    """
    بيسجل الادمن بالجروب عشان يتعامل في الخاص
    """

    Admins = data_private["Admins"]

        
    awner = data_groups["Groups"][f"{chat_id}"]["owner"]
    admn = data_groups["Groups"][f"{chat_id}"]["Admins"]
    # moder = data_groups["Groups"][f"{chat_id}"]["Moderators"]

    list_admins = admn #+ moder
    
    if user_id in list_admins:
        if f"{user_id}" in list(Admins.keys()):
            id_groups = Admins[f"{user_id}"]["groups"]
            if f"{chat_id}" in list(id_groups.keys()):
                username_chat = id_groups[f"{chat_id}"]["username"]
                title_chat = id_groups[f"{chat_id}"]["title"]
                countmember = id_groups[f"{chat_id}"]["countmember"]
                id_chat = id_groups[f"{chat_id}"]["id"]
                
                if ((username_chat == user_chat) and (id_chat == chat_id) and (title_chat == chat_title) and(countmember == chat_members_count)):
                    pass

                else:
                    new_group_data={
                    f"{chat_id}":{
                        "title":f"{chat_title}",
                        "username":f"{user_chat}",
                        "countmember":chat_members_count,
                        "id":f"{chat_id}"
                        }
                    }
                    data_private["Admins"][f"{user_id}"]["groups"].update(new_group_data)
                    with open('backend/Users_Data.json', 'w') as f:
                        json.dump(data_private, f)

            else:                    
                new_group_data={
                    f"{chat_id}":{
                        "title":f"{chat_title}",
                        "username":f"{user_chat}",
                        "countmember":chat_members_count,
                        "id":f"{chat_id}"
                    }
                }
                data_private["Admins"][f"{user_id}"]["groups"].update(new_group_data)
                with open('backend/Users_Data.json', 'w') as f:
                    json.dump(data_private, f)    
                    
        else:
            new_group_data={
                f"{user_id}":{
                    "groups":{
                        f"{chat_id}":{
                            "title":f"{chat_title}",
                            "username":f"{user_chat}",
                            "countmember":chat_members_count,
                            "id":f"{chat_id}"
                        }
                    }
                }
            }
            data_private["Admins"].update(new_group_data)
            with open('backend/Users_Data.json', 'w') as f:
                json.dump(data_private, f)
        
    else:
        if f"{user_id}" in list(Admins.keys()):
            groups = list(Admins[f"{user_id}"]["groups"].keys())
            # print("Groups : ",groups)
            if str(chat_id)in groups:
                # ازالة العنصر المطلوب
                # del Admins[f"{user_id}"]["groups"][f"{chat_id}"]
                del data_private["Admins"][f"{user_id}"]["groups"][f"{chat_id}"]
                # إعادة كتابة الملف بعد الحذف
                with open("backend/Users_Data.json", 'w') as file:
                    json.dump(data_private, file)#, indent=4)
                # print("Sucess Delete")
        else:
            pass
            # print("else  ",list(Admins.keys()))


    return data_groups,data_private

#?تسجيل الجروب اذا مش متسجل
#?تسجيل الادمن والاعضاء والمالك بالمرة
def save_Chat_info(data_private,data,message,user,chat_members_count,link_Chat):
    chat_id = message.chat.id
    user_chat = message.chat.username 
    chat_title = message.chat.title

    full_name = message.from_user.full_name
    user_id = message.from_user.id
    username = message.from_user.username
    state_user = user.status 

    groups = list(data['Groups'].keys())

    Static_data = {
        f"{chat_id}":{
            "owner":"None",
            "countmember":chat_members_count,
            "Admins":[],
            "Moderators":[1087968824,777000],
            "Banned":[],
            "linkes":[],
            "forward_message":[],
            "unavailable": [],
            "rep_words": [{}],
            "chat_member":[{}],
            "OK_Link":"True",
            "forword message":"True",
            "send book":"True",
            "Specific links": "False",
            "Specific forword": "False",            
            "warning":"False",
            }         
        }

    #?اذا الجروب مش مسجل    
    if str(chat_id) not in groups :

        messagee_new_chat =f"""
تم تشغيل البوت في مجموعة جديدة :
الاسم : [{chat_title}]({link_Chat})
أيدي المجموعة: {chat_id}
اسم المستخدم للمجموعة: @{user_chat}
رابط المجموعة : [انقر هنا للانتقال]({link_Chat})
عدد الاعضاء: {chat_members_count}
--------------------------------------------------
من قام بارسال الرسالة قبل التشغيل :
الاسم : [{full_name}](tg://user?id={user_id})
الايدي: {user_id}
اسم المستخدم : @{username}
حالة العضو: {state_user}
--------------------------------------------------
"""

        Admins = [1814696703,5176738408]
        for i in Admins:
            bot.send_message(i,messagee_new_chat,parse_mode="markdown")

        data["Groups"].update(Static_data)

        if state_user == "creator":
            user_stat = "مالك المجموعة"
            owner = user_id          
            admins = data['Groups'][f'{chat_id}']['Admins']
            admins.append(owner)
            #? إضافة البيانات الجديدة إلى البيانات الحالية
            new_data = {
                    "owner":owner,
                    "countmember":chat_members_count,
                    "Admins":admins,
                }            
            # إضافة البيانات الجديدة إلى البيانات الحالية
            data["Groups"][f"{chat_id}"].update(new_data)
            # كتابة البيانات المحدثة إلى الملف
            with open('backend/Chat_Data.json', 'w') as f:
                json.dump(data, f)

            data,data_private = sing_admins_to_private(data_private,data,user_id,chat_id,user_chat,chat_title,chat_members_count)

        elif state_user == "administrator":
            user_stat = "ادمن في المجموعة"
            Moderators = data['Groups'][f'{chat_id}']['Moderators']
            if user_id in Moderators:
                pass
            else:
                Moderators.append(user_id)
                new_data = {
                    "countmember":chat_members_count,
                    "Moderators":Moderators,                     
                }
                # إضافة البيانات الجديدة إلى البيانات الحالية
                data["Groups"][f"{chat_id}"].update(new_data)
                # كتابة البيانات المحدثة إلى الملف
                with open('backend/Chat_Data.json', 'w') as f:
                    json.dump(data, f)
                
                data,data_private = sing_admins_to_private(data_private,data,user_id,chat_id,user_chat,chat_title,chat_members_count)

        elif (state_user == "member") or (state_user == "restricted"):
            user_stat = "عضو في المجموعة"
            with open('backend/Chat_Data.json', 'w') as f:
                json.dump(data, f)

            data,data_private = sing_admins_to_private(data_private,data,user_id,chat_id,user_chat,chat_title,chat_members_count)
        
        else:
            user_stat = "ربما يكون العضو مخفي" 
            with open('backend/Chat_Data.json', 'w') as f:
                json.dump(data, f)

            data,data_private = sing_admins_to_private(data_private,data,user_id,chat_id,user_chat,chat_title,chat_members_count)
        
        return user_stat,data
    #?اذا الجروب مسجل
    else:
        Admin_list = list(data['Groups'][f'{chat_id}']['Admins'])
        Moderators_list = list(data['Groups'][f'{chat_id}']['Moderators'])

        #!اعمل قائمة عشان الادمن بتوع المجموعة والمالك يعرفو يتحكمو في البوت في الخاص
        if state_user == "creator":
            user_stat = "مالك المجموعة"
            awner =  data['Groups'][f'{chat_id}']['owner']

            if str(user_id) == awner:
                if user_id in Admin_list:                    
                    pass
                else:
                    Admin_list.append(user_id)
                    new_data = {
                        "Admins":Admin_list
                    }
                    data['Groups'][f'{chat_id}'].update(new_data)
                    with open('backend/Chat_Data.json', 'w') as f:
                        json.dump(data, f)
            
            else:
                if user_id in Admin_list:
                    new_data = {
                        "owner":str(user_id),
                    }
                else:                    
                    Admin_list.append(user_id)
                    new_data = {
                        "owner":str(user_id),
                        "Admins":Admin_list
                    }
                data['Groups'][f'{chat_id}'].update(new_data)
                with open('backend/Chat_Data.json', 'w') as f:
                    json.dump(data, f)

            data,data_private = sing_admins_to_private(data_private,data,user_id,chat_id,user_chat,chat_title,chat_members_count)

        elif state_user == "administrator":
            user_stat = "ادمن في المجموعة"            
            if user_id in Moderators_list:
                pass
            else:
                Moderators_list.append(user_id)
                new_data = {
                    "Moderators":Moderators_list,
                }
                data['Groups'][f'{chat_id}'].update(new_data)
                with open('backend/Chat_Data.json', 'w') as f:
                    json.dump(data, f)

            data,data_private = sing_admins_to_private(data_private,data,user_id,chat_id,user_chat,chat_title,chat_members_count)

        elif state_user == "member":
            user_stat = "عضو في المجموعة"
            if user_id in Moderators_list:
                Moderators_list.remove(user_id)
                new_data = {
                    "Moderators":Moderators_list,
                }
                data['Groups'][f'{chat_id}'].update(new_data)
                with open('backend/Chat_Data.json', 'w') as f:
                    json.dump(data, f)
                #?هنا المفروض يتحقق في قائمة الادمن تبع البوت ولا لأ
            data,data_private = sing_admins_to_private(data_private,data,user_id,chat_id,user_chat,chat_title,chat_members_count)

        else:
            user_stat = "ربما يكون العضو مخفي"
            data,data_private = sing_admins_to_private(data_private,data,user_id,chat_id,user_chat,chat_title,chat_members_count)


        return user_stat,data,data_private
    

#?تحقق من رسالة الاعضاء ويتم اضافتهم الي قائمة الاعضاء
def check_save_member(data,message,user_id,first_name,username,chat_id):

    members = data['Groups'][f"{chat_id}"]["chat_member"][0]

    if str(user_id) in list(members.keys()):

        if message.new_chat_member:
            pass

        else:
            if message.text:              
                count_message = members[f"{user_id}"]["Number of messages"] + 1
                
                #?هنا هيتحقق اذا كان نفس البيانات او هيضيف التحديثات علي طول
                update_member ={
                    "Number of messages": count_message,
                    "username": f"{username}",
                    "name_user": f"{first_name}"     
                    }
                    
            elif message.document:
                count_message = members[f"{user_id}"]["Number of Document"] + 1
                                
                #?هنا هيتحقق اذا كان نفس البيانات او هيضيف التحديثات علي طول
                update_member ={
                    "Number of Document": count_message,
                    "username": f"{username}",
                    "name_user": f"{first_name}"  
                    }

            data['Groups'][f"{chat_id}"]["chat_member"][0][f"{user_id}"].update(update_member)
            # كتابة البيانات المحدثة إلى الملف
            with open('backend/Chat_Data.json', 'w') as f:
                json.dump(data, f)
        
            return data
        
        return data
    
    else:
        new_member ={
            f"{user_id}":{
                "safeCounter": 0,
                "Number of messages": 0,
                "Number of Document": 0,
                "username": f"{username}",
                "name_user": f"{first_name}",
                "Rank": "member",
                "Gender": "UnKnow"
            }
        }
        data['Groups'][f"{chat_id}"]["chat_member"][0].update(new_member)
        # كتابة البيانات المحدثة إلى الملف
        with open('backend/Chat_Data.json', 'w') as f:
            json.dump(data, f)
        # print("تم اضافتة الان")
        data = check_save_member(data,message,user_id,first_name,username,chat_id)
    
        return data

#?التحقق من البوت
def check_me(data_admin ,chat_id,chat_username,message):
    me = bot.get_me()
    bot_id = me.id

    Admins = list(data_admin['Groups'][f"{chat_id}"]["Admins"])
    if bot_id in Admins:
        pass
    else:
        Admins.append(bot_id)
        new_data = {
            "Admins":Admins
        }
        data_admin['Groups'][f'{chat_id}'].update(new_data)
        with open('backend/Chat_Data.json', 'w') as f:
            json.dump(data_admin, f)

    return data_admin


# #?الازرار الخاصة بالقنوات
# def btn_to_groups():
#     links = ["https://t.me/katabatakatabata",               
#                 "https://t.me/katabataa",
#                 "https://t.me/monakashaa",
#                 "https://t.me/asamaalmoslem",
#                 "https://t.me/ahmedalhimdan",
#                 "https://t.me/HasanAlgendy",
#                 "https://t.me/agathakresty",
#                 "https://t.me/dostwifski",
#                 "https://t.me/ahmadkhaledtawfek",
#                 "https://t.me/hananlashen"]
    
#     count_links = len(links)
#     keybord = types.InlineKeyboardMarkup()
#     count = 0 
#     name_url =[]
#     link_url=[]
#     btn1 = types.InlineKeyboardButton(text="مكتبة ضاد",url="https://t.me/katabatakatabata")
#     btn2 = types.InlineKeyboardButton(text="طلبات كتب وروايات",url="https://t.me/katabataa")
#     btn3 = types.InlineKeyboardButton(text="مناقشة كتب",url="https://t.me/monakashaa")
#     btn4 = types.InlineKeyboardButton(text="روايات أسامة المسلم",url="https://t.me/asamaalmoslem")
#     btn5 = types.InlineKeyboardButton(text="كتب أحمد آل حمدان",url="https://t.me/ahmedalhimdan")
#     btn6 = types.InlineKeyboardButton(text="كتب حسن الجندي",url="https://t.me/HasanAlgendy")
#     btn7 = types.InlineKeyboardButton(text="كتب أجاثا كريستي",url="https://t.me/agathakresty")
#     btn8 = types.InlineKeyboardButton(text="دوستويفسكي",url="https://t.me/dostwifski")
#     btn9 = types.InlineKeyboardButton(text="كتب أحمد خالد توفيق",url="https://t.me/ahmadkhaledtawfek")
#     btn10 = types.InlineKeyboardButton(text="كتب حنان لاشين",url="https://t.me/hananlashen")
    
#     keybord.add(btn1,btn2)
#     keybord.add(btn3,btn4)
#     keybord.add(btn6,btn5)
#     keybord.add(btn8,btn7)
#     keybord.add(btn9,btn10)


#     # if (count_links % 2) == 0:
#     #     print("زوجي")        
        
#     #     for i in links:
#     #         url = i
#     #         response = requests.get(url)
#     #         soup = BeautifulSoup(response.content, 'html.parser')
#     #         title = soup.find_all('meta')[2].get('content')
#     #         keybord.add(types.InlineKeyboardButton(text=f"{title}",url=i))
#     #         print(title)
    
#     # else:
#     #     print("فردي")
#     #     for i in links:
#     #         url = i
#     #         response = requests.get(url)
#     #         soup = BeautifulSoup(response.content, 'html.parser')
#     #         title = soup.find_all('meta')[2].get('content')
#     #         keybord.add(types.InlineKeyboardButton(text=f"{title}",url=i))
#     #         print(title)

#     #?تحقق اذا العنوان صالح
#     # resp = requests.get('https://google.com')
#     # if not resp.ok:
#     #     print (resp.status_code)
    
#     return keybord

# #?اذا العضو مشترك في المجموعة
# #!التحقق مما اذا كان ادمن داخل هذه امجموعة
# def check_user_in_group(message,user_id,chat_username):
#     url = f"https://api.telegram.org/bot{BOT_TOKEN}/getchatmember?chat_id=@{chat_username}&user_id={user_id}"
#     req = requests.get(url)
    
#     if 'member' in req.text or 'creator' in req.text or 'administrator' in req.text:
#         # print(req.text)
#         return True
#     if "left" in req.text:
#         keybord = btn_to_groups()
#         bot.reply_to(message,"~~~~~قنواتنا علي التلجرام~~~~~",reply_markup=keybord)

#         return False
 
# # check_user_in_group(message,user_id,"dqlkhabdo")