class Translation(object):
    START_TEXT = """Hey! This is a simple Telegram All-In-One Bot that has so many function. Click /help button to Know How To Use Me.\n Made with ❤ By @TeleRoidGroup"""
    RENAME_403_ERR = "<b>Sorry. You Are Not Permitted To Rename This File.\nAsk In [Support Group](https://t.me/TeleRoid14)</b>"
    ABS_TEXT = " <b>Please Don't Be Selfish.</b>"
    UPGRADE_TEXT = "<b>This Bot Is Free To Use If U R My  Friend......\n\n@TheTeleRoid</b>"
    FORMAT_SELECTION = "<b>Select The Desired Format:</b> "
    SET_CUSTOM_USERNAME_PASSWORD = """<b>If You Want To Download Premium Videos, Provide In The Following Format:
URL | filename | username | password</b>"""
    NOYES_URL = "<b>This Is Dam Slow Link Bro! I Wont Waste My Time On This. Get Me A Fast Link</b>"
    DOWNLOAD_START = "<b>Downloading Your Files.....📥</b>"
    UPLOAD_START = "<b>Uploading Your Files.....📤</b>"
    RCHD_BOT_API_LIMIT ="<b>Size Greater Than Maximum Allowed Size. Neverthless, Trying To Upload.</b>"
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\n<b>Sorry. But, I Cannot Upload Files Greater Than 2GB Due To Telegram API Limitations.</b>"
    AFTER_SUCCESSFUL_UPLOAD_MSG = "<b>File Uploaded Successfully</b>"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds. \nUploaded in {} seconds."
    NOT_AUTH_USER_TEXT = "You Are Not Authorise To Do This. This Is Only <b>Admin</b> Command"
    NOT_AUTH_USER_TEXT_FILE_SIZE = "Detected File Size: {}. Free Users can only upload: {}\nPlease /upgrade your subscription."
    SAVED_CUSTOM_THUMB_NAIL = "<b>Custom video / file thumbnail saved. This image will be used in the video / file.</b>"
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ <b>Custom thumbnail cleared succesfully."
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media Cleared Succesfully.</b>"
    SAVED_RECVD_DOC_FILE = "<b>Document Downloaded Successfully.</b>"
    CUSTOM_CAPTION_UL_FILE = " <b>Bot Created By \n   👉**@TheTeleRoid**</b>"
    NO_CUSTOM_THUMB_NAIL_FOUND = "<b>No Custom ThumbNail Found .</b>"
    NO_VOID_FORMAT_FOUND = "Can You Check The Url? <b>I Am Unable To Detect Video Format From UrL.</b> If You Think This Could Be A Bug Please Report On https://t.me/TeleRoid14"
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    CURENT_PLAN_DETAILS = """Current plan details
-----------------------------
👤Telegram ID: <code>{}</code>

📝Plan name: 75GB Per Month

🚸Expires on: 10/12/2021

😎If You need Private Bot Please Ch3ck @PayForBotz.
-----------------------------"""
    HELP_USER = """<b>There Are Multiple Things I Can Do:</b>\n\n <b>All Supported Video Formats of [YTDLp]</b>

☞  <b>Upload as file from any Direct link</b>

☞  <b>Convert To Video of TG Media.\nReply /converttovideo to Any Media</b>

☞  <b>ReName Telegram files, with custom thumbnail support.\nReply /rename To File</b>

☞  <b>Get High Speed Direct Download Link Of Any Telegram File.\nReply /getlink To File</b>
-----------------------------

Send /me To Know Your Current Plan Details"""
    REPLY_TO_DOC_GET_LINK = "<b>Reply to a Telegram media to get High Speed Direct Download Link.</b>"
    REPLY_TO_DOC_FOR_C2V = "<b>Reply to a Telegram Media To Convert.\n@TheTeleRoid</b>"
    REPLY_TO_DOC_FOR_SCSS = "<b>Reply to a Telegram Media To Get Screenshots.\n@TheTeleRoid</b>"
    SOURCE = """<b>Hello! You Want to Know More About Me</b>

<em>🤖 My Name : <i>TeleRoid AnyDLBot</i></em>

<em>👨‍💻 Creator : <a href='https://telegram.dog/TheTeleRoid'>This Person</a></em>

<em>🧛‍♂️ Credits : Everyone In This Journey</em>

<em>📝 Language : Python 3.9</em>

<em>📚 Library : Pyrogram Asyncio</em>

<em>🗂 Cloned From : AnyDLBot [Spechide]</em>

<em>🧬 Source Code :  <a href="https://github.com/PredatorHackerzZ/AnyDLBot-2">𝗖𝗹𝗶𝗰𝗸 𝗛𝗲𝗿𝗲</a></em>

<em>📡 Server : <a href='https.heroku.com'>Heroku</a></em>

<b>💡 Build Status : Beta v1</b>"""

    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('⚙Join Updates Channel ⚙ ', url='https://t.me/TeleRoidGroup')
        ],[
        InlineKeyboardButton('🆘 Hᴇʟᴘ', callback_data='help'),
        InlineKeyboardButton('👤 Aʙᴏᴜᴛ', callback_data='about')
        ],[
        InlineKeyboardButton('🔐 Cʟᴏsᴇ', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 ʜᴏᴍᴇ', callback_data='home'),
        InlineKeyboardButton('👤 Aʙᴏᴜᴛ', callback_data='about')
        ],[
        InlineKeyboardButton('🔐 Cʟᴏsᴇ', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 Hᴏᴍᴇ', callback_data='home'),
        InlineKeyboardButton('🆘 Hᴇʟᴘ', callback_data='help')
        ],[
        InlineKeyboardButton('🔐 Cʟᴏsᴇ', callback_data='close')
        ]]
    )
    BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 ʜᴏᴍᴇ', callback_data='home'),
        InlineKeyboardButton('🆘 ʜᴇʟᴘ', callback_data='help')
        ],[
        InlineKeyboardButton('🔐 ᴄʟᴏsᴇ', callback_data='close')
        ]]
    )

    REPLY_TO_DOC_FOR_RENAME_FILE = "<b>Reply to a Telegram Media To /rename With Custom Thumbnail Support.Or Ask In Support Group.</b>"
    AFTER_GET_DL_LINK = "Direct Link <a href='{}'>Generated</a> valid for {} days."
    FF_MPEG_RO_BOT_RE_SURRECT_ED = """Syntax: /trim HH:MM:SS [HH:MM:SS]"""
    FF_MPEG_RO_BOT_STEP_TWO_TO_ONE = "<b>First send /downloadmedia To Any Media So That It Can Be Downloaded To My Local. \nSend /Storageinfo To Know The Media, That Is Currently Downloaded.</b>"
    FF_MPEG_RO_BOT_STOR_AGE_INFO = "Video Duration: {}\nSend /clearffmpegmedia To Delete This Media, From My Storage.\nSend /trim HH:MM:SS [HH:MM:SS] to cu[l]t A Small Photo / Video, From The Above Media."
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "<b>A Saved Media Already Exists. Please Send /Storageinfo To Know The Current Media Details.</b>"
    USER_DELETED_FROM_DB = "User <a href='tg://user?id={}'>{}</a> deleted from DataBase."
    REPLY_TO_DOC_OR_LINK_FOR_RARX_SRT = "<b>Reply to a Telegram media (MKV), to extract embedded streams.</b>"
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "<b>Reply /generatecustomthumbnail to a media album, to generate custom thumbail</b>"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "<b>Media Album Should Contain Only Two Photos. Please Re-send The Media Album, And Then Try Again, Or Send Only Two Photos In An Album.</b>"
    INVALID_UPLOAD_BOT_URL_FORMAT = "<b>URL format is incorrect. make sure your url starts with either http:// or https://. You can set custom file name using the format link | file_name.extension</b>"
    ABUSIVE_USERS = "<b>You are not allowed to use this bot. If you think this is a mistake, please check /me to remove this restriction.</b>"
    FF_MPEG_RO_BOT_AD_VER_TISE_MENT = "Holy Shit!!"
    EXTRACT_ZIP_INTRO_ONE = "Send a compressed file first, Then reply /unzip command to the file."
    EXTRACT_ZIP_INTRO_THREE = "Analyzing received file. ⚠️ This might take some time. Please be patient. "
    UNZIP_SUPPORTED_EXTENSIONS = ("zip", "rar")
    EXTRACT_ZIP_ERRS_OCCURED = "Sorry. Errors occurred while processing compressed file. Please check everything again twice."
    EXTRACT_ZIP_STEP_TWO = """Select file_name to upload from the below options.
You can use /rename command after receiving file to rename it with custom thumbnail support."""
    CANCEL_STR = "Process Cancelled"
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds"
    FREE_USER_LIMIT_Q_SZE = """Cannot Process.
 users only 1 request per 5 minutes.
/upgrade or Try 300 seconds later."""
    SLOW_URL_DECED = "Gosh That Seems To Be A Very Slow URL. Since You Were Screwing My Home, I Am In No Mood To Download This File. Meanwhile, Why Don't You Get Me A Fast URL So That I can Upload To Telegram, Without Me Slowing Down For Other Users."
    IFLONG_FILE_NAME = """File Name limit allowed by Telegram is {alimit} characters.
The given file name has {num} characters.

<b>Essays Not allowed in Telegram file name!</b>
Please short your file name and try again!"""
