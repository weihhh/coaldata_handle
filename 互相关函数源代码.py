def correlate(a, v, mode='valid'):
    """
    Cross-correlation of two 1-dimensional sequences.
    This function computes the correlation as generally defined in signal
    processing texts::
        c_{av}[k] = sum_n a[n+k] * conj(v[n])
    with a and v sequences being zero-padded where necessary and conj being
    the conjugate.
    Parameters
    ----------
    a, v : array_like
        Input sequences.
    mode : {'valid', 'same', 'full'}, optional
        Refer to the `convolve` docstring.  Note that the default
        is 'valid', unlike `convolve`, which uses 'full'.
    old_behavior : bool
        `old_behavior` was removed in NumPy 1.10. If you need the old
        behavior, use `multiarray.correlate`.
    Returns
    -------
    out : ndarray
        Discrete cross-correlation of `a` and `v`.
    See Also
    --------
    convolve : Discrete, linear convolution of two one-dimensional sequences.
    multiarray.correlate : Old, no conjugate, version of correlate.
    Notes
    -----
    The definition of correlation above is not unique and sometimes correlation
    may be defined differently. Another common definition is::
        c'_{av}[k] = sum_n a[n] conj(v[n+k])
    which is related to ``c_{av}[k]`` by ``c'_{av}[k] = c_{av}[-k]``.
    Examples
    --------
    >>> np.correlate([1, 2, 3], [0, 1, 0.5])
    array([ 3.5])
    >>> np.correlate([1, 2, 3], [0, 1, 0.5], "same")
    array([ 2. ,  3.5,  3. ])
    >>> np.correlate([1, 2, 3], [0, 1, 0.5], "full")
    array([ 0.5,  2. ,  3.5,  3. ,  0. ])
    Using complex sequences:
    >>> np.correlate([1+1j, 2, 3-1j], [0, 1, 0.5j], 'full')
    array([ 0.5-0.5j,  1.0+0.j ,  1.5-1.5j,  3.0-1.j ,  0.0+0.j ])
    Note that you get the time reversed, complex conjugated result
    when the two input sequences change places, i.e.,
    ``c_{va}[k] = c^{*}_{av}[-k]``:
    >>> np.correlate([0, 1, 0.5j], [1+1j, 2, 3-1j], 'full')
    array([ 0.0+0.j ,  3.0+1.j ,  1.5+1.5j,  1.0+0.j ,  0.5+0.5j])
    """
    mode = _mode_from_name(mode)
    return multiarray.correlate2(a, v, mode)