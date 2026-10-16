def list_items(items, sort=False):
    """やることの一覧を返す。sort=True なら名前の順に並べる。（検証用）"""
    return sorted(items) if sort else list(items)
