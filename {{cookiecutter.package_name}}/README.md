# {{ cookiecutter.package_name }}

## セットアップ

```bash
uv sync
uv run python manage.py migrate
uv run python manage.py runserver
```

## 環境変数

| 変数名 | 説明 | 既定値 |
| --- | --- | --- |
| `DJANGO_SECRET_KEY` | シークレットキー（本番では必ず設定） | 生成時のランダム値 |
| `DJANGO_DEBUG` | デバッグモード | `True` |
| `DJANGO_ALLOWED_HOSTS` | 許可するホスト（カンマ区切り） | なし |

## 静的ファイル

本番では `collectstatic` を実行し、WhiteNoise で配信します。

```bash
uv run python manage.py collectstatic
```

## SBOM

[uv-sbom](https://pypi.org/project/uv-sbom/) が必要です。

```bat
build-sbom.bat
```
