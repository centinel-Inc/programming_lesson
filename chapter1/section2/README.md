# 第 2 節 HTML の基礎を学ぼう

## 目的

第 4 節・第 5 節の動画を理解しやすくするために HTML について基本的な知識をインプットします。

## 学び方

聞き流し、時々気になったところで手を動かしながら軽く理解することを心がけてください。
覚える必要は全くありません。
実際に利用するときになった際、調べることのできる最低限のとっかかりを作ることが重要です。

## HTML とは

ハイパーテキスト・マークアップ・ランゲージ（Hyper Text Markup Language）の略で、コンピュータが理解できる文字で指示を出すことにより Web ページを表現できます。

## HTML の書き方

```html
<!DOCTYPE html>
<html lang="ja">
  <head>
    <meta charset="UTF-8" />
    <title>chapter1-section2</title>
  </head>
  <body>
    <h1>見出しです。1から</h1>
    <h6>6まであり、数字が小さいほど文字が大きくなります。</h6>

    <a href="https://centinel.jp/" target="_blank" rel="noopener"
      >よくみるリンクです。
    </a>

    <p>
      target=_blankと指定することで、クリックした際に新しいタブでリンク先を開くことができます。
    </p>
    <p>
      もしtargetに_blankを使用する際は、rel=noopenerをつけることでセキュリティを向上させることができるのでおすすめです
    </p>

    <button>ボタン</button>

    <button href="https://centinel.jp/" target="_blank" rel="noopener">
      リンク付きボタン
    </button>

    <img src="https://centinel.jp/images/logo.png" alt="centiロゴ" />

    <div></div>

    <div>
      <h1>
        divタグの説明
        <p>divタグは単体で利用することは少なく</p>
        <p>CSSと連携して使用することが多いです。</p>
      </h1>
    </div>

    <table>
      <tr>
        <th>名前</th>
        <th>好きなプログラミング言語</th>
        <th>プログラミング歴</th>
      </tr>
      <tr>
        <td>テストA</td>
        <td>Swift</td>
        <td>3</td>
      </tr>
      <tr>
        <td>テストB</td>
        <td>TypeScript</td>
        <td>5</td>
      </tr>
    </table>
  </body>
</html>
```
