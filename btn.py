from info import *

#?عرض المجموعات اللتي لدي
def btn_show_group(user_id):
    keyboard = types.InlineKeyboardMarkup()

    with open(f"Admins_bot/{user_id}.json", 'r') as f:
        my_groups = json.load(f)
    list_grop = my_groups["Groups"]
    list_btn = []
    small_list = []
    cc = 0 
    for i in list(list_grop.keys()) :        
        title = list_grop[i]["title"]
        id = list_grop[i]["id"]        
        small_list.append(types.InlineKeyboardButton(text=title,callback_data=id))
        cc +=1
        if cc == 2:
            cc =0
            list_btn.append(small_list)
            small_list = []
        
    if small_list != []:
        list_btn.append(small_list)

    for i in list_btn:
        keyboard.row(*i)
    
    return keyboard
#?عرض الخيارات
def btn_option(new_user_id):    
    keyboard = types.InlineKeyboardMarkup()

    with open(f"Admins_bot/{new_user_id}.json", 'r') as f:
        my_groups = json.load(f)

    now_group = my_groups["now_group"]

    list_option = {
        "الاوامر 🤖":f"{now_group}_comands",
        "الروابط 🔗":f"{now_group}_links",
        "الردود 🗣":f"{now_group}_replay",
        "القنوات القابلة للتحويل 🎗":f"{now_group}_channel",
        "الادمن 🕵️‍♂️":f"{now_group}_admin",
        "عودة ↩":f"{now_group}_back"
    }

    list_btn = []
    small_list = []
    cc = 0 

    for i in list(list_option) :        
        title = i
        id = list_option[i]  
      
        small_list.append(types.InlineKeyboardButton(text=title,callback_data=id))
        cc +=1
        if cc == 2:
            cc =0
            list_btn.append(small_list)
            small_list = []
        
    if small_list != []:
        list_btn.append(small_list)

    for i in list_btn:
        keyboard.row(*i)
    
    return keyboard
    
#?عرض معلومات المجموعة
def info(data,Groups,chat_id,message_id):
    keybord = types.InlineKeyboardMarkup()
    
    for i in list(Groups.keys()):
        if data == i:
            data_my_group = f"""
اسم المجموعة : {Groups[i]["title"]}

اسم مستخدم المجموعة : @{Groups[i]["username"]}

أيدي المجموعة : {Groups[i]["id"]}

عدد اعضاء المجموعة : {Groups[i]["countmember"]}
    """
                
            keybord.add(types.InlineKeyboardButton(text="عودة ↩️",callback_data="home"),
                        types.InlineKeyboardButton(text="الاعدادات ⚙️",callback_data="Settings"))
            bot.edit_message_text(data_my_group,chat_id,message_id=message_id,reply_markup=keybord)
            break
    # return keybord

#?عرض الاوامر
def command(chat_id,message_id):

    command_text = """
===========================

@admin -->>👇
لاستدعاء الادمن في الخاص

===========================

الادمن -->>👇
لعرض الادمن 

===========================

رفع ادمن   -->> لتعيين ادمن للبوت (خاص لمالك المجموعة فقط)
تنزيل ادمن -->>  لتنزيل ادمن للبوت (خاص لمالك المجموعة فقط)

===========================

--->> فتح الكل
--->> قفل الكل 

===========================

-->> فتح التحويل
-->> منع التحويل
--->>> (لمنع - للسماح) تحويل الرسائل/الملفات داخل المجموعة

===========================

-->> فتح تحويل محدد
-->> قفل تحويل محدد
--->>> (لمنع - للسماح) تحويل الرسائل/الملفات داخل المجموعة من مجموعات/قنوات محددة

===========================

-->> تعطيل الكتب
-->> تفعيل الكتب
--->>> يقوم البوت بارسال الملفات داخل المجموعة

===========================

-->> تعطيل الروابط
(منع ارسال الروابط)
-->> تفعيل الروابط
(السماح بارسال الروابط)

===========================

-->> فتح روابط معينة
-->> قفل روابط معينة
السماح بارسال روابط محددة

===========================

-->> تعطيل التحذير
-->> تفعيل التحذير
يقوم البوت بارسال التحذيرات بشأن الروابط

===========================
"""
    
    keybord = types.InlineKeyboardMarkup()
    keybord.add(types.InlineKeyboardButton(text="عودة",callback_data="Settings"))
    bot.edit_message_text(text=command_text,chat_id=chat_id,message_id=message_id,reply_markup=keybord)

#?عرض ادمن البوت داخل المجموعة
def show_admin(data,chat_id,message_id):

    with open("backend/Chat_Data.json", 'r') as f:
        data_groups = json.load(f)
    id_chat = data_groups["Groups"][data]
    admins_chat = data_groups["Groups"][data]["Admins"]

    list_admin = """
قائمة الادمن : 🕵️‍♂️\n
"""
    
    for i in admins_chat:
        admin =bot.get_chat_member(data,i)
        if admin.user.is_bot:
            pass
        else:
            full_name = admin.user.full_name
            user_id = admin.user.id
            username = admin.user.username
            list_admin +=f"""

الاسم : [{full_name}](tg://user?id={user_id})

اسم المستخدم : @{username}

"""

    keybord = types.InlineKeyboardMarkup()
    keybord.add(types.InlineKeyboardButton(text="عودة",callback_data="Settings"))
    bot.edit_message_text(text=list_admin,chat_id=chat_id,message_id=message_id,reply_markup=keybord,parse_mode="markdown")

#!!!!!####################################
#!!!!!####################################

#?لعرض الردود
def show_rep_words(chat,chat_id,message_id):
    with open("backend/Chat_Data.json", 'r') as f:
        data_groups = json.load(f)
    id_chat = data_groups["Groups"][chat]
    rep_words_list = data_groups["Groups"][chat]["rep_words"][0]

    list_rep_words = """
الكلمات اللتي يتم الرد عليها بغير متوفر : ☣ ☢
----------------------------------------------------
"""
    
    # استخدام حلقة تكرار لعرض كل عنصر مع رقمه
    for index, item in enumerate(rep_words_list, start=1):
        list_rep_words +=f"""
{index}- الكلمة :  {item} -->> الرد : {rep_words_list[item]}
"""

    keybord = types.InlineKeyboardMarkup()
    keybord.add(types.InlineKeyboardButton(text="اضافة رد",callback_data=f"{chat}_addreplay"),
                types.InlineKeyboardButton(text="حذف رد",callback_data=f"{chat}_delreplay"))
    keybord.add(types.InlineKeyboardButton(text="عودة",callback_data="Settings"))
    bot.edit_message_text(text=list_rep_words,chat_id=chat_id,message_id=message_id,reply_markup=keybord,parse_mode="markdown")

#?لإضافة الردود
def add_rep_words(chat,chat_id,call):
    message = call.message
    bot.send_message(chat_id,"ارسل الكلمة اللذي تريد الرد عليها")
    bot.register_next_step_handler(message, lambda m: get_rep_words1(m,chat_id, chat))

def get_rep_words1(message,chat_id,chat):
    try:            
        with open("backend/Chat_Data.json", 'r') as f:
            data_groups = json.load(f)
        rep_words_list = data_groups["Groups"][chat]["rep_words"][0]

        if message.text in  list(rep_words_list):
            bot.reply_to(message,"هذا الرد مسجل من قبل")
        else:
            word1 = message.text
            bot.send_message(chat_id,"ارسل الان الرد")
            bot.register_next_step_handler(message, lambda m: get_rep_words2(m,word1, chat))
    except:
        bot.send_message(message.chat.id, "يبدو ان هناك مشكلة في الرد الذي ادخلته")

def get_rep_words2(message,word1,chat):
    try:
        with open("backend/Chat_Data.json", 'r') as f:
            data_groups = json.load(f)
        rep_words_list = data_groups["Groups"][chat]["rep_words"][0]

        new_rep = {
            word1:message.text
        }
        rep_words_list.update(new_rep)
        with open("backend/Chat_Data.json", "w",encoding="utf-8") as f:
            json.dump(data_groups, f)
        bot.reply_to(message,"تم تسجيل الرد بنجاح")
    except:
        bot.reply_to(message,"يبدو ان هناك خطأ ما")

#?لحذف الردود
def del_rep_words(chat,chat_id,call):
    message = call.message
    bot.send_message(chat_id,"ارسل الكلمة اللذي تريد حذفها")
    bot.register_next_step_handler(message, lambda m: del_word(m,chat_id, chat))

def del_word(message,chat_id, chat):
    try:
        with open("backend/Chat_Data.json", 'r') as f:
            data_groups = json.load(f)
        rep_words_list = data_groups["Groups"][chat]["rep_words"][0]
        if message.text in rep_words_list:
            del data_groups["Groups"][chat]["rep_words"][0][message.text]
            with open("backend/Chat_Data.json", "w",encoding="utf-8") as f:
                json.dump(data_groups, f)
            bot.reply_to(message,"تم الحذف بنجاح")
        else:
            bot.reply_to(message,"يبدو انه ليس هناك هذا الرد")
    except:
        bot.send_message(chat_id,"يبدو انه هناك مشكلة ما")

#!!!!!####################################
#!!!!!####################################

#?لعرض القنوات القابلة للتحويل
def show_channel_forword(chat,chat_id,message_id):
    with open("backend/Chat_Data.json", 'r') as f:
        data_groups = json.load(f)
    id_chat = data_groups["Groups"][chat]
    chat_forword = data_groups["Groups"][chat]["forward_message"]

    list_groups = """
القنوات المسموح بالتحويل منها : 🎗
----------------------------------------------------
"""
    
    for i in chat_forword:
        grop = bot.get_chat(f"@{i}")
        grop_type = grop.type
        if grop_type == "channel":
            grop_type = "قناة"
        elif grop_type == "supergroup":
            grop_type = "مجموعة"
        grop_name = grop.title
        grop_username = grop.username
        grop_description = grop.description
        list_groups +=f"""
الاسم : {grop_name}
اسم المستخدم : @{grop_username}
الوصف : {grop_description}
النوع : {grop_type}
----------------------------------------------------
"""
        
    keybord = types.InlineKeyboardMarkup()
    keybord.add(types.InlineKeyboardButton(text="اضافة مجموعة او قناة",callback_data=f"{chat}_Addchannel"),
            types.InlineKeyboardButton(text="حذف مجموعة او قناة",callback_data=f"{chat}_delchannel"))
    keybord.add(types.InlineKeyboardButton(text="عودة",callback_data="Settings"))
    bot.edit_message_text(text=list_groups,chat_id=chat_id,message_id=message_id,reply_markup=keybord,parse_mode="markdown")

#?لإضافة القنوات القابلة للتحويل
def add_channel_forword(chat,chat_id,call):
    message = call.message
    bot.send_message(chat_id,"ارسل اسم المستخدم للمجموعة او القناة اللتي تريد اضافتها")
    bot.register_next_step_handler(message, lambda m: get_channel(m, chat))

def get_channel(message,chat):
    try:
        group_user = bot.get_chat(f"@{message.text}")
        grop_type = group_user.type
        if grop_type == "channel":
            grop_type = "قناة"
        elif grop_type == "supergroup":
            grop_type = "مجموعة"
        grop_name = group_user.title
        grop_username = group_user.username
        grop_description = group_user.description
        msg_to_user =f"""
       ~~ تم التسجيل بنجاح ~~
----------------------------------------------------
الاسم : {grop_name}
اسم المستخدم : @{grop_username}
الوصف : {grop_description}
النوع : {grop_type}
----------------------------------------------------
"""

        with open("backend/Chat_Data.json", 'r') as f:
            data_groups = json.load(f)
        forward_message = list(data_groups["Groups"][chat]["forward_message"])
        if message.text in  forward_message:
            bot.reply_to(message,f"هذه ال{grop_type} مسجلة من قبل")

        else:
            forward_message.append(message.text)
            new_forword = {
                "forward_message":forward_message
            }
            data_groups["Groups"][chat].update(new_forword)
            with open("backend/Chat_Data.json", "w",encoding="utf-8") as f:
                json.dump(data_groups, f)

            bot.reply_to(message,msg_to_user)

    except:
        bot.send_message(message.chat.id, "الرجاء إدخال اسم المستخدم للمجموعة او القناة بشكل صحيح")

#!!!!!####################################
#!!!!!####################################


#?العرض
def show_items(chat,chat_id,message_id,kind_list,text_list,btn_addtxt,btn_addcomand,btn_deltxt,btn_delcommand):
    with open("backend/Chat_Data.json", 'r') as f:
        data_groups = json.load(f)
    id_chat = data_groups["Groups"][chat]
    list_items = data_groups["Groups"][chat][kind_list]

    item_list = f"""{text_list}
----------------------------------------------------
"""
    
    # استخدام حلقة تكرار لعرض كل عنصر مع رقمه
    for index, item in enumerate(list_items, start=1):
        item_list +=f"""
{index}- {item}
"""

    keybord = types.InlineKeyboardMarkup()
    keybord.add(types.InlineKeyboardButton(text=btn_addtxt,callback_data=f"{chat}_{btn_addcomand}"),
                types.InlineKeyboardButton(text=btn_deltxt,callback_data=f"{chat}_{btn_delcommand}"))
    keybord.add(types.InlineKeyboardButton(text="عودة",callback_data="Settings"))
    bot.edit_message_text(text=item_list,chat_id=chat_id,message_id=message_id,reply_markup=keybord,parse_mode="markdown")

#?الاضافة
def add_item(chat,chat_id,call,txt1,ifrep_txt,elsrep_txt,list_kind):
    message = call.message
    bot.send_message(chat_id,txt1)
    bot.register_next_step_handler(message, lambda m: get_item(m, chat,ifrep_txt,elsrep_txt,list_kind))

def get_item(message,chat,ifrep_txt,elsrep_txt,list_kind):
    try:
        with open("backend/Chat_Data.json", 'r') as f:
            data_groups = json.load(f)
        list_items = data_groups["Groups"][chat][list_kind]
        if message.text in  list_items:
            bot.reply_to(message,elsrep_txt)

        else:
            list_items.append(message.text)
            new_item = {
                list_kind:list_items
            }
            data_groups["Groups"][chat].update(new_item)
            with open("backend/Chat_Data.json", "w",encoding="utf-8") as f:
                json.dump(data_groups, f)

            bot.reply_to(message,ifrep_txt)

    except:
        bot.send_message(message.chat.id, "يبدو ان هناك مشكلة ما")

#?الحذف
def del_item(chat,chat_id,call,kind_list,txt,elsetxt):
    message = call.message
    bot.send_message(chat_id,txt)
    bot.register_next_step_handler(message, lambda m: del_item_1(m,chat_id, chat,kind_list,elsetxt))

def del_item_1(message,chat_id, chat,kind_list,elsetxt):
    try:
        with open("backend/Chat_Data.json", 'r') as f:
            data_groups = json.load(f)

        list_items = list(data_groups["Groups"][chat][kind_list])
        if message.text in list_items:
            list_items.remove(message.text)
            new={
                kind_list:list_items
            }
            data_groups["Groups"][chat].update(new)
            with open("backend/Chat_Data.json", "w",encoding="utf-8") as f:
                json.dump(data_groups, f)
            bot.reply_to(message,"تم الحذف بنجاح")
        else:
            bot.reply_to(message,elsetxt)
    except:
        bot.send_message(chat_id,"يبدو انه هناك مشكلة ما")
    

def manage_btn(call,Groups,data,new_user_id,chat_id,message_id):
    keybord_home = btn_show_group(new_user_id)    
    keybord_option = btn_option(new_user_id)
    #?عرض معلومات المجموعة
    info(data,Groups,chat_id,message_id)
    
    if data.lstrip('-').isdigit():
        with open(f"backend/Chat_Data.json",'r',encoding='utf-8') as f:
            data_group = json.load(f)
        admin_list = data_group["Groups"][data]["Admins"]
        if new_user_id in admin_list:
            with open(f"Admins_bot/{new_user_id}.json", 'r') as f:
                my_groups = json.load(f)
            now_group = {
                "now_group":f"{data}"
            }
            my_groups.update(now_group)
            with open(f"Admins_bot/{new_user_id}.json", "w",encoding="utf-8") as f:
                json.dump(my_groups, f, ensure_ascii=False, indent=4)
        else:
            bot.delete_message(chat_id,message_id)

    if '_' in data:
        with open(f"backend/Chat_Data.json",'r',encoding='utf-8') as f:
            data_group = json.load(f)
        data = data.split("_")
        chat = data[0]
        admin_list = data_group["Groups"][chat]["Admins"]
        if new_user_id in admin_list:

            #?العودة لمعلومان الجموعة
            if data[1] == "back":
                info(chat,Groups,chat_id,message_id)

            #?عرض الاوامر
            elif data[1] == "comands":
                command(chat_id,message_id)

            #?عرض الروابط واضافتها
            #*تم
            elif data[1] == "links":
                text_list="الروابط المسموح بارسالها داخل المجموعة : 🔗"
                btn_addtxt="اضافة رابط"            
                btn_addcomand="Addlink"              
                btn_deltxt="حذف رابط"
                btn_delcommand="dellink"
                show_items(chat,chat_id,message_id,
                        "linkes",text_list,
                        btn_addtxt,btn_addcomand,
                        btn_deltxt,btn_delcommand)
            #*تم
            elif data[1] == "Addlink": 
                txt1 = "ارسل الرابط اللذي تريد اضافتة"
                list_kind = "linkes"
                ifrep_txt = "تم الاضافة بنجاح"
                elsrep_txt = "يبدو ان هذا الرابط مسجل من قبل"
                add_item(chat,chat_id,call,
                        txt1,ifrep_txt,
                        elsrep_txt,list_kind)
            #*تم
            elif data[1] == "dellink":
                txt ="ارسل الرابط اللذي تريد حذفة"
                elsetxt = "يبدو انه ليس هناك هذا الرابط"
                del_item(chat,chat_id,call,"linkes",txt,elsetxt)

    #!#####################################
            #?الردود
            elif data[1] == "replay":
                show_rep_words(chat,chat_id,message_id)

            elif data[1] == "addreplay":
                add_rep_words(chat,chat_id,call)
            
            elif data[1] == "delreplay": 
                del_rep_words(chat,chat_id,call)

    #!#####################################


            #? عرض القنوا المحول منها واضافتها
            elif data[1] == "channel":
                show_channel_forword(chat,chat_id,message_id)
            
            elif data[1] == "Addchannel":
                add_channel_forword(chat,chat_id,call)

            #*تم
            elif data[1] == "delchannel":
                txt ="ارسل القناة او المجموعة اللتي تريد حذفها"
                elsetxt = "يبدو انه ليس هناك هذه المجموعة او القناة"
                del_item(chat,chat_id,call,"forward_message",txt,elsetxt)


            elif data[1] == "admin":
                show_admin(chat,chat_id,message_id)

        else:
            bot.delete_message(chat_id,message_id)

    else:
        if data == "home":
            bot.edit_message_text(text="هذه مجموعاتك 😯",chat_id=chat_id,message_id=message_id,reply_markup=keybord_home)

        if data == "Settings":
            bot.edit_message_text(text="⚙ ⚙ ⚙ ⚙ ⚙",chat_id=chat_id,message_id=message_id,reply_markup=keybord_option)
    
    with open(f"backend/Chat_Data.json",'r',encoding='utf-8') as f:
        data_group = json.load(f)
    return data_group

def btn_my_groups(message,user_id):
    keyboard = btn_show_group(user_id)
    tousermsg = bot.reply_to(message,"هذه مجموعاتك 😯",reply_markup=keyboard)

def btn_private_chat():
    keybord = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="اضفني الي مجموعتك",url="https://t.me/Zeqo0qobot?startgroup=Commands&admin=ban_users+restrict_members+delete_messages+change_info+invite_users+manage_chat")
    keybord.add(btn1)
    return keybord
    
