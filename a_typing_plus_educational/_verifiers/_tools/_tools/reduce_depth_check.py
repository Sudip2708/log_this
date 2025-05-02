def reduce_depth_check(depth_check):
    """Metoda sníží hodnotu pro kontrolu vnitřních položek"""
    if isinstance(depth_check, int):
        depth_check = depth_check - 1 if depth_check >= 0 else 0
    return depth_check