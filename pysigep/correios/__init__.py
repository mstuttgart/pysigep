# -*- coding: utf-8 -*-
# © 2016 Alessandro Fernandes Martini, Trustcode
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from pysigep import send


def calcular_preco_prazo(**kwargs):
    path = 'CalcularPrecoPrazo.xml'
    return send(path, 'CalcPrecoPrazoResponse', 'CalcularFretePrazo',
                'http://tempuri.org/CalcPrecoPrazo', **kwargs)
