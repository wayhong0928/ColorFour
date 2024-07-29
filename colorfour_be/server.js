const express = require('express');
const { OAuth2Client } = require('google-auth-library');
const jwt = require('jsonwebtoken');
require('dotenv').config();
const cors = require('cors');

const app = express();
const port = 8000;

const client = new OAuth2Client(
  process.env.GOOGLE_CLIENT_ID,
  process.env.GOOGLE_SECRET_KEY,
  `${process.env.HOST}/accounts/google/login/callback/`
);

app.use(express.json());
app.use(cors());

// 平台處理 Google OAuth 授權，會取得GOOGLE提供的token
app.get('/accounts/google/login/callback', async (req, res) => {
  const { code } = req.query;

  try {
    const { tokens } = await client.getToken(code);
    client.setCredentials(tokens);

    const userInfo = await client.request({
      url: 'https://www.googleapis.com/oauth2/v3/userinfo', //取得個資
    });

    const token = jwt.sign(userInfo.data, process.env.JWT_SECRET); //JWT: 用戶儲存的token
    res.cookie('token', token, { httpOnly: true });

    res.redirect('http://localhost:8080/?loginResult=success'); //轉址至登入成功畫面
  } catch (error) {
    console.error('Error during token exchange or user info retrieval:', error.message);
    if (error.response) {
      console.error('Error response data:', error.response.data);
    }
    res.redirect('http://localhost:8080/login?loginResult=failure');
  }
});

// 啟動伺服器
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
