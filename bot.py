{ 
   "name": "TikTok Bot", 
   "description": "بوت تيليجرام لتحميل الفيديوهات او المقاطع الصوتية من التيكتوك.", 
   "keywords": [ 
     "telegram", 
     "تيكتوك", 
     "video", 
     "tiktok" 
   ], 
   "success_url": "https://T.me/TEKSAS1_BOT", 
   "website": "https://github.com/TEKSAS1_BOT", 
   "repository": "https://github.com/TEKSAS1_BOT", 
   "env": { 
     "BOT_TOKEN": { 
       "description": "ضع هنا توكن البوت احصل عليه من هنا  https://t.me/botfather", 
       "value": "" 
     }, 
     "APP_ID": { 
       "description": "ضع هنا الايبب ايدي احصل عليه من هنا https://my.telegram.org", 
       "value": "" 
     }, 
     "API_HASH": { 
       "description": "ضع هنا الايبي هاش احصل عليه من هنا https://my.telegram.org", 
       "value": "" 
     } 
   }, 
   "addons": [ 
   ], 
   "buildpacks": [{ 
     "url": "https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest" 
   }, { 
     "url": "heroku/python" 
   }], 
   "stack": "heroku-20", 
   "formation": { 
     "worker": { 
       "quantity": 1, 
       "size": "free" 
     } 
   } 
 }