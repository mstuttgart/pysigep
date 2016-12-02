# -*- coding: utf-8 -*-
# © 2016 Alessandro Fernandes Martini, Trustcode
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import os
from pysigep import send

TEMPLATES = os.path.join(os.path.join(os.getcwd(), os.pardir))
TEMPLATES = os.path.join(TEMPLATES, 'templates')


def calcular_preco_prazo(**kwargs):
    TEMPLATE = os.path.join(TEMPLATES, 'CalcularPrecoPrazo.xml')
    return send(TEMPLATE, 'CalcPrecoPrazoResponse', 'CalcularFretePrazo',
                'http://tempuri.org/CalcPrecoPrazo', **kwargs)
