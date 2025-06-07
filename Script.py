import os
class script(object):
    START_TXT = """<b>Salut {}, {}\n\nJe suis un ultime bot capable de vous fournir des cartoons (dessin animé) il suffira juste d'écrire uniquement le nom de votre demande dans mon groupe privé! 😍\n<blockquote>🌿 Maintenu par: <a href="https://t.me/BotZFlix">Bot ZFlix</a></blockquote></b>"""
    
    HELP_TXT = """<b>« Cliquez sur les boutons ci-dessous pour obtenir de la documentation sur des modules spécifiques. »..</b>"""
    
    TELE_TXT = """<b>/telegraph - Envoie-moi une image ou une vidéo de moins de (5 Mo).

Note : cette commande fonctionne dans les deux groupes et en message privé.</b>"""
    FSUB_TXT = """<b>• Ajoute-moi à ton groupe et fais de moi un admin 😗  
• Fais de moi un admin dans ton canal ou groupe d'abonnement cible 😉  
• Envoie /fsub ton_id_de_chat_cible
ᴇx: <code>/fsub -100xxxxxx</code>

Maintenant c'est fait. Je vais inciter vos utilisateurs à rejoindre votre canal/groupe, et je ne fournirai aucun fichier tant que vos utilisateurs ne rejoindront pas votre canal cible.

Pour désactiver fsub dans votre groupe, envoyez simplement <code>/del_fsub</code>

Pour vérifier si fsub est connecté ou non, utilisez... <code>/show_fsub</code></b>"""

    FORCESUB_TEXT="""<b>
Pour obtenir le Cartoon demandé par vous.

Vous devrez rejoindre notre canal officiel.

D'abord, cliquez sur le bouton "Rejoindre le canal de mise à jour", puis cliquez sur le bouton "Demander à rejoindre".

Après cela, essayez d'accéder à ce Cartoon, puis cliquez sur le bouton "Réessayer".
    </b>"""
    
    TTS_TXT="""
<b>• sᴇɴᴅ /tts Pour utiliser cette fonctionnalité...</b>"""

    DISCLAIMER_TXT = """
<b>Ceci est un projet open source.

Tous les fichiers de ce bot sont librement disponibles sur Internet ou publiés par quelqu'un d'autre. Juste pour faciliter la recherche, ce bot indexe des fichiers qui sont déjà téléchargés sur Telegram. Nous respectons toutes les lois sur le droit d'auteur et travaillons en conformité avec le DMCA et l'EUCD. Si quelque chose est contre la loi, veuillez me contacter afin qu'il puisse être retiré dès que possible. Il est interdit de télécharger, de diffuser, de reproduire, de partager ou de consommer du contenu sans l'autorisation explicite du créateur du contenu ou du titulaire légal des droits d'auteur. Si vous pensez que ce bot enfreint votre propriété intellectuelle, contactez les chaînes respectives pour leur retrait. Le bot ne possède aucun de ces contenus, il indexe uniquement les fichiers provenant de Telegram.. 

<blockquote>🌿 Maintenu par : <a href='https://t.me/BotZFlix'>Kingcey</a></b></blockquote>"""
    

    ABOUT_TEXT = """<blockquote><b>‣ Mon nom : Frids\n‣ Créateur : <a href='https://t.me/Kingcey'>MR.Kingcey</a>\n‣ Bibliothèque : pyrogram\n‣ Langue : Python\n‣ Base de données : MongoDB\n‣ Hébergé sur : All web\n‣ Statut de construction : ᴠ5.2 [sᴛᴀʙʟᴇ]</b></blockquote>"""    
    
    SUPPORT_GRP_MOVIE_TEXT = '''<b>Hey {}

J'ai trouvé {} résultats 🎁,  
mais je ne peux pas envoyer ici 🤞🏻  
Veuillez rejoindre notre groupe de demande pour obtenir.✨</b>'''

    CHANNELS = """
<u>Nos tous groupes et canaux</u>

▫️ Tous les derniers et anciens films & séries.  
▫️ Tous les films disponibles dans toutes les langues.  
▫️ Toujours un support admin.  
▫️ 24x7 services disponibles.."""

    LOGO = """

BOT WORKING PROPERLY 🔥"""
    
    RESTART_TXT = """
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !
> {} 
📅 Dᴀᴛᴇ : <code>{}</code>
⏰ Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code>
🛠️ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: <code>v4.2 [ Sᴛᴀʙʟᴇ ]</code>

Bʏ @BotZFlix</b>"""
        
    
    STATUS_TXT = """<b><u>🗃 ᴅᴀᴛᴀʙᴀsᴇ 1 🗃</u>

» ᴛᴏᴛᴀʟ ᴜsᴇʀs - <code>{}</code>
» ᴛᴏᴛᴀʟ ɢʀᴏᴜᴘs - <code>{}</code>
» ᴜsᴇᴅ sᴛᴏʀᴀɢᴇ - <code>{} / {}</code>

<u>🗳 ᴅᴀᴛᴀʙᴀsᴇ 2 🗳</u></b>

» ᴛᴏᴛᴀʟ ꜰɪʟᴇs - <code>{}</code>
» ᴜsᴇᴅ sᴛᴏʀᴀɢᴇ - <code>{} / {}</code>

<u>🤖 ʙᴏᴛ ᴅᴇᴛᴀɪʟs 🤖</u>

» ᴜᴘᴛɪᴍᴇ - <code>{}</code>
» ʀᴀᴍ - <code>{}%</code>
» ᴄᴘᴜ - <code>{}%</code></b>"""

    NEW_USER_TXT = """<b>#New_User {}

≈ ɪᴅ:- <code>{}</code>
≈ ɴᴀᴍᴇ:- {}</b>"""

    NEW_GROUP_TXT = """#New_Group {}

Group name - {}
Id - <code>{}</code>
Group username - @{}
Group link - {}
Total members - <code>{}</code>
User - {}"""

    REQUEST_TXT = """<b>📜 ᴜꜱᴇʀ - {}
📇 ɪᴅ - <code>{}</code>

🎁 ʀᴇǫᴜᴇꜱᴛ ᴍꜱɢ - <code>{}</code></b>"""  
   
    IMDB_TEMPLATE_TXT = """
<b>ʜᴇʏ {message.from_user.mention}, Voici les résultats pour votre requête {search}.

🍿 Titre : {title}  
🎃 Genres : {genres}  
📆 Année : {release_date}  
⭐️ Note : {rating} / 10</b>
"""

    FILE_CAPTION = """<b>{file_name}\n\nRejoins aussi➥ 「<a href="https://t.me/ZflixTeam">𝒁𝒇𝒍𝒊𝒙-𝑻𝒆𝒂𝒎</a>」</b>"""
    

    ALRT_TXT = """Créé Par: @Kingcey !"""

    OLD_ALRT_TXT = """Vous utilisez mes anciens messages... envoyez une nouvelle demande..."""

    NO_RESULT_TXT = """<b>Ce message n'est pas publié ou ajouté dans ma base de données. Veuillez réssayer aPrès ou Contacter: @Kingcey 🙄</b>"""
    
    I_CUDNT = """🤧 Salut {}

Je n'ai pas pu trouver de film ou de série avec ce nom... 😐"""

    I_CUD_NT = """😑 Salut {}

Je n'ai rien trouvé lié à cela 😞... vérifiez votre orthographe.."""
    
    CUDNT_FND = """🤧 Salut {}

Je n'ai rien trouvé lié à cela. Vouliez-vous dire l'un de ces éléments ?? \nClique sur l'un des élements👇"""
    
    FONT_TXT= """<b>Vous pouvez utiliser ce mode pour changer le style de vos polices, envoyez-moi simplement dans ce format :

<code>/font hi how are you</code></b>"""
    
    PLAN_TEXT = """<b>ᴡᴇ ᴀʀᴇ ᴘʀᴏᴠɪᴅɪɴɢ ᴘʀᴇᴍɪᴜᴍ ᴀᴛ ᴛʜᴇ ʟᴏᴡᴇsᴛ ᴘʀɪᴄᴇs:
    
1 ʀᴜᴘᴇᴇ ᴘᴇʀ ᴅᴀʏ 👻
29 ʀᴜᴘᴇᴇs ғᴏʀ ᴏɴᴇ ᴍᴏɴᴛʜ 😚
55 ʀᴜᴘᴇᴇs ғᴏʀ ᴛᴡᴏ ᴍᴏɴᴛʜs 😗

ᴄʟɪᴄᴋ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ ʙᴜʏɪɴɢ ↡↡↡
</b>"""
    
    VERIFICATION_TEXT = """<b>👋 ʜᴇʏ {} {},

📌 <u>ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴠᴇʀɪғɪᴇᴅ ᴛᴏᴅᴀʏ, ᴘʟᴇᴀꜱᴇ ᴄʟɪᴄᴋ ᴏɴ ᴠᴇʀɪғʏ & ɢᴇᴛ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇꜱꜱ ғᴏʀ ᴛɪʟʟ ɴᴇxᴛ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ</u>

#ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ:- 1/3 ✓

ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴅɪʀᴇᴄᴛ ғɪʟᴇꜱ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴꜱ ᴛʜᴇɴ ʙᴜʏ ʙᴏᴛ ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ 😊

💶 sᴇɴᴅ /plan ᴛᴏ ʙᴜʏ sᴜʙsᴄʀɪᴘᴛɪᴏɴ</b>"""

    VERIFY_COMPLETE_TEXT = """<b>👋 ʜᴇʏ {},

ʏᴏᴜ ʜᴀᴠᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴛʜᴇ 1st ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ✓

ɴᴏᴡ ʏᴏᴜ ʜᴀᴠᴇ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ꜰᴏʀ ɴᴇxᴛ <code>{}</code></b>"""

    SECOND_VERIFICATION_TEXT = """<b>👋 ʜᴇʏ {} {},

📌 <u>ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴠᴇʀɪꜰɪᴇᴅ, ᴛᴀᴘ ᴏɴ ᴛʜᴇ ᴠᴇʀɪꜰʏ ʟɪɴᴋ ᴀɴᴅ ɢᴇᴛ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ꜰᴏʀ ᴛɪʟʟ ɴᴇxᴛ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ</u>

#ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ:- 2/3

ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴅɪʀᴇᴄᴛ ғɪʟᴇꜱ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴꜱ ᴛʜᴇɴ ʙᴜʏ ʙᴏᴛ ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ 😊

💶 sᴇɴᴅ /plan ᴛᴏ ʙᴜʏ sᴜʙsᴄʀɪᴘᴛɪᴏɴ</b>"""

    SECOND_VERIFY_COMPLETE_TEXT = """<b>👋 ʜᴇʏ {},

ʏᴏᴜ ʜᴀᴠᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴛʜᴇ 2nd ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ✓

ɴᴏᴡ ʏᴏᴜ ʜᴀᴠᴇ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ꜰᴏʀ ɴᴇxᴛ <code>{}</code></b>"""

    THIRDT_VERIFICATION_TEXT = """<b>👋 ʜᴇʏ {},
    
📌 <u>ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴠᴇʀɪꜰɪᴇᴅ ᴛᴏᴅᴀʏ, ᴛᴀᴘ ᴏɴ ᴛʜᴇ ᴠᴇʀɪꜰʏ ʟɪɴᴋ & ɢᴇᴛ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ꜰᴏʀ ɴᴇxᴛ ꜰᴜʟʟ ᴅᴀʏ.</u>

#ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ:- 3/3

ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴅɪʀᴇᴄᴛ ꜰɪʟᴇs ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ᴛᴀᴋᴇ ᴘʀᴇᴍɪᴜᴍ sᴇʀᴠɪᴄᴇ (ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪꜰʏ)</b>"""

    THIRDT_VERIFY_COMPLETE_TEXT= """<b>👋 ʜᴇʏ {},
    
ʏᴏᴜ ʜᴀᴠᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴛʜᴇ 3rd ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ✓

ɴᴏᴡ ʏᴏᴜ ʜᴀᴠᴇ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ꜰᴏʀ ɴᴇxᴛ ꜰᴜʟʟ ᴅᴀʏ </b>"""

    VERIFIED_LOG_TEXT = """<b><u>☄ ᴜsᴇʀ ᴠᴇʀɪꜰɪᴇᴅ sᴜᴄᴄᴇssꜰᴜʟʟʏ ☄</u>

⚡️ ɴᴀᴍᴇ:- {} [ <code>{}</code> ] 
📆 ᴅᴀᴛᴇ:- <code>{} </code></b>

#verified_{}_completed"""


    MOVIES_UPDATE_TXT = """<b>#𝑵𝒆𝒘_𝑭𝒊𝒍𝒆_𝑨𝒅𝒅𝒆𝒅 ✅
🍿 **Titre** : {title}  
🎃 **Genres** : {genres}  
📆 **Année** : {year}  
⭐️ **Note** : {rating} / 10
</b>"""

    PREPLANS_TXT = """<b>👋 ʜᴇʏ {},

<blockquote>🎁 ᴘʀᴇᴍɪᴜᴍ ғᴇᴀᴛᴜʀᴇ ʙᴇɴɪꜰɪᴛꜱ:</blockquote>

❏ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴏᴘᴇɴ ʟɪɴᴋꜱ
❏ ɢᴇᴛ ᴅɪʀᴇᴄᴛ ғɪʟᴇs   
❏ ᴀᴅ-ғʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ 
❏ ʜɪɢʜ-sᴘᴇᴇᴅ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ                         
❏ ᴍᴜʟᴛɪ-ᴘʟᴀʏᴇʀ sᴛʀᴇᴀᴍɪɴɢ ʟɪɴᴋs                           
❏ ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴏᴠɪᴇs ᴀɴᴅ sᴇʀɪᴇs                                                                        
❏ ꜰᴜʟʟ ᴀᴅᴍɪɴ sᴜᴘᴘᴏʀᴛ                              
❏ ʀᴇǫᴜᴇsᴛ ᴡɪʟʟ ʙᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ɪɴ 𝟷ʜ [ ɪꜰ ᴀᴠᴀɪʟᴀʙʟᴇ ]

⛽️ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ: /myplan
</b>"""    

    PREPLANSS_TXT = """<b>👋 ʜᴇʏ {}
    
<blockquote>🎁 ᴘʀᴇᴍɪᴜᴍ ғᴇᴀᴛᴜʀᴇ ʙᴇɴɪꜰɪᴛꜱ:</blockquote>

❏ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴏᴘᴇɴ ʟɪɴᴋꜱ
❏ ɢᴇᴛ ᴅɪʀᴇᴄᴛ ғɪʟᴇs   
❏ ᴀᴅ-ғʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ 
❏ ʜɪɢʜ-sᴘᴇᴇᴅ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ                         
❏ ᴍᴜʟᴛɪ-ᴘʟᴀʏᴇʀ sᴛʀᴇᴀᴍɪɴɢ ʟɪɴᴋs                           
❏ ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴏᴠɪᴇs ᴀɴᴅ sᴇʀɪᴇs                                                                        
❏ ꜰᴜʟʟ ᴀᴅᴍɪɴ sᴜᴘᴘᴏʀᴛ                              
❏ ʀᴇǫᴜᴇsᴛ ᴡɪʟʟ ʙᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ɪɴ 𝟷ʜ [ ɪꜰ ᴀᴠᴀɪʟᴀʙʟᴇ ]

⛽️ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ: /myplan
</b>"""

    OTHER_TXT = """<b>👋 Hey {},

🎁 <u>Autre plan</u>  
⏰ Jours personnalisés  
💸 Selon les jours que vous choisissez  

🏆 Si vous voulez un nouveau plan en dehors de celui proposé, vous pouvez parler à notre <a href='https://t.me/Kingcey'>propriétaire</a> directement en cliquant sur le bouton de contact ci-dessous.

👨‍💻 Contactez le propriétaire pour obtenir votre autre plan.

➛ Utilisez /plan pour voir tous nos plans en une fois.  
➛ Vérifiez votre plan actif en utilisant : /myplan</b>"""

    FREE_TXT = """<b>👋 ʜᴇʏ {}
    
<blockquote>🎖️ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʀᴇᴍɪᴜᴍ ᴘʟᴀɴꜱ :</blockquote>

 ❏ 𝟶𝟷𝟻₹    ➠    𝟶𝟷 ᴡᴇᴇᴋꜱ
 ❏ 𝟶𝟹𝟿₹    ➠    𝟶𝟷 ᴍᴏɴᴛʜ
 ❏ 𝟶𝟽𝟻₹    ➠    𝟶𝟸 ᴍᴏɴᴛʜ
 ❏ 𝟷𝟷𝟶₹    ➠    𝟶𝟹 ᴍᴏɴᴛʜ
 ❏ 𝟷𝟿𝟿₹    ➠    𝟶𝟼 ᴍᴏɴᴛʜ
 ❏ 𝟹𝟼𝟶₹    ➠    𝟷𝟸 ᴍᴏɴᴛʜ

🆔 ᴜᴘɪ ɪᴅ ➩ <code>jishan@fam</code> [ᴛᴀᴘ ᴛᴏ ᴄᴏᴘʏ]
 
⛽️ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ: /myplan

🏷️ <a href='https://t.me/jisshu_Premium_proof'>ᴘʀᴇᴍɪᴜᴍ ᴘʀᴏᴏꜰ</a>

‼️ ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ.
‼️ ɢɪᴠᴇ ᴜꜱ ꜱᴏᴍᴇᴛɪᴍᴇ ᴛᴏ ᴀᴅᴅ ʏᴏᴜ ɪɴ ᴘʀᴇᴍɪᴜᴍ ʟɪꜱᴛ.
</b>"""

    ADMIN_CMD_TXT = """<b><blockquote>
-------------Utilisateur Premium------------
➩ /add_premium {user ID} {Times} - Ajouter un utilisateur premium  
➩ /remove_premium {user ID} - Supprimer un utilisateur premium  
➩ /add_redeem - Générer un code de rachat  
➩ /premium_users - Lister tous les utilisateurs premium  
➩ /refresh - Rafraîchir l'essai gratuit pour les utilisateurs  

-------------Canal de Mise à Jour----------
➩ /set_muc {channel ID} - Définir le canal de mise à jour des films  

--------------Recherche PM--------------
➩ /pm_search_on - Activer la recherche PM  
➩ /pm_search_off - Désactiver la recherche PM  

--------------Vérifier l'ID--------------
➩ /verify_id - Générer un ID de vérification uniquement pour usage en groupe  

--------------Configurer les Annonces----------------
➩ /set_ads {ads name}}#{Times}#{photo URL} - <a href="https://t.me/Jisshu_developer/11">Expliquer</a>  
➩ /del_ads - Supprimer les annonces  

-------------Tendances du Moment------------
➩ /setlist {Mirzapur, Money Heist} - <a href=https://t.me/Jisshu_developer/10>Expliquer</a>  
➩ /clearlist - Effacer toutes les listes
</blockquote></b>"""

    ADMIN_CMD_TXT2 = """<b><blockquote>
--------------Fichier d'Index--------------
➩ /index - Indexer tous les fichiers  

--------------Quitter le Lien--------------
➩ /leave {group ID} - Quitter le groupe spécifié  

-------------Envoyer un Message-------------
➩ /send {user-name} - Utilisez cette commande en réponse à tout message  

----------------Bannir un Utilisateur---------------
➩ /ban {user-name} - Bannir l'utilisateur  
➩ /unban {user-name} - Débannir l'utilisateur  

--------------Diffusion--------------
➩ /broadcast - Diffuser un message à tous les utilisateurs  
➩ /grp_broadcast - Diffuser un message à tous les groupes connectés

</blockquote></b>"""
    
    GROUP_TEXT = """<b><blockquote>
--------------Configurer la Vérification-------------
/set_verify {{website link}} {{website api}}  
/set_verify_2 {{website link}} {{website api}}  
/set_verify_3 {{website link}} {{website api}}  

-------------Configurer le Temps de Vérification-----------
/set_time_2 {{seconds}} Définir le temps de vérification secondaire  
/set_time_3 {{seconds}} Définir le temps de vérification tertiaire  

--------------Vérification Activée/Désactivée------------
/verifyoff {{verify.off code}} - désactiver la vérification <a href="https://t.me/Kingcey">Contacter</a> l'administrateur du bot pour un code de désactivation de vérification  
/verifyon - activer la vérification  

------------Configurer la Légende du Fichier-----------
/set_caption - définir une légende personnalisée pour le fichier  

-----------Configurer le Modèle IMDb-----------
/set_template - définir le modèle IMDb <a href="https://t.me/Jisshu_developer/8">Exemple</a>  

--------------Configurer le Tutoriel-------------
/set_tutorial - définir le tutoriel de vérification  

-------------Configurer le Canal de Log-----------
--> Ajouter le canal de log avec ce format et assurez-vous que le bot est administrateur dans votre canal de log 👇  
/set_log {{log channel id}}  

---------------------------------------  
Vous pouvez vérifier tous les détails par la commande /details
</blockquote>
Aᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴍᴀᴋᴇ ᴍᴇ ᴀᴅᴍɪɴ ᴀɴᴅ ᴜsᴇ ᴀʟʟ ғᴇᴀᴛᴜʀᴇs😇</b>"""

    SOURCE_TXT = """<b>
NOTE :  
- Code source ici ◉› :<blockquote><a href="https://t.me/botzflix">Frids</a></blockquote>  

Développeur : @Kingcey
</b>""" 
    GROUP_C_TEXT = """<b><blockquote>
 --------------Set Verify-------------
/set_verify {website link} {website api}
/set_verify_2 {website link} {website api}
/set_verify_3 {website link} {website api}
-------------Set Verify Time-----------
/set_time_2 {seconds} Sᴇᴛ ᴛʜᴇ sᴇᴄᴏɴᴅ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ ᴛɪᴍᴇ
/set_time_3 {seconds} Sᴇᴛ ᴛʜᴇ ᴛʜɪʀᴅ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ ᴛɪᴍᴇ
--------------Verify On Off------------
/verifyoff {verify.off code} - off verification <a href="https://t.me/IM_JISSHU">Cᴏɴᴛᴀᴄᴛ</a> ᴛʜᴇ ʙᴏᴛ ᴀᴅᴍɪɴ ғᴏʀ ᴀ ᴠᴇʀɪғʏ.ᴏғғ ᴄᴏᴅᴇ
/verifyon - on verification 
------------Set File Caption-----------
/set_caption - set coustom file caption 
-----------Set Imdb Template-----------
/set_template - set IMDb template <a href="https://t.me/Jisshu_developer/8">Example</a>
--------------Set Tutorial-------------
/set_tutorial {tutorial link} - set 1 verification tutorial 
/set_tutorial_2 {tutorial link} - set 2 verification tutorial 
/set_tutorial_3 {tutorial link} - set 3 verification tutorial 
-------------Set Log Channel-----------
--> ᴀᴅᴅ ʟᴏɢ ᴄʜᴀɴɴᴇʟ ʙʏ ᴛʜɪs ꜰᴏʀᴍᴀᴛ & ᴍᴀᴋᴇ sᴜʀᴇ ʙᴏᴛ ɪs ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ʟᴏɢ ᴄʜᴀɴɴᴇʟ 👇

/set_log {log channel id}
---------------------------------------
ʏᴏᴜ ᴄᴀɴ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀʟʟ ᴅᴇᴛᴀɪʟs 
ʙʏ /details ᴄᴏᴍᴍᴀɴᴅ
</blockquote>
Iғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ᴅᴏᴜʙᴛs ᴘʟᴇᴀsᴇ <a href="https://t.me/IM_JISSHU">ᴄᴏɴᴛᴀᴄᴛ</a> ᴍʏ <a href="https://t.me/IM_JISSHU">ᴀᴅᴍɪɴ</a></b>"""
