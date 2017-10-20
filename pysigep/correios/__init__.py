# -*- coding: utf-8 -*-
# © 2016 Alessandro Fernandes Martini, Trustcode
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

# #############################################################################
#
#    Brazillian Carrier Correios Sigep WEB
#    Copyright (C) 2015 KMEE (http://www.kmee.com.br)
#    @author: Michell Stuttgart <michell.stuttgart@kmee.com.br>
#    @author: Rodolfo Bertozo <rodolfo.bertozo@kmee.com.br>
#    Sponsored by Europestar www.europestar.com.br
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


import base64
import io
from PIL import Image, ImageDraw, ImageFont
from StringIO import StringIO
import textwrap
import os

BASE_DIR = os.path.dirname(__file__)
_TTF_ARIAL = os.path.join(BASE_DIR, 'data/fonts/arial.ttf')
_TTF_ARIAL_N = os.path.join(BASE_DIR, 'data/fonts/arial_negrito.ttf')


def sign_chancela(chancela, usuario_correios):
    """
    :params:
        chancela: imagem da chancela, codificada em base64
        usuario_correios: {'contrato': idContrato,
                           'nome': nome da empresa,
                           'ano_assinatura': ano de assinatura,
                           'origem': sigla do estado de origem,
                           'postagem': sigla de estado de destino,}
    :return:
        imagem em base64
    """
    t = base64.decodestring(chancela)
    img = Image.open(StringIO(t)).convert("RGB")
    draw = ImageDraw.ImageDraw(img)
    font = ImageFont.truetype(_TTF_ARIAL, int(img.size[0]*0.07))
    texto = usuario_correios['contrato'] + '/' + usuario_correios['ano_assinatura']
    texto += ' - DR/' + usuario_correios['origem']
    if usuario_correios['postagem'] != usuario_correios['origem']:
        texto += '/' + usuario_correios['postagem']
    tamanho_texto = draw.textsize(texto)
    h_position = (img.size[0] - tamanho_texto[0]) / 2
    v_position = img.size[1] / 2
    draw.text((h_position, v_position), texto, fill=(0, 0, 0), font=font)
    list_name = textwrap.wrap(usuario_correios['nome'], width=20)
    font = ImageFont.truetype(_TTF_ARIAL_N, int(img.size[0]*0.07))
    v_position = img.size[1] / 2 + int(img.size[0]*0.07)
    y_text = v_position
    for line in list_name:
        width, height = font.getsize(line)
        h_position = (img.size[0] - width) / 2
        draw.text((h_position, y_text), line, fill=(0, 0, 0), font=font)
        y_text += height + 5
    size = max(img.size[0], img.size[1])
    bg = Image.new("RGBA", (size, size), (255, 255, 255))
    h_position = (bg.size[0] - img.size[0]) / 2
    v_position = (bg.size[1] - img.size[1]) / 2
    bg.paste(img, box=(h_position, v_position))
    tmp = io.BytesIO()
    bg.save(tmp, 'png')
    bg = base64.b64encode(tmp.getvalue())
    return bg
