# 你的專屬穿搭造型師 ColorFour！
>[!NOTE]
>以線上衣櫃資料庫為核心概念，結合六大功能打造服裝管理的全方位解決方案，解決「今天要穿什麼？」的問題。

戰績：
1. 系上專題初賽 - 第二名
2. 創天下競賽 - 入圍決賽
3. 資訊服務創新競賽 - 入圍決賽
4. 系上專題複賽 - 第一名
---
### 系統功能
1. 色彩分析（color_analyzer）
   - 使用者上傳臉部色彩圖片後，系統依照照片中的膚色、髮色與瞳色進行判斷，提供個人化四季型色彩分析結果 。
2. 智慧衣櫃（wardrobe_manager）
   - 服飾上傳與辨識：使用者上傳服飾照片後，系統自動偵測服裝種類並建立個人服飾資料庫。
   - 服飾管理：透過搜尋、篩選和排序功能，使用者可以方便找到需要的服飾。
   - 最愛穿搭：使用者可在衣櫃中自由搭配喜歡的單品組成一套穿搭。
3. 穿搭推薦（outfit_recommender）
   - 智慧推薦：根據位置、天氣、個人色彩分析結果，結合智慧衣櫃資料庫提供每日智慧推薦。
   - 偏好推薦：根據當天的情選擇自己想要穿的服飾類型或排除不想穿的服飾類型，提供相應的推薦。
4. 穿搭日程（outfit_scheduler）
   - 快速查詢：透過LineBot點選穿搭日程，即可快速查詢指定日期有沒有穿搭日程安排。若有安排，會回傳穿搭服裝圖片以及日程描述。若無安排，則詢問是否要新增一項穿搭日程。
   - 新增活動：透過LineBot中新增穿搭日程安排，輸入地點、時間與活動目的，再選擇最愛穿搭。系統會自動新增至Google日曆。
   - 及時提醒：LineBot聊天機器人會在設定的時間提醒使用者當天的穿搭安排。使用者可以利用穿搭推薦與最愛穿搭功能，將當天需要的穿衣搭配登錄在穿搭日程中，確保每次出門前都做好充分的準備。
5. 採購建議（shopping_advisor）
   - 當使用者在購物時覺得某件想買的服飾似曾相識，可透過系統與現有的資料做比對，估算出服飾重複率和適合程度，減少重複購買或衝動購物。
   - 結合LineBot聊天機器人，提供即時的建議。
6. 社群互動（social_platform）
   - 單品分享：使用者在上傳服飾單品到資料庫的時候，可以選擇分享到社群平台，
   - 穿搭交流：透過平台分享自己的最愛穿搭，搜尋並瀏覽其他使用者的穿著搭配，並透過點讚、留言、分享功能與其他使用者互動與交流。 
7. LineBot互動（line）
   - 透過圖文選單快速連結各功能網頁以及快速查詢等功能。
---
## ColorFour專案環境設定
- 專案系統環境
  - 前端：Vue3 CLI, Bootstrap
  - 後端：Anaconda3, python 3.11, Django 4.2, LineBot, MySQL
  - 第三方服務：Google日曆API、中央氣象署API
  - 其他服務：ngrok
- 目次
    - 建立虛擬環境
    - 設定前端環境
    - 設定後端環境
    - 設定 Ngrok
- 需要準備：Git&Github、VScode、Anaconda Prompt、cmd、MySQL Workbench，耐心。

---

### 虛擬環境建立

1. 建立後端虛擬環境
    
    ```bash
    建立：conda create --name colorfour python=3.11
    啟動：conda activate colorfour
    ```
    
    成功的話，會長這樣
    
    (base) →  (colorfour) <你的檔案路徑>
    

> [!TIP]
> 建立成功之後，之後的開啟方式如下：
> 1. 開啟Anaconda prompt
> 2. `conda activate colorfour`

---

### 前端設定（use commend line）

1. 切換到專案前端根目錄，安裝/檢查 nodeJS、VueCLI版本
    
    ```bash
    cd ColorFour/colorfour_fe
    node -v
    npm -v
    npm install
    npm install -g @vue/cli
    vue --version
    ```
    
2. 如果沒安裝NodeJS、Vue的話，安裝Nodev18.18，安裝完畢之後切換到專案前端根目錄。
    
    - https://nodejs.org/download/release/v18.18.0/
    
    ```python
    檢查node版本：  node -v
    檢查npm版本：   npm -v
    安裝套件：      npm install
    安裝vue：       npm install -g @vue/cli
    檢查Vue版本：   vue --version
    ```
    
    
3. 如果一直不成功又跳error，建議可以刪掉node，裝18.18版本。裝好之後重開cmd檢查版本。
   - 刪除node：打開設定 > 搜尋" 新增或移除程式 “ > 搜尋node > 然後刪除之前的版本
   - 安裝：要裝x86還是x64？去設定找系統資訊 -> 系統類型
   - https://nodejs.org/download/release/v18.18.0/
        
4. 安裝以下套件
    
    ```bash
    npm install axios
    npm install bootstrap
    ```
    
5. 建立 `env` 檔案
   ```bash
    VUE_APP_NGROK_URL=''
    VUE_APP_BACKEND_URL=''

    VUE_APP_LINE_LOGIN_CHANNEL_ID=''
    VUE_APP_LINE_LOGIN_CHANNEL_SECRET=''
    VUE_APP_LINE_LOGIN_CALLBACK=''

    VUE_APP_GOOGLE_CLIENT_ID=''
    VUE_APP_GOOGLE_CLIENT_SECRET=''
    VUE_APP_LOGIN_CALLBACK=''
   ```
6. 啟動前端 `server`
    
    ```bash
    cd colorfour/colorfour_fe
    npm run serve
    ```
    
    
7. 關閉server：快速鍵ctrl + c

>[!TIP]
>1. 成功之後，之後的開啟方式如下：
>2. 在專案前端根目錄開啟 cmd，執行 `npm run serve`

---

### 後端設定（use Anaconda Prompt）

1. Fork 專案
2. 開啟虛擬環境（conda activate colorfour）
3. 安裝必要套件，讓大家的開發環境與版本一樣
    
    ```bash
    切換到專案根目錄：cd path_to_ColorFour
    安裝套件： pip install -r requirements.txt
    ```
    
4. 設定環境變數（.env）： 在後端專案根目錄建立「.env」檔案   
    ```bash
    DJANGO_SECRET_KEY=''

    DATABASE_NAME=''
    DATABASE_USER=''
    DATABASE_PASSWORD=''
    DATABASE_HOST=''
    DATABASE_PORT=''

    FRONTEND_URL=''
    NGROK_URL=''
    LOGIN_CALLBACK_URL=''

    LINE_LOGIN_CHANNEL_ID=''
    LINE_LOGIN_CHANNEL_SECRET=''
    LINE_LOGIN_CALLBACK_URL=''

    LINE_MESSAGING_CHANNEL_ACCESS_TOKEN=''
    LINE_MESSAGING_CHANNEL_SECRET=''

    GOOGLE_CLIENT_ID=''
    GOOGLE_CLIENT_SECRET=''
    GOOGLE_SECRET_KEY=''
    
    ```
       
5. 遷移資料庫（用 Anaconda prompt）   
   1. 請打開 MySQL Workbench，建立資料庫
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
    
    2. 回到MySQL，再刷新一次，應該可以看到 Colorfour 資料庫多了不少 Table。
    3. member_user table > username 欄位改成空值（允許 null ）
    
6. 啟動伺服器
    
    ```bash
    cd colorfour/colorfour_be
    python manage.py runserver
    ```
    
7.  關閉 Server：快速鍵ctrl + c

>[!TIP]
> 1. 成功之後，之後的開啟方式如下：
> 2. 開啟Anaconda Prompt，啟動虛擬環境
> 3. `cd ColorFour/colorfour_be`
> 4. `python manage.py runserver`

---

### 建立 ngrok

1. 下載 ngrok.exe，放到專案後端根目錄（ColorFour/colorfour_be）
2. 到 ngrok 網站登入專題帳號  https://ngrok.com/
3. 到” **Your Authtoken” → Command Line 複製**
4. 打開ngrok，貼上授權（下面的例子是專題帳號的授權）
    
    ```python
    ngrok config add-authtoken "your token"
    ```
    
5. 到 ”**Domains**” → Tunnel ，點開之後複製內容。
    
6. 開啟 ngrok，貼上剛剛複製的內容。
    
    ```python
    ngrok http --domain="url" 8000
    ```
    
7. 打開 Line develops 的 messageAPI，點選 webhook 的驗證
   - 需同時開啟後端 Server 才會生效
8. 關閉 Ngrok：快速鍵ctrl + c

>[!TIP]
> 1. 成功之後，之後的開啟方式如下：
> 2. 開啟Ngrok.exe
> 3. `ngrok http --domain="url" 8000`
