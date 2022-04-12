# “神圣跨性别帝国”护照生成器

> 警告：该帝国为臆造，仅供娱乐。  
WARNING: This empire is based on imagination and for entertainment only.

## 什么是神圣跨性别帝国？ What's the Holy Trans. Empire?

- 神圣：指性别平等权益神圣不可侵犯
- 跨性别：字面意思
- 帝国：基于区块链，人人皆可成为皇帝


+ Holy -- The sacredness and inviolability of Gender-equity
+ Trans. -- Transgender.
+ Empire -- Everyone can be the Emperor by taking advantage of Blockchain.


## Passport / 护照

![EXAMPLE](docs/example.jpg)

### Generate 生成

原项目地址：<https://github.com/saeziae/holy_trans_passport>

1. 首先你要有一个以太坊地址。  
  You MUST have your own Ethereum wallet.
1. 对于Windows用户，应先安装 [Microsoft VC++ Build Tool](https://visualstudio.microsoft.com/visual-cpp-build-tools/) 14.0 或以上。包括：MSBuild 工具，以及“使用 C++ 的桌面开发”。  
  For Windows, [Microsoft VC++ Build Tool](https://visualstudio.microsoft.com/visual-cpp-build-tools/) 14.0 or above MUST be installed. For my instance,included: Build tools core features; MSVC toolset C++ 2019 v142; Visual C++ 2019 Redistributable; Windows 10 SDK.
1. 安装以下依赖包：`pip install pillow opencv-python web3 numpy qrcode pdf417gen`  
  Install the dependencies above.
1. 修改 `info.json` 内的个人信息。  
  Fill your personal info in `info.json`:
   - `name` -- 全名 / Full name
   - `birth` -- 生日 / Date of birth
   - `place` -- 出生或重生地点 / Place of Birth or Rebirth
   - `pronouns` -- 偏好的代词 / Preferred pronouns, see the example above
   - `hash` -- 以太坊钱包地址 / Address of Ethereum wallet
1. 替换照片 `photo.png`。建议尺寸：320 x 480。  
  Replace `photo.png` with others you prefer. Recommended size: 320 x 480.
1. 生成：`python generate_passport_and_pic.py info.json photo.png`  
  Generate the passport using the command above.
1. 验证护照真伪：`python view_passport.py 编号.tgdpassport`，真的才会有信息。  
  If the check for the passport is needed, run `python view_passport.py <Passport_Number>.tgdpassport`.

