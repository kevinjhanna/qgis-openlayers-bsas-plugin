# -*- coding: utf-8 -*-
"""
/***************************************************************************
OpenLayers Plugin
A QGIS plugin

                             -------------------
begin                : 2009-11-30
copyright            : (C) 2009 by Pirmin Kalberer, Sourcepole
email                : pka at sourcepole.ch
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from weblayer import WebLayer3857

class OlBSASMapLayerBase(WebLayer3857):

    emitsLoadEnd = True

    def __init__(self, html, name):
        WebLayer3857.__init__(self, groupName="Buenos Aires", groupIcon="./bsas_icon.png", name=name, html=html)


class OlBSASMapLayer(OlBSASMapLayerBase):

    def __init__(self):
        OlBSASMapLayerBase.__init__(self, name='Área Metropolitana de Buenos Aires', html='bsas_con_transporte.html')

class OlBSASFotografia1965MapLayer(OlBSASMapLayerBase):
    
    def __init__(self):
        OlBSASMapLayerBase.__init__(self, name='AMBA Fotos 1965', html='caba_fotografias_1965.html')

class OlBSASFotografia1978MapLayer(OlBSASMapLayerBase):
    
    def __init__(self):
        OlBSASMapLayerBase.__init__(self, name='AMBA Fotos 1978', html='caba_fotografias_1978.html')


