##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class RGgsci(RPackage):
    """ggsci: Scientific Journal and Sci-Fi Themed Color Palettes for
    'ggplot2'"""

    homepage = "https://github.com/road2stat/ggsci"
    url      = "https://cran.r-project.org/src/contrib/ggsci_2.4.tar.gz"
    list_url = "https://cran.r-project.org/src/contrib/Archive/ggsci"

    version('2.4', '8e5dc2fcf84352cacbb91363e26c7175')

    depends_on('r@3.0.2:')
    depends_on('r-scales', type=('build', 'run'))
    depends_on('r-ggplot2@2.0.0:', type=('build', 'run'))
