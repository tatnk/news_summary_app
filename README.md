# News Summary App

このアプリケーションは、ニュース記事を検索し、その要約を提供するためのものです。Flaskフレームワークを使用して構築されています。
## セットアップ

このアプリケーションを使用するには、OpenAIのAPIキーが必要です。以下の手順に従ってセットアップを行ってください。

1. OpenAIのアカウントを作成し、APIキーを取得します。
    - OpenAIの[公式サイト](https://www.openai.com/)にアクセスし、アカウントを作成します。
    - ダッシュボードからAPIキーを取得します。

2. 環境変数を設定します。`.env`ファイルを作成し、以下の内容を追加します。
    ```
    OPENAI_API_KEY=your_openai_api_key
    ```

## インストール方法

1. リポジトリをクローンします。
    ```bash
    git clone https://github.com/tatnk/news_summary_app.git
    cd news_summary_app
    ```

2. 仮想環境を作成し、アクティブにします。
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Windowsの場合は `venv\Scripts\activate`
    ```

3. 必要なパッケージをインストールします。
    ```bash
    pip install -r requirements.txt
    ```

4. 環境変数を設定します。`.env`ファイルを作成し、以下の内容を追加します。
    ```
    OPENAI_API_KEY=your_openai_api_key
    ```

## 使い方

1. アプリケーションを起動します。
    ```bash
    python run.py
    ```

2. ブラウザで `http://127.0.0.1:5000` にアクセスします。

3. 検索バーにキーワードを入力し、「Search」ボタンをクリックします。

4. 検索結果が表示されます。各記事の「Read Summary」リンクをクリックすると、記事の要約が表示されます。
