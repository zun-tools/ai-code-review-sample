def list_items(items, sort=False):
    """やることの一覧を返す。sort=True なら名前の順に並べる。"""
    return sorted(items) if sort else list(items)
