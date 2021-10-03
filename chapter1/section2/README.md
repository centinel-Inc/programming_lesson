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

役割を持った「タグ」で要素を囲うように記述していきます。
タグは数が多いため覚える必要はなく、必要になるたびに調べていけば大丈夫です。

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

    <p>ボタンにも同じくリンクを付与することができます。</p>

    <img
      src="https://centinel.jp/images/logo.png"
      alt="centiロゴ"
      width="600px"
      height="300px"
    />

    <p>imgタグは画像を表示することができます。</p>

    <div></div>

    <div>
      <h1>
        divタグの説明
        <p>
          divタグで囲んだ範囲をひとかたまりとして扱うことができるようになるため
        </p>
        <p>CSSを連携して使用することが多いです</p>
        <p>
          CSSというのはHTMLの要素に装飾を加え、見た目を変更することができます。
        </p>
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

### <!DOCTYPE html>

文章の種類が HTML であることを宣言しています。
最初は特に考えずに記述することをおすすめします。

### <html lang="ja">

このタグの中に HTML の要素が入っていることを宣言しています。
最初は特に考えずに記述することをおすすめします。

### <title>chapter1-section2</title>

サイトのタイトルを指定することができます。

## 実際のサイトで HTML をいじって遊ぶ

1. [このサイト](https://centinel.jp/)にアクセスする

### 注意

上記のサイトは我々が運営しているサイトなので今回の作業に用いて問題ありませんが、他のサイトを本作業に用いるのは目的外の利用ですので推奨しません。

2. Chrome の開発者ツールを開く
   Mac: `command + option + i`
   Windows: `control + shift + i`

3. HTML の要素が丸見えになるので、いじって遊ぶ

4. いじるのに飽きたら次の第 3 節を始めてみてください
