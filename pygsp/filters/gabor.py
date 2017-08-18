# -*- coding: utf-8 -*-

import numpy as np

from . import Filter
from pygsp import utils


_logger = utils.build_logger(__name__)


class Gabor(Filter):
    r"""
    Gabor filterbank

    Parameters
    ----------
    G : graph
    k : lambda function
        kernel

    Notes
    -----
    This function create a filterbank with the kernel *k*. Every filter is
    centered in a different frequency.

    Examples
    --------
    >>> from pygsp import graphs, filters
    >>> G = graphs.Logo()
    >>> k = lambda x: x/(1.-x)
    >>> F = filters.Gabor(G, k);

    """
    def __init__(self, G, k, **kwargs):

        Nf = G.e.shape[0]

        g = []
        for i in range(Nf):
            g.append(lambda x, ii=i: k(x - G.e[ii]))

        super(Gabor, self).__init__(G, g, **kwargs)
