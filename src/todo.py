def list_items(items, sort=False, keyword=None):
    """やることの一覧を返す。sort=True なら名前の順に並べる。keyword があれば、含む項目だけ返す。"""
    result = list(items)
    if keyword is not None:
        result = [item for item in result if keyword in item]
    return sorted(result) if sort else result
