<<<<<<< HEAD
# colorfour_fe

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
=======
# 你的專屬穿搭造型師 ColorFour！
### 功能
1. 色彩分析（color_analyzer）
   - 使用者上傳臉部色彩圖片後，系統依照照片中的膚色、髮色與瞳色進行判斷，提供個人化四季型色彩分析結果 。
2. 智慧衣櫃（wardrobe_manager）
   - 服飾上傳與辨識：使用者上傳服飾照片後，系統自動偵測服裝種類並建立個人服飾資料庫。
   - 服飾管理：透過搜尋、篩選和排序功能，使用者可以方便找到需要的服飾。
   - 最愛穿搭：使用者可在衣櫃中自由搭配喜歡的單品組成一套穿搭。
3. 穿搭推薦（outfit_recommender）
   - 智慧推薦：系統根據位置、天氣、個人色彩分析結果，結合智慧衣櫃資料庫提供每日智慧推薦。
   - 偏好推薦：根據當天的情選擇自己想要穿的服飾類型或排除不想穿的服飾類型，提供相應的推薦。
4. 採購建議（shopping_advisor）
   - 當使用者在購物時覺得某件想買的服飾似曾相識，可透過系統與現有的資料做比對，估算出服飾重複率和適合程度，減少重複購買或衝動購物。
   - 結合LineBot聊天機器人，提供即時的建議。
5. 社群互動（social_platform）
   - 單品分享：使用者在上傳服飾單品到資料庫的時候，可以選擇分享到社群平台，
   - 穿搭交流：透過平台分享自己的最愛穿搭，搜尋並瀏覽其他使用者的穿著搭配，並透過點讚、留言、分享功能與其他使用者互動與交流。 
6. 穿搭日程（outfit_scheduler）
   - 快速查詢：透過LineBot點選穿搭日程，即可快速查詢指定日期有沒有穿搭日程安排。若有安排，會回傳穿搭服裝圖片以及日程描述。若無安排，則詢問是否要新增一項穿搭日程。
   - 新增活動：透過LineBot中新增穿搭日程安排，輸入地點、時間與活動目的，再選擇最愛穿搭。系統會自動新增至Google日曆。
   - 及時提醒：LineBot聊天機器人會在設定的時間提醒使用者當天的穿搭安排。使用者可以利用穿搭推薦與最愛穿搭功能，將當天需要的穿衣搭配登錄在穿搭日程中，確保每次出門前都做好充分的準備。
7. LineBot互動（line）
   - 透過圖文選單快速連結各功能網頁以及快速查詢等功能。
---
## ColorFour專案環境設定
- 專案系統環境
  - 前端：Vue, Bootstrap
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

1. 安裝 Anaconda3 ， 開啟 Anaconda Prompt
2. 建立後端虛擬環境
    
    ```bash
    建立：conda create --name colorfour python=3.11
    啟動：conda activate colorfour
    ```
    
    成功的話，會長這樣
    
    (base) →  (colorfour) <你的檔案路徑>
    

> 建立成功之後，之後的開啟方式如下：
> 
1. 開啟Anaconda prompt
2. 輸入：`conda activate colorfour`
3. 輸入：`cd ColorFour/colorfour_be`

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
        
4. 都有安裝的話，就安裝以下套件（bulma 是 vue 自己的 css framework）
    
    ```bash
    npm install axios
    npm install bulma
    npm install bulma-toast
    npm install bootstrap
    ```
    
5. 切換到前端專案目錄啟動server
    
    ```bash
    cd colorfour/colorfour_fe
    npm run serve
    ```
    
    
6. 關閉server：快速鍵ctrl + c

> 成功之後，之後的開啟方式如下：
> 
- 在專案前端根目錄開啟cmd，然後執行 `npm run serve`

---

### 後端設定（use Anaconda Prompt）

1. Fork 專案（請找威宏的 Fork 教學）
2. 開啟虛擬環境（conda activate colorfour）
3. 安裝必要套件，讓大家的開發環境與版本一樣
    
    ```bash
    切換到專案根目錄：cd path_to_ColorFour
    安裝套件： pip install -r requirements.txt
    ```
    
4. 設定環境變數（.env）： 在專案根目錄建立「.env」檔案    
    
5. 建立資料庫
    1. 請打開 MySQL Workbench
    2. 打開新的 SQL file，然後複製 code
    3. 點擊閃電圖示執行。如果跳出錯誤，把 line 2「CREATE USER」 → 「ALTER USER」        
    4. 點選右上角刷新，應該可以看到colorfour資料庫被建立了。
        
6. 遷移資料庫（用 Anaconda prompt）
    
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
    
    回到MySQL，再刷新一次，應該可以看到Colorfour資料夾多了不少 Table。
    
7. 啟動伺服器
    
    ```css
    切換目錄：cd colorfour/colorfour_be
    啟動Server：python manage.py runserver
    ```
    
8. 網址列加上「/api」
    
    剛打開 http 404 是正常的
    網址改成：「http://127.0.0.1:8000/api」
    成功的話，會長這樣。後端環境建置到此結束。
    
9. 關閉 Server：快速鍵ctrl + c

> 成功之後，之後的開啟方式如下：
> 
1. 開啟Anaconda Prompt，啟動虛擬環境
2. `cd ColorFour/colorfour_be`
3.  `python manage.py runserver`

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

> 成功之後，之後的開啟方式如下：
> 
1. 開啟Ngrok.exe
2. `ngrok http --domain="url" 8000`
>>>>>>> upstream/main
