# Kanzi Framework 4.1.0 RAG/VDB 最適化パイプライン構築およびプロセス記録

---

## データ前処理手法


| # | 最適化手法 | 実装内容と詳細仕様 |
|---|---|---|
| **[A]** | **ノイズフォルダ・ページの除外** | 技術QAに不要な法的テキスト (`licenses/` 694KB)、旧バージョン情報 (`release-notes/kanzi-3.0/` 88ファイル)、本文が200文字未満のナビゲーション用スタブページ (`*.md`) を自動削除。 |
| **[B]** | **絶対URLリンクの整形** | Sphinx出力特有の冗長な `[https://x.com](https://x.com)` 形式をシンプルな `https://x.com` に統一しトークン消費を抑圧。 |
| **[C]** | **H2/H3セマンティックチャンク分割** | ファイル単位ではなく、ドキュメントの節・項 (`H1 > H2 > H3`) の境界を検出して意味単位でスライス。単語の分断を防止。 |
| **[D]** | **VDBメタデータスキーマ設計** | 各チャンクに `source_url`, `local_path`, `page_title`, `section_path`, `chunk_type`, `code_lang`, `hash` などの高度なメタデータを自動付与。 |
| **[E]** | **コードブロック分離とタグ付け** | テキスト解説（`prose`）とコードサンプル（`code`: C++, Lua, Java等）を自動判定し、`chunk_type: "code"` メタデータと `code_lang` 情報を付与。 |
| **[F]** | **重複コンテンツの排除 (Dedup)** | 各チャンクのコンテンツから SHA-256 ハッシュ値を算出し、ハブページ等での重複テキストを100%検出・一元化排除。 |
| **[G]** | **チャンクサイズ & Overlap 設定** | 1チャンクあたり目標文字数を **500〜800文字**（段落境界を優先）に設定し、オーバーラップを設けて文章のつながりを維持。 |
| **[H]** | **VDB Ready データセットの構築** | Qdrant / ChromaDB / Pinecone 等に即座にバッチ投入可能な一括JSONデータセット `kanzi_rag_chunks.json.gz` (5.29MB 圧縮版 / 106.54MB 解凍版) を自動生成。 |
| **[I]** | **Contextual Retrieval (文脈付与)** | Anthropic推奨のチャンキング戦略。各チャンク本文の先頭に `[Document Context: Title > Section]` を自動合成し、ベクトル類似度検索の失敗率を激減させる。 |
| **[J]** | **Parent-Document Retrieval (親検索)** | 小さな子チャンク (200-250文字) で高精度ベクトル検索を行い、ヒット時に `metadata.parent_content` (1,500文字の親文脈) をLLMへ渡す二重コンテキスト設計。 |
| **[K]** | **マークダウン表の平坦化 (Table Flattening)** | 2次元のMarkdown表構造を `Key: Value` 形式の自然言語行リストへ自動変換し、ベクトル検索における表データの構造・文脈認識精度を大幅向上。 |
| **[L]** | **予想質問のメタデータ化 (Hypothetical Questions)** | LLMを用いて各チャンクに対して「ユーザーが探しそうな質問文」を2〜3件自動生成し、チャンクのメタデータ/埋め込み対象に加える。 |



```mermaid
sequenceDiagram
    autonumber
    actor User as User / Admin
    participant Scraper as scrape_kanzi.py
    participant Web as docs.kanzi.com
    participant Notebook as build_vdb_dataset.ipynb
    participant Storage as Local Storage (kanzi_docs)
    participant VectorDB as Vector Database (Chroma/Qdrant)

    Note over User, VectorDB: Phase 1: Web Scraping & HTML to Markdown Conversion
    User->>Scraper: Execute Scraping
    Scraper->>Web: Fetch HTML Pages (HTTP GET)
    Web-->>Scraper: Return HTML Content
    Scraper->>Storage: Save converted Markdown (*.md)

    Note over User, VectorDB: Phase 2: Integrated Cleaning & Semantic Chunking (Jupyter Notebook)
    User->>Notebook: Run All-in-One Notebook
    Notebook->>Storage: Delete Noise (licenses/, release-notes/kanzi-3.0/, <200 char stubs)
    Notebook->>Storage: Apply 11-Rule Markdown Text Cleaning
    Notebook->>Notebook: Parse Frontmatter & Split H2/H3 Sections
    Notebook->>Notebook: Separate Code vs Prose & Prepend Context Headers
    Notebook->>Notebook: Link Parent Content (Small-to-Big Strategy) & Deduplicate SHA-256
    Notebook->>Storage: Export kanzi_rag_chunks.json.gz (5.29 MB)

    Note over User, VectorDB: Phase 3: Vector Database Indexing
    User->>VectorDB: Ingest kanzi_rag_chunks.json.gz
    VectorDB->>VectorDB: Compute Embeddings & Create Index
    VectorDB-->>User: RAG Pipeline Complete & Ready for QA Search
```


---


