def ft_filter(function, iter):
    """
    Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true.
    """
    if function:
        return [i for i in iter if function(i)]
    return [i for i in iter if i]
# Pour chaque i dans iter, garde-le si function(i) renvoie True. 