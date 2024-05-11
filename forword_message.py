from info import *

#?التعامل مع التحويل
def About_forward_message(message,chat_id,
        user_id,message_type,message_id,
        list_fowrword,awnar,
        Moderators_list,Admin_list
        ,OK_forword,some_forword,
        warning,safeCounter,full_name,
        data,link_Chat,chat_title):
    
    """
    هذه الوظيفة للتحقق من الرسائل المحولة
    1) اذا الرسالة من نفس الشخص سوف تسمح بالتحويل
    2) اذا الرسالة من نفس الجروب هتسمح بالتحويل
    3) اذا الرسالة محولة من جروب او قناة مسجلة هتسمح بالتحويل
    4) اذا الرسالة محولة من شخص مخفي 
    5) 
    """

    # print(message.forward_origin.type)
    all_Admins = Moderators_list + Admin_list
    found_message = True
    worning = f"[{full_name}](tg://user?id={user_id})"
    try:
        if "forward_origin" in message.json:

            #?نوع الشخص المحول منو
            type_user = message.forward_origin.type

            if message.text :
                text = message.text
                
            elif message.document :
                text = message.caption


            #?يبعت رسالة للمشرفين في الخاص
            if text == "@admin":
                addmi = Admin_list + Moderators_list
                for i in addmi:
                    state_admin = bot.get_chat_member(chat_id,i)
                    if state_admin.user.is_bot:
                        pass
                    else:
                        # f"[{"full_name"}](tg://user?id={user_id})"[{chat_title}]
                        m_to_admin= f"""
    تم ارسال [@admin]({link_Chat}) داخل المجموعة :
    ---------------------------------------
    اسم المجموعة :
    ------------- ( [{chat_title}]({link_Chat}) ) -------------
    ---------------------------------------
    تم الارسال بواسطة :
    ------------- <  < [{full_name}](tg://user?id={user_id}) > > -------------
    ---------------------------------------
    اذهب الان للتحقق"""
                    
                        bot.send_message(i,m_to_admin,parse_mode="markdown")

                return found_message

            #?اذا ادمن البوت هيحول اي حاجة
            elif user_id in Admin_list:
                return found_message
            
            #?اذا التحويل مفتوح هيحول اي حاجة
            elif (OK_forword == "True") and (some_forword == "False"):
                return found_message

            elif (OK_forword == "True") and (some_forword == "True") and (warning == "False"):
                if (type_user == "chat") or (type_user == "channel"):                        
                    if "forward_from_chat" in message.json:
                        #?######القناة او المجموعةالمحول منها########
                        Chat_forword_id = message.json["forward_from_chat"]["id"]
                        chat_forword_username = message.json["forward_from_chat"]["username"]
                        if (Chat_forword_id == chat_id)  or (str(Chat_forword_id) in list_fowrword) or (chat_forword_username in list_fowrword):
                            return found_message
                        
                        else:
                            bot.delete_message(chat_id=chat_id,message_id=message_id)
                            bot.send_message(chat_id=chat_id,text=f"{worning}\nممنوع التحويل من المجموعات او القنوات غير المخصصة",parse_mode="markdown")
                            found_message = False
                            return found_message
                                        
                    return found_message

                #?الجزء الخاص بالتحويل من مستخدم    
                elif type_user == "user":
                    if "forward_from" in message.json:
                        #?######المستخدم المحول منو########
                        user_forword_id = message.json["forward_from"]["id"]                
                        if (user_forword_id == user_id) or (user_forword_id in all_Admins):
                            return found_message

                        else:                        
                            bot.send_message(chat_id=chat_id,text=f"{worning}\n ممنوع التحويل من غير المشرفين",parse_mode="markdown")
                            bot.delete_message(chat_id=chat_id,message_id=message_id)
                            found_message = False
                            return found_message
                        
                    return found_message

                else:
                    bot.delete_message(chat_id=chat_id,message_id=message_id)
                    bot.send_message(chat_id=chat_id,text=f'{worning}\n ممنوع التحويل من خارج المجموعات المخصصة',parse_mode="markdown")
                        
                    found_message = False
                    return found_message 

            elif (OK_forword == "True") and (some_forword == "True") and (warning == "True"):
                if (type_user == "chat") or (type_user == "channel"):                        
                    if "forward_from_chat" in message.json:
                        #?######القناة او المجموعةالمحول منها########
                        Chat_forword_id = message.json["forward_from_chat"]["id"]
                        chat_forword_username = message.json["forward_from_chat"]["username"]
                        if (Chat_forword_id == chat_id)  or (str(Chat_forword_id) in list_fowrword) or (chat_forword_username in list_fowrword):
                            return found_message
                        
                        else:
                            bot.delete_message(chat_id=chat_id,message_id=message_id)
                            bot.send_message(chat_id=chat_id,text=f"{worning}\n ممنوع التحويل من المجموعات او القنوات غير المخصصة",parse_mode="markdown")
                            found_message = False
                            return found_message
                                        
                    return found_message
                
                #?الجزء الخاص بالتحويل من مستخدم    
                elif type_user == "user":
                    if "forward_from" in message.json:
                        #?######المستخدم المحول منو########
                        user_forword_id = message.json["forward_from"]["id"]                
                        if (user_forword_id == user_id) or (user_forword_id in all_Admins):
                            return found_message

                        else:
                            bot.send_message(chat_id=chat_id,text=f"{worning}\n ممنوع التحويل من غير المشرفين",parse_mode="markdown")
                            bot.delete_message(chat_id=chat_id,message_id=message_id)
                            found_message = False
                            return found_message
                        
                    return found_message

                else:
                    bot.delete_message(chat_id=chat_id,message_id=message_id)
                    bot.send_message(chat_id=chat_id,text=f'{worning}\n ممنوع التحويل من خارج المجموعات المخصصة',parse_mode="markdown")
                        
                    found_message = False
                    return found_message 

            #?اذا التحويل مقفول هيسمح للمشرفين بس يحولي للي متحدد
            elif (OK_forword == "False") and (warning == "True") :
                if user_id in all_Admins:
                    if (type_user == "chat") or (type_user == "channel"):
                        if "forward_from_chat" in message.json:                
                            #?######القناة او المجموعةالمحول منها########
                            Chat_forword_id = message.json["forward_from_chat"]["id"]
                            chat_forword_username = message.json["forward_from_chat"]["username"]
                            if (Chat_forword_id == chat_id) or (str(Chat_forword_id) in list_fowrword) or (chat_forword_username in list_fowrword):
                                # found_message = True
                                return found_message
                            
                            else:
                                bot.delete_message(chat_id=chat_id,message_id=message_id)
                                if message_type == "text":
                                    bot.send_message(chat_id=chat_id,text=f'{worning}\n ممنوع تحويل الرسائل من المجموعات او القنوات غير المسجلة',parse_mode="markdown")
                                elif message_type == "document":
                                    bot.send_message(chat_id=chat_id,text=f'{worning}\n ممنوع تحويل الكتب ولكن يمكنك تنزيلها في المجموعة',parse_mode="markdown")
                                found_message = False
                                return found_message
                    
                    #?الجزء الخاص بالتحويل من مستخدم    
                    elif type_user == "user":
                        if "forward_from" in message.json:
                            #?######المستخدم المحول منو########
                            user_forword_id = message.json["forward_from"]["id"]                
                            if (user_forword_id == user_id) or (user_forword_id in all_Admins):
                                # found_message = True
                                return found_message
                            else:
                                bot.delete_message(chat_id=chat_id,message_id=message_id)
                                if message_type == "text":
                                    bot.send_message(chat_id=chat_id,text=f'{worning}\n ممنوع تحويل الرسائل التي لاتخصك او تخص المشرفين',parse_mode="markdown")
                                elif message_type == "document":
                                    bot.send_message(chat_id=chat_id,text=f'{worning}\n ممنوع تحويل الكتب ولكن يمكنك تنزيلها في المجموعة',parse_mode="markdown")

                                found_message = False
                                return found_message
                            
                        return found_message

                    #?تم التحويل من مستخدم مخفي
                    elif type_user == "hidden_user":
                        bot.delete_message(chat_id=chat_id,message_id=message.id)
                        found_message = False
                        return found_message
                    
                    return found_message

                else:
                    bot.delete_message(chat_id=chat_id,message_id=message_id)

                    if message_type == "text":                    
                        bot.send_message(chat_id=chat_id,text=f"{worning}\nممنوع تحويل الرسائل",parse_mode="markdown")

                    elif message_type == "document":
                        bot.send_message(chat_id=chat_id,text=f"{worning}\nممنوع تحويل الكتب",parse_mode="markdown")
                        
                    found_message = False
                    return found_message  
                
            elif (OK_forword == "False") and (warning == "False") :
                if user_id in all_Admins:
                    if (type_user == "chat") or (type_user == "channel"):
                        if "forward_from_chat" in message.json:                
                            #?######القناة او المجموعةالمحول منها########
                            Chat_forword_id = message.json["forward_from_chat"]["id"]
                            chat_forword_username = message.json["forward_from_chat"]["username"]
                            if (Chat_forword_id == chat_id) or (str(Chat_forword_id) in list_fowrword) or (chat_forword_username in list_fowrword):
                                # found_message = True
                                return found_message
                            
                            else:
                                bot.delete_message(chat_id=chat_id,message_id=message_id)
                                if message_type == "text":
                                    bot.send_message(chat_id=chat_id,text=f'{worning}\n ممنوع تحويل الرسائل من المجموعات او القنوات غير المسجلة',parse_mode="markdown")
                                elif message_type == "document":
                                    bot.send_message(chat_id=chat_id,text=f'{worning}\n ممنوع تحويل الكتب ولكن يمكنك تنزيلها في المجموعة',parse_mode="markdown")
                                    
                                found_message = False
                                return found_message
                    
                    #?الجزء الخاص بالتحويل من مستخدم    
                    elif type_user == "user":
                        if "forward_from" in message.json:
                            #?######المستخدم المحول منو########
                            user_forword_id = message.json["forward_from"]["id"]                
                            if (user_forword_id == user_id) or (user_forword_id in all_Admins):
                                # found_message = True
                                return found_message

                            else:
                                bot.delete_message(chat_id=chat_id,message_id=message_id)
                                if message_type == "text":                    
                                    bot.send_message(chat_id=chat_id,text=f"{worning}\nيمكنك التحويل من المشرفين فقط",parse_mode="markdown")

                                elif message_type == "document":
                                    bot.send_message(chat_id=chat_id,text=f"{worning}\nممنوع تحويل الكتب ولكن يمكن تنزيلها في المجموعة",parse_mode="markdown")
                        
                                found_message = False
                                return found_message
                            
                        return found_message

                    #?تم التحويل من مستخدم مخفي
                    elif type_user == "hidden_user":
                        bot.delete_message(chat_id=chat_id,message_id=message.id)
                        found_message = False
                        return found_message
                    
                    return found_message

                else:
                    bot.delete_message(chat_id=chat_id,message_id=message_id)
                    if message_type == "text":
                        bot.send_message(chat_id=chat_id,text=f'{worning}\n ممنوع تحويل الرسائل',parse_mode="markdown")
                    elif message_type == "document":
                        bot.send_message(chat_id=chat_id,text=f'{worning}\n ممنوع تحويل الكتب',parse_mode="markdown")
                        
                    found_message = False
                    return found_message
            
            else:
                return found_message
        
        else:
            return found_message

    except:
        found_message = False
        return found_message