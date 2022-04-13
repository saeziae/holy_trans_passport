## 什么是神圣跨性别帝国？ What's the Holy Trans Empire?

- 神圣：指性别平等权益神圣不可侵犯
- 跨性别：字面意思
- 帝国：基于区块链，人人都是皇帝

- Holy -- The sacredness and inviolability of Gender-equity
- Trans -- Transgender.
- Empire -- Everyone can be the Emperor by taking advantage of Blockchain.

## Passport / 护照

![EXAMPLE](example.jpg)

### Generate 生成

项目地址：<https://github.com/saeziae/holy_trans_passport>

1. 首先你要有一个以太坊地址，并准备好私钥。
   You MUST have your own Ethereum wallet, and prepare your private key.
1. 安装以下依赖包：`pip3 install -r requirements.txt`  
   Install the dependencies above.
1. 修改 `info.json` 内的个人信息。  
   Fill your personal info in `info.json`:
   - `name` -- 全名 / Full name
   - `birth` -- 生日 / Date of birth
   - `place` -- 出生或重生地点 / Place of Birth or Rebirth
   - `pronouns` -- 偏好的代词 / Preferred pronouns
     推荐使用 / recommended:
     - ELLE/He
     - ELLA/She
     - ILLVD/They
   - `hash` -- 以太坊钱包地址 / Address of Ethereum wallet
1. 替换照片 `photo.png`。建议尺寸：2:3 比例，128 x 192 或者 320 x 480  
   Replace `photo.png` with others you prefer. Recommended size: 2:3 ratio 128 x 192 or 320 x 480
1. 生成：`python generate_passport_and_pic.py info.json photo.png`  
   Generate the passport using the command above.
1. 验证护照真伪：`python view_passport.py 编号.tgdpassport`，真的才会有信息。  
   If the check for the passport is needed, run `python view_passport.py <Passport_Number>.tgdpassport`.
